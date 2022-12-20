from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import CommentForm
from .models import News, Comment


# News list view
class NewsListView(generic.ListView):
    template_name = 'news/news_list.html'
    queryset = News.objects.filter(is_publish=True).order_by('-published_date')  # ordering by latest published time
    paginate_by = 10  # show Rural360 number in one page


# News detail View
class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news/news_detail.html'


# News search view
class NewsSearchView(generic.ListView):
    paginate_by = 10
    template_name = 'news/news_search_result.html'

# Return search result
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = News.objects.order_by('-published_date').filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(affiliation__icontains=query) | Q(news_content__icontains=query) | Q(published_date__icontains=query)
            )
        return object_list

# Add query content in context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


# Add comment view for news
class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'news/add_comment.html'

    def form_valid(self, form):
        form.instance.news_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        news_id = self.kwargs['pk']
        return reverse_lazy('news:news_detail', kwargs={'pk': news_id})