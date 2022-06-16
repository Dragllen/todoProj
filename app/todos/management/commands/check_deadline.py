from datetime import timedelta, time, datetime

from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware
from django.core.mail import send_mail
from todos.models import Todo
now = datetime.now()
today = timezone.now()
tomorrow = today + timedelta(1)
today_start = make_aware(datetime.combine(today, time()))
today_end = make_aware(datetime.combine(tomorrow, time()))


class Command(BaseCommand):
    help = "Send email if deadline is near"

    def handle(self, *args, **options):
        todos = Todo.objects.all()

        if todos:
            message = ""

            for todo in todos:
                dt = todo.deadline - now
                hours = dt.seconds /60 / 60
                if hours <= 1:
                    message += f"{todo} \n"

                    subject = (
                        f"Remind of todo {todo.title}, deadline is {todo.deadline}"
                        )

                    send_mail(subject=subject, message=message, html_message=None)

                    self.stdout.write("E-mail Report was sent.")
