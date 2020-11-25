from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/accounts/login/')
def user_info(request):
    current_user = request.user
    context = {"current_user": current_user}
    return render(request, 'user/user_info.html', context=context)