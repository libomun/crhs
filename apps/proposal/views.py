from django.core.exceptions import PermissionDenied
from django.db.models import Q, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProposalForm, TeamForm, ReferencesForm, BudgetForm, WorkPlanForm, AppendicesForm
from .models import Proposal, Team, References, Budget, WorkPlan, Appendices


@login_required
def proposal_all(request):
    proposals = Proposal.objects.filter(Q(creator=request.user) | Q(co_pi=request.user)).distinct()
    draft_count = proposals.filter(status=Proposal.DRAFT).count()
    requiring_attention_count = proposals.filter(status=Proposal.REQUIRING_ATTENTION).count()
    under_review_count = proposals.filter(status=Proposal.UNDER_REVIEW).count()
    post_review_count = proposals.filter(status=Proposal.POST_REVIEW).count()
    withdrawn_count = proposals.filter(status=Proposal.WITHDRAWN).count()
    return render(request, 'proposal/proposal_all.html', {'proposals': proposals,
                                                  'draft_count': draft_count,
                                                  'requiring_attention_count': requiring_attention_count,
                                                  'under_review_count': under_review_count,
                                                  'post_review_count': post_review_count,
                                                  'withdrawn_count': withdrawn_count})


@login_required
def draft_proposals(request):
    proposal = Proposal.objects.filter(Q(creator=request.user) | Q(co_pi=request.user)).distinct()
    proposals = proposal.filter(status=Proposal.DRAFT)
    return render(request, 'proposal/proposal_draft.html', {'proposals': proposals})


@login_required
def requiring_attention_proposals(request):
    proposal = Proposal.objects.filter(Q(creator=request.user) | Q(co_pi=request.user)).distinct()
    proposals = proposal.filter(status=Proposal.REQUIRING_ATTENTION)
    return render(request, 'proposal/proposal_ra.html', {'proposals': proposals,})


@login_required
def under_review_proposals(request):
    proposal = Proposal.objects.filter(Q(creator=request.user) | Q(co_pi=request.user)).distinct()
    proposals = proposal.filter(status=Proposal.UNDER_REVIEW)
    return render(request, 'proposal/proposal_ur.html', {'proposals': proposals,})


@login_required
def post_review_proposals(request):
    proposal = Proposal.objects.filter(Q(creator=request.user) | Q(co_pi=request.user)).distinct()
    proposals = proposal.filter(status=Proposal.POST_REVIEW)
    return render(request, 'proposal/proposal_pr.html', {'proposals': proposals,})


@login_required
def withdrawn_proposals(request):
    proposal = Proposal.objects.filter(Q(creator=request.user) | Q(co_pi=request.user)).distinct()
    proposals = proposal.filter(status=Proposal.WITHDRAWN)
    return render(request, 'proposal/proposal_wd.html', {'proposals': proposals,})



