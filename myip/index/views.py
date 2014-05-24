from django.shortcuts import render


def home(request):
    return render(request, "index.html",
                  {"remote_ip": request.META["REMOTE_ADDR"]})
