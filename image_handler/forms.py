from django import forms
from .models import RecipeImage


class RecipeImageUploadForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['name', 'type', 'description', 'alt_description', 'image_file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'alt_description': forms.TextInput({'class': 'form-control'}),
            'image_file': forms.FileInput(attrs={'class': 'form-control'}),
        }
