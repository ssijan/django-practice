from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from django.db.models import Sum

# Create your views here.
def index(request):
    obj = Student.objects.all().order_by('student_id__student_id')

    paginator = Paginator(obj,15)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})


def cal_GPA(x):
    if x >= 80:
        return 'A+'
    elif x >= 70:
        return 'A'
    elif x >= 60:
        return 'A-'
    elif x >= 50:
        return 'B'
    elif x >= 40:
        return 'C'
    elif x >= 33:
        return 'D'
    else:
        return 'F'
    

def get_rankTotal(st_id):

    total = Student.objects.filter(student_id__student_id = st_id)\
    .aggregate(total_mark = Sum('studentmarks__mark'))['total_mark']

    rank = Student.objects.annotate(total_mark = Sum('studentmarks__mark'))\
        .filter(total_mark__gt = total).count() + 1
    
    return total, rank

def result(request):
    student = None
    mark = None
    error = None
    total = None
    rank = None
    if request.method == 'POST':
        student_id = request.POST.get('student_id')

        try:
            student = Student.objects.get(student_id__student_id = student_id)
            mark = student.studentmarks.all()

            for m in mark:
                m.grade = cal_GPA(m.mark)

            total , rank = get_rankTotal(student_id)
        except Student.DoesNotExist:
            error = 'Student Not Found'

    return render(request, 'result.html', {
        'student': student,
        'marks': mark,
        'error': error,
        'total':total,
        'rank': rank,
    })


# Download Result in PDF
def result_pdf(request, student_id):
    # Fetch the student and marks
    student = get_object_or_404(Student, student_id__student_id=student_id)
    marks = student.studentmarks.all()

    for m in marks:
        m.grade = cal_GPA(m.mark)

    total , rank = get_rankTotal(student_id)

    # Render HTML template to string
    html_string = render_to_string('result_pdf.html', {
        'student': student,
        'marks': marks,
        'total':total,
        'rank': rank,
    })

    # Generate PDF
    pdf_file = HTML(string=html_string).write_pdf()

    # Return as response
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.student_name}_result.pdf"'
    return response