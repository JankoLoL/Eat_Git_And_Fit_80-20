from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import RecipeImage


class RecipeImageUploadForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['name', 'type', 'description', 'alt_description', 'image_file']

    def __init__(self, *args, **kwargs):
        super(RecipeImageUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'type',
            'description',
            'alt_description',
            'image_file',
            Submit('submit', 'Upload', css_class='btn-primary')
        )
