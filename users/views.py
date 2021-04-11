from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from .forms import CustomUserCreationForm


# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request):
    if request.method == 'GET':
        return render(
            request, 'users/register.html',
            {'form': CustomUserCreationForm}
        )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            login(request, user)
            return redirect(reverse('dashboard'))


def see_request(request):
    text = f"""
        Some attributes of the HttpRequest object:

        scheme: {request.scheme}
        path: {request.path}
        method: {request.method}
        GET: {request.GET}
        POST: {request.POST}
        user: {request.user}
      """
    return HttpResponse(text, content_type='application/json')


def user_info(request):
    text = f"""
      Selected HttpRequest.user attributes:
      username: {request.user.username}
      is_anonymous: {request.user.is_anonymous}
      is_staff: {request.user.is_staff}
      is_superuser: {request.user.is_superuser}
      is_active: {request.user.is_active}
    """
    return HttpResponse(text, content_type='application/json')


@login_required
def private_route(request):
    return HttpResponse('For members only!', content_type='application/json')


@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse('Employees must wash hands',
                        content_type='application/json')


@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f'Hello {username}!')
    messages.add_message(request, messages.WARNING, 'Danger will Robinson')
    return HttpResponse('Messages added', content_type='application/json')
