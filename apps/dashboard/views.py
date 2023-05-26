from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from apps.proposal.models import Proposal
from django.shortcuts import render, redirect, get_object_or_404
from apps.members.forms import MembersForm
from apps.members.models import Members
from django.views import generic
from django.contrib import messages
from apps.publication.forms import ArticlesForm, PresentationsForm, BooksForm, OnlineForm
from apps.publication.models import Articles, Presentations, Books, Online


@login_required
def dashboard_base(request):
    profile = Members.objects.get(user=request.user)
    return render(request, 'dashboard/dashboard_base.html', {'profile': profile})


@login_required
def article_list(request):
    try:
        article = Members.objects.get(user=request.user)

    except Members.DoesNotExist:
        article = None
    return render(request, 'dashboard/article_list.html', {'article': article})


@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.creator = request.user
            article.save()
            co_editor_users = form.cleaned_data['co_editor']
            article.co_editor.set(co_editor_users)
            author_list_member = form.cleaned_data['author_list']
            article.author_list.set(author_list_member)
            messages.success(request, 'Article created successfully')
            return redirect('dashboard:article_list')
    else:
        form = ArticlesForm()
    return render(request, "dashboard/article_create.html", {'form': form})


@login_required
def article_edit(request, pk):
    member = Members.objects.get(user=request.user)
    article = get_object_or_404(Articles, id=pk)
    if not (request.user == article.creator or member in article.author_list.all()):
        raise PermissionDenied
    if request.method == 'POST':
        form = ArticlesForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            co_editor_users = form.cleaned_data['co_editor']
            article.co_editor.set(co_editor_users)
            author_list_member = form.cleaned_data['author_list']
            article.author_list.set(author_list_member)
            messages.success(request, 'Article updated successfully')
            return redirect('dashboard:article_list')

    else:
        form = ArticlesForm(instance=article)
    return render(request, 'dashboard/article_edit.html', {'form': form, 'article_id': pk})


@login_required
def article_delete(request, pk):
    article = get_object_or_404(Articles, id=pk, creator=request.user)
    article.delete()
    messages.success(request, 'Article deleted successfully')
    return redirect('dashboard:article_list')


@login_required
def presentation_list(request):
    try:
        presentation = Members.objects.get(user=request.user)

    except Members.DoesNotExist:
        presentation = None
    return render(request, 'dashboard/presentation_list.html', {'presentation': presentation})


@login_required
def presentation_create(request):
    if request.method == 'POST':
        form = PresentationsForm(request.POST, request.FILES)
        if form.is_valid():
            presentation = form.save(commit=False)
            presentation.creator = request.user
            presentation.save()
            co_editor_users = form.cleaned_data['co_editor']
            presentation.co_editor.set(co_editor_users)
            author_list_member = form.cleaned_data['author_list']
            presentation.author_list.set(author_list_member)
            messages.success(request, 'Presentation created successfully')
            return redirect('dashboard:presentation_list')
    else:
        form = PresentationsForm()
    return render(request, "dashboard/presentation_create.html", {'form': form})


@login_required
def presentation_edit(request, pk):
    member = Members.objects.get(user=request.user)
    presentation = get_object_or_404(Presentations, id=pk)
    if not (request.user == presentation.creator or member in presentation.author_list.all()):
        raise PermissionDenied
    if request.method == 'POST':
        form = PresentationsForm(request.POST, request.FILES or None, instance=presentation)
        if form.is_valid():
            presentation = form.save(commit=False)
            presentation.save()
            co_editor_users = form.cleaned_data['co_editor']
            presentation.co_editor.set(co_editor_users)
            author_list_member = form.cleaned_data['author_list']
            presentation.author_list.set(author_list_member)
            messages.success(request, 'Presentation updated successfully')
            return redirect('dashboard:presentation_list')

    else:
        form = PresentationsForm(instance=presentation)
    return render(request, 'dashboard/presentation_edit.html', {'form': form})


