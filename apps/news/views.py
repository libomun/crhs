from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
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
def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.comments.filter(parent=None)
    return render(request, 'news/news_detail.html', {'news': news, 'comments': comments})


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


@login_required
def create_comment(request, pk, parent_comment_id=None):
    news = get_object_or_404(News, pk=pk)
    parent_comment = None
    if parent_comment_id:
        parent_comment = get_object_or_404(Comment, pk=parent_comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.user = request.user
            comment.parent = parent_comment
            comment.save()
            return redirect('news:news_detail', pk=news.pk)
    else:
        form = CommentForm()

    return render(request, 'news/add_comment.html', {'form': form, 'news': news})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.user:
        return HttpResponseForbidden("You can't delete this comment")

    news = comment.news
    comment.delete()
    return redirect('news:news_detail', pk=news.pk)
