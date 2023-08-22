#!/usr/bin/python
from faker import Faker
import random
from random import randrange
from datetime import datetime
from datetime import time
import os
import pandas as pd
import numpy as np
import time
import string

START_YEAR = 2012
START_MONTH = 1
START_DATE = 1

END_YEAR = 2022
END_MONTH = 12
END_DATE = 31
# DATE_FORMAT = '%m/%d/%Y %I:%M %p'
DATE_FORMAT = '%m/%d/%Y'

PROD_ID_COLM = 0
PROD_NAME_COLM = 1
PROD_PRICE_COLM = 2

PROD_SPEC_FOLDER = './prod_spec'
faker = Faker()

class GenProdDetails():
    prod_data = []
    prod_name = ['Inspiron Laptop', 'Infinity Laptop', 'Gravity Laptop', 'Ascend Workstation', 'Prelude Workstation']
        

    def __init__(self):
        file_list = os.listdir(PROD_SPEC_FOLDER)
        sep = '.'
        prod_list = [prod.split(sep, 1)[0] for prod in file_list]

        # print(prod_list)

        if prod_list is None:
            print(f"*** NOTE: There are no product spec documents ***")

        for one_prod in prod_list:
            tmp_list = []
            prod_id = one_prod
            tmp_list.append(prod_id)
            prod_name = random.choice(self.prod_name)
            tmp_list.append(prod_name)
            unit_price = round(random.uniform(300.0, 2000.0), 2)
            tmp_list.append(unit_price)
            self.prod_data.append(tmp_list)
        # print(self.prod_data)

    def get_prod_data(self):
        prod_details = random.choice(self.prod_data)
        return prod_details

def prod_type():
    prod_name = ['Inspiron Laptop', 'Infinity Laptop', 'Gravity Laptop', 'Ascend Workstation', 'Prelude Workstation']
    return random.choice(prod_name)

def gen_transaction_id():
    # Faker.seed(0) Faker seed when you want the same generation

    # str_fake = faker.pystr(4,4)
    str_random = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return f"{str_random}"

def gen_date():
    
    rand_date = faker.date_between_dates(date_start=datetime(START_YEAR, START_MONTH, START_DATE), \
                                         date_end=datetime(END_YEAR, END_MONTH, END_DATE))

    return rand_date

def main():
    prod_data = GenProdDetails()
    # exit(1)
    number_of_records = int(input("Enter the number of records to be added: ") or '10')

    start = time.process_time()

    dict_record = dict()
    df4csv = pd.DataFrame()
 
    for i in range(number_of_records):
        #columns that use faker
        # d['first_name'] = lambda: faker.first_name()
        # d['last_name'] = lambda: faker.last_name()
        dict_record['transaction_id'] = gen_transaction_id()
        dict_record['sale_date'] = gen_date()
        list_data = prod_data.get_prod_data()


        dict_record['product_id'] = list_data[PROD_ID_COLM]
        dict_record['type of prduct'] = list_data[PROD_NAME_COLM]
        dict_record['items_sold'] = random.randint(1, 10)
        dict_record['unit_price'] = list_data[PROD_PRICE_COLM]
        dict_record['total_amount'] = round((dict_record['items_sold'] * dict_record['unit_price']), 2)
        dict_record['first_name'] = faker.first_name()
        dict_record['last_name'] = faker.last_name()
        dict_record['customer_email'] = f"{dict_record['first_name']}.{dict_record['last_name']}@{faker.domain_name()}"
        address = faker.address()
        address = address.replace("\n", "")
        dict_record['customer_address'] = f"{address}"
        # print(dict_record)
        
        dict_df = pd.DataFrame([dict_record])
        df4csv = pd.concat([df4csv, dict_df], ignore_index=True)

        # Performance test
        if (i % 1000 == 0):
            end = time.process_time()
            print(f"...records created {i} Time taken: {end - start}")

    end = time.process_time()
    print(f"total time creating records: {end-start}")
    

    file_name = input("Enter the name of the csv file to which the data is to be appended: [sales_data.csv] ")\
        or 'sales_data.csv'
    
    try:
        f = open(file_name)
        truncate_or_overwrite_file = input("File exists. Append or overwrite? 'o' or 'a': ")
        if truncate_or_overwrite_file == 'a':
            pass
        elif truncate_or_overwrite_file == 'o':
            os.remove(file_name)
    except FileNotFoundError:
        if '.csv' not in file_name:
            file_name = file_name + '.csv'  
    print(f"File name is {file_name}")
    
    # print(df4csv.head(12))
    df4csv.to_csv(file_name, mode='a', lineterminator= "\n", index=False)

    print(f"The data has been appended to {file_name}")

if __name__ == '__main__':
    main()


'''
Required columns
1. transaction_id - Integer - start from 10000 to 1 million
2. sale_date - DD-MMM-YYYY
3. product_id - String[20]
4. type_of_product - String[50]
5. items_sold - Integer
6. unit_price - Float
7. total_amount - Float
8. customer_first_name - String
9. customer_last_name
10. customer_email - String
11. customer_address - String
'''


