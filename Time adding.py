# Version 1: Military Time
# Clean copy that works

def iter_minutes(starthr,startmin,endhr,endmin):
    j = 0
    i = 0
    d = starthr
    e = startmin
    b = (60-startmin) + 60*(endhr - (starthr + 1)) + endmin
    
    if starthr < 1 or starthr > 24 or endhr < 1 or endhr > 24 or startmin >= 60 or startmin < 0 or endmin >= 60 or endmin < 0 or starthr > endhr:
        print("Error.  Invalid hour and/or minute.")
    else:
        # Prints total time in minutes
        print("Total time: ",b,"minutes")
    
        # While loop to print time iterations
        if b < 60:
            while (j+e) < b+1:
                j += 1
                if (j+e) < 10:
                    print(d," : 0",(j+e),sep="")
                else:
                    print(d,":",(j+e))    
        else:
            while (i+e) < b:
                i += 1
                if (i+e) < 10:
                    print(d," : 0",(i+e),sep="")
                elif (i+e) < 60:
                    print(d,":",(i+e))
                elif (i+e) % 60 == 0:
                    print(d + 1,": 00")
                    d += 1
                    b = b - i
                    i = 0
                    e = 0
