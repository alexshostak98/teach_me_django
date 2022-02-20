from django.shortcuts import render, redirect

from .forms.add_publication_form import AddPublicationForm

from .models import Post


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-create_date', '-id').all()
    context = {'title': 'First django_app', 'posts': posts}
    return render(request, "mainpage.html", context)


def add_publication_page(request):
    if request.method == 'POST':
        form = AddPublicationForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(**form.cleaned_data)
            post.save()
            return redirect('/')
    else:
        form = AddPublicationForm()
    context = {'title': 'add_publication', 'add_post_form': form}
    return render(request, "add_publication_page.html", context)
