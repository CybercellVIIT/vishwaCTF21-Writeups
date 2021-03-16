## Another Excellent Secure encryption

Author : <a href="https://github.com/Rshrimali17/">Rishi Shrimali</a>

Title : Another Excellent Secure encryption

Category : Cryptography

Scoring : Dynamic

Points : 500

Description : Richa and Parth have made a new Encryption System which is really Advanced and secure. They used their name in some way to create some sort of key and also a combination of their phone numbers in some way to create the nonce.
<br>note- > sha256 AES is used and convert both nonce and key to hex while decrypting 

Flags : vishaCTF{n07_7ha7_4dv4nc3D}

Files : encrypted_text.txt, IV.txt

Hints : None

Solves : 0


## SOLUTION

AES encrypted text file and the key is the xor of the binary of their names. (Richa and Parth)
The question suggests that we have used the names is some way to create a key. First we convert the names in binary and then perform xor operation on it.

Richa -> 01010010 01101001 01100011 01101000 01100001
Parth -> 01010000 01100001 01110010 01110100 01101000

Richa xor Parth -> 1000001000000100010001110000001001

The questions says that they have used hex so we convert the xor to hex. 
We used this website to convert -> https://gchq.github.io/CyberChef/

hex of the xor -> 31 30 30 30 30 30 31 30 30 30 30 30 30 31 30 30 30 31 30 30 30 31 31 31 30 30 30 30 30 30 31 30 30 31

The hex in 34 bytes so we convert it to 32 bytes for AES-256 decryption.

1IV -> 8497450324983725978249873143962

Input these two values and decrypth the encrypted text and volla the flag pops out.

flag -> vishaCTF{n07_7ha7_4dv4nc3D}

encrpyted text ->  d2344068b78b4db2c0ee11bb9681b7bc8100e0495f5830492b54e9744ed8bc40