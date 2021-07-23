from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm

def home(request):
    contents = Book.objects
    #모든 글들을 대상으로
    book_list = Book.objects.all()
    #객체 세 개를 한 페이지로 자르기
    paginator = Paginator(book_list, 4)
    #request된 페이지가 뭔지 알아내고 (request페이지에 변수를 담고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해줌
    posts = paginator.get_page(page)
    return render(request, 'book_home.html', {'contents': contents, 'posts':posts})

def detail(request, id):
    data = get_object_or_404(Book, pk = id)
    return render(request, 'book_detail.html', {'data':data})

def new(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.p_date = timezone.now() #날짜 생성
            book.save() 
            return redirect('book')
    else:
        book_form = BookForm()
        return render(request, 'book_new.html', {'form':book_form})

def edit(request, id):
    post = get_object_or_404(Book, pk = id)
    if request.method == 'GET':
        book_form = BookForm(instance = post)
        return render(request, 'book_edit.html', {'edit_book' : book_form})
    else:
        book_form = BookForm(request.POST, request.FILES, instance = post)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.p_date = timezone.now() 
            book.save()
        return redirect('/book/' + str(id))

def delete(request, id):
    erase_book = Book.objects.get(id = id)
    erase_book.delete()
    return redirect('book')

def search(request):
    blogs = Book.objects.all().order_by('-id')

    q = request.POST.get('q', "") 

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'book_search.html', {'blogs' : blogs, 'q' : q})
    
    else:
        return render(request, 'book_search.html')