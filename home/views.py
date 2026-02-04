from django.shortcuts import render


# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def trigger_500(request):
    raise Exception("Intentional 500 error for testing")
