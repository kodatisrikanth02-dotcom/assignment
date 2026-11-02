import random
code1=random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)
code2=random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
print(f"The 3-digit code :", *code1)
print(f"The 4-digit code :", *code2)