from django.db.models import QuerySet
from django.http import request
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from . import models, forms
from django.views import generic

# def say_hello(request):
#     return HttpResponse('Hello world')


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()

class BookDetailView(generic.DateDetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)

class BookCreateViev(generic.CreateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm
    success_url = '/books/'
    queryset = models.Book.objects.all() 

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)

class BookUpdateView(generic.UpdateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)    

class BookDeleteView(generic.DeleteView):
    template_name = 'book_delete.html'
    success_url = '/books/' 

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)


# def get_books(request):
#     post = models.Book.objects.all()
#     return render(request, 'post_list.html', {'post': post})

# def book_detail(request, id):
#     try:
#         post = models.Book.objects.get(id=id)
#         try:
#             comment = models.Comments.objects.filter(post_id=id).order_by('created_date')
#         except models.Comments.DoesNotExist:
#             return HttpResponse('No Comments')
#     except models.Post.DoesNotExist:
#         raise Http404('Post does not exiest, baby')  

#     return render(request, 'book_detail.html', {'post': post, 'book_comment': comment})     


# def add_book(request):
#     method = request.method
#     if method == "POST":
#         form = forms.PostForm(request.POST, request.FILES)
#         print(form.data)
#         models.Book.objects.create(title=form.data['title'], 
#         description=form.data['description'], 
#         image=form.data['image'])

#         return HttpResponse('Book Created Successfully')
#     else:
#         form = forms.BookForm()

#     return render(request, 'add_book.html', {'form': form})    


# def add_comments(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.CommentsForm(request.POST, request.FILES)
#         print(form.data)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Comment Created Succssefully')
#     else:
#         form = forms.CommentsForm()
#     return render(request, 'add_comments.html', {'form': form})