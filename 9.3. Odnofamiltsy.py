print("Однофамильцы")
amountOfWorkers = int(input())
workers = []
workersCheck = []
for i in range(amountOfWorkers):
    workers.append(input())
    workersCheck.append(int(0))
for i in range(amountOfWorkers):
    for k in range(amountOfWorkers):
        if workers[i] == workers[k] and i != k:
            workersCheck[k] += 1
answer=0
for i in range(amountOfWorkers):
    if workersCheck[i] != 0:
        answer += 1
print(answer)