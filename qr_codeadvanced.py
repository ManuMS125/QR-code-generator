import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=1,border=1,)

qr.add_data('https://docs.python.org/3/c-api/memory.html')
qr.make(fit=True)
img=qr.make_image(fill_color='red',back_color='white')
img.save('qrcode.png')
