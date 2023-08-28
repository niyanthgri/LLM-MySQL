import os
import openai
from user_details import *
from sqlalchemy import text
from llama_index.indices.struct_store.sql_query import NLSQLTableQueryEngine
from llama_index import SQLDatabase, ServiceContext
from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.query_engine import SubQuestionQueryEngine
from llama_index.tools.query_engine import QueryEngineTool
from llama_index.tools import ToolMetadata
from llama_index.query_engine import SQLJoinQueryEngine, RetrieverQueryEngine
import sys


# Getting the API key from your environment variable or a local file on your system. 
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # Reading the local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

# Function to get names of the pdf files present in a specific folder
# The name of the file, stripped off of ".pdf" indicates the prod_id
def get_prod_details():
    file_list = os.listdir(PROD_SPEC_FOLDER)
    sep = '.'
    prod_list = [prod.split(sep, 1)[0] for prod in file_list]
    return prod_list

from sqlalchemy import (
    create_engine,
    MetaData 
)

# Creating an engine to connect to MySQL
connect_cred = f'{SQL_TYPE}://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_HOST_URL}/{SQL_DB}'
engine = create_engine(connect_cred)

# Connecting to MySQL using the created engine
connection = engine.connect()
results = connection.execute(text('select version()')).fetchone()
print(f"MySQL version: {results[0]}")

# Using MetaData from SQL Alchemy
metadata_obj = MetaData()
tbl_to_use = f"{SQL_DB}.{MYSQL_TABLE}"
print(f"tbl_to_use: tbl_to_use")

# Choosing the OpenAI model to use
llm = OpenAI(temperature=0, model="gpt-3.5-turbo")
service_context = ServiceContext.from_defaults(llm=llm)

# Build SQL Index for MYSQL
sql_database = SQLDatabase(engine, include_tables=["sales_data"])

print(sql_database.table_info)

# Creating the query engine
sql_query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=[f"{MYSQL_TABLE}"],
)    

print("Reading product specs...")
pdf_docs = SimpleDirectoryReader('./prod_spec').load_data()

# Creating inMemory Vector Store 
index = VectorStoreIndex.from_documents(pdf_docs)
query_engine = index.as_query_engine(verbose=False)

# Testing if data was being read properly by asking a generic question
response = query_engine.query("What is the battery life of the product?")
print(f"Test response: {response}")

# Initializing the pdf and database vector indices
vector_indices = {}
vector_query_engines = {}

prod_id_list = get_prod_details()
print(f"prod_id_list: {prod_id_list}")

# Build Vector Index for pdf docs
for prod_id, pdf_doc in zip(prod_id_list, pdf_docs):
    vector_index = VectorStoreIndex.from_documents([pdf_doc])
    query_engine = vector_index.as_query_engine(similarity_top_k=2)
    vector_indices[prod_id] = vector_index
    vector_query_engines[prod_id] = query_engine

# Build Vector Index for MySQL database
query_engine_tools = []
for prod_id in prod_id_list:
    query_engine = vector_query_engines[prod_id]

    query_engine_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name=prod_id, description=f"Provides information about {prod_id}"
        ),
    )
    query_engine_tools.append(query_engine_tool)

# LlamaIndex can support more general multi-document queries via SubQuestionQueryEngine
s_engine = SubQuestionQueryEngine.from_defaults(query_engine_tools=query_engine_tools)

# To route the query, first different sub indices were built
# Then corresponding query engines were made to be QueryEngineTool
sql_tool = QueryEngineTool.from_defaults(
    query_engine=sql_query_engine,
    description=(
        "Useful for translating a natural language query into a SQL query over a table containing: "
        "containing the sales data for each product "
    ),
)
s_engine_tool = QueryEngineTool.from_defaults(
    query_engine=s_engine,
    description=f"Useful for answering semantic questions about different products",
)

# Joining the two query engine tools 
query_engine = SQLJoinQueryEngine(
    sql_tool, s_engine_tool, service_context=service_context
)


sys_message = f"""
Your task is to get data from the table provided. When data is not available 
in the table, refer the PDF document provided and answer the following question.
"""

# Recording the query
query_str = "Tell me about the Maximum Memory of the prod_id that sold most in the year 2021"
while query_str not in ['QUIT', 'quit', 'Quit', 'q', 'Q']:
    query_str = input(f"Enter the query: [Default:'{query_str}']: ") or query_str
    if query_str in ['QUIT', 'quit', 'Quit', 'q', 'Q']:
        print("Quitting")
        break
    print(f"Your question is: {query_str}")

    prompt = f"{sys_message} Question: {query_str}" 
    print(f"\nPROMPT: {prompt}\n")
    response = query_engine.query(prompt)
    print(response)


'''
Tips to make it work:
-- Use 'year' while referring year
-- Use 'prod_id' or product specification
-- Working Questions:
-- find out least sold product in year 2021 and get the memory slots from product specification
-- get the memory slots from product specification of the least sold product in year 2021
-- Tell me transaction_id 8Y3CLHVW0Z details
-- what is the unit price of prod_id z0888728? 
-- Find out the most sold product in year 2022
'''


'''
To Do:
1. Modify code to upload CSV file to MySQL
2. Clean up current LLM file and upload to Git
3. Identify questions that work correctly and include it in the ReadME file
4. Prepeare ReadME file with deatils and screenshots
    - Purpose of application
    - Use Case
    - Persona, who will be using this?
    - How it wotks, should come in the beginning
'''