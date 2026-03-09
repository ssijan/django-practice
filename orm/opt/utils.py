from django.conf import settings
from django.core.mail import send_mail, EmailMessage

def send_mail_to_client(pdf_file,student):
    email = EmailMessage(
        subject='Your Result Report',
        body='Please Find The Attachment',
        from_email=settings.EMAIL_HOST_USER,
        to=['mdsijan12122002@gmail.com']
    )

    email.attach(
        f"{student.student_name}_result.pdf",
        pdf_file,
        'application/pdf'
    )

    email.send()
