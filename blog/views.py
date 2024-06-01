from django.shortcuts import render

# Create your views here.
posts=[
    
   { 'title':'Blog1',
    'aurhor':'Futik bhai',
    'content':'ICT Dept'
   },
   { 'title':'Blog2',
    'aurhor':'Futik bhai',
    'content':'EEE dept'
   }
]
def index(request):
    context={
        'posts':posts
    }
    return render(request,'blog/index.html',context)


def text(request):
    return render(request,'blog/text.html')