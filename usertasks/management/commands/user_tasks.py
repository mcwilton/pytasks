from django.core.management.base import BaseCommand, CommandError
from usertasks.models import Current, Completed, Deleted
import xlsxwriter
from django.utils import timezone
from datetime import datetime, timezone

workbook = xlsxwriter.Workbook('tasks.xlsx', {'remove_timezone': True})

worksheet = workbook.add_worksheet('Current Tasks')
preview = 'This is a Header Line'
worksheet.write('A1', preview)

worksheet1 = workbook.add_worksheet('Deleted Tasks')
preview1 = 'This is a Header Line'
worksheet.write('A1', preview1)

worksheet2 = workbook.add_worksheet('Completed Tasks')
preview2 = 'This is a Header Line'
worksheet.write('A1', preview2)


class Command(BaseCommand):
    help = 'Tasks Excel Sheet'

    def handle(self, *args, **options):
        row_num = 2

        columns = ['Task', 'User', 'Status','Date']


        for col_num in range(len(columns)):
            worksheet.write(row_num, col_num, columns[col_num])

        rows = Current.objects.all().values_list('task', 'user', 'status', 'date')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                worksheet.write(row_num, col_num, row[col_num])


        for col_num in range(len(columns)):
            worksheet1.write(row_num, col_num, columns[col_num])

        rows = Deleted.objects.all().values_list('task', 'status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                worksheet1.write(row_num, col_num, row[col_num])


        for col_num in range(len(columns)):
            worksheet2.write(row_num, col_num, columns[col_num])

        rows = Completed.objects.all().values_list('task', 'status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                worksheet2.write(row_num, col_num, row[col_num])

        workbook.close()
