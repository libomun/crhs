from django.views import generic
from django.db.models import Q
from .models import Members


# All members List view
class MembersListView(generic.ListView):
    template_name = 'members/member_index.html'
    queryset = Members.objects.filter(is_active=True).order_by('member_number')
    paginate_by = 6


# Faculty List view
class FacultyListView(generic.ListView):
    template_name = 'members/member_staff.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(is_faculty=True)).order_by('member_number')
    paginate_by = 6


# Staff List view
class StaffListView(generic.ListView):
    template_name = 'members/member_staff.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(is_staff=True)).order_by('member_number')
    paginate_by = 6


# RA List view
class RAListView(generic.ListView):
    template_name = 'members/member_ra.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(is_ra=True)).order_by('member_number')
    paginate_by = 6


# GraduateList view
class GraduateListView(generic.ListView):
    template_name = 'members/member_graduate.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(is_graduate=True)).order_by('member_number')
    paginate_by = 6


# Undergrad List view
class UndergradListView(generic.ListView):
    template_name = 'members/member_undergrad.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(is_undergrad=True)).order_by('member_number')
    paginate_by = 6


# Postdoc List view
class PostdocListView(generic.ListView):
    template_name = 'members/member_postdoc.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(is_postdocs=True)).order_by('member_number')
    paginate_by = 6


# Alumni List view
class AlumniListView(generic.ListView):
    template_name = 'members/member_alumni.html'
    queryset = Members.objects.filter(Q(is_active=True) & Q(is_alumni=True)).order_by('member_number')
    paginate_by = 6


# Personnel Detail View
class MembersDetailView(generic.DetailView):
    model = Members
    template_name = 'members/member_detail.html'


# Personnel Detail View
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
        object_list = Members.objects.order_by('member_number').filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(title__icontains=query) | Q(affiliation__icontains=query)
            )
        return object_list

# add query content in  context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

