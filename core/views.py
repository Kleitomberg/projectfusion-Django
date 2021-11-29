from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario, Funcionalidade
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] =Servico.objects.order_by('criado').all()[:6]
        context['funcionarios'] =Funcionario.objects.order_by('?').all()
        context['funcionalidades1'] =Funcionalidade.objects.order_by('criado').all()[0:3]
        context['funcionalidades2'] =Funcionalidade.objects.order_by('criado').all()[3:6]
        return context

    
    def form_valid(self, form, *args, **kwargs):
       form.send_mail()
       messages.success(self.request, 'E-mail Enviado com sucesso')
       return super(IndexView, self).form_valid(form,*args,**kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Falha ao enviar e-mail')
        return super(IndexView, self).form_invalid(form,*args,**kwargs)