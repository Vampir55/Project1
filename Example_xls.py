# Example works with xls tablets

import openpyxl

workbook = openpyxl.load_workbook(filename="Data1.xlsx")  # load xls file
sheet = workbook['Лист1']

val = sheet['A1'].value

print(val)
