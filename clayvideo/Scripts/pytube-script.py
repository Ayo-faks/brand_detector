#!c:\users\ayool\desktop\videoindexingproject\clayvideo\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pytube==10.5.1','console_scripts','pytube'
__requires__ = 'pytube==10.5.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pytube==10.5.1', 'console_scripts', 'pytube')()
    )
