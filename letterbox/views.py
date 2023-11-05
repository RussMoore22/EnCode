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

def all_inbox(request):
    secret_messages = SecretMessage.objects.all()
    encrypted_messages = []
    for secret_message in secret_messages:
        obj_inst = secret_message
        obj_inst.text = cipher_message(secret_message.text, secret_message.encoder)
        obj_inst.mess_id = secret_message.id
        encrypted_messages.append(obj_inst)
    context = {
        'secret_messages': secret_messages,
        'encrypted_messages': encrypted_messages,
        }
    return render(request, 'inbox/board.html', context)

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

def message_detail(request, id):
    secret_message = SecretMessage.objects.get(id=id)
    print('*******************************')
    print(SecretMessage.objects.get(id=id).text)
    encrypted_message = secret_message
    encrypted_message.text = cipher_message(secret_message.text, secret_message.encoder)
    encrypted_message.mess_id = secret_message.id
    print(encrypted_message.text)

    context = {
        'encrypted_message': encrypted_message
    }
    return render(request, 'inbox/detail.html', context)
