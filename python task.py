char=256
def max_dis_char(string,n): 
    count=[0]*char 
    for i in range(n): 
        count[ord(string[i])]+=1
    max_distinct=0
    for i in range(char): 
        if count[i]!=0: 
            max_distinct+=1    
    return max_distinct 
def substr_maxchar(string): 
    n=len(string)
    max_distinct=max_dis_char(string,n) 
    minl=n     
    for i in range(n): 
        for j in range(n): 
            sub_str=string[i:j] 
            sub_length=len(sub_str) 
            sub_distinct_char=max_dis_char(sub_str,sub_length) 
            if (sub_length<minl and max_distinct==sub_distinct_char): 
                minl=sub_length 
    return minl
print("enter a string:")
string=input()
l=substr_maxchar(string); 
print(l)
  
