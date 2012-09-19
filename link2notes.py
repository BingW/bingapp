#! /usr/bin/env python
#coding: utf-8
import os
source_post_path = "/Users/bingwang/zen/homepage/source/_posts/"
target_path = "/Users/bingwang/zen/notes/"

handle = os.popen("grep categories "+source_post_path+"*")
#popen: get the output form terminal
exists = os.listdir(target_path) +['']
categories = set()
for line in handle:
    line = line.strip().split(":")
    if line[1] == "categories":
        categories|=set(line[2].split(" "))
for new_folder in categories - set(exists):
    os.system("mkdir "+target_path+new_folder)
handle = os.popen("grep categories "+source_post_path+"*")
for line in handle:
    line = line.strip().split(":")
    if line[1] != "categories": continue
    os.system("ln "+line[0]+" "+target_path+"archives/")
    for categories in set(line[2].split(" ")):
        if categories:
            os.system("ln "+line[0]+" "+target_path+categories+"/")


