from django.contrib import admin

from .models import DraftArticles, PublishedArticles, DraftPresentations, PublishedPresentations, DraftBooks, PublishedBooks, DraftOnline, PublishedOnline


# Register Draft Articles to the admin
@admin.register(DraftArticles)
class DraftArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'statues')
    ordering = ['-date']
    list_filter = ('statues', 'date', 'is_rural360', 'is_6for6', 'is_surgecon')
    # fields = ('title', 'main_authors', 'other_authors', 'author_list', 'doi', 'date', 'affiliation', 'journal', 'abstract', 'keywords',
    #           ('is_rural360', 'is_6for6', 'is_surgecon'), 'statues')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["author_list"].help_text = "Please select relevant authors so that we implement an association"
        return form

# can not edit statues and Is_publish part
    def get_fields(self, request, obj=None):
        fields1 = ('title', 'main_authors', 'other_authors', 'author_list', 'doi', 'date', 'affiliation', 'journal', 'abstract', 'keywords', ('is_rural360', 'is_6for6', 'is_surgecon'), 'statues')
        fields2 = ('title', 'main_authors', 'other_authors', 'author_list', 'doi', 'date', 'affiliation', 'journal', 'abstract', 'keywords', ('is_rural360', 'is_6for6', 'is_surgecon'))
        if request.user.is_superuser is True or request.user.username == 'rural360admin':
            return fields1
        else:
            return fields2

# filter published Rural360 for not_supervisor
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(statues='1')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        if request.user.is_superuser or request.user.username == 'rural360admin':
            if obj.statues == '1':
                article = PublishedArticles.objects.create(
                                                     title=obj.title,
                                                     main_authors=obj.main_authors,
                                                     other_authors=obj.other_authors,
                                                     doi=obj.doi,
                                                     date=obj.date,
                                                     affiliation=obj.affiliation,
                                                     journal=obj.journal,
                                                     abstract=obj.abstract,
                                                     keywords=obj.keywords,
                                                     is_rural360=obj.is_rural360,
                                                     is_6for6=obj.is_6for6,
                                                     is_surgecon=obj.is_surgecon,
                                                     is_published=True,
                                                     )
                member = obj.author_list.all()
                article.author_list.set(member)

        else:
            DraftArticles.objects.update(statues=0)


# Register Published Articles to the admin
@admin.register(PublishedArticles)
class PublishedArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'doi', 'date', 'is_published')
    ordering = ['-date']
    fields = ('title', ('main_authors', 'other_authors', 'author_list'), 'doi', 'date', 'affiliation', 'journal', 'abstract', 'keywords', ('is_rural360', 'is_6for6', 'is_surgecon'), 'is_published')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["author_list"].help_text = "Please select relevant authors so that we implement an association"
        return form


@admin.register(DraftPresentations)
class DraftPresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'statues')
    ordering = ['-date']
    list_filter = ('statues', 'date', 'types', 'is_rural360', 'is_6for6', 'is_surgecon')
    fields = ('title', 'main_authors', 'other_authors', 'author_list', 'date', 'types', 'abstract', 'external_link', 'archive', 'picture',
              ('is_rural360', 'is_6for6', 'is_surgecon'), 'statues')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["author_list"].help_text = "Please select relevant authors so that we implement an association"
        return form

    # can not edit statues and Is_publish part
    def get_fields(self, request, obj=None):
        fields1 = ('title', 'main_authors', 'other_authors', 'author_list', 'date', 'types', 'abstract', 'external_link', 'archive', 'picture', ('is_rural360', 'is_6for6', 'is_surgecon'), 'statues')
        fields2 = ('title', 'main_authors', 'other_authors', 'author_list', 'date', 'types', 'abstract', 'external_link', 'archive', 'picture', ('is_rural360', 'is_6for6', 'is_surgecon'))
        if request.user.is_superuser is True or request.user.username == 'rural360admin':
            return fields1
        else:
            return fields2

    # filter published Rural360 for not_supervisor
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(statues='1')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        if request.user.is_superuser:
            if obj.statues == '1':
                presentations = PublishedPresentations.objects.create(
                                                                     title=obj.title,
                                                                     main_authors=obj.main_authors,
                                                                     other_authors=obj.other_authors,
                                                                     date=obj.date,
                                                                     types=obj.types,
                                                                     abstract=obj.abstract,
                                                                     external_link=obj.external_link,
                                                                     archive=obj.archive,
                                                                     picture=obj.picture,
                                                                     is_rural360=obj.is_rural360,
                                                                     is_6for6=obj.is_6for6,
                                                                     is_surgecon=obj.is_surgecon,
                                                                     is_published=True)
                member = obj.author_list.all()
                presentations.author_list.set(member)
        else:
            DraftPresentations.objects.update(statues=0)


