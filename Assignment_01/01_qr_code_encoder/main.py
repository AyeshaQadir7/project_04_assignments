from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(r"C:/Users/Soft Hands/Documents/QR code Python/myqrcode.png")

result = decode(img)

print(result)

# import qrcode

# data = "Hello from Ayesha!"

# # img = qrcode.make(data)

# # img.save("C:/Users/Soft Hands/Documents/QR code Python/myqrcode.png")

# qr = qrcode.QRCode(version=1, box_size=10, border=5)

# qr.add_data(data)

# qr.make(fit=True)
# img = qr.make_image(fill_color="blue", back_color="white")

# img.save("C:/Users/Soft Hands/Documents/QR code Python/myqrcode.png")
