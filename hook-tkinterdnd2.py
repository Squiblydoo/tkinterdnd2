"""pyinstaller hook file.

You need to use this hook-file if you are packaging a project using tkinterdnd2.
Just put hook-tkinterdnd2.py in the same directory where you call pyinstaller and type:

    pyinstaller myproject/myproject.py --additional-hooks-dir=.
"""

import os
import platform
from PyInstaller.utils.hooks import collect_data_files

s = platform.system()
p = {
    'Windows': 'win64',
    'Linux': 'linux64',
    'Darwin': 'osx64',
}
if s in p:
    datas = [x for x in collect_data_files('tkinterdnd2') if os.path.split(x[1])[1] == p[s]]
else:
    raise RuntimeError(f'TkinterDnD2 is not supported on platform "{s}".')
