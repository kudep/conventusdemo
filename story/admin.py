from django.contrib import admin
from story.models import Story, Scene, Answer

# Register your models here.
#class AnswerInline(admin.StackedInline):
#    model = Answer
#    extra = 2

class SceneInline(admin.TabularInline):
    model = Answer
    extra = 0


class SceneAdmin(admin.ModelAdmin):
    fields =['scene_title', 'scene_question', 'scene_story', 'scene_order']
    list_display = ('scene_title', 'scene_question', 'scene_story', 'scene_order')
    list_editable = ( 'scene_question', 'scene_story', 'scene_order')
    inlines = [SceneInline]
    list_filter = ('scene_story',)

class StoryInline(admin.TabularInline):
    model = Scene
    extra = 0
    exclude = ['scene_likes']


class StoryAdmin(admin.ModelAdmin):
    fields =['story_title', 'story_text']
    inlines = [StoryInline]

admin.site.register(Story,StoryAdmin)
admin.site.register(Scene,SceneAdmin)