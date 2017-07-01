#!/usr/bin/python3

from ftplib import FTP
import yaml
import parser
import os

class InvalidIPAddress(Exception):
  pass

def getConf():
  try:
    with open('config.yaml', 'r') as yamlFile:
      cfg = yaml.load(yamlFile)

  except FileNotFoundError:
    return ("Config not found! Please create a config.yaml file " +
           "and follow the example of config.yaml.example")

  return cfg

if __name__ == "__main__":
  cfg = getConf()
  args = parser.parseArgs(cfg)

  if cfg[args.serverName]['hostname'] == 'dynamic':
    if args.serverAddress:
      cfg[args.serverName]['hostname'] = args.serverAddress
    else:
      raise InvalidIPAddress("%s uses a dynamic IP, please supply one with the -a flag or specify"
                             "the address in config.yaml" % args.serverName)

  address = cfg[args.serverName]['hostname']
  user = cfg[args.serverName]['ftp']['user']
  password = cfg[args.serverName]['ftp']['password']
  port = cfg[args.serverName]['ftp']['port']
  localLibrary = cfg['local_conf']['music_dir']

  ftp = FTP()
  ftp.connect(address, port)
  ftp.login(user=user, passwd=password)
  serverFolders = set(ftp.nlst())
  print(serverFolders)
  localFolders = set(os.listdir(localLibrary))
  diff = localFolders - serverFolders
  ftp.quit()

  for item in diff:
    fullpath = os.path.join(localLibrary, item)
    if os.path.isfile(fullpath):
      print("%s is a file" % fullpath)
    elif os.path.isdir(fullpath):
      print("%s is a folder" % fullpath)
