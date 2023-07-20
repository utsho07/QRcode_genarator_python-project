import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=5)

qr.add_data("https://www.linkedin.com/in/chayon-datta-utsho-423aab20b/")
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="green")
img.save("linkedin.png")
