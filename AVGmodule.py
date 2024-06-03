from statistics import median, mean
from collections import defaultdict

def average_carat(data):
    return mean(float(row['carat']) for row in data)

def average_price_by_color(data):
    color_price = defaultdict(list)
    for row in data:
        color_price[row['color']].append(float(row['price']))
    return {color: mean(prices) for color, prices in color_price.items()}

def median_weight(data):
    weights = [float(row['carat']) for row in data]
    return median(weights)