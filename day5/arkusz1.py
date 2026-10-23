import openpyxl

# pip install openpyxl

# działania na plikach excel, formatowanie, stylizacja, wykresy

wokrbook = openpyxl.load_workbook('sales.xlsx')
worksheet = wokrbook.active

print(worksheet)  # <Worksheet "Arkusz1">

print(worksheet.title)  # Arkusz1
