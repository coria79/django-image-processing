# Image Processing Web Application - Django

---

### Explanation of Sections:

1. **Introduction**: A clear summary of the project's purpose and main functionality.
2. **Installation**: Details on how to set up the project in your local environment, including creating the virtual environment and installing dependencies.
3. **Configuration**: Configuration of the database and media files.
4. **Running the Application**: Instructions for running the development server.
5. **Using the Application**: Steps to interact with the application through the web interface.
6. **Project Files**: Mention of the main project files (without showing the code, so users can view it directly in the repository).
7. **Contributions**.
8. **License**: Mention of the project's license.
9. **Acknowledgments**.

## Introduction

This project's main goal is to create a **Django web application** that allows users to:

- **Upload images**: Users can upload images from their devices.
- **Process the images**: The application generates a heatmap (although in the current code, it generates an empty image, in real scenarios, the image could be processed to create a visual heatmap).
- **Generate PDF reports**: After processing the image, a PDF report is generated with the client data and a link to the processed image (e.g., the generated heatmap).

### Key Features

- **Image upload**: Users can upload images through a form.
- **Storing images and client data**: The application stores both client data (name, email, phone) and uploaded images.
- **Heatmap generation**: Although the current code does not implement real processing, the goal is to generate a heatmap from the uploaded images, which is commonly used in image analysis, computer vision, and more.
- **PDF report generation**: A PDF file is generated with the client's data and the processed image, which can be downloaded.
- **Web interface**: The application is accessible via a browser, allowing users to interact with the forms.

### Summary

This is a **web application** that allows users to:

1. Upload images of their choice.
2. Process them (e.g., by creating a heatmap).
3. Generate a **PDF report** with the client's data and the processed image.

### Potential Applications

This type of platform is useful in various fields, such as:

- **Image analysis**: For medical images, scientific research, or spatial data visualization.
- **Customer information management**: Storing contact data and performing analysis or image visualization.
- **Automatic report generation**: These reports can be downloaded or sent as PDF files.

---

## Installation

### Prerequisites

Make sure you have **Python** and **Django** installed on your system. You will also need some additional dependencies to handle images and generate PDFs.

#### Install dependencies

1. Clone the repository:

```bash
git clone https://github.com/your_user/image-processing-django.git
cd image-processing-django
```
2. Create a virtual environment and activate it (optional but recommended):

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate
```
3. Install the project dependencies:

```bash
pip install -r requirements.txt
```
This **requirements.txt** file should contain the following essential packages:

```bash
Django==4.x
opencv-python==4.x
numpy==1.x
weasyprint==52.x
```

---

## Project Configuration

1. Database: This project uses SQLite by default. No additional configuration is required to use SQLite, but if you'd like to use another database system (like PostgreSQL or MySQL), you will need to update the configuration in **settings.py**.

2. Static and media files: The project is configured to serve static files and media files (such as uploaded images and generated PDF reports) during development.

    Make sure to create the **media/** folder in the root directory of your project to store images and generated heatmaps.

```bash
mkdir media
```

Also, ensure that your **static/** folder is set up correctly, as it will store static files like custom CSS files.

```bash
mkdir static/css
```

3. Configuring **settings.py**: Open the settings.py file in the project and add the following lines to ensure Django handles static and media files correctly:

```bash
# Media files (for the uploaded images and generated heatmaps)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files (CSS and other files)
STATIC_URL = '/static/'

# Static files folder
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Ensure Django can find the static folder
]
```

---
## Migrate the Database
Before running the server, perform the migrations to create the necessary tables in the database:

```bash
python manage.py migrate
```
---
## Running the Development Server
To run the Django development server:

```bash
python manage.py runserver
```
This will start the server at **http://127.0.0.1:8000/** (or the URL shown in the terminal).

---
## Using the Application
1. Access the application through your browser at **http://127.0.0.1:8000/**
2. Complete the form with the client's data (name, email, phone).
3. Upload the image from your device.
4. The system will process the image and generate a heatmap (currently empty).
5. The report will be generated in PDF format, including the client's data and the processed image (heatmap).

## Project Files
You can view the details of the files in the repository to understand the project structure. Below are the main files in the project:

- **models.py**: Defines the data models for the application (client and image).
- **forms.py**: Defines the forms used to upload images and collect client information.
- **views.py**: Handles the logic for the views, including image upload, processing, and PDF generation.
- **index.html**: HTML template for the image upload form and client data input.
- **pdf_template.html**: HTML template for generating the PDF report with client data and the processed image.
---
## Contributions
If you'd like to contribute to the project, please follow these steps:

- Fork this repository.
- Create a new branch (**git checkout -b feature/new-feature**).
- Make your changes.
- Commit your changes (**git commit -am 'Added new feature'**).
- Push the branch (**git push origin feature/new-feature**).
- Open a Pull Request.

---
## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---
## Acknowledgments

Thank you for reviewing this project. I hope you find the application useful! If you have any suggestions or improvements, feel free to open an issue or pull request.