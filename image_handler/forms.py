from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div
from .models import RecipeImage


class RecipeImageUploadForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['name', 'type', 'description', 'alt_description', 'image_file']

    def __init__(self, *args, **kwargs):
        recipe_id = kwargs.pop('recipe_id', None)
        super(RecipeImageUploadForm, self).__init__(*args, **kwargs)

        if recipe_id is not None:
            main_image_exists = RecipeImage.objects.filter(recipe_id=recipe_id, type='main_image').exists()
            if main_image_exists:
                self.fields['type'].choices = [choice for choice in self.fields['type'].choices if choice[0] != 'main_image']

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'type',
            'description',
            'alt_description',
            'image_file',
            Div(
                Submit('submit', 'Upload', css_class='btn-primary'),
                HTML('<button type="button" class="btn btn-secondary ml-2" onclick="history.back()">Go Back</button>'),
                css_class='d-flex justify-content-between'
            )
        )
