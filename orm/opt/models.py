from django.db import models

# Create your models here.
class StudentID(models.Model):
    student_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.student_id 
    
    
class Department(models.Model):
    department = models.CharField(max_length=100, unique= True)

    def __str__(self):
        return self.department
    
    class Meta:
        ordering = ['department']


class Student(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete = models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name='studentid', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering = ['student_id']
        verbose_name = 'student'        


class Subject(models.Model):
    subject = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['subject']
    

class SubjectMark(models.Model):
    student = models.ForeignKey(Student, related_name='studentmarks', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.student.student_name} {self.subject.subject}'
    
    class Meta:
        unique_together = ['student', 'subject']


