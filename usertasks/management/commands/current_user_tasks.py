from django.core.management.base import BaseCommand
from usertasks.models import Current, Completed, Deleted


class Command(BaseCommand):
    help = 'Current Lists'

    def handle(self, *args, **options):
        current_tasks = Current.objects.all()

        if not current_tasks:
            raise CommandError('No tasks', returncode=2)

        for task in current_tasks:
            task.current()
            self.stdout.write(self.style.SUCCESS(f'Here is the "{task}"'))

