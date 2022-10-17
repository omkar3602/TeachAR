
# Import QRCode from pyqrcode
import pyqrcode
from pyqrcode import QRCode

def generate_qr(s, name):    
    # Generate QR code
    url = pyqrcode.create(s)
    
    # Create and save the png file naming "myqr.png"
    url.png(f'{name}_qr.png', scale = 6)

generate_qr("https://ng900.zappar.io/3528775801665792790/1.0.2/", "fcc")