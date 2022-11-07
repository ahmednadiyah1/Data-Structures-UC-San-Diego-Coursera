no_of_tables, operations=map(int, input().split())
rows=list(map(int, input().split()))
pointers=[0]*no_of_tables
result=[]
for i in range(no_of_tables):
    pointers[i]=i
i=1
while(i<=operations):
    first, second=map(int, input().split())
    if pointers[first-1]==pointers[second-1]:
        result.append(max(rows))
    else:
        rows[pointers[first-1]]+=rows[pointers[second-1]]
        result.append(max(rows))
        pointers[second-1]=pointers[first-1]

    i+=1

for i in result:
    print(i)
