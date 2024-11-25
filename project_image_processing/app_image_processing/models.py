import os
import time
from django.db import models
from django.core.exceptions import ValidationError

# Model for the client (person who uploads the image)
class Client(models.Model):
    # Name of the client
    name = models.CharField(max_length=100)

    # Email address of the client
    email = models.EmailField()

    # Phone number of the client
    phone = models.CharField(max_length=15)

    def __str__(self):
        # Return the name of the client when this object is printed
        return self.name


MAX_DATABASE_SIZE = 15  # Database registry limit

def generate_image_filename(instance, filename):
    """
    Function that generates a unique file name based on a timestamp and the client’s name.
    """
    # Get the client name and replace spaces with underscores, then lowercase it
    client_name = instance.client.name.replace(" ", "_").lower()

    # Create a unique timestamp (in seconds)
    timestamp = int(time.time())  # Timestamp in seconds

    # Get the file extension from the original file
    file_extension = os.path.splitext(filename)[1]  # Get file extension (e.g., .jpg, .png)

    # Generate a new filename using the timestamp and client name
    new_filename = f"{timestamp}_{client_name}{file_extension}"

    # Return the complete path where the file will be stored
    return os.path.join('uploads/', new_filename)


# Model for uploaded images
class ImageUpload(models.Model):
    # The uploaded image file
    image = models.ImageField(upload_to=generate_image_filename)

    # Date and time when the image was uploaded (automatically set when a new image is uploaded)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # Foreign key relationship to the 'Client' model
    # Each uploaded image is associated with a client
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Check the total number of records in the database before saving the new object
        total_count = ImageUpload.objects.count()
        if total_count >= MAX_DATABASE_SIZE:
            raise ValidationError(f"The database has reached its maximum size of {MAX_DATABASE_SIZE} records. Please delete some images before uploading new ones.")
        
        # If validation passes, save the object
        super().save(*args, **kwargs)

    def __str__(self):
        # Return the image name when this object is printed
        return self.image.name
