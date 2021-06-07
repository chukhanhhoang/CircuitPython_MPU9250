import time
import roboticsmasters_mpu9250
import busio

i2c = busio.I2C(23,22) # I2C channel 6

sensor = roboticsmasters_mpu9250.MPU9250(i2c_bus = i2c, mpu_addr=0x68)

#print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    time.sleep(0.5)
