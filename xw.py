import xlwings as xw
app = xw.apps.active
workbook = app.books.active
if workbook.name == "test.xls":
  sheet = workbook.sheets[0]
  sheet.range('A1').value= ""
else:
  print("シートが違うみたい")