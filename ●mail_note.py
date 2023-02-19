use_outlook = 1
use_reinstall_memo = 1
import xlrd
import datetime
from time import sleep
file = "sample.xls"
wb = xlrd.open_workbook(file)
ws1 = wb.sheet_by_index(0)


def get_row_no(key):
  for r in range(ws1.nrows):
    try:
      num = str(int(ws1.cell(r, 0).value))
    except:
      continue
    if num == key:
      return r

def ser_to_dt(serialVal:float) -> datetime:
    dtime = (datetime.datetime(1899,12,30) + datetime.timedelta(serialVal))
    return dtime

def gene_mail(number:str):
  try:
    row_no = get_row_no(number)
    salon_name = ws1.cell(row_no, 2).value
    salon_code = ws1.cell(row_no, 46).value
    nouhin_date = ser_to_dt(ws1.cell_value(row_no, 12)).strftime("%Y/%m/%d")
    nyuten_time = ser_to_dt(ws1.cell(row_no, 14).value).strftime("%H:%M")
    settei_kanryo_time = ser_to_dt(ws1.cell_value(row_no, 15)).strftime("%H:%M")
    taiten_time = ser_to_dt(ws1.cell(row_no, 17).value).strftime("%H:%M")
    atesaki = "tb_aaaaaanet.com"
    cc_atesaki = "vjcaaaaaaa-net.com"
    mail_title = f"■導入完了【{number}】 {salon_name}】★"
    #ここ
    if use_reinstall_memo:
      import 再インストールメモ as re
      sauce = re.get_sauce(salon_name)
    else:
      sauce = "///////////////////////////////////"  
    mail_main = f"""
    
【導入完了報告】
以下案件の導入作業が完了致しましたので、
ご報告致します。

　　　サロン名：{salon_name}
　　　サロンコード：{salon_code}
　　　納品日付：{nouhin_date}
　　　入店時間：{nyuten_time}
　　　設定完了時間：{settei_kanryo_time}
　　　退店時間：{taiten_time}

【申し送り】

{sauce}

以上、よろしくお願い致します。

"""
    mail_text = f"""
    宛先：
    {atesaki}
    ===================
    CC:
    {cc_atesaki}

    ===================
    タイトル：
    {mail_title}

    ====================
    本文：
    {mail_main}

"""
    with open("mail.txt", "w")as f:
      f.write(mail_text)
      f.close   
    return {"atesaki": atesaki, "cc_atesaki": cc_atesaki, "mail_title": mail_title, "mail_main": mail_main, "mail_text": mail_text}
  except:
    return "行が見つかりませんでした"

mail_data = gene_mail(input("番号"))
if not isinstance(mail_data, dict):
  print(mail_data)
  sleep(2)
else:
  if use_outlook:
    import outlook9222
    outlook9222.send_by_outlook(mail_data)

  else:
    import subprocess
    subprocess.Popen(["notepad","mail.txt"])


