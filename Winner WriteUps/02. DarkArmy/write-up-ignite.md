## Rotations
Strings --> rot_something(CyberChef)

## Apollo 11
Strings

## Misleading steps
Opening in any disassembler shows flag chars assigned to variables

## Give it to get it
`stoul` parses hex data, so reqd flag is hexdump fo given flag string

## FlowRev
Overflow 68 char array --> get numbers --> CYberchef octal something (used Cyberchef `magic`)

## Inspect the un-Inspected
parts in source code of home page, mini CTF page, faq page

## Facile
binwalk extract --> strings --> grep

## Git Up and Dance
`git log -p` and grep

## Weird Message
```py
from PIL import Image
f = open("wierd.txt")
data = f.read().decode()

img = Image.new( 'RGB', (1226,42), "black")
pixels = img.load()

c = 0

for i in range(41):
	for j in range(1226):
		if(int(str(data[c])) == 0):
			pixels[j,i] = (0,0,0)
		else:
			pixels[j,i] = (255,255,255)
		c += 1
img.show()
```

## Comments
unzip docs, flag is in a comment inside the xml files.

## Suisse
Patch check to get the digits, then -3 from all of them and decode ascii