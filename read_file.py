fhand = open('romeo-full.txt')
count = 0
count_r = 0
count_j = 0

for line in fhand:
    count = count + 1
    if line.startswith('ROMEO'):
        count_r = count_r + 1

    if line.startswith('JULIET'):
        count_j = count_j + 1


print('Line Count:', count)
print('ROMEO Count:', count_r)
print('JULIET Count:', count_j)

fout = open('output.txt', 'w')
fout.write(f'Line Count: {count}\n')
fout.write(f'ROMEO Count: {count_r}\n')
fout.write(f'JULIET Count: {count_j}')
fout.close()