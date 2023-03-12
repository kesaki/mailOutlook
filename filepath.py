import pathlib

dir_path = pathlib.Path("D:/スレーブDownload/")
latest_file = max(dir_path.glob("*.zip"), key=lambda f: f.stat().st_mtime)
print("最新のファイル名は", latest_file.name)
