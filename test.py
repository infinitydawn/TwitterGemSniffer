from math import trunc
from tracemalloc import start


Str = "abcd\nefgh\nijkopq\nrstuv\nwxyz\n123123123\n456\n789"
msgSize = 8
if(len(Str) > msgSize):
    chunks = []
    startPoint = 0
    lastPoint = msgSize
    
    while lastPoint<len(Str):
        truncStr=Str[startPoint:lastPoint]
        # rvsTruncStr = enumerate(reversed(truncStr))
        for i,val in enumerate(truncStr):
            if val =="\n":
                print("New line index: "+str(i)+" and value: "+val)
                chunks.append(truncStr[0:i])
                
                startPoint = lastPoint-i+1
                lastPoint = startPoint + msgSize
        
        testStr = ""
        for x in str(truncStr[0:i]):
            testStr += x
        print("Current Chunk: "+testStr)
        print("New Last Point: "+str(lastPoint))
        print("New Start Point: "+str(startPoint)+"\n")

print(chunks)
print(startPoint)