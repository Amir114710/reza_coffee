from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
from django.core.paginator import Paginator

class HomeView(TemplateView):
    template_name = 'home_app/index.html'
    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        context['posts_6'] = Post.objects.all()[:12]
        return context
    
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

