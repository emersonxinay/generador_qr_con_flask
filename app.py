from flask import Flask, render_template, request, send_file
import io
import qrcode
import base64

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    qr_generated = None

    if request.method == 'POST':
        data = request.form['data']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Crear un objeto BytesIO para almacenar la imagen en memoria
        img_stream = io.BytesIO()
        qr_img.save(img_stream)
        img_stream.seek(0)

        # Convertir la imagen a base64
        img_str = base64.b64encode(img_stream.getvalue()).decode()

        qr_generated = img_str

    return render_template('index.html', qr_generated=qr_generated, data=data)


if __name__ == '__main__':
    app.run(debug=True)
