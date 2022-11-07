
counter=0
result=[]


def heapify(arr, i, size):
    global counter
    min=i

    leftChild=2*i+1
    rightChild=2*i+2

    if leftChild<size and arr[leftChild]<arr[min]:
        min=leftChild
    if rightChild<size and arr[rightChild]<arr[min]:
        min=rightChild


    if min!=i:
        arr[i], arr[min]= arr[min], arr[i]
        result.append((i, min))
        counter+=1
        heapify(arr,min, size)

def MinHeap(arr, n):
    i=n//2
    for i in range(i, -1, -1):
        heapify(arr, i, n)

n=int(input())
arr=list(map(int, input().split()))
MinHeap(arr, n)
print(counter)
for i, j in result:
    print(i, j)
