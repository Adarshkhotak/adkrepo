#Right Side

def rotateArray(arr: list, k: int) -> list:

        def reverse(s,e):
            while s<e:
                arr[s],arr[e]=arr[e],arr[s]
                s+=1
                e-=1
            
        
        n=len(arr)
        k=k%n
        reverse(0,n-1)#first reverse the entire array
        reverse(0,k-1) #reverse first K elements we got after reverse
        reverse(k,n-1) #reverse the remaining 

        return arr
        

print(rotateArray([1,2,3,4,5,6,7],3))



