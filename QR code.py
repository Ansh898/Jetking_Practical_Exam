import pyqrcode
import png
from pyqrcode import QRCode
string = "https://www.google.com/"
url=pyqrcode.create(string)
url.png("qr.png",scale=8)
