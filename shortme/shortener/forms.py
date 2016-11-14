from django import forms

from .validators import validate_url, validate_url_epfl


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label="Submit URL", validators=[validate_url, validate_url_epfl])

    # def clean(self):
    #     '''
    #     Validate the form
    #     '''
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     print(cleaned_data)
    #
    # def clean_url(self):
    #     '''
    #     Validate the field
    #     '''
    #     url = self.cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL")
    #
    #     if not "epfl.ch" in url:
    #         raise forms.ValidationError("Invalid URL, this is only for URLS inside epfl.")
    #
    #     return url
