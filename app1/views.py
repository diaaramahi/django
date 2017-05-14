from django.shortcuts import render

def index(request):
    context = {
        "employees": [
            {
                "first_name": "Diaa",
                "last_name": "Ramahi"
            },
            {
                "first_name": "Talal",
                "last_name": "Talal"
            }
        ]
    }
    return render(request, 'app1/index.html', context)
