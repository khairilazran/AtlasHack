#import serial
from scanner import decode_qr

#ser = serial.Serial("COM3",9600) #setup the serial comms
drug = ""

#if(ser.read()): #if read input from COM3, do something...
	#print("Success!")
output = decode_qr().decode("utf-8")
print(output)
for char in output:
	if char.isnumeric():
		print("Dispensing " + drug + ", Quantity: " + char)
		break
	else:
		drug += char
		

