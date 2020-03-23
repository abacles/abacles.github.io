# ABACLES


template = 'pcprog/index.html'

fin = open(template,'r')
fout = open(input('New HTML: '),'w')

write = True
for line in fin:
    if write:
        fout.write(line)
    if line.strip() == '<!-- EOH -->':
        write = False
    if line.strip() == '<!-- BOF -->':
        write = True
        fout.write('\n\n' + line)

fin.close()
fout.close()
