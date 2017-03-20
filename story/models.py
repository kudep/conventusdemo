from __future__ import unicode_literals

#from django.contrib.postgres.fields import ArrayField
#from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.


class Story(models.Model):
    class Meta():
        db_table = "story"
    story_title = models.CharField(max_length = 200)
    story_text = models.TextField(default = "")
    story_likes = models.IntegerField(default = 0 )
#    scene_previos_scene = models.ForeignKey(Scene)
#    scene_next_scene = models.ForeignKey(Scene)


class Scene(models.Model):
    class Meta():
        db_table = "scene"
    scene_title = models.CharField(max_length = 200)
    scene_text = models.TextField(default = "")
    scene_text = models.TextField(default = "")
    scene_question = models.CharField(default = "",max_length = 400)
    scene_likes = models.IntegerField(default = 0 )
    scene_story = models.ForeignKey(Story)
#    scene_previos_scene = models.ForeignKey(Scene)
#    scene_next_scene = models.ForeignKey(Scene)


class Answer(models.Model):
    class Meta():
        db_table = "answer"
    answer_text = models.CharField(default = "",max_length = 400)
    answer_scene = models.ForeignKey(Scene)
#    answer_scene = models.ForeignKey(Scene)
#    answer_likes = models.IntegerField()
#    #answer_weight_vector = ArrayField(models.IntegerField(),size=3)

#,default=[1,1,1,1])

#    answer_next_scene = models.ForeignKey(Scene)

