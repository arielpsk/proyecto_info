from django.shortcuts import render, redirect
from apps.noticia.models import Noticia
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView;
from apps.noticia.forms import UserRegisterForm, NoticiaCreateForm, UserLoginForm, ComentarioForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, authenticate, login


# def index(request):
#     return render(request,'index.html')

# def nosotros(request):
#     return render(request, 'nosotros.html') 

class NoticiaCreateView(CreateView):
    form_class = NoticiaCreateForm
    model = Noticia
    template_name = "noticia/crear_noticia.html"
    
    def form_valid(self, form):
        post = form.instance
        post.usuario = self.request.user 
        post.save()
        return redirect('index')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'nombre_vista': 'Publicar'
        })
        return context

class NoticiaListview(ListView):
    model = Noticia
    template_name = 'index.html'

class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def login_view(request):
    form= UserLoginForm(request.POST or None)
    title = "Connexion"
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request.user.is_authenticated())
    # print(form)
    # print(username)
    # print(password)
    return render(request,"index",{"form":form, "title": title})
    #return redirect('index')

class NoticiaDetailView(DetailView):
    model = Noticia
    
    def post(self, *args, **kwargs):
        form = ComentarioForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comentario = form.instance
            comentario.usuario = self.request.user
            comentario.noticia = post
            comentario.save()
            return redirect('detail', post.id)
        else:
            return redirect('detail', self.get_object().id)
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': ComentarioForm
        })
        return context

