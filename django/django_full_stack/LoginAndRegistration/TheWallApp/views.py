from django.shortcuts import render,redirect
from datetime import datetime, date
from .models import *

def durationInMinutes(t1,t2=datetime.now()):
    t1 = t1.replace(tzinfo=None)
    t2 = t2.replace(tzinfo=None)
    duration = t2 - t1
    duration_in_s = duration.total_seconds()
    duration_in_min = divmod(duration_in_s, 60)[0]
    return duration_in_min

def TheWallApp_index(request):
    # now = datetime.now()
    #     # the_moment = Messages.objects.first().created_at
    #     # now = now.replace(tzinfo=None)
    #     # the_moment = the_moment.replace(tzinfo=None)
    #     # duration = now - the_moment
    #     # print("type of the monent is" ,type(the_moment))
    #     # duration_in_s = duration.total_seconds()
    #     # duration_in_min = divmod(duration_in_s,60)[0]
    #     # print("how many minutes ?",duration_in_min)




    if 'id' not in request.session:
        request.session['id'] = None
    the_user = Users.objects.filter(id=request.session['id']).first()
    context = {
        "the_user":the_user,
        "messages":Messages.objects.all()
    }
    return render(request, "TheWallApp_index.html",context)


def postMessage(request):
    message = request.POST['message_textarea']
    print(message)
    the_message = Messages.objects.create(message=message,user_id=request.session['id'])
    print("message is post => ",the_message.message)
    return redirect('/wall/')

def postComment(request):
    comment = request.POST['comment_textarea']
    message_id = request.POST['message_id']
    print(comment)
    the_comment = Comments.objects.create(comment=comment,user_id=request.session['id'],message_id=message_id)
    print("comment is post => ", the_comment.comment)
    return redirect('/wall/')

def deleteMessage(request):
    message_id_to_delete = request.POST['message_id_to_delete']
    the_message = Messages.objects.get(id=message_id_to_delete)
    the_message.delete()
    print("the message is deleted")
    return redirect('/wall/')