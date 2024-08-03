import qrcode as q

# This is url for my instagram page 
input_URL = "https://www.instagram.com/dptweets6?igsh=MWFpcDhtMzQyeGkxcQ=="

qr = q.QRCode(
    version=1,
    error_correction=q.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("url_qrcode.png")

print(qr.data_list)
