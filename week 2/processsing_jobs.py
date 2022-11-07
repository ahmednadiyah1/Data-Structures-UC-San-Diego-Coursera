from queue import Queue
def assign_jobs(jobs, threads, n_jobs):
    p=Queue()
    ans=[(-1,0)]*n_jobs

    for i in range(n_jobs):
        if i<threads:
            p.put((i, jobs[i]))
            ans[i]=(i,0)

        else:
            task=p.get()
            thread_name=int(task[0])
            time=int(task[1])
            ans[i]=(thread_name, time)
            p.put((thread_name, time+jobs[i]))
    return ans


threads, n_jobs=map(int, input().split())
jobs=list(map(int, input().split()))
result=assign_jobs(jobs, threads, n_jobs)
for i in result:
    print(i[0],i[1])