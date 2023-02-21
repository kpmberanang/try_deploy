from django.shortcuts import render
from deploy.models import Describe

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        text= request.POST['text']
        data = Describe(name=name,text=text)
        data.save()

    data=Describe.objects.all()
    dict = {
        'alldescribe': data
    }
    return render(request,'index.html',dict)



