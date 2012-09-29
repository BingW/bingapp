# coding:utf-8
# Author: bingwang
# Email: toaya.kase@gmail.com
# Copylight 2012-2012 Bing Wang
# LICENCES: GPL v3.0

__docformat__ = "epytext en"
# dependents: test file in test/right.gff

class GffRecord():
    """calss GffRecord for store Generic Feature Format,
    normally from a gff file, each line will generate a 
    GffRecord object.
    >>> a = GffRecord()
    >>> a.seqid = 1
    >>> print a.attributes
    {'ID':"",'Name':"",'Paraent':"",'Alias':"" ...} 
    """
    #TODO add value check
    def __init__(self):
        self.seqid = ""
        self.source = ""
        self.type = ""
        self.start = 0
        self.end = 0
        self.score = 0.0
        self.strand = ""
        self.phase = 0
        self.attributes = {'ID':"",'Name':"",'Paraent':"",'Alias':"",\
                'Parent':"",'Target':"",'Gap':"",'Deriver_from':"",\
                'Note':"",'Dbxref':"",'Ontology_term':""}

def gffIterator(handle):
    """handle - input file
    file has lines without nine columns will cause ValueError
    iterator yeilds Gffrecord object
    >>> for gffrecord in gffIterator(handle):
    >>>     print gffrecord.start,gffrecord.end
    """
    while 1:
        line = handle.readline()
        if line.startswith("#"): continue
        if not line: return
        if line.count("\t") != 8:
            raise ValueError("record in GFF3 file should have nine columns")
        r= GffRecord()
        r.seqid,r.source,r.type,r.start,r.end,\
        r.score,r.strand,r.phase,column9 = line.split("\t")
        for a in column9.split(";"):
            r.attributes[a.split("=")[0]] = a.split("=")[1].split(",")
        yield r

#TODO write gff_file

def _test():
    #TODO gff_pharse test
    gff_handle = open("test/right.gff")
    gffIterator(gff_handle).next()
    print "1 test pass"

if __name__ == "__main__":
    _test()