@login_required
def proposal_create(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.creator = request.user
            proposal.save()
            # Get the selected users for each field
            pi_users = form.cleaned_data['pi']
            co_pi_users = form.cleaned_data['co_pi']
            referee_users = form.cleaned_data['referee']
            supervisor_users = form.cleaned_data['supervisor']
            secretary_users = form.cleaned_data['secretary']
            # Add the selected users to the proposal object
            proposal.pi.set(pi_users)
            proposal.co_pi.set(co_pi_users)
            proposal.referee.set(referee_users)
            proposal.supervisor.set(supervisor_users)
            proposal.secretary.set(secretary_users)
            messages.success(request, 'Proposal created successfully')
            return redirect('proposal:proposal_edit', pk=proposal.id)
    else:
        form = ProposalForm()
    return render(request, 'proposal/proposal_create.html', {'form': form})


@login_required
def proposal_edit(request, pk):
    proposal = get_object_or_404(Proposal, id=pk)
    if not (request.user == proposal.creator or request.user in proposal.co_pi.all()):
        raise PermissionDenied
    if request.method == 'POST':
        form = ProposalForm(request.POST, instance=proposal)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.save()
            # Get the selected users for each field
            pi_users = form.cleaned_data['pi']
            co_pi_users = form.cleaned_data['co_pi']
            referee_users = form.cleaned_data['referee']
            supervisor_users = form.cleaned_data['supervisor']
            secretary_users = form.cleaned_data['secretary']
            # Add the selected users to the proposal object
            proposal.pi.set(pi_users)
            proposal.co_pi.set(co_pi_users)
            proposal.referee.set(referee_users)
            proposal.supervisor.set(supervisor_users)
            proposal.secretary.set(secretary_users)
            messages.success(request, 'Proposal updated successfully')
            if proposal.status == 'DR':
                return redirect('proposal:draft_proposals')
            elif proposal.status == 'RA':
                return redirect('proposal:requiring_attention_proposals')
            elif proposal.status == 'WD':
                return redirect('proposal:withdrawn_proposals')
    else:
        form = ProposalForm(instance=proposal)
    return render(request, 'proposal/proposal_edit.html', {'form': form, 'proposal_id': pk})


@login_required
def proposal_delete(request, pk):
    proposal = get_object_or_404(Proposal, id=pk, creator=request.user)
    proposal.delete()
    messages.success(request, 'Proposal deleted successfully')
    return redirect('proposal:draft_proposals')


@login_required
def team_list(request, proposal_id):
    teams = Team.objects.filter(proposal=proposal_id)
    return render(request, 'proposal/team_list.html', {'teams': teams, 'proposal_id': proposal_id})


@login_required
def team_create(request, proposal_id):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.proposal_id = proposal_id  # set the proposal_id value before saving
            form.save()
            return redirect('proposal:team_list', proposal_id=proposal_id)
    else:
        form = TeamForm()
    return render(request, 'proposal/team_create.html', {'form': form, 'proposal_id': proposal_id})


@login_required
def team_edit(request, pk, proposal_id):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('proposal:team_list', proposal_id=proposal_id)
    else:
        form = TeamForm(instance=team)
    return render(request, 'proposal/team_edit.html', {'form': form,  'proposal_id': proposal_id})


@login_required
def team_delete(request, pk, proposal_id):
    team = get_object_or_404(Team, pk=pk)
    team.delete()
    return redirect('proposal:team_list', proposal_id=proposal_id)


@login_required
def references_list(request, proposal_id):
    references = References.objects.filter(proposal=proposal_id)
    return render(request, 'proposal/references_list.html', {'references': references, 'proposal_id': proposal_id})


@login_required
def references_create(request, proposal_id):
    if request.method == 'POST':
        form = ReferencesForm(request.POST)
        if form.is_valid():
            reference = form.save(commit=False)
            reference.proposal_id = proposal_id  # set the proposal_id value before saving
            form.save()
            return redirect('proposal:references_list', proposal_id=proposal_id)
    else:
        form = ReferencesForm()
    return render(request, 'proposal/references_create.html', {'form': form, 'proposal_id': proposal_id})


@login_required
def references_edit(request, pk, proposal_id):
    reference = get_object_or_404(References, pk=pk)
    if request.method == 'POST':
        form = ReferencesForm(request.POST, instance=reference)
        if form.is_valid():
            form.save()
            return redirect('proposal:references_list', proposal_id=proposal_id)
    else:
        form = ReferencesForm(instance=reference)
    return render(request, 'proposal/references_edit.html', {'form': form, 'proposal_id': proposal_id, 'pk': pk})


@login_required
def references_delete(request, pk, proposal_id):
    reference = get_object_or_404(References, pk=pk)
    reference.delete()
    return redirect('proposal:references_list', proposal_id=proposal_id)


@login_required
def budget_list(request, proposal_id):
    budgets = Budget.objects.filter(proposal=proposal_id)
    total_cost = budgets.aggregate(Sum('cost'))['cost__sum'] or 0
    return render(request, 'proposal/budget_list.html', {'budgets': budgets, 'proposal_id': proposal_id, 'total_cost': total_cost})


@login_required
def budget_create(request, proposal_id):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.proposal_id = proposal_id  # set the proposal_id value before saving
            form.save()
            return redirect('proposal:budget_list', proposal_id=proposal_id)
    else:
        form = BudgetForm()
    return render(request, 'proposal/budget_create.html', {'form': form, 'proposal_id': proposal_id})


@login_required
def budget_edit(request, pk, proposal_id):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('proposal:budget_list', proposal_id=proposal_id)
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'proposal/budget_edit.html', {'form': form, 'proposal_id': proposal_id, 'pk': pk})


