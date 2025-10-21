# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    hours = n // 3600 % 24
    minutes = n // 60 % 60
    seconds = n % 60
    print(hours, ":", str(minutes).zfill(2), ":", str(seconds).zfill(2), sep="")

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
