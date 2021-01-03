#marks3.py
marks = [90,25,67,45,80]
i = 0
for number in range(len(marks)):
    i = i+1
    if marks[number] < 50: continue
    print("%d님 축하합니다" %i)