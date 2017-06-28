#!/usr/bin/python3

from ftplib import FTP
import yaml
import argparse

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

def parseArgs(cfg):
  def availableServer(server):
    return serverDefinedInConf(server, cfg)

  parser = argparse.ArgumentParser(description="Synchonises music directories between two devices")
  parser.add_argument('server',
                      type = availableServer,
                      help = "The name of the server defined in config")

  parser.add_argument('-p', type=int, help="Port number")
  return parser.parse_args()

if __name__ == "__main__":
  cfg = getConf()
  args = parseArgs(cfg)
  print(args.server)
