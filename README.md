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







