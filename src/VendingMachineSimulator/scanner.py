import cv2
import numpy as np
from pyzbar.pyzbar import decode
from cryptography.fernet import Fernet

def load_key():
    return open("secret.key","rb").read()

def decrypt_data(encrypted_data):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_data)




def decode_qr():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    cap.set(3,640)
    cap.set(4,480)

    data = ""

    while (not data):
        success, img = cap.read()
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            print(myData)
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,255),5)
            pts2 = barcode.rect
            cv2.putText(img, myData, (pts2[0], pts2[2]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,255), 2)
            data = myData
    
        cv2.imshow('Result',img)
        cv2.waitKey(1)

    print(data)
    cap.release()
    cv2.destroyAllWindows()
    return decrypt_data(bytes(data,"utf-8"))