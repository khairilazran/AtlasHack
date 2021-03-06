#import qrcode
#img = qrcode.make('test data',fit=True)
"""qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")"""

import pyqrcode
#url = pyqrcode.create('http://uca.edu')
#url.svg('uca-url.svg', scale=8)
#url.eps('uca-url.eps', scale=2)
#print(url.terminal(quiet_zone=1))

big_code = pyqrcode.create("PANADOL2990921107831", error='L', version=27, mode='binary')
big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
big_code.show()

