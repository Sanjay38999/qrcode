import qrcode as qr

image = qr.make("https://github.com")
image.save('Github.png')
