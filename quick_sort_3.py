import sys

def swap(lst,k,i):
    
    lst[k]=lst[k]+lst[i]
    lst[i]=lst[k]-lst[i]
    lst[k]=lst[k]-lst[i]
    return lst

def quick_sort(lst):
    global m

    if(len(lst)==1):
        return
    
    if(len(lst)%2==0):
        k=(len(lst)/2)-1
    else:
        k=(len(lst)-1)/2

    med=[lst[0],lst[k],lst[len(lst)-1]]
    med=med.sort()
    k=lst.index(med[1])
    
##    if(  (lst[k]-lst[0])*(lst[k]-lst[len(lst)-1]) > 0):
##            if( (lst[0]-lst[k])*(lst[0]-lst[len(lst)-1]) <0):
##                k=0
##            else:
##                k=len(lst)-1

    lst=swap(lst,0,k)
    
    P=lst[0] #PIVOT IS THE FIRST ELEMENT
    i=1
    
    for j in range(1,len(lst)):
        if(lst[j]<=P):
            if not i==j:
                lst=swap(lst,i,j)
            i=i+1
                

    
    if(i>1):
        quick_sort(lst[1:i])
        m=m+ i-2 #<p sub-array
    if (i<len(lst)):
        quick_sort(lst[i:])
        m=m+ len(lst)-1-i #>p sub-array
        
if __name__=='__main__':
    if len(sys.argv)>1:
        global m
       
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        lst=[]
        for line in inputDataFile.readlines():
            lst.append(int(line.split()[0]))    #Default value for split is '\n'

        inputDataFile.close()
        m=len(lst)-1
        quick_sort(lst)
        print m
        
    else:
        print 'This quick-sort program requires an input file.'
