# calculate-prime-numbers
## A Python 3 script to calculate prime numbers up to one trillion

**Synopsis**

This script is another python script to calculate prime numbers. I created this script because 
I woke up in the late night thinking about **prime numbers**. There are better things to think 
of in the middle of the night. But I was obsessed about how would I find a list of 
**prime numbers**, and I came up with this algorithm as an idea in my head. I decided to write 
this in **Python** because I wanted to.

My thought on this started with thinking about testing a number by seeing if it is divisible by 
any number. The standard way is to try dividing the number by every number that is smaller than 
the number. Then, you have to figure that you can skip testing even numbers, because any number
larger than two is automatically divisible by two.

So, I got to thinking that if I started keeping track of all prime numbers, then I only need to 
divide the number by a prime number. I do not need to test against every number, or every odd 
number, just every prime number. Then I figured that when the testing numbers were higher than
the square root of the number being tested, then that would be the limit of required testing.

So, I wrote this script. I am still learning Python. I have tweaked this a few times. I am 
running this script on a small under-powered SOC computer, a *Raspberry Pi Model B Rev 2*. 
I am running it on this device so that I can prove that it can run with limited resources. 

In Linux, set the execute attribute on this file, then you should be able to run it from the 
command line. In Windows, have fun.

`$ chmod +x calculate_prime_numbers.py
$ ./calculate_prime_numbers.py`

If you want to run this program in the background and let it chew away, especially on a system 
that is up mostly 24/7 *(such as a headless Raspberry Pi SBC)*, then you can launch it in 
Linux with this command .

`$ nohup nice ./calculate_prime_numbers.py &`

If you are running the script in the background and you want to see the progress that is being made,
list out the last few lines from the output file with this command.

`$ tail prime_numbers_list_file.txt`

If you want to clear the data created and rerun the script from scratch, you can clear up the datafile 
first before running the script.

`$ rm prime_numbers_list_file.txt`
