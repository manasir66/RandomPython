import csv
import os

csv_f_name = 'data.csv'

for image in os.listdir():
    
    name = 'gs://unlabelled_images/' + image
    row = [name]

    with open(csv_f_name, 'a') as csv_file:
        data_writer = csv.writer(csv_file)
        data_writer.writerow(row)

print("succesfully recorded the details")
csv_file.close()

with open('data.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)