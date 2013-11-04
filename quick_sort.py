import sys

def swap(lst,m,n):

    if(m==n):
        return lst
    else:
        lst[m]=lst[m]+lst[n]
        lst[n]=lst[m]-lst[n]
        lst[m]=lst[m]-lst[n]
        return lst

def quick_sort(lst):
    global m

    if(len(lst)==1):
        return
    
    m=m+ len(lst)-1
    
    #lst=swap(lst,0,len(lst)-1) #UNCOMMENT THIS FOR QUESTION TWO
    
    if(len(lst)%2==0):       #UNCOMMENT FOR QUESTION THREE
        k=(len(lst)/2)-1
    else:
        k=(len(lst)-1)/2
    med=[lst[0],lst[k],lst[len(lst)-1]]
    
    med.sort()
    
    k=lst.index(med[1])
    lst=swap(lst,0,k)
    #print ("median is %d" %lst[0])


    
    P=lst[0] #PIVOT IS THE FIRST ELEMENT
    i=1
    
    for j in range(1,len(lst)):
        if(lst[j]<=P):
            lst=swap(lst,i,j)
            i=i+1




    lst=swap(lst,0,i-1)
    
    if(i>1):
        #print lst[0:i-1]
        quick_sort(lst[0:i-1])
        
    if (i<len(lst)):
        #print(lst[i:])
        quick_sort(lst[i:len(lst)])
        
if __name__=='__main__':
    if len(sys.argv)>1:
        global m
        m=0
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        lst=[]
        for line in inputDataFile.readlines():
            lst.append(int(line.split()[0]))    #Default value for split is '\n'

        inputDataFile.close()
       
        quick_sort(lst)
        print m
        
    else:
        print 'This quick-sort program requires an input file.'
