from django.contrib.auth.decorators import login_required
from django.db.models import Q
from apps.proposal.models import Proposal
from django.shortcuts import render, redirect
from apps.members.forms import MembersForm
from apps.members.models import Members
from django.views import generic


@login_required
def dashboard_base(request):
    profile = Members.objects.get(user=request.user)
    return render(request, 'dashboard/dashboard_base.html', {'profile': profile})


def my_article(request):
    try:
        article = Members.objects.get(user=request.user)
    except Members.DoesNotExist:
        article = None
    return render(request, 'dashboard/my_article.html', {'article': article})


def my_presentation(request):
    try:
        presentation = Members.objects.get(user=request.user)
    except Members.DoesNotExist:
        presentation = None
    return render(request, 'dashboard/my_presentation.html', {'presentation': presentation})


def my_book(request):
    try:
        book = Members.objects.get(user=request.user)
    except Members.DoesNotExist:
        book = None
    return render(request, 'dashboard/my_book.html', {'book': book})


def my_online(request):
    try:
        online = Members.objects.get(user=request.user)
    except Members.DoesNotExist:
        online = None
    return render(request, 'dashboard/my_online.html', {'online': online})


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