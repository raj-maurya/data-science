score = raw_input("Enter Score: ")
scor = float(score)

if(scor<=1.0 and scor>=0.0):
    if(scor>=0.9):
        print "A"
    elif(scor >=0.8):
        print "B"
    elif(scor >=0.7):
        print "C"

    elif(scor >=0.6):
        print "D"

    else:
        print "F"

else:
    print ("error, please input correct range i.e. 1.0-0.0")
