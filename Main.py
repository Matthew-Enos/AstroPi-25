from sense_hat import SenseHat #import library that allows us to access env sensors
import time
import csv

sense = SenseHat()    #creates class instance on sensors so we can get the goods
sense.clear()

with open('data.csv', newline='') as file:
    file_data = csv.reader(file, delimiter='', quotechar='/')
    for row in file_data:
        print(','.join(row))

accel = sense.get_acceleration_raw()




