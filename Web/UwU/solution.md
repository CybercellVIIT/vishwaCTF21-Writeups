The description states when php, anime and robot come together..., and we get the hint!
We try to look for the robots.txt file and we get the text:
‘this time.. there might be a directory called as robots lol’
So we go to the /robot directory, where there’s a php file and we can see its source.
This seems to work on preg function, which is a pretty well-known php vulnerability 
We look for the get parameter which is php_is_hard, and compare it to suzuki_harumiya after replacing the occurrence suzuki_harumiya in its value with nothing i.e. blank. To bypass this simple check, we enter the get parameter suzuki_suzuki_harumiyaharumiya. By doing this, the preg_replace function will replace the occurrence which is found in the middle of the string, leaving it as suzuki_harumiya
.
Thus we get the flag, which is vishwaCTF{well_this_was_a_journey}.
