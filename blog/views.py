from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from .models import Blog,BlogType
from read_statistics.utils import add_once_read
from comment.forms import CommentForm
from comment.models import Comment

def base_data(request,blogs):
    try:
        page = int(request.GET.get('page',1))
    except Exception as e:
        page = 1
    # 分页器
    paginator = Paginator(blogs,settings.CONTENT_OF_EACH_PAGE)
    if page > paginator.num_pages or page < 1:
        page = 1
    page_of_blogs = paginator.get_page(page)
    # 获取页码范围
    page_range = [x for x in range(page - 2,page + 3) if x in paginator.page_range]
    # 加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0,'...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和末页
    if page_range[0] == '...':
        page_range.insert(0,1)
    if page_range[-1] == '...':
        page_range.append(paginator.num_pages)

    blog_types = BlogType.objects.annotate(blog_count=Count('blog'))
    # 获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('created_time','month',order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                         created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    all_blogs = Blog.objects.all().count()
    context = {}
    context['all_blogs_count'] = all_blogs
    context['blog_dates'] = blog_dates_dict
    context['blog_types'] = blog_types
    context['page_range'] = page_range
    context['page_of_blogs'] = page_of_blogs
    return context

def blog_list(request):
    blogs = Blog.objects.all()
    context = base_data(request,blogs)
    return render(request,'blog/blog_list.html',context)

def blogs_with_type(request,blog_type_pk):
    blogs_list = Blog.objects.filter(blog_type=blog_type_pk)
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context = base_data(request,blogs_list)
    context['blog_type'] = blog_type
    return render(request,'blog/blogs_with_type.html',context)

def blogs_with_date(request,year,month):
    blogs = Blog.objects.filter(created_time__year=year,created_time__month=month)
    context = base_data(request,blogs)
    all_blogs = Blog.objects.filter(created_time__year=year,created_time__month=month).count()
    context['date_blog_count'] = all_blogs
    context['blogs_date'] = "%s年%s月" %(year,month)
    return render(request,'blog/blogs_with_date.html',context)


def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog,pk=blog_pk)
    read_cookie_key = add_once_read(request,blog)
    referer = request.META.get('HTTP_REFERER',reverse('index'))
    content_type = ContentType.objects.get_for_model(blog)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST,user=request.user)
        if comment_form.is_valid():
            comment = Comment()
            comment.content_object = comment_form.cleaned_data['content_object']
            comment.user = comment_form.cleaned_data['user']
            comment.text = comment_form.cleaned_data['text']
            comment.save()
            return redirect(referer)
    else:
        comment_form = CommentForm(initial={
            'content_type':content_type,
            'object_id':blog.pk,
        })
    content_type = ContentType.objects.get_for_model(blog)
    comment_list = Comment.objects.filter(content_type=content_type,object_id=blog.pk)

    context = {}
    context['comment_list'] = comment_list
    context['comment_form'] = comment_form
    context['previous_page'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['next_page'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['blog'] = blog
    response = render(request,'blog/blog_detail.html',context) # 响应
    response.set_cookie(read_cookie_key,'true') # 添加阅读cookie
    return response