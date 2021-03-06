# this program reads logged sensor value to determine if a wifi-access code should be generated

# notes:
# might want to generate code as a QR code using (pip install qrcode[pil])

# change "Output.txt" at whatever point
sensor_file = open("Output.txt", "r")
# cast string to int, hopefully
sensor_value = int(sensor_file.read())
sensor_file.close()

if sensor_value == 1:
    print("Purchase authenticated!\nDispensing WiFi Access code")
else:
    print("Purchase invalid!")