while 1: print "->","".join(map(lambda x: {"A":"T","C":"G","G":"C","T":"A"}[x] if x in ["A","T","C","G"] else "N", reversed(list(raw_input().upper()))))
