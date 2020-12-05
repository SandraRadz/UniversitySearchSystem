from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/accounts/login/')
def user_info(request):
    current_user = request.user
    context = {"current_user": current_user}
    return render(request, 'users/user_info.html', context=context)


def login_view(request):
    return None


def logout_view(request):
    return None


def register(request):
    return None


def create_password(request):
    return None


def personal_information(request):
    return None


def edit_personal_information(request):
    return None