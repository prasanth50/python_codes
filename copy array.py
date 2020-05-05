from array import *
val=array('i',[3,-8,9,6])
newval=array(val.typecode,(a for a in val))
for e in newval:
    print(e)

