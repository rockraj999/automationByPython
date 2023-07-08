import os
import datetime


def getProdPrice():
    prod_price = {}
    with open('../master_data/product_master.csv') as f:
        lines = f.readlines()[1:]
        for i in lines:
            si = i.split(',')
            prod_price[si[0]] = si[2]
    return prod_price

def validate_product_id(val):
    prod_price = getProdPrice()
    if val in prod_price:
        return True
    return False

def validate_sales(val2, val3, val4):
    prod_price = getProdPrice()
    if int(val3)*int(prod_price[val2]) == int(val4):
        return True
    return False

def validate_order_date(val1):
    orderdate = datetime.datetime.strptime(val1, '%Y-%m-%d').date()
    today_date = datetime.date.today()
    delta_dt = (today_date-orderdate).days
    if delta_dt >= 0:
        return True
    return False

def validate_emptiness(split_list):
    if not any(len(split_list[item]) == 0 for item in range(len(split_list) - 1)):
        return True
    return False


def validate_city(val):
    if val.upper() in ("BANGALORE", "MUMBAI"):
        return True
    return False


# val_pid = v.validate_product_id(split_list[2])
#                             val_od = v.validate_order_date(split_list[1])
#                             val_city = v.validate_city(split_list[5])
#                             val_empty = v.validate_emptiness(split_list)
#                             val_sales = v.validate_sales(split_list[3], split_list[4])