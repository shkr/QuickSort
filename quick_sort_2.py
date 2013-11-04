import sys

def swap(lst,k,i):
    
    lst[k]=lst[k]+lst[i]
    lst[i]=lst[k]-lst[i]
    lst[k]=lst[k]-lst[i]
    return lst

def quick_sort(lst):
    lst=swap(lst,0,len(lst)
    if(len(lst)==1):
        return
    
    global m
             
    P=lst[len(lst)-1] #PIVOT IS THE FIRST ELEMENT
    i=0
    
    for j in range(0,len(lst)-1):
        if(lst[j]<=P):
            if not i==j:
                lst=swap(lst,i,j)
            i=i+1
                

    
    if(i>0):
        quick_sort(lst[:i])
        m=m+ i-1 #<p sub-array
    if (i<len(lst)-1):
        quick_sort(lst[i:len(lst)-1])
        m=m+ len(lst)-2-i #>p sub-array
        
        
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
