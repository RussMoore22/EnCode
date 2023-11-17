from django.shortcuts import render, redirect
from .models import SecretMessage
from .forms import ComposeForm, DecipherForm
from .cipher import cipher_message
from .decipher import decipher_message
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
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

@login_required
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

def message_decipher(request, id):
    print('step 1 ************')
    model_instance = SecretMessage.objects.get(id=id)
    print(model_instance.id)
    if request.method == "POST":
        form = DecipherForm(request.POST, instance=model_instance)
        print(form.is_valid(), '***************')
        if form.is_valid():
            form_model = form.save(False)
            print(form_model.encrypted_text,'************encrypted_text')
            model_instance.attempted_text = decipher_message(form_model.encrypted_text, form_model.key)
            model_instance.key = form_model.key
            model_instance.save()
            return redirect('reveal', id=model_instance.id)
    else:
        form = DecipherForm(instance=model_instance)
    context = {
        "form": form
    }
    return render(request, 'inbox/decipher.html', context)

def secret_detail(request, id):
    revealed_message = SecretMessage.objects.get(id=id)
    context = {
        'revealed_message': revealed_message,
    }
    return render(request, 'inbox/reveal.html', context)

def about_page(request):
    return render(request, 'inbox/about.html')
