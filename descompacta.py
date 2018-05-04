#!/usr/bin/env python3 

import subprocess
import glob
import os
import shutil

PATH_TO_FILE = "/mail_logs"
FILE_DIR = "/mail_logs/tmp"

for file in glob.glob(PATH_TO_FILE + "/*.gz"):
    if os.path.isdir(file) == False:
        shutil.copy(file, FILE_DIR)
        # Descompacta arquivos
        subprocess.call(["gunzip", FILE_DIR + "/" + os.path.basename(file)])
        #Remove o arquivo gz atual
        os.remove(file)
        # Altera permissao arquivos tmp
        for root, dirs, files in os.walk(FILE_DIR):
            for f in files:
                os.chmod(os.path.join(root,f), 0o644)
    else:
        exit(0)
~               
