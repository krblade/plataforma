from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required  
def DashBoard(request):

    return render(request, 'dashboard.html', {
      
       
        
    })
       