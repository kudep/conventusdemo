from __future__ import unicode_literals

#from django.contrib.postgres.fields import ArrayField
#from django.contrib.postgres.fields import JSONField
from django.db import models

###import ast

# Create your models here.

###class ListField(models.TextField):
###    description = "Stores a python list"
###
###    def __init__(self, *args, **kwargs):
###        super(ListField, self).__init__(*args, **kwargs)
###
###    def to_python(self, value):
###        if not value:
###            value = []
###
###        if isinstance(value, list):
###            return value
###
###        return ast.literal_eval(value)
###
###    def get_prep_value(self, value):
###        if value is None:
###            return value
###
###        return value
###
###    def value_to_string(self, obj):
###        value = self._get_val_from_obj(obj)
###        return self.get_db_prep_value(value)
###
###    test_list = ListField(default = 0)
class Story(models.Model):
    class Meta():
        verbose_name = 'История'
        verbose_name_plural = 'Истории'
    story_title = models.CharField(default = "",max_length = 200, verbose_name="Название истории")
    story_text = models.TextField(default = "", verbose_name="Описание истории")
    story_likes = models.IntegerField(default = 0, verbose_name="Нравится")
    def __str__(self):
       return self.story_title


class Scene(models.Model):
    class Meta():
        verbose_name = 'Сцена'
        verbose_name_plural = 'Сцены'
    scene_title = models.CharField(default = "",max_length = 200, verbose_name="Название сцены")
    scene_text = models.TextField(default = "", verbose_name="Описание сцены")
    scene_question = models.CharField(default = "",max_length = 400, verbose_name="Вопрос")
    scene_likes = models.IntegerField(default = 0, verbose_name="Нравится")
    scene_order = models.IntegerField(default = 1, verbose_name="Порядок в сюжете")
    scene_story = models.ForeignKey(Story, verbose_name="Привязан к истории")
    def __str__(self):
       return self.scene_title


class Answer(models.Model):
    class Meta():
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    answer_text = models.CharField(default = "",max_length = 400, verbose_name="Ответ")
    answer_scene = models.ForeignKey(Scene, verbose_name="Из вопроса")
    def __str__(self):
       return self.answer_text
