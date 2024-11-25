from django import forms
from .models import ImageUpload, Client

# Form to handle client information (name, email, phone)
class ClientForm(forms.ModelForm):
    class Meta:
        # The model we are creating the form for is 'Client'
        model = Client
        # Fields to be included in the form (name, email, phone)
        fields = ['name', 'email', 'phone']

# Form to handle image uploads (the file input)
class ImageUploadForm(forms.ModelForm):
    class Meta:
        # The model we are creating the form for is 'ImageUpload'
        model = ImageUpload
        # The form will include the 'image' field (the uploaded file)
        fields = ['image']
