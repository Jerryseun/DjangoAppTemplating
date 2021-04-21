from django.shortcuts import render

def home_view(request):
    food = "Bread"
    return render(
        request,
        "home.html",
        {"food": food}
    )
