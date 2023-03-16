#install all the libraries required
#create a function that taks input and converts it into qr code
#save the qr code as an image
import qrcode
def generate_qrcode(text):
    qr = qrcode.QRcode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save("QRimage.png")
text=input("enter your url : ")
generate_qrcode(text)