from django.shortcuts import render
from .forms import ImageUploadForm, ClientForm
from .models import ImageUpload, Client
from django.http import JsonResponse
import numpy as np  # pip install numpy
import cv2  # pip install opencv-python
import os
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML  # pip install weasyprint
from django.conf import settings  # For accessing MEDIA_URL

# Main view function to handle the form submission and image processing
def index(request):
    if request.method == 'POST':
        # Initialize the client and image upload forms with POST data
        client_form = ClientForm(request.POST)
        image_form = ImageUploadForm(request.POST, request.FILES)
        
        # Check if both forms are valid
        if client_form.is_valid() and image_form.is_valid():
            # Save the client data from the form
            client = client_form.save()
            
            # Save the uploaded image, but do not commit to the database yet
            image_upload = image_form.save(commit=False)
            # Associate the uploaded image with the client
            image_upload.client = client
            image_upload.save()

            # Process the uploaded image to generate a heatmap
            img = cv2.imread(image_upload.image.path)  # Read the uploaded image
            heatmap = create_heatmap(img)  # Create the heatmap for the image
            heatmap_path = save_heatmap(heatmap)  # Save the heatmap

            # Use the build_absolute_uri method to get the full URL for the heatmap
            heatmap_url = settings.MEDIA_URL + heatmap_path

            # Generate a PDF with the client's information, the original image, and the heatmap
            pdf_response = generate_pdf(request, client, image_upload, heatmap_url)
            return pdf_response

    else:
        # Initialize empty forms when the page is loaded without a POST request
        client_form = ClientForm()
        image_form = ImageUploadForm()

    # Render the 'index.html' template with the forms passed as context
    return render(request, 'index.html', {'client_form': client_form, 'image_form': image_form})


def create_heatmap(image):
    """
    Create a heatmap for the given image by converting it to grayscale,
    applying a Gaussian blur, and then using a colormap.
    """
    # Convert the image to grayscale to simplify the analysis
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to smooth the image and reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Normalize the blurred image to scale pixel values between 0 and 255
    normalized_image = cv2.normalize(blurred_image, None, 0, 255, cv2.NORM_MINMAX)

    # Apply the "HOT" colormap to create a heatmap from the normalized grayscale image
    heatmap = cv2.applyColorMap(normalized_image, cv2.COLORMAP_HOT)

    # Apply a Gaussian blur to the heatmap to create smoother transitions between colors
    heatmap = cv2.GaussianBlur(heatmap, (5, 5), 0)

    # Return the generated heatmap
    return heatmap


def save_heatmap(heatmap):
    """
    Save the generated heatmap to the media directory and return its file path.
    """
    # Define the file path where the heatmap will be saved
    heatmap_path = os.path.join(settings.MEDIA_ROOT, 'uploads/heatmap.png')
    
    # Ensure the directory exists, if not create it
    os.makedirs(os.path.dirname(heatmap_path), exist_ok=True)
    
    # Save the heatmap image to the specified path
    cv2.imwrite(heatmap_path, heatmap)
    
    # Return the relative path to the heatmap image
    return os.path.join('uploads', 'heatmap.png')


def generate_pdf(request, client, image_upload, heatmap_url):
    """
    Generate a PDF with the client's information, the original image, and the heatmap.
    """
    # Create the absolute URL for the original image
    original_image_url = request.build_absolute_uri(image_upload.image.url)
    
    # Create the absolute URL for the heatmap image
    heatmap_image_url = request.build_absolute_uri(heatmap_url)

    # Render the HTML template for the PDF, passing client data and image URLs
    html_string = render_to_string('pdf_template.html', {
        'client': client,
        'image_upload': image_upload,
        'original_image_url': original_image_url,
        'heatmap_url': heatmap_image_url  # Ensure the heatmap URL is passed correctly
    })
    
    # Create an HTTP response with the 'application/pdf' content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="report_{client.name}.pdf"'
    
    # Generate the PDF from the HTML string using WeasyPrint
    HTML(string=html_string).write_pdf(response)
    
    # Return the PDF response to be downloaded
    return response
