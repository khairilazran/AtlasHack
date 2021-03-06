import serial

ser = serial.Serial("COM3,9600) #setup the serial comms

if(ser.read()): #if read input from COM3, do something...
	print("Success!")
