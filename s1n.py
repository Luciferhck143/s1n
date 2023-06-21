import os
try:import requests
except:os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('git pull')
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
  import s1n
else:
  exit(' Sorry Device Not Support ')
