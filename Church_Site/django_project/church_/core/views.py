from django.shortcuts import render
from django.conf import settings
from .models import Email
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('EMAIL', '')
        
        # Verifique se o e-mail já existe no banco de dados para evitar duplicatas
        if not Email.objects.filter(email=email).exists():
            subscriber = Email(email=email)
            subscriber.save()
            
    # Não é necessário retornar uma resposta para o navegador
    return redirect('https://gmail.us13.list-manage.com/subscribe/post?u=ee6dc3c56054faf946bbd3a1c&amp;id=e2426a9f0e&amp;f_id=007491e2f0')

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

