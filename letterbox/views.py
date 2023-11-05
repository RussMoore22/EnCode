from django.shortcuts import render, redirect
from .models import SecretMessage
from .forms import ComposeForm
from .cipher import cipher_message


# Create your views here.


def secret_messages_inbox(request):
    secret_messages = SecretMessage.objects.filter(receipient=request.user)
    context = {
        'secret_messages': secret_messages,
        }
    return render(request, 'inbox/list.html', context)

def all_inbox(request):
    secret_messages = SecretMessage.objects.all()
    context = {
        'secret_messages': secret_messages,
        }
    return render(request, 'inbox/board.html', context)

def compose_message(request):
    if request.method == "POST":
        form = ComposeForm(request.POST)
        if form.is_valid():
            form = form.save(False)
            form.sender = request.user
            form.encrypted_text = cipher_message(form.text, form.encoder)
            form.save()
            if form is not None:
                return redirect('inbox_list')
    else:
        form = ComposeForm()
    context = {
        'form': form
    }
    return render(request, 'sent/compose.html', context)

def message_detail(request, id):
    secret_message = SecretMessage.objects.get(id=id)
    context = {
        'secret_message': secret_message
    }
    return render(request, 'inbox/detail.html', context)
