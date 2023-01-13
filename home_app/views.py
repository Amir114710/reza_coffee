from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView , FormView
from blog.models import Post
from blog.models import Poster
from django.core.paginator import Paginator
from .form import ContactUsForm 
from .models import ContactUs , About
from blog.models import Notification

class HomeView(TemplateView):
    template_name = 'home_app/index.html'
    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        context['posts_6'] = Post.objects.all()[:12]
        context['Poster'] = Poster.objects.all()
        context['about'] = About.objects.all()
        return context
    # def post(self):
    #     form = ContactUsForm(self.request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse('home_app:home'))
    #     return render(self.request, self.template_name , context={'forms': form})   
class SearchBox(TemplateView):
    queryset = None
    template_name = 'home_app/index.html'
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        queryset = Post.objects.filter(title_for_show__icontains = q)
        page_number = request.GET.get('page')
        paginator = Paginator(queryset , 12)
        objects = paginator.get_page(page_number)
        return render(request, self.template_name, {'posts': objects})

class ContactUsForm(FormView):
    template_name = 'home_app/contact.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('home_app:home')
    def form_valid(self, form):
        cd = form.cleaned_data
        if self.request.user.is_authenticated:
            form.save()
            return render(self.request , self.template_name , {'form':form})


