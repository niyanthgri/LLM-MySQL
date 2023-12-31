# LLM-MySQL

This program demonstrates how LLm can be used to query SQL table for insights and read the documents for additional details. In this example, we are using ```sales_data``` table to get insights and the documents present in ```prod_spec``` for additional information.

### Prerequisites:
1. Have pdf files ready
2. Have a MySQL account ready
3. Fill in your details, user-id, password and more in the ```user-details.py``` file

### Who will be using this (Use Case): 
Business analysts who aren't familiar with SQL queries can use this to analyse given data and also get reason for particulars beyond the sales_data.
For example: They can get the least sold product by quarter or year and they can get further details from the documents which may provide a reason as to why the product didn't sell well.

Query: ```Get the memory slots from product specification of the least sold product in year 2021.```


### Code
The folder has 4 files and 1 data folder.

_*Files*_
1. generate.py - code to generate random data of sales records
2. sales_data_100k.py - a csv file with a number of randomly generated sales records ~ 100k records
3. llm_mysql.py - The LLM code.
4. requirements.txt - The packages that need to be installed
5. user_details - Contains all your MySQL details which are to be filled by you

_*Folder*_
1. prod_spec - Files containing the product specicifations for a few electronic items.

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

Login to your MySQL Workbench
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

![Screenshot 2023-08-28 at 5 05 21 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/f4d80c35-8e5c-428c-8df9-46bf1555fca4)

- You'll get a pop up in which you browse to the location of your CSV file to be uploaded, click on ```Next``` once and then check if the schema and table name are right in the next pop up.
If they are, click on ```next``` again.

- In the Configure Import Settings, make sure the encoding is ```utf-8```

![Screenshot 2023-08-28 at 5 11 22 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/98434353-f577-4f39-a1f7-f976bef5bb8e)

Then click on ```Next``` twice and the table will be imported after you click on ```Finish```


## llm_mysql_sales.py

The code to run the progream:
> python llm_mysql.py

When you first run the program, this is what you'll be asked:

![Screenshot 2023-08-28 at 3 07 57 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/374e82a3-36a7-4c57-bd3c-3f4c45a0a9c7)


What you see in this screenshot, is the MySQL version, the table that's being used, the SQL query to create the table, a test response to just check whether the engine is running smoothly or not, and the product IDs.
You will now be asked to enter your query. The default query is: ```Tell me about the Maximum Memory of the prod_id that sold most in the year 2021```

As mentioned in this document, this query has ```prod_id``` and the word ```year``` in it.

1. After entering the query: ```find out least sold product in year 2021 and get the memory slots from the product specification. Limit to 50 words```, this is what the LLM answers: 

<img width="1912" alt="Screen Shot 2023-08-28 at 5 27 22 PM" src="https://github.com/niyanthgri/LLM-MySQL/assets/140157007/447e7a38-5116-4e52-999c-49c04349ce87">


2. After entering the query: ```What is the unit price of prod_id c0888728? Limit to 50 words```, this is what the LLM answers:

<img width="1868" alt="Screen Shot 2023-08-28 at 5 26 22 PM" src="https://github.com/niyanthgri/LLM-MySQL/assets/140157007/755ca233-87bf-4beb-83a2-78d9dc1ac758">


Some examples of queries that are working:

```1. get the memory slots from product specification of the least sold product in year 2021. Limit to 50 words.```

```2. Tell me transaction_id 8Y3CLHVW0Z details. Limit to 50 words.```

```3. what is the unit price of prod_id z0888728? Limit to 50 words.```

```4. Find out the most sold product in year 2022. Limit to 50 words.```

We are mentioning, ```Limit to 50 words.``` as the system gives an error in regards with exceeding tokens, if this is not provided.

## Requirements.txt

The code to download the packages from the txt file:
> pip install -r requirements.txt
or
> pip3 install -r requirements.txt


Similarly, the user may provide basic queries and get the LLM to answer the basic queries.
I hope this has been helpful to you.

Thank you.


