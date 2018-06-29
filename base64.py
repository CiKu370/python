#!usr/bin/python

# encoding base64 step by step
# copyright @CiKu370

kata = raw_input('masukan kata : ')

if len(kata)%3 == 2:
	padding = '='
elif len(kata)%3 == 1:
	padding = '=='
else:
	padding = ''

a = 'Encoding Base64 untuk kata "' + kata + '"'
print '-'*len(a)
print a


print '\nAmbil nilai binari dari Ascii setiap karakter'

b = ''
for i in kata:
	print '%s, binari: %s, ascii: %s'%(i, bin(ord(i))[2:].zfill(8),ord(i))
	b += str(bin(ord(i))[2:].zfill(8)+ ' ')

print '\nDeretan Binari dari "%s" adalah "%s"'%(kata,b[:-1])
print '\nDeretan Binari (dijadikan 1 baris panjang) dari "%s" adalah "%s"'%(kata,(b).replace(' ',''))

print '\nProses per 6 bit, setiap 6 bit akan mewakili 1 karakter base64'
x = (b).replace(' ','')
print x

k = '-'.join(x[i:i+6] for i in range(0, len(x), 6))
print '\n' + k

if padding != '':
	print '\nPanjang kata bukan kelipatan 3, akan ada padding "%s" sepanjang %s karakter'%(padding,len(padding))
	n = ', dengan padding'
else:
	n = ''

print '\n Binari  = desimal = karakter base64'
hsl = ''

w = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:'a',27:'b',28:'c',29:'d',30:'e',31:'f',32:'g',33:'h',34:'i',35:'j',36:'k',37:'l',38:'m',39:'n',40:'o',41:'p',42:'q',43:'r',44:'s',45:'t',46:'u',47:'v',48:'w',49:'x',50:'y',51:'z',52:'0',53:'1',54:'2',55:'3',56:'4',57:'5',58:'6',59:'7',60:'8',61:'9',62:'+',63:'/'}

for c in k.split('-'):
	if len(c) == 6:
		z = '00' + c
	elif len(c) == 4:
		z = '00' + c + '00'
	elif len(c) == 2:
		z = '00' + c + '0000'

	m = int(z,2)
	if len(str(m)) == 1:
		m = str(m) + ' '

	j = ''.join(w[o] for o in w if int(m) == o)

	print '%s = %s      = %s'%(z , m , j)
	hsl += j

print '\nHasil encoding base64%s : %s'%(n,hsl+padding)
