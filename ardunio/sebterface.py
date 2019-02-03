import serial
import time

port = '/dev/ttyACM0'
aserial = serial.Serial(port, 9600)

time.sleep(2)
print(aserial.readline())

print(aserial)


##int(aserial.readline())
##print("go")
##
##aserial.write(b'1')
##
##print("done")



while True:
    control = input("in: ")
    aserial.write(b'%d' %int(control))
    print("sent")

