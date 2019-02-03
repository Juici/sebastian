import serial
import io
import time

class Control:
    @staticmethod
    def _command(command):
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = '/dev/ttyACM0'
        ser.open()
        ser.readline()
        time.sleep(0.1)
        ser.write(command)
        time.sleep(0.1)
        ser.close()
    @staticmethod
    def forward():
        Control._command(b'3')
    @staticmethod
    def left():
        Control._command(b'1')
    @staticmethod
    def right():
        Control._command(b'2')
