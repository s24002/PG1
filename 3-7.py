f = open('sample.txt', 'r')
data = f.readline()
print(data)
f.close()

with open('sample.txt', 'r') as f:
    data = f.readline()
    print(data)

with open('sample.txt','w') as f:
    f.write('test')

with open('sample.txt','w') as f:
    f.write('test\n')

with open('sample.txt','r') as f:
    data = f.readline()
    line = data.strip()

with open('sample.txt','r') as f:
    for line in f:
        print(line.strip())

with open('sample.txt') as f:
    lines = f.readlines()
    print(lines)

with open('sample.txt','r') as f:
    lines = list(f)
    print(lines)
