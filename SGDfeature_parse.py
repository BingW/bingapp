# coding:utf-8
# Author: bingwang
# Email: toaya.kase@gmail.com
# Copylight 2012-2012 Bing Wang
# LICENCES: GPL v3.0

__docformat__ = "epytext en"
# dependents: test file in test/right.gff

class FeatureRecord():
    """calss FeatureRecord for store SGD Feature Format,
    normally from a tab file, each line will generate a 
    FeatureRecord object.
    >>> a = FeatureRecord()
    """
    #TODO add value check
    def __init__(self):
        self.SGDID= ""
        self.type = ""
        self.qualifier = ""
        self.fetname = ""
        self.stdname = ""
        self.alias = ""
        self.parent = ""
        self.SGDID2 = ""
        self.chr = ""
        self.start = ""
        self.end = ""
        self.strand = ""
        self.geneticpos = ""
        self.vercoord = ""
        self.verseq = ""
        self.descrip = ""

def featureIterator(handle):
    """handle - input file
    file has lines without 16 columns will cause ValueError
    iterator yeilds Gffrecord object
    >>> for featurerecord in featureIterator(handle):
    >>>     print featurerecord.start,featurerecord.end
    """
    while 1:
        line = handle.readline()
        if not line: return
        if line.count("\t") != 15:
            raise ValueError("record in SGDfeature file should have 16 columns")
        r= FeatureRecord()
        r.SGDID,r.type,r.qualifier,r.fetname,r.stdname,\
        r.alias,r.parent,r.SGDID2,r.chr,r.start,r.end,\
        r.strand,r.geneticpos,r.vercoord,r.verseq,r.descrip = line.split("\t")
        yield r

def _test():
    #TODO SGDfeature_pharse test
    SGD_handle = open("test/SGDfeature.tab")
    featureIterator(SGD_handle).next()
    print "1 test pass"

if __name__ == "__main__":
    _test()
