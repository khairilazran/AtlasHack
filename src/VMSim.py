import serial
from tkinter import *
import os 

port = "COM3"
ser = serial.Serial(port,9600)
value = 0

if(ser.read()):
	print("Success!")
  
    #if value == "1":
#print(ser.name)
       	#os.startfile("qrcode.py")
       	