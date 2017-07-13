#!/usr/bin/python3

import yaml

import parser
import exceptions
import synchronizer


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
      raise exceptions.InvalidIPAddress(
          "%s uses a dynamic IP, please supply one with the -a flag or specify"
          "the address in config.yaml" % args.serverName)

    synchronizer.synchronize(cfg, args.serverName)
