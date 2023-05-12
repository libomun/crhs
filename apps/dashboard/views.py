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
    # proposals = Proposal.objects.filter(Q(creator=request.user) | Q(co_pi=request.user)).distinct()
    # draft_count = proposals.filter(status=Proposal.DRAFT).count()
    # requiring_attention_count = proposals.filter(status=Proposal.REQUIRING_ATTENTION).count()
    # under_review_count = proposals.filter(status=Proposal.UNDER_REVIEW).count()
    # post_review_count = proposals.filter(status=Proposal.POST_REVIEW).count()
    # withdrawn_count = proposals.filter(status=Proposal.WITHDRAWN).count()
    return render(request, 'dashboard/dashboard_base.html', {'profile': profile})
                                                  # 'draft_count': draft_count,
                                                  # 'requiring_attention_count': requiring_attention_count,
                                                  # 'under_review_count': under_review_count,
                                                  # 'post_review_count': post_review_count,
                                                  # 'withdrawn_count': withdrawn_count})


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
    return render(request, 'dashboard/my_book.html', {'article': book})


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
            return redirect('dashboard:dashboard_base',)
    context = {
        'form': form,
    }

    return render(request, 'dashboard/profile_edit.html', context)