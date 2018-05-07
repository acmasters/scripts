#!/usr/bin/python3
import os
import time
import subprocess

# Remove arquivos com mais de 24 horas 
now = time.time()

folder = '/mail_logs/tmp'

files = [os.path.join(folder, filename) for filename in os.listdir(folder)]
for filename in files:
    if (now - os.stat(filename).st_mtime) > 86400:
        command = "rm {0}".format(filename)
        subprocess.call(command, shell=True)

