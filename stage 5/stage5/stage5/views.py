



from django.http import HttpResponse


def main_view(request):
    return HttpResponse("""<h1> KODECAMP </h1>""")