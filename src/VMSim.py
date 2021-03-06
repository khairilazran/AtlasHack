import serial

port = "COM3"
ser = serial.Serial(port,9600)
value = 0

if(ser.read()):
	print("Success!")