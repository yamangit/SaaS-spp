from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request, *args, **kwargs):
    
    return about_view(request, *args, **kwargs)


def my_old_home_page_view(request, *args, **kwargs):
    html_ = ""
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(html_)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    html_ = ""
    my_title = "My Page"
    try:
        percent = f"{page_qs.count() * 100.0 / qs.count():.2f}"
    except:
        percent = 0
    
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "page_visit_percent": f'{percent}',
        "total_visit_count": qs.count(),
    }
    html_template = "home.html"
    PageVisit.objects.create(path = request.path)
    return render(request, html_template, my_context)
