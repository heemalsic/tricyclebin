import serial
ser=serial.Serial('/dev/ttyACM0', 9600)
ser.write(str(3).encode())