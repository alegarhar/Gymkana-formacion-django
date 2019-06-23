from django import forms

from .models import New
from django.core.validators import FileExtensionValidator
from .validators import FileLimitSize


class NewNews(forms.ModelForm):
    image = forms.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), FileLimitSize(limit_value=10)], required=False)

    class Meta:
        model = New
        fields = ('title', 'subtitle', 'body', 'image')