@login_required
def presentation_delete(request, pk):
    presentation = get_object_or_404(Presentations, id=pk, creator=request.user)
    presentation.delete()
    messages.success(request, 'Presentation deleted successfully')
    return redirect('dashboard:presentation_list')


@login_required
def book_list(request):
    try:
        book = Members.objects.get(user=request.user)

    except Members.DoesNotExist:
        presentation = None
    return render(request, 'dashboard/book_list.html', {'book': book})


@login_required
def book_create(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.creator = request.user
            book.save()
            co_editor_users = form.cleaned_data['co_editor']
            book.co_editor.set(co_editor_users)
            author_list_member = form.cleaned_data['author_list']
            book.author_list.set(author_list_member)
            messages.success(request, 'Book created successfully')
            return redirect('dashboard:book_list')
    else:
        form = BooksForm()
    return render(request, "dashboard/book_create.html", {'form': form})


@login_required
def book_edit(request, pk):
    member = Members.objects.get(user=request.user)
    book = get_object_or_404(Books, id=pk)
    if not (request.user == book.creator or member in book.author_list.all()):
        raise PermissionDenied
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES or None, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            co_editor_users = form.cleaned_data['co_editor']
            book.co_editor.set(co_editor_users)
            author_list_member = form.cleaned_data['author_list']
            book.author_list.set(author_list_member)
            messages.success(request, 'Book updated successfully')
            return redirect('dashboard:book_list')

    else:
        form = BooksForm(instance=book)
    return render(request, 'dashboard/book_edit.html', {'form': form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Presentations, id=pk, creator=request.user)
    book.delete()
    messages.success(request, 'Book deleted successfully')
    return redirect('dashboard:book_list')


@login_required
def online_list(request):
    try:
        online = Members.objects.get(user=request.user)

    except Members.DoesNotExist:
        presentation = None
    return render(request, 'dashboard/online_list.html', {'online': online})


@login_required
def online_create(request):
    if request.method == 'POST':
        form = OnlineForm(request.POST)
        if form.is_valid():
            online = form.save(commit=False)
            online.creator = request.user
            online.save()
            co_editor_users = form.cleaned_data['co_editor']
            online.co_editor.set(co_editor_users)
            author_list_member = form.cleaned_data['author_list']
            online.author_list.set(author_list_member)
            messages.success(request, 'Online created successfully')
            return redirect('dashboard:online_list')
    else:
        form = OnlineForm()
    return render(request, "dashboard/online_create.html", {'form': form})


@login_required
def online_edit(request, pk):
    member = Members.objects.get(user=request.user)
    online = get_object_or_404(Online, id=pk)
    if not (request.user == online.creator or member in online.author_list.all()):
        raise PermissionDenied
    if request.method == 'POST':
        form = OnlineForm(request.POST, instance=online)
        if form.is_valid():
            online = form.save(commit=False)
            online.save()
            co_editor_users = form.cleaned_data['co_editor']
            online.co_editor.set(co_editor_users)
            author_list_member = form.cleaned_data['author_list']
            online.author_list.set(author_list_member)
            messages.success(request, 'Online updated successfully')
            return redirect('dashboard:online_list')

    else:
        form = OnlineForm(instance=online)
    return render(request, 'dashboard/online_edit.html', {'form': form, 'online_id': pk})


@login_required
def online_delete(request, pk):
    book = get_object_or_404(Online, id=pk, creator=request.user)
    book.delete()
    messages.success(request, 'Online deleted successfully')
    return redirect('dashboard:online_list')


# update member profile information
@login_required
def member_profile(request):
    member = Members.objects.get(user=request.user)
    context = {
        'profile': member,
    }

    return render(request, 'dashboard/member_profile.html', context)


@login_required
def profile_edit(request):
    user = request.user
    member = Members.objects.get(user=request.user)
    form = MembersForm(request.POST or None, request.FILES or None, instance=member)
    if request.method == 'POST':
        if form.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            form.save()
            return redirect('dashboard:profile',)
    context = {
        'form': form,
        'profile': member
    }

    return render(request, 'dashboard/profile_edit.html', context)