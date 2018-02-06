#Decode Matrix!!
#Input the rows and columns of the matrix to be decoded
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
#Convert the matrix to a list
for matrix_i in range(n):
    matrix_t = str(input())
    matrix.append(matrix_t)
#Decode the matrix
decode = []
for i in range(m):
    for j in range(n):
        decode.append(matrix[j][i])
    j = 0
stri = ''
newstri = ''
#convert the decoded matrix to string
stri = ''.join(map(str, decode))
newstri = stri
#make the string more readable
a = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91))) + list(range(0, 10))
for i in range(len(stri)):
    if stri[i] not in a:
        stri = stri.replace(stri[i], " ")
stri = ' '.join(stri.split())
revs = ''
for i in range(len(newstri)-1, -1, -1):
    if newstri[i] in a:
        break
    revs = revs + newstri[i]
rrev = ''
for i in range(len(revs)-1, -1, -1):
    rrev = rrev + revs[i]
print(stri.rstrip() + rrev)
