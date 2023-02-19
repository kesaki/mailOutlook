import xlwt
wb = xlwt.Workbook()
sheet = wb.add_sheet("sheet1")
sheet.write(0, 0, 'A')
sheet.write(0, 1, 'B')
sheet.write(1, 0, 10)
sheet.write(1, 1, 20)
wb.save("メモ1.xls")

import subprocess
subprocess.Popen(["start","メモ.xls"], shell = True)