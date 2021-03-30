##Solution

This question is very similar to the previous question,"please help!!" This question requires you to solve the previous question as it uses the same methodology i.r. hamming codes. 
The question contains binary grouped in 16bit. To decrypt the flag, we have to find a hamming code with 16bits. Also it was not enough to know the parity bits but also how they checked
the data bits. For this question i used a variation of the (15,11) hamming code. 

 Put the 16bit data into a 4 x 4 table. Lets use 0011101100101011. Start from the top left and go to the right and fill the table as shown.

|0 |0 |1 |1| <br>
|1 |0 |1 |1| <br>
|0 |0 |1 |0| <br>
|1 |0 |1 |1| <br>


|0  |1  |2  |3 | <br>
|4  |5  |6  |7 | <br>
|8  |9  |10 |11| <br>
|12 |13 |14 |15| <br>

Now the bits at postion 0,1,2,4,8  are the parity bits and the rest 11 bit are data. 

Now parity at postion 1 checks bits at 1,5,9,13,3,7,11,15 or the 2nd and 4th column. Since it has odd numbers or 1's we can say tbat the error is in one of there bits (5,9,13,3,7,11,15)

Now parity at postion 2 will check the bits at 2,6,10,14,3,7,11,15 or the 3rd and 4th column. Since it has odd numbers or 1's we can say tbat the error is in one of there bits (5,9,13,3,7,11,15,6,10,14)

Now parity at postion 4 will check the bits at 4,5,6,7,12,13,14,15 or the 2nd and 4th row. Since it has even number of ones, the bits in those rows do not contaion error. Therefore the bits that can contain error are -> 9,3,11,6,10

Now parity at position 8 will check the bits at 8,9,10,11,12,13,14,15 or the 3rd and 4th row. Since it has even number of ones, the bits in those rows do not contaion error. Therefore the bits that can contain error are -> 3

The parity at position 0 cross checks the whole block and the block contains even number of 1's and therefore it is not faulty and we have succefully found the error. Now we change the bit at position 3 and the table becomes

|0 |0 |1 |0| <br>
|1 |0 |1 |1| <br>
|0 |0 |1 |0| <br>
|1 |0 |1 |1| <br>

After removing the parity bits, the 11 bits of correct data are -> 0011010011. Doing the same for the rest of the note given and then converting it from binary to text gives the flag for the question. 

 11 bits of data      <- removed parity cheker <- changed 1 bit 
		
1.  00110101011 <-  0010101100101011   <- 0011101100101011 <br>
2.  01001011011 <-  0010010011011011   <- 0010010010011011 <br>
3.  01011010010 <-  0010110111010010   <- 0010100111010010 <br>
4.  11011000011 <-  0101010111000011   <- 0101010110000011 <br>
5.  01000111001 <-  0010010010111101   <- 0010011010111101 <br>
6.  00101111101 <-  1000001001111101   <- 1000001001101101 <br>
7.  11100100110 <-  0101011010100110   <- 0101011010100111 <br>
8.  01100110111 <-  0010111010110111   <- 0010111010110101 <br>
9.  01011111011 <-  1110110101111011   <- 1110110101110011 <br>
10. 00100011010 <-  0110101010011010   <- 0111101010011010 <br>
11. 01011001100 <-  1010010111001100   <- 1010010110001100 <br>
12. 11001100011 <-  1001110001100011   <- 1001110001101011 <br>
13. 00110111001 <-  0110001100111001   <- 0110001100111101 <br>
14. 00011001101 <-  1000000101001101   <- 1000001101001101 <br>
15. 10111000110 <-  0001101111000110   <- 0001101011000110 <br>
16. 11100100001 <-  1101111000100001   <- 1101111000101001 <br>
