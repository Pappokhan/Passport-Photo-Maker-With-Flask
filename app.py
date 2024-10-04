import os
from flask import Flask, request, render_template, send_file, redirect, url_for
from rembg import remove
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    bg_color = request.form['bg_color']
    photo_size = request.form['photo_size']

    try:
        width, height = map(int, photo_size.split(','))
    except ValueError:
        return 'Invalid photo size format. Use width,height (e.g., 600,800)', 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Remove background
    with open(filepath, 'rb') as input_file:
        input_data = input_file.read()
        result = remove(input_data)

    # Save the result as PNG
    output_filepath = os.path.join(OUTPUT_FOLDER, 'passport_photo.png')
    with open(output_filepath, 'wb') as output_file:
        output_file.write(result)

    image = Image.open(output_filepath).convert("RGBA")
    colored_background = Image.new("RGBA", image.size, bg_color)  # Use user-selected color
    passport_photo = Image.alpha_composite(colored_background, image).convert("RGB")

    passport_photo = passport_photo.resize((width, height), Image.LANCZOS)
    passport_photo.save(output_filepath)

    return {
        'download_url': url_for('download_image', _external=True),
        'image_url': url_for('static', filename='passport_photo.png', _external=True)
    }

@app.route('/download')
def download_image():
    filepath = os.path.join(OUTPUT_FOLDER, 'passport_photo.png')
    return send_file(filepath, as_attachment=True)

@app.route('/static/<filename>')
def static_file(filename):
    return send_file(os.path.join(OUTPUT_FOLDER, filename))

if __name__ == '__main__':
    app.run(debug=True, port=8080)
