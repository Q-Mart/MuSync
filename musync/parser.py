import argparse
import re

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
