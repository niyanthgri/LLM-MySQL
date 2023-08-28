# LLM-MySQL

# LLM-MySQL

The purpose of this program is to use LLM and answer basic questions based on information provided via pdf documents and a MySQL databse.

### Key things to note, to make the LLM work:
- While talking about a year in the prompt, use the word "year"
- While talking about product specification in the prompt, use the word "prod_id"

### Prerequisites:
1. Have pdf files ready
2. Have a MySQL account ready

### Who will be using this: 
Business analysts, analysts who don't know how to understand or code, can use this to analyse given data.

### Code
The folder has 2 codes.
1. generate.py
2. sales_data.py


## generate_data.py
This program creates random data that you can insert into your MySQL table to then do further analysis on

The code to run the program:
> python generate_data.py

When you first run the program, this is what you'll be asked:
![Screenshot 2023-08-28 at 12 17 30 PM](https://github.com/niyanthgri/LLM-MySQL/assets/140157007/0e0493bc-21e2-465a-a76d-b2549144159b)

Here, you provide the number of records that you want generated. Let's say we want 100 records generated. 
After mentioning the number of records you want added, the program mentions the time taken to create and append the records to the CSV file.
It now asks you which file you'd like to append these records to. The default file it appends to is called ```sales_data.csv```