@login_required
def budget_delete(request, pk, proposal_id):
    budget = get_object_or_404(Budget, pk=pk)
    budget.delete()
    return redirect('proposal:budget_list', proposal_id=proposal_id)


@login_required
def workplan_list(request, proposal_id):
    workplans = WorkPlan.objects.filter(proposal=proposal_id)
    return render(request, 'proposal/workplan_list.html', {'workplans': workplans, 'proposal_id': proposal_id})


@login_required
def workplan_create(request, proposal_id):
    if request.method == 'POST':
        form = WorkPlanForm(request.POST)
        if form.is_valid():
            workplan = form.save(commit=False)
            workplan.proposal_id = proposal_id  # set the proposal_id value before saving
            form.save()
            return redirect('proposal:workplan_list', proposal_id=proposal_id)
    else:
        form = WorkPlanForm()
    return render(request, 'proposal/workplan_create.html', {'form': form, 'proposal_id': proposal_id})


@login_required
def workplan_edit(request, pk, proposal_id):
    workplan = get_object_or_404(WorkPlan, pk=pk)
    if request.method == 'POST':
        form = WorkPlanForm(request.POST, instance=workplan)
        if form.is_valid():
            form.save()
            return redirect('proposal:workplan_list', proposal_id=proposal_id)
    else:
        form = WorkPlanForm(instance=workplan)
    return render(request, 'proposal/workplan_edit.html', {'form': form, 'proposal_id': proposal_id, 'pk': pk})


@login_required
def workplan_delete(request, pk, proposal_id):
    workplan = get_object_or_404(WorkPlan, pk=pk)
    workplan.delete()
    return redirect('proposal:workplan_list', proposal_id=proposal_id)


@login_required
def appendices_list(request, proposal_id):
    appendices = Appendices.objects.filter(proposal=proposal_id)
    return render(request, 'proposal/appendices_list.html', {'appendices': appendices, 'proposal_id': proposal_id})


@login_required
def appendices_create(request, proposal_id):
    if request.method == 'POST':
        form = AppendicesForm(request.POST, request.FILES)
        if form.is_valid():
            appendices = form.save(commit=False)
            appendices.proposal_id = proposal_id  # set the proposal_id value before saving
            form.save()
            return redirect('proposal:appendices_list', proposal_id=proposal_id)
    else:
        form = AppendicesForm()
    return render(request, 'proposal/appendices_create.html', {'form': form, 'proposal_id': proposal_id})


@login_required
def appendices_edit(request, pk, proposal_id):
    appendices = get_object_or_404(Appendices, pk=pk)
    if request.method == 'POST':
        form = AppendicesForm(request.POST, request.FILES, instance=appendices)
        if form.is_valid():
            form.save()
            return redirect('proposal:appendices_list', proposal_id=proposal_id)
    else:
        form = AppendicesForm(instance=appendices)
    return render(request, 'proposal/appendices_edit.html', {'form': form, 'proposal_id': proposal_id, 'pk': pk})


@login_required
def appendices_delete(request, pk, proposal_id):
    appendices = get_object_or_404(Appendices, pk=pk)
    appendices.delete()
    return redirect('proposal:appendices_list', proposal_id=proposal_id)
