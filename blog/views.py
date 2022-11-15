from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView , TemplateView
from .models import Comments, Like, Post 
from django.core.paginator import Paginator

class OurMenu(ListView):
    model = Post
    template_name = 'blog/Our-menu.html'
    paginate_by = 12
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/details.html'
    context_object_name = 'post'
    queryset = None
    def get_context_data(self , *args, **kwargs ):
        context = super().get_context_data(*args, **kwargs)
        queryset = Post.objects.get(slug = self.object.slug)
        queryset.views += 1
        queryset.save()
        if self.request.user.is_authenticated == True:
            if self.request.user.likes2.filter(posts__important_title = self.object.important_title , users_id = self.request.user.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False
        else:
            pass
        return context 
    def post(self,request,slug):
        posts = Post.objects.get(slug=slug)
        parent_id = request.POST.get('parent_id')
        message = request.POST.get('message')
        Comments.objects.create(message=message, parent_id=parent_id , posts=posts , user=request.user)
        return redirect('blog:detail' , slug)

class ShopView(ListView):
    model = Post
    template_name = 'blog/shop.html'
    paginate_by = 12
    context_object_name = 'products'
    def get_context_data(self, *args, **kwargs):
        context = super(ShopView, self).get_context_data(*args, **kwargs)
        context['products'] = Post.objects.sellers()
        return context

class SearchBox(TemplateView):
    queryset = None
    template_name = 'blog/Our-menu.html'
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        queryset = Post.objects.filter(important_title__icontains = q)
        page_number = request.GET.get('page')
        paginator = Paginator(queryset , 12)
        objects = paginator.get_page(page_number)
        return render(request, self.template_name, {'posts': objects})

def like(request , slug , pk):
    try:
        like = Like.objects.get(posts__slug = slug , users_id=request.user.id)
        like.delete()
        return JsonResponse({"response" : "unliked"})
    except:
        Like.objects.create(posts_id=pk , users_id = request.user.id)
        return JsonResponse({"response" : "liked"})

