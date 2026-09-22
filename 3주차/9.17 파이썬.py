##### 1. get_area()
def get_area(radius):
    area = 3.14 * radius ** 2
    return area
print("반지름이 5인 원의 넓이: ", get_area(5))


##### 2. 중첩 별찍기
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print("")
    
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

##### 3. 가변인수 합계
def add(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
print(add(10, 20))
print(add(10, 20, 30))


##### 4. 행, 열, 문자
def print_pattern(rows, cols, char):
    for i in range(rows):
        for j in range(cols):
            print(char, end="")
        print()
print_pattern(3, 5, "@")
