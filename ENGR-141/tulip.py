import math
err = 0
num = 0
words = 0
with open('Series1.txt', 'r') as error:
    lines = error.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line2 = line.strip().split()
        inp = line2[0]
        out = line2[1]
        print(inp)
        print(out)
        if inp == out:
            words += 1
            num += len(inp)
            print('its fine')
        else:
            for v in range(len(inp)):
                if inp[v] != out[v]:
                    err += 1
                num += 1
                print(v)

print(err / num)
print(words)