from pathlib import Path
from datetime import date

def get_file_path(name):
  today = date.today().strftime("%Y%m%d")
  i = name.index("【")
  name = name[0:i]
  target_dir = Path("C:/Users/hk/Desktop/somewhere") # ここ  
  file_path = target_dir.glob(f"*{today}*{name}*.txt")
  return file_path.__next__()

def get_sauce(salon_name):
  file_path = get_file_path(salon_name)
  with open(file_path, "r", encoding= "utf-8") as f:
    lines = f.readlines()
  ls = []
  le = []
  for cnt in range(len(lines)):
    if lines[cnt].startswith("<<<"):
      ls.append(cnt)
    if lines[cnt].startswith(">>>"):
      le.append(cnt)
  sauce = ""
  for i in zip(ls, le):
    s = "".join(lines[i[0]+1: i[1]])
    sauce = sauce+ s+ "\n"
  return sauce

