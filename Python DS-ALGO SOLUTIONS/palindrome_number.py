#this program reverses a number and adds them, if sum is a palindrome it will return the number otherwise, 
#it will repeat the process until a palindrome is found or until the max threshold is reached, in this case 100 runs.

def palind_number(n):
    runs = 0 #number of runs to reach threshold 
    while True:
        string_numb = str(n)
        if string_numb == string_numb[::-1]: #if number is equal to reversed number, it returns number
            return n 
        elif runs>100:
            return "No palindrome found in 100 runs" #checks runs are under 100(max threshold)
        else:
            int_num = int(string_numb[::-1])
            n += int_num #adds to original number
            runs+= 1
    

print(palind_number(1234)) #this will find a palindrome
print(palind_number(13596)) #no palindrome number is found
