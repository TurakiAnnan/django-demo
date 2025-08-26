from django.shortcuts import render

# Create your views here.

def home(request):
    city = request.GET.get("city", "").strip()
    return render(request, "weather/home.html", {"city": city})
