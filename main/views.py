from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhammad Madhani Putra',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)