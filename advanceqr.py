import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H, #corrects High Level Error
                   box_size = 10, border = 4) #box_size means hight-width of qr code #border is for padding
 
qr.add_data("https://www.youtube.com/@thunderstrikerecords6818")
qr.make(fit = True) # fit means if qr.add_data is not null then only make qrcode
img = qr.make_image(fill_color = "gold",
                    back_color = "indigo")
img.save("ThunderstrikeRecords.png")