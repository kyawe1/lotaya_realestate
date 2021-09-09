from django.contrib.auth.decorators import user_passes_test

def checkloggedin(request):
    if request.user.is_authenticated:
        return False
    else :
        return True
