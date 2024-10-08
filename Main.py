from sense_hat import SenseHat #import library that allows us to access env sensors
import time
import csv
import logging
import datetime

sense = SenseHat()    #creates class instance on sensors so we can get the goods
sense.clear()

date = datetime.datetime.now()
filename_datalog = f'data_{date.strftime('%d')}{date.strftime('%m')}{date.strftime('%y')}{date.strftime('%h')}{date.strftime('%M')}{date.strftime('%S')}'
print(filename_datalog)

with open(f'{filename_datalog}.csv', newline='') as envdata:
    file_data = csv.reader(envdata, delimiter='', quotechar='/')
    for row in file_data:
        print(','.join(row))

accel = sense.get_acceleration_raw()
ac_x = accel['x']
ac_y = accel['y']
ac_z = accel['z']




