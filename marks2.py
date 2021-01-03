#marks2.py 60점 이상인 사람에게는 축하메시 , 나머지 아무메시지도 전하지x
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number+1
    if mark < 60: continue
    print("%d번 학생, 축하합니다" %number)
    
