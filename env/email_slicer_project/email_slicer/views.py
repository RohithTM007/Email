from django.shortcuts import render
import re

def email_slicer(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        if re.match(r'^[\w\.-]+@[\w\.-]+$',email): #regex for validating email

            username,domain =email.split('@')
            custom_message = f"Hello {username}, welcome to our website. You will be informed about further updates and information about our website"
            return render(request,'result.html', {'username': username, 'domain': domain, 'message': custom_message})
        else:
            return render(request, 'error.html')
    else:
        return render(request,'email_form.html')





def result(request):
    return render(request, 'result.html')

def error(request):
    
    return render(request, 'error.html')





