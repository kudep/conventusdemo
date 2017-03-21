from django.contrib import admin
from story.models import Story, Scene, Answer

# Register your models here.
#class AnswerInline(admin.StackedInline):
#    model = Answer
#    extra = 2

class SceneInline(admin.StackedInline):
    model = Answer
    extra = 0
#    inlines = [AnswerInline]


class SceneAdmin(admin.ModelAdmin):
    fields =['scene_title', 'scene_text']
    inlines = [SceneInline]

class StoryInline(admin.StackedInline):
    model = Scene
    extra = 0
#    inlines = [AnswerInline]


class StoryAdmin(admin.ModelAdmin):
    fields =['story_title', 'story_text']
    inlines = [StoryInline]

admin.site.register(Story,StoryAdmin)
admin.site.register(Scene,SceneAdmin)