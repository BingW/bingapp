#! /usr/bin/env python
# coding:utf-8
# Author: bingwang
# Email: toaya.kase@gmail.com
# Copylight 2012-2012 Bing Wang
# LICENCES: GPL v3.0

__docformat__ = "epytext en"
# dependents: dialign-tx
import os

conf = "/Users/bingwang/zen/bing/dialign/conf/"
def aln_one(fsafile):
    dialign = "dialign-tx "
    outfile = fsafile[:fsafile.rfind(".")]+".aln"
    cmd = dialign+" "+conf+" "+fsafile+" "+outfile
    os.system(cmd)

def aln_path(path):
    fsalist = [path+fsa for fsa in os.listdir(path) if fsa.endswith(".fsa")]
    print fsalist
    for fsafile in fsalist:
        aln_one(fsafile)

if __name__ == "__main__":
    #fsapath = "/Users/bingwang/zen/bing/test/"
    fsapath = "/Users/bingwang/zen/yeast_anno_pipe/output/"
    aln_path(fsapath) 
