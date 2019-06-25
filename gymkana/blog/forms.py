from django import forms
from .models import New, Event
from django.core.validators import FileExtensionValidator
from .validators import FileLimitSize


class NewNews(forms.ModelForm):
    image = forms.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), FileLimitSize(limit_value=10)], required=False)

    class Meta:
        model = New
        fields = ('id', 'title', 'image', 'subtitle', 'body',)


class NewEvents(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))
    end_date = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Event
        fields = ('id', 'title', 'subtitle', 'body', 'start_date', 'end_date')

    def clean(self):
        cleaned_data = super().clean()
        cc_start_date = cleaned_data.get("start_date")
        cc_end_date = cleaned_data.get("end_date")

        if cc_start_date > cc_end_date:
            raise forms.ValidationError("Start date should be before end time")
