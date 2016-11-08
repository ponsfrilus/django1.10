import string
import random

def generate_code(size):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def create_short_url(instance, size=6):
    while True:
        new_code = generate_code(size)
        # Note :
        # with instance.__class__ we can have access to ShortURL without importing it
        # ... it couldn't be possible otherwise (circular import)
        code_already_exists = instance.__class__.objects.filter(shortcode=new_code).exists()
        if not code_already_exists:
            return new_code
        else:
            print("Collision for code : " + new_code)
