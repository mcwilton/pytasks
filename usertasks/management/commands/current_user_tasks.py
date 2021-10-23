from django.core.management.base import BaseCommand
from usertasks.models import Current, Completed, Deleted


class Command(BaseCommand):
    help = 'Current Lists'

    def handle(self, *args, **options):
        current_tasks = Current.objects.all()

        for task in taskss:
            task.current()
            self.stdout.write(f'Here is the "{task}"')