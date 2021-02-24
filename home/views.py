from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from home.models import Dars, Faculty, Time

# Create your views here.
def index(request):
    faculty = Faculty.objects.all()
    time = Time.objects.all()
    page = 'home'
    data = []
    context = {
        'time': time,
        'page': page,
        'faculty': faculty,
    }
    return render(request, 'index.html', context)


def faculty_page(request, id, slug):
    faculty = Faculty.objects.all()
    dars = Dars.objects.filter(yunalish__id=id)
    times = dars.order_by('time').values_list('time__soat', flat=True).distinct()
    data_list = []
    if dars.exists():
        for time in times:
            courses = []
            for week in dars[0].WEEK:
                get_dars_list = dars.filter(time__soat=time, hafta=week[0])
                course_list = []
                if get_dars_list.exists():
                    for d in get_dars_list:
                        course_list.append(d)
                else:
                    course_list = ''
                courses.append({'week': week[0], 'course_list': course_list})
            data_list.append({'time': time, 'courses': courses})
    print(data_list)

    context = {
        'dars': data_list,
        'faculty': faculty,
    }
    return render(request, 'faculty_page.html', context)