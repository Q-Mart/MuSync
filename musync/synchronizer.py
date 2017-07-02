from ftplib import FTP, error_perm
import os

GREEN='\033[0;32m'
YELLOW='\033[0;33m'
END='\033[0m'

def printGreen(txt):
  print(GREEN+txt+END)

def printYellow(txt):
  print(YELLOW+txt+END)

def ftpUpload(name, pathToParent, ftp):
  fullpath = os.path.join(pathToParent, name)
  if os.path.isfile(fullpath):
    printYellow("+ %s" % fullpath)
    ftp.storbinary('STOR ' + name, open(fullpath,'rb'))
  elif os.path.isdir(fullpath):
    printGreen("+ %s" % fullpath)

    try:
      ftp.mkd(name)

    # ignore "directory already exists"
    except error_perm as e:
      if not e.args[0].startswith('550'): 
        raise

    ftp.cwd(name)
    for item in os.listdir(fullpath):
      ftpUpload(item, fullpath, ftp)
    ftp.cwd('..')


def synchronizeWithFTP(cfg, serverName):
  address = cfg[serverName]['hostname']
  user = cfg[serverName]['ftp']['user']
  password = cfg[serverName]['ftp']['password']
  port = cfg[serverName]['ftp']['port']
  localLibrary = cfg['local_conf']['music_dir']

  ftp = FTP()
  ftp.connect(address, port)
  ftp.login(user=user, passwd=password)
  serverFolders = set(ftp.nlst())
  localFolders = set(os.listdir(localLibrary))
  diff = localFolders - serverFolders
  for item in diff:
    ftpUpload(item, localLibrary, ftp)
  ftp.quit()
