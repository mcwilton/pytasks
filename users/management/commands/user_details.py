from django.core.management.base import BaseCommand, CommandError
from usertasks.models import Current, Completed, Deleted
import xlsxwriter
from users.models import Profile;


workbook = xlsxwriter.Workbook('users.xlsx')
worksheet = workbook.add_worksheet()
preview = 'This is a Header Line'

worksheet.write('A1', preview)

class Command(BaseCommand):
    help = 'User Details'

    def handle(self, *args, **options):
        row_num = 2

        columns = ['Username', 'First name', 'Last name', 'Email address', 'ID Number', 'Address', 'Phone', 'User ID' ]

        for col_num in range(len(columns)):
            worksheet.write(row_num, col_num, columns[col_num])

        rows = Profile.objects.all().values_list('user', 'first_name', 'second_name', 'email', 'id_number', 'address', 'phone', 'user_id')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                worksheet.write(row_num, col_num, row[col_num])

        workbook.close()
