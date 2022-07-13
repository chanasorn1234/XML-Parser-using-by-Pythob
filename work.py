import re
import os


inp = input(r'')
path = inp

fname = os.listdir(path)
if not os.path.exists(path+'\\output'):
    os.makedirs(path+'\\output')

for f in fname:
    print('processing:',f)
    file_read = open(path+'\\'+f)
    stri = file_read.read()
    file_write = open(path+'\\output\\'+f,'w')
    stri = re.sub('&','&amp;',stri)
    stri = re.sub('&amp;amp;', '&amp;', stri)
    file_write.write(stri)
    file_read.close()
    file_write.close()

print('all done')
input()