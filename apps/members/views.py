from django.views import generic
from django.db.models import Q
from .models import Members


# All members List view
class MembersListView(generic.ListView):
    template_name = 'members/member_all.html'
    queryset = Members.objects.filter(Q(is_active=True)).order_by('first_name')
    paginate_by = 6


# Faculty List view
class FacultyListView(generic.ListView):
    template_name = 'members/member_staff.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(role__exact='faculty')).order_by('first_name')
    paginate_by = 6


# Staff List view
class StaffListView(generic.ListView):
    template_name = 'members/member_staff.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(role__exact='staff')).order_by('first_name')
    paginate_by = 6


# RA List view
class RAListView(generic.ListView):
    template_name = 'members/member_ra.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(role__exact='ra')).order_by('first_name')
    paginate_by = 6


# GraduateList view
class GraduateListView(generic.ListView):
    template_name = 'members/member_graduate.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(role__exact='graduate')).order_by('first_name')
    paginate_by = 6


# Undergrad List view
class UndergradListView(generic.ListView):
    template_name = 'members/member_undergrad.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(role__exact='undergraduate')).order_by('first_name')
    paginate_by = 6


# Postdoc List view
class PostdocListView(generic.ListView):
    template_name = 'members/member_postdoc.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(role__exact='postdocs')).order_by('first_name')
    paginate_by = 6


# Alumni List view
class AlumniListView(generic.ListView):
    template_name = 'members/member_alumni.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(role__exact='alumni')).order_by('first_name')
    paginate_by = 6


# Personnel Detail View
class MembersDetailView(generic.DetailView):
    model = Members
    template_name = 'members/member_detail.html'


# Alumni Detail View
class AlumniDetailView(generic.DetailView):
    model = Members
    template_name = 'members/alumni_detail.html'


# Search view
class SearchMemberView(generic.ListView):
    paginate_by = 6
    template_name = 'members/member_search.html'

# return search Rural360 result
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Members.objects.order_by('first_name').filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(title__icontains=query) | Q(affiliation__icontains=query)
            )
        return object_list

# add query content in  context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
