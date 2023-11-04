from django.shortcuts import render, redirect
from .models import SecretMessage
from .forms import ComposeForm
from .cipher import cipher_message


# Create your views here.


def secret_messages_inbox(request):
    secret_messages = SecretMessage.objects.filter(receipient=request.user)
    encrypted_messages = []
    for secret_message in secret_messages:
        obj_inst = secret_message
        obj_inst.text = cipher_message(secret_message.text, secret_message.encoder)
        encrypted_messages.append(obj_inst)
    context = {
        'secret_messages': secret_messages,
        'encrypted_messages': encrypted_messages,
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
