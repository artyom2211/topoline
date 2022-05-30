from django.shortcuts import render

def index(request):
    return render(request, 'page1app/homepage.html')


def contact(request):
    return render(request, 'page1app/basic.html', {'values': ['Есть вопросы задай их по телефону', '068 345 67 56']})