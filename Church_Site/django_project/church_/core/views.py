from django.shortcuts import render
from .models import Email
from django.shortcuts import redirect
from .models import Email
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return render(request, 'cadastro.html')

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')

        # Verificar se o email já está registrado
        email_exists = Email.objects.filter(email=email).exists()

        if email_exists:
            mensagem = 'Erro: O email já está registrado.'
            return render(request, 'cadastro.html', {'mensagem': mensagem})
        else:
            novo_email = Email(nome=nome, sobrenome=sobrenome, email=email)
            novo_email.save()
            mensagem = 'Email Cadastrado com sucesso'
            # Redirecionar para a URL '/subscribe/'
            return redirect(reverse('subscribe'))

    return render(request, 'index.html')

'''
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        if  not name or not email or not message:
            mensagem = 'Todos os campos devem ser preenchidos'
        recipient_email = 'seuemail@example.com'
        
        send_mail(
            'Mensagem de ' + name,
            'Nome: {}\nEmail: {}\nMensagem: {}'.format(name, email, message),
            email,
            [recipient_email],
            fail_silently=False,
        )

        # Adiciona a variável de contexto 'success' com valor True
        context = {'success': True}

    else:
        context = {}

    return render(request, 'contact.html', context )
'''

