from django.contrib import admin
from movies.models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'release_date', 'created_at', 'updated_at']
    search_fields = ['title', 'sinopse']
    list_filter = ['created_at', 'updated_at', 'release_date']
    date_hierarchy = 'release_date'
    ordering = ['title']
    fields = ['title', 'sinopse', 'duration', 'release_date', 'cover', 'trailer']
    readonly_fields = ['created_at', 'updated_at']
    save_on_top = True
    save_as = True
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ['duration']
    list_display_links = ['title']
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    actions = ['delete_selected']
    fieldsets = [
        ('Informações do filme', {
            'fields': ['title', 'sinopse', 'duration', 'release_date']
        }),
        ('Mídia', {
            'fields': ['cover', 'trailer']
        }),
        ('Datas', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        })
    ]
    filter_horizontal = ['actors']
    filter_vertical = ['genres']
    radio_fields = {'rating': admin.HORIZONTAL}
    autocomplete_fields = ['actors']
    raw_id_fields = ['actors']
    prepopulated_fields = {'slug': ['title']}