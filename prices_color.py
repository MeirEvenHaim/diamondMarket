import csv
import CSV_LOAD_save

def highest_price(data):
    return max(data, key=lambda x: float(x['price']))

def colors_of_diamonds(data):
    return set(row['color'] for row in data)