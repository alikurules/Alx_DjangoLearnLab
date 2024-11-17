from django.shortcuts import render, get_object_or_404
from bookshelf.models import Post
from .forms import ExampleForm
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book  

def book_list(request):
    """
    View to display a list of all books.
    """
    books = Book.objects.all()  
    return render(request, 'bookshelf/book_list.html', {'books': books})

def books(request, book_id):
    """
    View to display details for a specific book.
    """
    book = get_object_or_404(Book, id=book_id)  
    return render(request, 'bookshelf/book_detail.html', {'book': book})


@permission_required('app_name.can_view', raise_exception=True)
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'view_post.html', {'post': post})

@permission_required('app_name.can_create', raise_exception=True)
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'create_post.html')

@permission_required('app_name.can_edit', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'edit_post.html', {'post': post})

@permission_required('app_name.can_delete', raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post.html', {'post': post})

def example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            # Add processing logic here
            return render(request, 'bookshelf/success.html', {'title': title})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})

