from django.contrib import admin

from .models import Rural360DraftNews, Rural360PublishedNews, SixforsixDraftNews, SixforsixPublishedNews, SurgeConDraftNews, SurgeConPublishedNews


# Register Rural360 Draft News to the admin site
@admin.register(Rural360DraftNews)
class Rural360DraftNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'updated_date', 'statues')
    ordering = ['-updated_date']
    list_filter = ['statues']
    readonly_fields = ('created_date',)

# CRHS admin and rural360 admin can change draft news statues
    def get_fields(self, request, obj=None):
        fields1 = ['title', 'author', 'username', 'news_text', 'news_img', 'statues', 'created_date']
        fields2 = ['title', 'author', 'username', 'news_text', 'news_img', 'created_date']
        if request.user.is_superuser is True or request.user.username == 'rural360admin':
            return fields1
        else:
            return fields2

# Once the draft news was approved and published, this news will not display in the draft news list
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.username == 'rural360admin':
            return qs.exclude(statues='1')
        return qs.filter(username=request.user.username) and qs.exclude(statues='1')

# When admin approve the draft news, this news will be saved in the published news.
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        if request.user.is_superuser or request.user.username == 'rural360admin':
            if obj.statues == '1':
                Rural360PublishedNews.objects.create(title=obj.title, author=obj.author, news_text=obj.news_text, news_img=obj.news_img,)
        else:
            Rural360DraftNews.objects.update(statues=0)

# AutoFill username that keep same with your login username
    def get_changeform_initial_data(self, request):
        return {'username': request.user.username}


# Register Rural360 Published news to the admin site
@admin.register(Rural360PublishedNews)
class Rural360PublishedNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_date', 'is_publish')
    ordering = ['-updated_date']
    readonly_fields = ('published_date', 'news_type')


# Register 6for6 Draft News to the admin site
@admin.register(SixforsixDraftNews)
class SixforsixDraftNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'updated_date', 'statues')
    ordering = ['-updated_date']
    list_filter = ['statues']
    readonly_fields = ('created_date',)

# CRHS admin and 6for6 admin can change draft news statues
    def get_fields(self, request, obj=None):
        fields1 = ['title', 'author', 'username', 'news_text', 'news_img', 'statues', 'created_date']
        fields2 = ['title', 'author', 'username', 'news_text', 'news_img', 'created_date']
        if request.user.is_superuser is True or request.user.username == 'rural360admin':
            return fields1
        else:
            return fields2

# Once the draft news was approved and published, this news will not display in the draft news list
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.username == '6for6admin':
            return qs.exclude(statues='1')
        return qs.filter(username=request.user.username) and qs.exclude(statues='1')

# When admin approve publishing draft news, this news will be saved in the published news
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        if request.user.is_superuser or request.user.username == '6for6admin':
            if obj.statues == '1':
                SixforsixPublishedNews.objects.create(title=obj.title, author=obj.author, news_text=obj.news_text, news_img=obj.news_img,)
        else:
            SixforsixDraftNews.objects.update(statues=0)

# Autofill username that keep same with your login username
    def get_changeform_initial_data(self, request):
        return {'username': request.user.username}


# Register 6for6 Published news to the admin site
@admin.register(SixforsixPublishedNews)
class SixforsixPublishedNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_date', 'is_publish')
    ordering = ['-updated_date']
    readonly_fields = ('published_date', 'news_type')


# Register SurgeCon draft news to the admin site
@admin.register(SurgeConDraftNews)
class SurgeConDraftNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'updated_date', 'statues')
    ordering = ['-updated_date']
    list_filter = ['statues']
    readonly_fields = ('created_date',)

# CRHS admin and SurgeCon admin can change draft news statues
    def get_fields(self, request, obj=None):
        fields1 = ['title', 'author', 'username', 'news_text', 'news_img', 'statues', 'created_date']
        fields2 = ['title', 'author', 'username', 'news_text', 'news_img', 'created_date']
        if request.user.is_superuser is True or request.user.username == 'surgeconadmin':
            return fields1
        else:
            return fields2

# Once the draft news was approved and published, this news will not display in the draft news list
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.username == 'surgeconadmin':
            return qs.exclude(statues='1')
        return qs.filter(username=request.user.username) and qs.exclude(statues='1')

#  When admin approve publishing draft news, this news will be saved in the published news
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        if request.user.is_superuser or request.user.username == 'surgeconadmin':
            if obj.statues == '1':
                SurgeConPublishedNews.objects.create(title=obj.title, author=obj.author, news_text=obj.news_text, news_img=obj.news_img,)
        else:
            SurgeConDraftNews.objects.update(statues=0)

# Autofill username that keep same with your login username
    def get_changeform_initial_data(self, request):
        return {'username': request.user.username}


# Register SurgeCon published news to the admin site
@admin.register(SurgeConPublishedNews)
class SurgeConPublishedNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_date', 'is_publish')
    ordering = ['-updated_date']
    readonly_fields = ('published_date', 'news_type')


























