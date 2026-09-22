# 1. get_area()
def get_area(radius):
    area = 3.14 * radius ** 2
    return area

print("--- 1. get_area() ---")
print("반지름이 5인 원의 넓이:", get_area(5))


# 2. 중첩 별찍기
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print("")
    
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

# 3. 가변인수 합계
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("\n--- 3. 가변인수 합계 ---")
print("1, 2, 3의 합:", sum_all(1, 2, 3))
print("10, 20, 30, 40의 합:", sum_all(10, 20, 30, 40))


# 4. 행, 열, 문자
def print_pattern(rows, cols, char):
    for i in range(rows):
        for j in range(cols):
            print(char, end="")
        print()

print("\n--- 4. 행, 열, 문자 패턴 출력 ---")
print_pattern(3, 5, "@")
