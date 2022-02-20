from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from .forms.registration import RegistrationForm
from .forms.authorization import AuthorizationForm
from .forms.edit_profile import EditProfileForm, EditUserForm


def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "title": "Registration", "reg_form": RegistrationForm()
    }
    return render(request, "registration_page.html", context)


def authorization_page(request):
    error = False
    if request.method == 'POST':
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('/profile/')
            error = True
    else:
        form = AuthorizationForm()
    context = {"title": "Authorization", "auth_form": form, 'error': error}
    return render(request, "authorization_page.html", context)


# TODO: Поправить ошибку анонимности пользователя после смены пароля
def profile_page(request):
    user = request.user
    profile = user.profile
    context = {'title': 'Profile', 'user': user, 'profile': profile}
    return render(request, "profile_page.html", context)


def edit_profile_page(request):
    error = False
    user = request.user
    profile = request.user.profile
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user)
        profile_form = EditProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            # profile_form.save()
            if user_form.save() is not None:
                profile_form.save()
                return redirect('/')
            error = True
    else:
        user_form = EditUserForm(instance=user)
        profile_form = EditProfileForm(instance=profile)
    context = {
        "title": "Edit profile",
        "edit_user_form": user_form,
        "edit_profile_form": profile_form,
        'error': error
    }
    return render(request, "edit_profile_page.html", context)
