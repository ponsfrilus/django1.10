from django import forms

from .validators import validate_url, validate_url_epfl


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label="Submit URL", validators=[validate_url, validate_url_epfl])

    # def clean(self):
    #     '''
    #     Clean the form
    #     '''
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     print(cleaned_data)

    def clean_url(self):
        '''
        Clean the field 'url'
        '''
        url = self.cleaned_data['url']
        url = validate_url(url)
        return url
