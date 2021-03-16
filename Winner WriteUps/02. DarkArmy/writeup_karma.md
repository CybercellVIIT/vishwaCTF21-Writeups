# Uwu
robots.txt -> robots directory -> https://uwu.vishwactf.com/robots/?showThem -> https://uwu.vishwactf.com/robots/?php_is_hard=suzuki_hsuzuki_harumiyaarumiya

# bot not not bot
```
import request
for i in range(1,501):
	x = requests.get("https://bot-not-not-bot.vishwactf.com/page"+str(i)+".html",verify=False)
	if "Useless" not in x.text:
		print(x.text)

Manually arrange the flag char with its index
```
> 

# Is Js Necessary?
Disable js -> input 10 -> source code
PS: https://thenewstack.io/brendan-eich-on-creating-javascript-in-10-days-and-what-hed-do-differently-today/#:~:text=%E2%80%9CBack%20then%2C%20the%20pace%20of,the%20language%20that%20would%20become

# find the room
https://www.google.com/maps/@18.4596665,73.8839656,3a,45.7y,33.69h,98.34t/data=!3m8!1e1!3m6!1sAF1QipOlrCtXB5DCwoxPjA6tr5RLYa7vGMggM69z_yvT!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOlrCtXB5DCwoxPjA6tr5RLYa7vGMggM69z_yvT%3Dw203-h100-k-no-pi0-ya293.77466-ro-0-fo100!7i13312!8i6656

> A 003

# Front Page
https://www.reddit.com/user/vishwaCTF/comments/lt1gzm/could_this_be_the_flag_for_a_vishwactf_2021/
on way back url
https://web.archive.org/web/20210226163747if_/https://www.reddit.com/user/vishwaCTF/comments/lt1gzm/could_this_be_the_flag_for_a_vishwactf_2021/
vigenere decoder with key (vishwactf) -> flag


# time is an illusion
```
import requests
import string
t=[]
for i in string.printable:
  x = requests.get("https://time-is-an-illusion.vishwactf.com/handle.php?key=str(i)+"_____")
  t.append(x.elapsed.total_seconds())
  print(x.elapsed.total_seconds(),i)
print(max(t))

Manully run the script for each charater in final we get the kye as `KuKa9`
```

# can u see
```
a = """1 0 1 0 1 0 1 0 1 1 0 1 1 1 1 1 0 0 1 1 0 1 0 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 0 0 1 1 0 0 0 1 0 1 0
1 0 1 0 1 1 0 1 0 1 0 1 0 0 0 0 0 1 0 1 1 0 0 1 0 0 0 1 0 1 0 0 1 0 0 1 1 1 0 1 0 1 0 1 0 1 0 1 0 1
1 1 1 1 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 0 1 0 1 1 0 0 1 1 1 1 0 0 1 0 1 1 0 0 1 0 1 1 0 0 0 1 0 0 0 0"""
t= []
for i in a.split("\n"):
	t.append(i.split(" "))
res = []
for i in range(len(t[0])):
	for j in range(len(t)):
		res.append(t[j][i])

c  = ''.join(res)

res = [c[i:i+6] for i in range(0, len(c), 6)]
print(' '.join(res))

# 111001 111001 110010 101010  101110 001111 100100 100100 000011 100110 011100  001111 100100 101111 001111 100100 011100  001111 110110 101010  001111 100010 000011 100010 100010
```
Manually match to bits to dots for the flag on https://www.dcode.fr/braille-alphabet

# My Awesome Youtube recommendation
Normal ssti {{config}} -> flag