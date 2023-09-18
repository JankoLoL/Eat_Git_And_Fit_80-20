from django import forms
from .models import Recipe, Category, Occasion, Cuisine, Ingredients, RecipeIngredients, RecipeCategory, RecipeOccasion

from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RecipeIngredientsForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ['ingredients', 'quantity', 'measure']


RecipeIngredientsFormset = inlineformset_factory(
    Recipe,
    RecipeIngredients,
    form=RecipeIngredientsForm,
    extra=1,
    widgets={
        'ingredients': forms.Select,
        'quantity': forms.NumberInput(attrs={'min': 1}),
        'measure': forms.Select,
    }
)


class RecipeAddForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    occasion = forms.ModelMultipleChoiceField(queryset=Occasion.objects.all(), widget=forms.CheckboxSelectMultiple)
    cuisine = forms.ModelMultipleChoiceField(queryset=Cuisine.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'instructions', 'category', 'occasion', 'cuisine']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        user = authenticate(**cleaned_data)
        if user is None:
            raise ValidationError('Incorrect login or password')
        cleaned_data['user'] = user
        return cleaned_data


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='password1')
    password2 = forms.CharField(widget=forms.PasswordInput, label='password2')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Passwords are not equal')
        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email']
