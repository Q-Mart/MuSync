#!/usr/bin/python3

from ftplib import FTP
import yaml
import argparse
import re

def getConf():
  try:
    with open('config.yaml', 'r') as yamlFile:
      cfg = yaml.load(yamlFile)

  except FileNotFoundError:
    return ("Config not found! Please create a config.yaml file " +
           "and follow the example of config.yaml.example")

  return cfg

def serverDefinedInConf(name, cfg):
  if name in cfg: return name
  else:
    raise argparse.ArgumentTypeError("%s is not defined in config.yaml" % name)

def validIP(address):
  ipRegex = ("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}" 
            "(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
  if re.match(ipRegex, address):
    return address
  else:
    raise argparse.ArgumentTypeError("%s is not an IP Address" % address)

def parseArgs(cfg):

  def availableServer(server):
    return serverDefinedInConf(server, cfg)
  parser = argparse.ArgumentParser(description="Synchronises music directories between two devices")
  parser.add_argument('serverName',
                      type = availableServer,
                      help = "The name of the server defined in config")

  parser.add_argument('-a',
                      dest="serverAddress",
                      type=validIP,
                      help="IP address of server if it is dynamic")

  return parser.parse_args()

if __name__ == "__main__":
  cfg = getConf()
  args = parseArgs(cfg)
  print(args.serverName)
  print(args.serverAddress)

  if cfg[args.serverName]['hostname'] == 'dynamic' and not args.serverAddress:
    print("%s uses a dynamic IP, please supply one with the -a flag or specify"
          "the address in config.yaml" % args.serverName)
