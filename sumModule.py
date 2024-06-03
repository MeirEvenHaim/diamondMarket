import csv


def number_of_ideal_diamonds(data):
    return sum(1 for row in data if row['cut'] == 'Ideal')

def sum_of_diamonds(data):
    return sum(float(row['price']) for row in data)
