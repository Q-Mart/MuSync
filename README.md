# MuSync
File syncing for a music library shared across multiple devices, written in python 3

Currently only supports synchronization over FTP but more methods (rsync to come).

## How to run ##
1. Start an FTP server from the device you wish to synch with. Make sure that it serves its music directory as root
2. Make sure your working directory is `Musync/musync`
3. Create a config.yaml file (copy from the example)
4. If the server is using a dynamic ip run `./musync -a {{ IP Address }} {{ Profile Name}}` otherwise run `./musync {{ Profile Name }}`
