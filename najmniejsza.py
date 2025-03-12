nums = []
while(True):
    x = int(input("Podaj liczbę całkowitą: "))
    if x == 0: break
    nums.append(x)

print(f"najmeniejsza liczba z podanych to: {min(nums)}")