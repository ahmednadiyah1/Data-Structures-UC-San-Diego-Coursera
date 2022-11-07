def create_stack():
    stack=[]
    return stack


def empty(stack):
    return len(stack)==0


def push(stack, num):
    stack.append(num)


def pop(stack):
    if empty(stack):
        print("Stack is empty")
    else: stack.pop()
    return stack



def match(b1,b2):
    if b1=='(' and b2==')':
        return True
    elif b1=='[' and b2==']':
        return True
    elif b1=='{' and b2=='}':
        return True
    else: return False

def index_range(stack):
    if empty(stack):
        return 0
    else:
        n=len(stack)-1
        return stack[n]




l1=input()
stack=create_stack()
index=[]
req=0
top1=''
for i, n in enumerate(l1):
    if n in '([{':
        push(stack,n)
        top1=n
        index.append(i)
    if match(top1, n):
        pop(stack)
        index.pop()
        top1 = index_range(stack)


    else:
        if n in ')]}':
            req=i+1
            print(req)
            exit()

if empty(stack):
    print('\nSuccess')
else:
    print(index[len(index)-1]+1)
