##Solution

This question is very similar to the previous question,"please help!!" This question requires you to solve the previous question as it uses the same methodology i.r. hamming codes. 
The question contains binary grouped in 16bit. To decrypt the flag, we have to find a hamming code with 16bits. Also it was not enough to know the parity bits but also how they checked
the data bits. For this question i used a variation of the (15,11) hamming code. 

Step 1 ->  Put the 16bit data into a 4 x 4 table. Lets use 0011101100101011. Start from the top left and go to the right and fill the table as shown.

|--|--|--|--|

|0 |0 |1 |1|
|1 |0 |1 |1|
|0 |0 |1 |0|
|1 |0 |1 |1|