@admin.register(PublishedPresentations)
class PublishedPresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_published')
    list_filter = ( 'date', 'types', 'is_rural360', 'is_6for6', 'is_surgecon')
    ordering = ['-date']
    fields = ('title', 'main_authors', 'other_authors', 'author_list', 'date', 'types', 'abstract', 'external_link', 'archive', 'picture',
              ('is_rural360', 'is_6for6', 'is_surgecon'), 'is_published')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["author_list"].help_text = "Please select relevant authors so that we implement an association"
        return form


@admin.register(DraftBooks)
class DraftBooksAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'date', 'statues')
    ordering = ['-date']
    list_filter = ('statues', 'date',  'is_rural360', 'is_6for6', 'is_surgecon')
    fields = ('isbn', 'title', 'main_authors', 'other_authors', 'author_list', 'date', 'categories', 'introduction', 'picture', 'external_link', 'archive',
              ('is_rural360', 'is_6for6', 'is_surgecon'), 'statues')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["author_list"].help_text = "Please select relevant authors so that we implement an association"
        return form

    # can not edit statues and Is_publish part
    def get_fields(self, request, obj=None):
        fields1 = ('isbn', 'title', 'main_authors', 'other_authors', 'author_list', 'date', 'categories', 'introduction', 'picture', 'external_link', 'archive', ('is_rural360', 'is_6for6', 'is_surgecon'), 'statues')
        fields2 = ('isbn', 'title', 'main_authors', 'other_authors', 'author_list', 'date', 'categories', 'introduction', 'picture', 'external_link', 'archive', ('is_rural360', 'is_6for6', 'is_surgecon'))
        if request.user.is_superuser is True or request.user.username == 'rural360admin':
            return fields1
        else:
            return fields2

    # filter published Rural360 for not_supervisor
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(statues='1')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        if request.user.is_superuser:
            if obj.statues == '1':
                books = PublishedBooks.objects.create(
                                             isbn=obj.isbn,
                                             title=obj.title,
                                             main_authors=obj.main_authors,
                                             other_authors=obj.other_authors,
                                             date=obj.date,
                                             categories=obj.categories,
                                             introduction=obj.introduction,
                                             archive=obj.archive,
                                             external_link=obj.external_link,
                                             picture=obj.picture,
                                             is_rural360=obj.is_rural360,
                                             is_6for6=obj.is_6for6,
                                             is_surgecon=obj.is_surgecon,
                                             is_published=True)

                member = obj.author_list.all()
                books.author_list.set(member)
        else:
            DraftBooks.objects.update(statues=0)


@admin.register(PublishedBooks)
class PublishedBooksAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'date', 'is_published')
    ordering = ['-date']
    list_filter = ('date',  'is_rural360', 'is_6for6', 'is_surgecon')
    fields = ('isbn', 'title', 'main_authors', 'other_authors', 'author_list', 'date', 'categories', 'introduction', 'picture', 'external_link', 'archive',
              ('is_rural360', 'is_6for6', 'is_surgecon'), 'is_published')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["author_list"].help_text = "Please select relevant authors so that we implement an association"
        return form


@admin.register(DraftOnline)
class DraftOnlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'statues')
    ordering = ['-date']
    list_filter = ('statues', 'date',  'is_rural360', 'is_6for6', 'is_surgecon')
    fields = ('title', 'main_authors', 'other_authors', 'author_list', 'date', 'abstract',  'external_link',
              ('is_rural360', 'is_6for6', 'is_surgecon'), 'statues')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["author_list"].help_text = "Please select relevant authors so that we implement an association"
        return form

    # can not edit statues and Is_publish part
    def get_exclude(self, request, obj=None):
        exclude = ('statues',)
        if request.user.is_superuser is False:
            return exclude

    # filter published Rural360 for not_supervisor
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(statues='1')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        if request.user.is_superuser:
            if obj.statues == '1':
                online = PublishedOnline.objects.create(
                                             title=obj.title,
                                             main_authors=obj.main_authors,
                                             other_authors=obj.other_authors,
                                             date=obj.date,
                                             abstract=obj.abstract,
                                             external_link=obj.external_link,
                                             is_rural360=obj.is_rural360,
                                             is_6for6=obj.is_6for6,
                                             is_surgecon=obj.is_surgecon,
                                             is_published=True)

                member = obj.author_list.all()
                online.author_list.set(member)
        else:
            DraftOnline.objects.update(statues=0)


@admin.register(PublishedOnline)
class PublishedOnlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_published')
    ordering = ['-date']
    list_filter = ('date',  'is_rural360', 'is_6for6', 'is_surgecon')
    fields = ('title', 'main_authors', 'other_authors', 'author_list', 'date',  'abstract',  'external_link',
              ('is_rural360', 'is_6for6', 'is_surgecon'), 'is_published')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["author_list"].help_text = "Please select relevant authors so that we implement an association"
        return form
