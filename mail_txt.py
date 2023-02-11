import xlrd
import datetime
from time import sleep
file = "sample.xls"
wb = xlrd.open_workbook(file)
ws1 = wb.sheet_by_index(0)

def get_row_no(key):
  for r in range(ws1.nrows):
    try:
      number = str(int(ws1.cell(r,0).value))
    except:
      continue
    if number == key:
      return(r)

def ser_to_dt(serialVal:float) -> datetime:
    dtime = (datetime.datetime(1899,12,30) + datetime.timedelta(serialVal))
    return dtime

def get_mail(number:str):
  try:
    row_no = get_row_no(number)
    salon_name = ws1.cell(row_no, 1).value
    sagyou_date = ser_to_dt(ws1.cell(row_no, 2).value).strftime("%Y/%m/%d")
    nyuten_time = ser_to_dt(ws1.cell_value(row_no, 3)).strftime("%H:%M")
    sagyo_kanryo_time = ser_to_dt(ws1.cell_value(row_no, 4)).strftime("%H:%M")
    atesaki = "atesaki@mail"
    cc_atesaki = "cc_atesaki@mail"
    title = f"{salon_name}の作業報告"
    mail = f"""店名:{salon_name}
日付:{sagyou_date}
入店時刻：{nyuten_time}
退店時刻：{sagyo_kanryo_time}
"""
    return {"atesaki": atesaki, "cc_atesaki": cc_atesaki, "title": title, "mail": mail}
  except:
    return "行が見つかりませんでした"

 
mail_data = get_mail(input("番号"))
if type(mail_data) != dict:
  print(mail_data)
  sleep(3)
  exit ()
m_txt =f"""
宛先：
{mail_data["atesaki"]}
 ===================
CC:
{mail_data["cc_atesaki"]}

 ===================
タイトル：
{mail_data["title"]}

====================
本文：
{mail_data["mail"]}

 """

with open("mail.txt", "w")as f:
  f.write(m_txt)
  f.close

if __name__ == "__main__":
  import subprocess
  subprocess.Popen(["notepad","mail.txt"])