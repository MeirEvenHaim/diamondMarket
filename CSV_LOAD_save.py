import csv
# this function is used to show the csv file this allowing me to display the data by pressing 1 inside the terminal
#by using csv DictREADER we can put said data to display inside a dict data structure
def load_data(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

#takes the returned data from load_data and prints it inside the terminal 
def display_data(data):
    for row in data:
        print(row)
        
# this function uses dump methodes to save the data inside the data.csv and is used by pressing 3
def save_data(data, file_path):
    fieldnames = data[0].keys()
    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)
