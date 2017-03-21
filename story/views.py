from django.shortcuts import render_to_response

from story.models import *

# Create your views here.

def init(request):
    return render_to_response('home.html')

def storytest(request):
    return render_to_response('storylist.html',
        {'stories':Story.objects.all(),
        'story_title':Story._meta.get_field("story_title").verbose_name.title(),
        'story_text':Story._meta.get_field("story_text").verbose_name.title(),
        'story_likes':Story._meta.get_field("story_likes").verbose_name.title(),
        })

def scenepage(request,story_id=1,order=1):
    content={'story_id':story_id}
    content['scene']=Scene.objects.filter(scene_story_id=story_id).filter(scene_story_id=story_id).filter(scene_order=order)[0]
    content['order']=order+1
    if(True):
        return render_to_response('scene.html',{'story_id':content['story_id'],
    'scene':content['scene'],
    'order':content['order'],

            })

    return render_to_response('home.html')
