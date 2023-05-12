from django.contrib import admin

from .models import Articles, Presentations, Books, Online


# Register Published Articles to the admin
@admin.register(Articles)
class PublishedArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'doi', 'date', 'is_published')
    ordering = ['-date']
    fields = ('title', ('main_authors', 'other_authors', 'author_list'), 'doi', 'date', 'affiliation', 'journal', 'abstract', 'keywords', ('is_rural360', 'is_6for6', 'is_surgecon'), 'is_published')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["author_list"].help_text = "Please select relevant authors so that we implement an association"
        return form


@admin.register(Presentations)
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


@admin.register(Books)
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


@admin.register(Online)
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
