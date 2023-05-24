from django.views import generic
from django.db.models import Q
from .models import Articles, Books, Presentations, Online


class ArticlesListView(generic.ListView):
    template_name = 'publication/article_list.html'
    queryset = Articles.objects.filter(is_published=True).order_by('-date')
    paginate_by = 10


class ArticlesSearchView(generic.ListView):
    template_name = 'publication/article_search.html'
    paginate_by = 10


    def get_queryset(self):
        query = self.request.GET.get("q")
        start_year = self.request.GET.get("start_year")
        end_year = self.request.GET.get("end_year")
        check_rural360 = self.request.GET.get("check_rural360")
        check_6for6 = self.request.GET.get("check_6for6")
        check_surgecon = self.request.GET.get("check_surgecon")

        # if query is not None:
        if check_rural360 is not None and check_6for6 is not None and check_surgecon is not None:
            object_list = Articles.objects.filter(
                    (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(doi__iexact=query)
                     | Q(abstract__icontains=query) | Q(keywords__icontains=query) | Q(affiliation__icontains=query))
                    & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_6for6=True) & Q(is_surgecon=True) & Q(is_published=True)
                )
            return object_list
        elif check_rural360 is not None and check_6for6 is not None and check_surgecon is None:
            object_list = Articles.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(doi__iexact=query)
                 | Q(abstract__icontains=query) | Q(keywords__icontains=query) | Q(affiliation__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_6for6=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is None and check_surgecon is not None:
            object_list = Articles.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(doi__iexact=query)
                 | Q(abstract__icontains=query) | Q(keywords__icontains=query) | Q(affiliation__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is not None and check_surgecon is not None:
            object_list = Articles.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(doi__iexact=query)
                 | Q(abstract__icontains=query) | Q(keywords__icontains=query) | Q(affiliation__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_6for6=True) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is None and check_surgecon is None:
            object_list = Articles.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(doi__iexact=query)
                 | Q(abstract__icontains=query) | Q(keywords__icontains=query) | Q(affiliation__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is not None and check_surgecon is None:
            object_list = Articles.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(doi__iexact=query)
                 | Q(abstract__icontains=query) | Q(keywords__icontains=query) | Q(affiliation__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_6for6=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is None and check_surgecon is not None:
            object_list = Articles.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(doi__iexact=query)
                 | Q(abstract__icontains=query) | Q(keywords__icontains=query) | Q(affiliation__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is None and check_surgecon is None:
            object_list = Articles.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(doi__iexact=query)
                 | Q(abstract__icontains=query) | Q(keywords__icontains=query) | Q(affiliation__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_published=True)
            )
            return object_list



# add query content in  context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['start_year'] = self.request.GET.get('start_year')
        context['end_year'] = self.request.GET.get('end_year')
        context['check_rural360'] = self.request.GET.get('check_rural360')
        context['check_6for6'] = self.request.GET.get('check_6for6')
        context['check_surgecon'] = self.request.GET.get('check_surgecon')
        return context


class ArticlesDetailView(generic.DetailView):
    model = Articles
    template_name = 'publication/article_detail.html'


class PresentationListView(generic.ListView):
    template_name = 'publication/pre_list.html'
    queryset = Presentations.objects.filter(is_published=True).order_by('-date')  # ordering by latest published time
    paginate_by = 10


class PresentationDetailView(generic.DetailView):
    model = Presentations
    template_name = 'publication/pre_detail.html'


# Search News view
class PresentationSearchView(generic.ListView):
    template_name = 'publication/pre_search.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        start_year = self.request.GET.get("start_year")
        end_year = self.request.GET.get("end_year")
        check_rural360 = self.request.GET.get("check_rural360")
        check_6for6 = self.request.GET.get("check_6for6")
        check_surgecon = self.request.GET.get("check_surgecon")

        if check_rural360 is not None and check_6for6 is not None and check_surgecon is not None:
            object_list = Presentations.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query) | Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query) | Q(types__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_6for6=True) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is not None and check_surgecon is None:
            object_list = Presentations.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query) | Q(types__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_6for6=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is None and check_surgecon is not None:
            object_list = Presentations.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query) | Q(types__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q( is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is not None and check_surgecon is not None:
            object_list = Presentations.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query) | Q(types__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_6for6=True) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is None and check_surgecon is None:
            object_list = Presentations.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query) | Q(types__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is not None and check_surgecon is None:
            object_list = Presentations.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query) | Q(types__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_6for6=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is None and check_surgecon is not None:
            object_list = Presentations.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query) | Q(types__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is None and check_surgecon is None:
            object_list = Presentations.objects.filter(
                (Q(title__icontains=query)| Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query) | Q(types__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_published=True)
            )
            return object_list

    # add query content in  context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['start_year'] = self.request.GET.get('start_year')
        context['end_year'] = self.request.GET.get('end_year')
        context['check_rural360'] = self.request.GET.get('check_rural360')
        context['check_6for6'] = self.request.GET.get('check_6for6')
        context['check_surgecon'] = self.request.GET.get('check_surgecon')
        return context


class BookListView(generic.ListView):
    template_name = 'publication/book_list.html'
    queryset = Books.objects.filter(is_published=True).order_by('-date')
    paginate_by = 10


# News Detail View
class BookDetailView(generic.DetailView):
    model = Books
    template_name = 'publication/book_detail.html'


# Search News view
class BookSearchView(generic.ListView):
    template_name = 'publication/book_search.html'
    paginate_by = 10

    # return search Rural360 result
    def get_queryset(self):
        query = self.request.GET.get("q")
        start_year = self.request.GET.get("start_year")
        end_year = self.request.GET.get("end_year")
        check_rural360 = self.request.GET.get("check_rural360")
        check_6for6 = self.request.GET.get("check_6for6")
        check_surgecon = self.request.GET.get("check_surgecon")

        # if query is not None:
        if check_rural360 is not None and check_6for6 is not None and check_surgecon is not None:
            object_list = Books.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(isbn__iexact=query) | Q(introduction__icontains=query) | Q(categories__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_6for6=True) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is not None and check_surgecon is None:
            object_list = Books.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(isbn__iexact=query) | Q(introduction__icontains=query) | Q(categories__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_6for6=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is None and check_surgecon is not None:
            object_list = Books.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(isbn__iexact=query) | Q(introduction__icontains=query) | Q(categories__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is not None and check_surgecon is not None:
            object_list = Books.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(isbn__iexact=query) | Q(introduction__icontains=query) | Q(categories__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_6for6=True) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is None and check_surgecon is None:
            object_list = Books.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(isbn__iexact=query) | Q(introduction__icontains=query) | Q(categories__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is not None and check_surgecon is None:
            object_list = Books.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(isbn__iexact=query) | Q(main_authors__icontains=query) | Q(other_authors__icontains=query) | Q(introduction__icontains=query) | Q(categories__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_6for6=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is None and check_surgecon is not None:
            object_list = Books.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(isbn__iexact=query) | Q(introduction__icontains=query) | Q(categories__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is None and check_surgecon is None:
            object_list = Books.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(isbn__iexact=query) | Q(introduction__icontains=query) | Q(categories__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_published=True)
            )
            return object_list

    # add query content in  context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['start_year'] = self.request.GET.get('start_year')
        context['end_year'] = self.request.GET.get('end_year')
        context['check_rural360'] = self.request.GET.get('check_rural360')
        context['check_6for6'] = self.request.GET.get('check_6for6')
        context['check_surgecon'] = self.request.GET.get('check_surgecon')
        return context


class OnlineListView(generic.ListView):
    template_name = 'publication/online_list.html'
    queryset = Online.objects.filter(is_published=True).order_by('-date')
    paginate_by = 10


# News Detail View
class OnlineDetailView(generic.DetailView):
    model = Online
    template_name = 'publication/online_detail.html'


# Search News view
class OnlineSearchView(generic.ListView):
    template_name = 'publication/online_search.html'
    paginate_by = 10

    # return search Rural360 result
    def get_queryset(self):
        query = self.request.GET.get("q")
        start_year = self.request.GET.get("start_year")
        end_year = self.request.GET.get("end_year")
        check_rural360 = self.request.GET.get("check_rural360")
        check_6for6 = self.request.GET.get("check_6for6")
        check_surgecon = self.request.GET.get("check_surgecon")

        # if query is not None:
        if check_rural360 is not None and check_6for6 is not None and check_surgecon is not None:
            object_list = Online.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_6for6=True) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is not None and check_surgecon is None:
            object_list = Online.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_6for6=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is None and check_surgecon is not None:
            object_list = Online.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is not None and check_surgecon is not None:
            object_list = Online.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_6for6=True) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is not None and check_6for6 is None and check_surgecon is None:
            object_list = Online.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_rural360=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is not None and check_surgecon is None:
            object_list = Online.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_6for6=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is None and check_surgecon is not None:
            object_list = Online.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(main_authors__icontains=query) | Q(other_authors__icontains=query) | Q(abstract__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_surgecon=True) & Q(is_published=True)
            )
            return object_list
        elif check_rural360 is None and check_6for6 is None and check_surgecon is None:
            object_list = Online.objects.filter(
                (Q(title__icontains=query) | Q(author_list__first_name__icontains=query)|Q(author_list__last_name__icontains=query) | Q(abstract__icontains=query))
                & Q(date__year__range=[start_year, end_year]) & Q(is_published=True)
            )
            return object_list

    # add query content in  context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['start_year'] = self.request.GET.get('start_year')
        context['end_year'] = self.request.GET.get('end_year')
        context['check_rural360'] = self.request.GET.get('check_rural360')
        context['check_6for6'] = self.request.GET.get('check_6for6')
        context['check_surgecon'] = self.request.GET.get('check_surgecon')
        return context


