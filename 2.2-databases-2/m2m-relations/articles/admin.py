from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']

class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        tags_ids = set([form.clened_data['tag'].id for form in self.forms])
        if len(tags_ids) != len(self.forms):
            raise ValidationError('Ошибка!')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline,]
