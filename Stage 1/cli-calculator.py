# operations = input("enter the calculator operation")
# for char in s:
#     if char.isdigit():
#         num+=char
#     else:
#         if num:
#             tokens.append(int(num))
#             num=""
#         tokens.append(char)
# if(num):
#     tokens.append(int(num))
# print(tokens)

def tokenizer(s):
    tokens=[]
    num=""
    for char in s:
        if char.isdigit():
            num+=char
        elif char in {"+","-","*","/"}:
            if num:
                tokens.append(int(num))
                num=""
            tokens.append(char)
        elif char.isspace():
            continue
        else:
            raise ValueError(f"Invalid operator:{char}")
    if(num):
        tokens.append(int(num))
    return tokens
def parser(arr):
    if not arr:
        raise ValueError("expression cannot be empty")
    if len(arr)==1 and isinstance(arr[0],int):
        raise ValueError("Please provide the full expression")
    if arr[0] in ("*","/","+","-"):
        raise ValueError("expression cannot start with an operator")
    if(arr[-1] in ("*","/","+","-")):
        raise ValueError("Expression cannot end with a operator")
    for i in range(1, len(arr)):
        if arr[i] in ("*", "/", "+", "-") and arr[i - 1] in ("*", "/", "+", "-"):
            raise ValueError("Two operators cannot appear together")
    i=0
    while i<len(arr):
        if(arr[i]=="*"):
            result=int(arr[i-1])*int(arr[i+1])
            arr[i-1:i+2]=[result]
            i=0
        elif(arr[i]=="/"):
            result=int(arr[i-1])/int(arr[i+1])
            arr[i-1:i+2]=[result]
            i=0
        else:
            i+=1
    i=0        
    while i<len(arr):
                if(arr[i]=="+"):
                    result=int(arr[i-1])+int(arr[i+1])
                    arr[i-1:i+2]=[result]
                    i=0
                elif(arr[i]=="-"):
                    result=int(arr[i-1])-int(arr[i+1])
                    arr[i-1:i+2]=[result]
                    i=0
                else:
                    i+=1

    return arr[0]
def calculation():
    try:
        str = input("please enter the calculation you want to make")
        tokens=tokenizer(str)
        result = parser(tokens)
        print(result)
    except ValueError as e:
        print("Error",e)
    except ZeroDivisionError:
        print("cannot divide by zero")
calculation()
#one liner code 
print(eval(input("enter calculation")))