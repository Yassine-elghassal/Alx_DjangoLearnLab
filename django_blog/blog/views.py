from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  
    context_object_name = 'posts'
    ordering = ['-created_at']  

# Show details of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  

# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

# Update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only author can edit

# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only author can delete


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm

# Add a comment to a post
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['post_id']})

# Edit a comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.id})

# Delete a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.id})

from django.shortcuts import render
from django.db.models import Q  # Import Q for complex queries
from .models import Post

def search_posts(request):
    query = request.GET.get('q')  # Get the search query from the GET request
    results = Post.objects.all()  # Default to all posts if no query is provided

    if query:
        # Filter posts where title, content, or tags contain the query
        results = results.filter(
            Q(title__icontains=query) |  # Search by title
            Q(content__icontains=query) |  # Search by content
            Q(tags__name__icontains=query)  # Search by tags
        ).distinct()  # Ensure no duplicate posts if they match multiple fields

    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status="published")  # Ensure filtering is used
    return render(request, "blog/post_list.html", {"posts": posts})

from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag  # Ensure you're using taggit for tagging

def posts_by_tag(request, tag):
    tag_obj = get_object_or_404(Tag, slug=tag)  # Get the tag object based on its slug
    posts = Post.objects.filter(tags=tag_obj)  # Filter posts by the tag

    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag': tag_obj})
