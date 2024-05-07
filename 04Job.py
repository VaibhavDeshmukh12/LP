def printJobScheduling(arr, t):    
    arr.sort(key=lambda x: x[2], reverse=True)
    result = [False] * t
    job = ['-1'] * t
    total_profit = 0

    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                total_profit += arr[i][2]
                break
    print("Sequence of jobs:", job)
    print("Maximum profit:", total_profit)

n = int(input("Enter the number of jobs: "))
arr = []

print("Enter job details in the format 'job_id deadline profit':")
for _ in range(n):
    job_id, deadline, profit = input().split()
    arr.append((job_id, int(deadline), int(profit)))

print("Following is the maximum profit sequence of jobs:")
printJobScheduling(arr, max(job[1] for job in arr))
