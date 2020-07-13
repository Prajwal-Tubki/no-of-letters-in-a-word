string=eval(input("Please enter a string (in quotes!):"))
string.casefold()

if (type(string)==str):
    
    def most_frequent(j,i,t):
        a=len(string)
        instring={}
        while(j<a):
            while(i<a):
                if(string[j]==string[i]):
                    t+=1
                
                i+=1
            i=0
            instring[string[j]]=t
            t=0
            j+=1
        sort_instring=sorted(instring.items(),key=lambda x: x[1], reverse=True)
        for letters in sort_instring:
            print(letters[0],'=',str(letters[1]))
            
            
    most_frequent(0,0,0)
    
else:
    print("Invalid output")
    
    
    
