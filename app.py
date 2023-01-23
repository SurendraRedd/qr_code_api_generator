# This working code is generated by chatgpt

# Search String used : code for python flask api server that take 'GET' request with url as 
# string and convert it to qr code image and send it back as api response.

# how to make response downloadeble

from flask import Flask, jsonify, request, Response
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def generate_qr():
    url = request.args.get('url')
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    #Convert PIL image to png
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    headers = {
                'Content-Disposition': 'attachment',
                'filename':'qr.png'
            }
    return Response(img_io.getvalue(), mimetype='image/png',headers=headers)

if __name__ == '__main__':
    app.run()
