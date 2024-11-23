import food
import csv

csv_path = r"Food Data.csv"

headings: list

def load_csv():
   with open(csv_path, mode ='r') as file:
      csvFile = csv.reader(file)
      counter = 0
      for line in csvFile:
        if line[0] == 'Foods':
            headings = line
            continue
        food.food(line)

load_csv()
print(food.food.getList())