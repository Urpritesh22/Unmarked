from flask import Flask, request, render_template, redirect, url_for, send_file
import fitz  # PyMuPDF
from PIL import Image
import io
import os

app = Flask(__name__)

# Folder to store the uploaded files
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

def remove_background_watermark(input_pdf, output_pdf, min_width=400, min_height=400):
    pdf_document = fitz.open(input_pdf)

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        image_list = page.get_images(full=True)

        if image_list:
            for img_index, img in enumerate(image_list):
                xref = img[0]
                width, height = img[2], img[3]

                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))

                if is_grey_white_image(image) and width >= min_width and height >= min_height:
                    page.delete_image(xref)

    pdf_document.save(output_pdf)
    pdf_document.close()

def is_grey_white_image(image, grey_threshold=180, white_threshold=240):
    grey_pixels = 0
    white_pixels = 0
    total_pixels = image.width * image.height

    if image.mode != "RGB":
        image = image.convert("RGB")

    for pixel in image.getdata():
        r, g, b = pixel
        
        if abs(r - g) < 20 and abs(r - b) < 20 and r < grey_threshold:
            grey_pixels += 1
        
        elif r > white_threshold and g > white_threshold and b > white_threshold:
            white_pixels += 1

    grey_ratio = (grey_pixels + white_pixels) / total_pixels
    return grey_ratio > 0.85

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle the file upload
        uploaded_files = request.files.getlist('pdf_files')
        for file in uploaded_files:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], f"{filename.replace('.pdf', '_without_WM.pdf')}")
            
            # Save the file to the upload folder
            file.save(file_path)
            
            # Remove watermark
            remove_background_watermark(file_path, output_path)

        return redirect(url_for('download'))

    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    # Display the processed files for download
    output_files = os.listdir(app.config['OUTPUT_FOLDER'])
    return render_template('download.html', files=output_files)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
