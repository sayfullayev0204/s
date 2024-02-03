from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Vazifa
from .models import Bolimlar,Fan,Vazifa,Question,Answer

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Bolimlar)
admin.site.register(Fan)
admin.site.register(Vazifa)
admin.site.register(Question, QuestionAdmin)




