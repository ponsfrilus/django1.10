from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    is_valid = False
    for prefix in ('', 'http://'):
        try:
            new_value = prefix + value
            url_validator(new_value)
            is_valid = True
            break
        except:
            pass
    if not is_valid:
        raise ValidationError("Invalid URL for this field")
    return new_value

def validate_url_epfl(value):
    if not "epfl.ch" in value:
        raise ValidationError("This only works for epfl URLs")
