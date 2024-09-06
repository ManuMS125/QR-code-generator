import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=1,border=1,)

qr.add_data('https://youtu.be/FOGRHBp6lvM?si=H8t0Z40kY_c8xDb1')
qr.make(fit=True)
img=qr.make_image(fill_color='red',back_color='white')
img.save('wscube_web.png')
