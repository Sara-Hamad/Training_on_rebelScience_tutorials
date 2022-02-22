output = []
with open('t.txt', 'r') as f :
    output = [line for pos, line in enumerate(f.readlines()) if pos % 2!=0]
    print(output)
with open('t2.txt','w') as f :
    f.write(''.join(line for line in output))