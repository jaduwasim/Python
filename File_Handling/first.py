f = open('abc.txt','r')
print('file Name:',f.name)
print('file Mode:',f.mode)
print('is file readable:',f.readable())
print('is file writable',f.writable())
print('is file is closed',f.closed)
f.close()
print('is file closed',f.closed)