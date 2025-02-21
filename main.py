from sense_hat import SenseHat #import library that allows us to access env sensors
from orbit import ISS # The simulator will only compile when using the 'orbit' library, even though the actual library that we are using is 'astro_pi_orbit
import time
import csv
import datetime

sense = SenseHat()    #creates class instance on sensors so we can get the goods
sense.clear()
Velocity_Final = 0
date = datetime.datetime.now()
iss = ISS()


with open("data.csv", "w") as f:
    writer = csv.writer(f)
    header = ['ac_X', 'ac_Y', 'ac_Z', 'lat', 'lon', 'elev']
    writer.writerow(header)
    for i in range(570): #once every second for 570 seconds (9.5 minutes)
        accel = sense.get_accelerometer_raw()
        ac_x = accel['x']
        ac_y = accel['y']
        ac_z = accel['z']
        coordinates = iss.coordinates()
        print(coordinates)
        data = [ac_x, ac_y, ac_z, coordinates.longitude.signed_dms(), coordinates.longitude.signed_dms(), coordinates.elevation]
        #Velocity_angular = sense._read_imu()
        #print(Velocity_angular)
        print(ac_x, ac_y, ac_z)
        writer.writerow(data)
        time.sleep(1) # Wait one second






