import serial
import io
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyACM0'

ser.open()
ser.readline()
time.sleep(1)
ser.write(b'1\n')
time.sleep(1)
ser.close()
