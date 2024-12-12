from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
def game_bar(request):
    return render(request, "page3.html")


def game_render(request, id):
    return render(request, f"game_{id}.html")
