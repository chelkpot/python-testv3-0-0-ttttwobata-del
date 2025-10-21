# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    hours = (n // 60) % 24
    minutes = n % 60
    print(hours, minutes)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
