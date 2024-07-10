a = 0
while a < 100:
    if a > 10:
        print(a)
        break
    a += 2
print('whileの中にprint')
a = 0
while a < 100:
    if a > 10:
        break
    print(a)
    a += 2
print('ifの中にprint')
a = 0
while a < 100:
    if a > 10:
        print(a)
        break
    a += 2
