import time
import board
import busio
import adafruit_bno055

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)
#sensor.use_external_crystal = True

i = 0
while True:
    #print(i)
    i += 1
    print('Acceleration: {}'.format(sensor.acceleration))
    print('Gravity: {}'.format(sensor.euler))
 

    time.sleep(.01)
