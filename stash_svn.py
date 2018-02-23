#!/usr/bin/python3

import git
import os
import shutil 
import time,datetime 
import subprocess

DIR_NAME = "/bkp/temp"
DIR_HOME = "/home/user/svn/"
REMOTE_URL = "https://xxxxxx@github.com/script.git"
SVN_SCRIPTS = "/home/user/svn/scripts/"

#Cria diretorio temporario
if os.path.isdir(DIR_NAME):
   shutil.rmtree(DIR_NAME)
os.mkdir(DIR_NAME)

# Clone do repo
repo = git.Repo.init(DIR_NAME)
origin =  repo.create_remote('origin', REMOTE_URL)
origin.fetch()
origin.pull(origin.refs[0].remote_head)

# Removendo dirs local
shutil.rmtree("/home/user/svn/scripts")

#Copia de dados pro svn local 
shutil.move("/bkp/temp/", SVN_SCRIPTS)

#Dos2Unix tabview caso necessario
dos2unix = "dos2unix /home/user/svn/script/teste.xyz"
process =  subprocess.Popen(dos2unix, 
			   shell = True,  
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE, 
                           universal_newlines=True)
out, err = process.communicate() 

print ("===== Pronto =====")
