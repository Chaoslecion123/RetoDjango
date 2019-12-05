from django.shortcuts import render,redirect
import string
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.views.generic import  ListView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import UserForm

from .tasks import send_emails_users




def generate_users(request):
    quantity_users = request.POST.get('quantityUser',0)
    email = request.POST.get('email',None)
    subject = request.POST.get('subject',None)
    message = request.POST.get('message',None)

    for i in range(int(quantity_users)):
        username = 'username_{}'.format(get_random_string(5,string.ascii_letters))
        email = '{}@imedia.pe'.format(username)
        password = get_random_string(50)
        User.objects.create_user(
            username=username,
            email=email,
            password=email
        )
        send_emails_users.delay(email,subject,message)

        print('Se creo exitosamente los usuarios')


    return render(request,'tasks/generate.html')

class UserListView(ListView):
    model = User
    template_name = 'users/list.html'

class UserEditView(UpdateView):
    model = User
    template_name = 'users/edit.html'
    form_class = UserForm
    success_url = reverse_lazy('list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('list')