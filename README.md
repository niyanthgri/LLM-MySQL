# LLM-MySQL

The purpose of this program is to use LLM and answer basic questions based on information provided via pdf documents and a MySQL databse.

### Prerequisites:
1. Have pdf files ready
2. Have a MySQL account ready

### Who will be using this: 
Business analysts, analysts who don't know how to understand or code, can use this to analyse given data.

### Code
The folder has 2 codes.
1. generate.py - generate random data of records
2. sales_data.py - a csv file with a number of randomly generated 


## generate_data.py
This program creates random data that you can insert into your MySQL table to then do further analysis on

The code to run the program:
> python generate_data.py

When you first run the program, this is what you'll be asked:

![Screenshot 2023-08-28 at 12 17 30 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/0e0493bc-21e2-465a-a76d-b2549144159b)

Here, you provide the number of records that you want generated. Let's say we want 100 records generated. 
After mentioning the number of records you want added, the program mentions the time taken to create and append the records to the CSV file.
It now asks you which file you'd like to append these records to. The default file it appends to is called ```sales_data.csv```

![Screenshot 2023-08-28 at 12 30 24 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/d1b89e0d-8d5a-41aa-89ef-8feef2145599)

### File Exists
If the file deosn't exist, it'll create a file with the name you mentioned and this is what the command line would look like:

![Screenshot 2023-08-28 at 12 57 27 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/ad97a539-a0be-4b8d-8252-5aa5d269037f)

### File doesn't exist
If the file exists, then yoou'll be asked if you want to append or overwrite the data in the CSV file. If you're appending, please make sure that the number of columns and the name of the columns match in the CSV file, or else please overwrite or create a new file.

This is what you'll see if the file exists:

![Screenshot 2023-08-28 at 12 45 10 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/cb5d8c5f-7969-4f1b-b364-8af6b63540b8)

This is what you'll see after appending or overwriting to the CSV file:

![Screenshot 2023-08-28 at 12 55 51 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/568c630f-2778-48c5-ac56-b8ff505fab47)

## Uploading file to MySQL

Login to your MySQL
- Create a table with the following SQL query:
> create TABLE <NameOfDatabase>.<TableName>(\
            TRANSACTION_ID VARCHAR(50),\
            SALE_DATE VARCHAR(50),\
            PRODUCT_ID VARCHAR(50),\
            TYPE_OF_PRODUCT VARCHAR(50),\
            ITEMS_SOLD NUMBER(38,0),\
            UNIT_PRICE FLOAT,\
            TOTAL_AMOUNT FLOAT,\
            CUSTOMER_FIRST_NAME VARCHAR(50),\
            CUSTOMER_LAST_NAME VARCHAR(50),\
            CUSTOMER_EMAIL VARCHAR(50),\
            CUSTOMER_ADDRESS VARCHAR(200));

- Check if the table exists by using this query:
> select count(0) from <TableName>;

Make sure you're in the right schema and right database when running that query

- In the top left corner, locate the table in your schema, database and under tables:
  
![Screenshot 2023-08-28 at 5 03 54 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/8cb547c0-59d1-4a22-8701-309eafde2526)


Right click on the name of the table, and click on: ```Table Data Import Wizard```

- You'll get a pop up in which you browse to the location of your CSV file to be uploaded, click on ```Next``` once and then check if the schema and table name are right in the next pop up.
If they are, click on ```next``` again.

- In the Configure Import Settings, make sure the encoding is ```utf-8```

![Screenshot 2023-08-28 at 5 05 21 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/f4d80c35-8e5c-428c-8df9-46bf1555fca4)

Then click on ```Next``` twice and the table will be imported.


## llm_mysql_sales.py

### Key things to note, to make the LLM work:
- While talking about a year in the prompt, use the word ```year```
- While talking about product specification in the prompt, use the word ```prod_id```
This program uses LLM to read the data from the pdf files and the MySQL databse to answer basic questions

The code to run the progream:
> python llm_mysql_sales.py

When you first run the program, this is what you'll be asked:

![Screenshot 2023-08-28 at 3 07 57 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/374e82a3-36a7-4c57-bd3c-3f4c45a0a9c7)


What you see in this screenshot, is the MySQL version, the table that's being used, the SQL query to create the table, a test response to just check whether the engine is running smoothly or not, and the product IDs.
You will now be asked to enter your query. The default query is: ```Tell me about the Maximum Memory of the prod_id that sold most in the year 2021```

As mentioned in this document, this query has ```prod_id``` and the word ```year``` in it.

After entering the default query, this is what the LLM answers: 

