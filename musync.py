#!/usr/bin/python3

from ftplib import FTP
import yaml

def getConf():
  try:
    with open('config.yaml', 'r') as yamlFile:
      cfg = yaml.load(yamlFile)

  except FileNotFoundError:
    return ("Config not found! Please create a config.yaml file " +
           "and follow the example of config.yaml.example")

  return cfg

print(getConf())
