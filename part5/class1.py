# result = 0

# def add(num):
#     global result
#     result += num
#     return result

# print(add(3))
# print(add(4))

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal1.add(3))
print(cal1.add(7))
