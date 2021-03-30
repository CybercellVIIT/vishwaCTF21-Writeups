##Solution

As the description suggests, this question had stated distortion created due to noise. This was meant to lead the player in the direction of bit correction. One of the popular single 
bit correction methods is the use of parity bits as shown in the hamming code methodology. If you observe the binary digits, they are in groups of 12 which commonly means
8 data bits and 4 parity bits. The parity bits check the number of even or odd number of ones in specific location of the 8 bit data. 

So to add parity bits we use the following method. 
Take for example -> 00110111 

We add parity bit at 2^(x) till it is < the number of bits there the parity bits are added at 1st,2nd,4th and 8th position. 

We mark the places in the data as _ _ 0 _ 0 1 1 _ 0 1 1 1

Now the 1st postion checks the bits -> 1,3,5,7,9,11. 
As shown above 3,5,7,9,11 have a total of 2 1's i.e. even number of ones there the first parity is 0 and the data becomes 0_ 0 _ 0 1 1 _ 0 1 1 1

Now the 2nd postion check the bits -> 2,3,6,7,10,11.
As shown above 3,6,7,10,11 has a total of 4 1's i.e. even number of ones there the second parity is also 0 and the data becomes 0 0 0 _ 0 1 1 _ 0 1 1 1

Now the 4th postion checks the bits -> 4,5,6,7,12.
As shown above 5,6,7,12 has 3 1's i.e. odd number of ones there the 4th bit has to be a 1 to make total number of 1's even and the data becomes 0 0 0 10 1 1 _ 0 1 1 1

For the finaly parity bit at position 8, we check the bits ->  8,9,10,11,12:
As shown above 5,6,7,12 has 3 1's i.e. odd number of ones there the 8th bit has to be a 1 to make total number of 1's even and the data becomes 0 0 0 10 1 1 1 0 1 1 1

Now we have 12 bits of data containing 4 parity bits and 8 data bits. If any of the data bits are changed, we can simply use the parity bits and check them one by one to pinpoint the 
exact location of where the bit was manipulated. This is the basic concept used to make the question. IF you followiing this process in reverse by checking the parity bits and then 
correcting the single bit error and removing the parity bits. The binary message would output the flag for this question.


Data                   corrected msg             Msg with incorrect bit                  

00110111     <-   000101100111  <- 001101100111 <br> 
01101000     <-   010011011000  <- 010010011000  <br>
01101001     <-   010111001001  <- 010111001011 <br>
00110101     <-   110101100101  <- 110101000101<br>
01011111     <-   000110101111  <- 000110101111<br>
01110110     <-   100111100110  <- 100110100110<br>
01110110     <-   100111100110  <- 100111100111<br>
01100001     <-   110111010001  <- 111111010001<br>
00110101     <-   110101100101  <- 110101100100<br>
01011111     <-   010110101111  <- 010110101101<br>
01100110     <-   010011000110  <- 010011000100<br>
01010101     <-   000110100101  <- 001110100101<br>
01101110     <-   110011011110  <- 110011011111 <br>
