from pathlib import Path

root_dir= Path("destination")

for path in root_dir.glob("*.csv"):
  with open(path, "wb") as file:         #"wb" means write binnary
    file.write(b"")                      # delete the content of the files
  path.unlink()                          # delete the files
