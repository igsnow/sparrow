from django.contrib import admin

from .models import Question, Choice


# 自定义后台模型类
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # 列表展示的字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 列表右侧添加过滤器
    list_filter = ['pub_date']
    # 添加搜索框
    search_fields = ['question_text']
    list_per_page = 8


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
