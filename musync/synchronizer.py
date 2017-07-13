import subprocess

GREEN='\033[0;32m'
YELLOW='\033[0;33m'
END='\033[0m'


def printGreen(txt):
  print(GREEN+txt+END)

def printYellow(txt):
  print(YELLOW+txt+END)

def synchronize(cfg, serverName):
  address = cfg[serverName]['hostname']
  user = cfg[serverName]['user']
  password = cfg[serverName]['password']
  port = cfg[serverName]['port']
  remoteLibrary = cfg[serverName]['music_dir']
  localLibrary = cfg['local_conf']['music_dir']

  rsyncArgs="-rvzn+--progress+--ignore-existing"
  if port: rsyncArgs += "+-e+'/usr/bin/ssh -p {0}'".format(port)

  cmd = 'rsync+{0}+{1}+{2}@{3}:{4}'.format(rsyncArgs, localLibrary, user, address, remoteLibrary)
  
  printYellow('Your command is:')
  printGreen(cmd)
  printYellow('Please Copy and Paste into the terminal to run')
