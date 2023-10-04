import io
import qrcode
from PIL import Image
import datetime
import base64
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    title = "Generador QR"
    qr_image = None
    data = None
    fecha = datetime.datetime.now().year

    if request.method == 'POST':
        data = request.form['data']
        image = request.files['image']

        # Crear código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(
            fill_color="black", back_color="white").convert('RGBA')

        # Insertar la imagen en el centro del código QR
        if image:
            img = Image.open(image).convert('RGBA')
            # Redimensionar la imagen según sea necesario
            img = img.resize((50, 50))

            # Calcular las coordenadas de posición para el centro del código QR
            qr_width, qr_height = qr_img.size
            img_width, img_height = img.size
            x = (qr_width - img_width) // 2
            y = (qr_height - img_height) // 2

            qr_img.paste(img, (x, y), img)

        # Convertir el código QR con la imagen a base64
        buffered = io.BytesIO()
        qr_img.save(buffered, format="PNG")
        qr_image = base64.b64encode(buffered.getvalue()).decode()

    return render_template('index.html', qr_image=qr_image, data=data, title=title, fecha=fecha)


if __name__ == '__main__':
    app.run(debug=True)
