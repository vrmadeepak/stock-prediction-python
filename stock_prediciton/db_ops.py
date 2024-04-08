from user.models import User

def create_user(email, password):
    return User.objects.create(email=email, password=password)

def get_user(email):
    return User.objects.filter(email__iexact=email).first()

def validate_user(email, password):
    return User.objects.filter(email__iexact=email, password=password).first()

