#import qrcode
#from qrcode.image.pure import PymagingImage
#img = qrcode.make('test data',image_factory=PymagingImage)
#img = qrcode.make("PANADOL2",fit=True)
"""
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
"""
import pyqrcode

big_code = pyqrcode.create('0987654321', error='L', version=27, mode='binary')
big_code.png('code.png', scale=4, module_color=[0, 0, 0, 255], background=[0xff, 0xff, 0xcc])
big_code.show()
