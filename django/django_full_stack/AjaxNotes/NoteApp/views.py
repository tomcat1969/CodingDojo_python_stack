from django.shortcuts import render,redirect
from .models import Notes

def index(request):
    context = {
        "all_the_notes":Notes.objects.all()
    }

    return render(request,'index.html',context)

def addNote(request):
    Notes.objects.create(title=request.POST['title'],content=request.POST['content'])
    return redirect('/feedbackNotes')

def delete(request,note_id):
    print('enter delete function ..',note_id)
    the_note = Notes.objects.get(id=note_id)
    print("note id ", the_note.id, "is deleting")
    the_note.delete()

    return redirect('/feedbackNotes')

def feedbackNotes(request):
    context = {
        "all_the_notes": Notes.objects.all()
    }
    print('rendering the notes.html')
    return render(request,'notes.html',context)