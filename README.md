# MuSync
File syncing for a music library shared across multiple devices, written in python 3

Currently only supports synchronization over rsync

## How to run ##
1. Make sure you can ssh into the device you want to synch with. I use sshelper for my android phone
2. Make sure your working directory is `Musync/musync`
3. Create a config.yaml file (copy from the example)
4. If the server is using a dynamic ip run `./musync -a {{ IP Address }} {{ Profile Name}}` otherwise run `./musync {{ Profile Name }}`
