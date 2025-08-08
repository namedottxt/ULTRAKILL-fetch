from getpass import getuser
from pathlib import Path
from shutil import move
import os

# Config
USERNAME = getuser()
WINDOWS_PATH = Path('C:/ProgramData/fastfetch/config.jsonc')
UNIX_PATH = Path(f'/home/{USERNAME}/.config/fastfetch/config.jsonc')
SRC_FILE = 'config.jsonc'

def overwrite(dst_path: Path, src_file_path: str):    
    if os.path.isfile(dst_path):
        os.remove(dst_path)

    move(src_file_path, dst_path)

# Windows
if os.name == 'nt': overwrite(WINDOWS_PATH, SRC_FILE)

# Unix
else: overwrite(UNIX_PATH, SRC_FILE)