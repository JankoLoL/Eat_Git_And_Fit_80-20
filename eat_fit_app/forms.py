from .models import Recipe, Category, Occasion, Cuisine, Ingredients, RecipeIngredients, RecipeCategory, RecipeOccasion
from django import forms
from django.forms import inlineformset_factory



class RecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    occasion = forms.ModelChoiceField(
        queryset=Occasion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cuisine = forms.ModelChoiceField(
        queryset=Cuisine.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
    instructions = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'instructions', 'category', 'occasion', 'cuisine']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}),
        }


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ['ingredients', 'quantity', 'measure']
        widgets = {
            'ingredients': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'measure': forms.Select(attrs={'class': 'form-control'}),
        }


RecipeIngredientFormSet = inlineformset_factory(Recipe, RecipeIngredients, form=RecipeIngredientForm, extra=1)


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
