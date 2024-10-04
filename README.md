# Passport-Photo-Maker-With-Flask
Passport Photo Maker is a web-based application that allows users to easily upload an image, select a passport photo size, and customize the background color. The app processes the image by removing the background and resizing it to the chosen dimensions. Users can preview the processed image and download the final passport photo in one click.

# Flask Image Processing Application

This Flask app allows users to upload, process, and display images. Uploaded files are stored in the `uploads` folder, and processed images in the `output` folder, both of which are created automatically. The frontend interface is handled by an HTML template in `templates/index.html`.

## Project Structure

- `app.py`: Main Flask application.
- `uploads`: Folder for uploaded files (auto-created).
- `output`: Folder for processed images (auto-created).
- `templates/index.html`: HTML file for the application's interface.

### Setup

1. Install dependencies via `pip install -r requirements.txt`.
2. Run the app using `python app.py`.
3. Access it at `http://127.0.0.1:8080/`.

After navigating to the homepage, users can upload an image, which the app processes and displays. The processed image is saved in the `output` folder. This project uses Flask for backend functionality, and Jinja2 for rendering the HTML frontend. Contributions are welcome; fork the repository and submit a pull request. The project is licensed under the MIT License.
