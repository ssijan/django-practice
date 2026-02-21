from faker import Faker
from .models import *
import random
fake = Faker()

def add_student(n=10):

    try:
        for _ in range(n):
            department_ob = Department.objects.all()

            department = department_ob[random.randint(0,len(department_ob)-1)]
            student_id = f'STU-0{random.randint(100,999)}'
            student_name =fake.name()
            student_email = fake.email()
            student_age = random.randint(20,35)
            student_address= fake.address()

            create_student_id = StudentID.objects.create(student_id = student_id)
            student_ob = Student.objects.create(
                department = department,
                student_id = create_student_id,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address
            )


    except Exception as e:
        print(e)
        

def add_mark():
    try:
        student_obj = Student.objects.all()
        subs = Subject.objects.all()
        for st in student_obj:
            for sub in subs:
                SubjectMark.objects.create(
                    student = st,
                    subject = sub,
                    mark = random.randint(0,100)
                )
    except Exception as e:
        print(e)