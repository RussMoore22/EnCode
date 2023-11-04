from django.shortcuts import render, redirect
from .models import SecretMessage
from .forms import ComposeForm


# Create your views here.


def secret_messages_inbox(request):
    secret_messages = SecretMessage.objects.all()
    context = {
        'secret_messages': secret_messages,
        }
    return render(request, 'inbox/list.html', context)

def compose_message(request):
    if request.method == "POST":
        form = ComposeForm(request.POST)
        if form.is_valid():
            form = form.save(False)
            form.sender = request.user
            form.save()
            if form is not None:
                return redirect('inbox_list')
    else:
        form = ComposeForm()
    context = {
        'form': form
    }
    return render(request, 'sent/compose.html', context)
