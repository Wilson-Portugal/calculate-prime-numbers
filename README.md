# calculate-prime-numbers
## A Python 3 script to calculate prime numbers up to one trillion

**Synopsis**

This script is a python script that I wrote and I run on a small under-powered SOC computer, a 
*Raspberry Pi Model B Rev 2*. I am running it on this device so that I can prove that it can run 
with limited resources. The script writes to a file a list of prime numbers and it uses that file 
to find more prime numbers. As I am writing this README.md file, I am already seeing fixes that I 
can implement into this script for efficiency. I have not had this script run to the level of one 
trillion yet.

If you set the execute attribute on this file, then you should be able to run it from the command line.

`$ chmod +x calculate_prime_numbers.py
$ ./calculate_prime_numbers.py`

If you want to run this program in the background and let it chew away, especially on a system that is 
up mostly 24/7 *(such as a headless Raspberry Pi SBC)*, then you can launch it with this command.

`$ nohup nice ./calculate_prime_numbers.py &`

If you are running the script in the background and you want to see the progress that is being made,
list out the last few lines from the output file with this command.

`$ tail prime_numbers_list_file.txt`

If you want to clear the data created and rerun the script from scratch, you can clear up the datafile 
first before running the script.

`$ rm prime_numbers_list_file.txt`

I have heavily documented the script file to the point that there is more comments than code.

## Further thoughts

I created this script because I woke up in the late night thinking about **prime numbers**. There are
better things to think of in the middle of the night. But I was obsessed about how would I find a list
of **prime numbers**, and I came up with this algorithm as an idea in my head. I decided to write this
in **Python** because I wanted to. I started creating this without writing anything down on paper. I 
tweaked it a couple of times.

So, I have a few **Raspberry Pi** devices, and my very first one was a *Raspberry Pi Model B Rev 2*. 
I have kept up with a headless installation. I run the operating system on a 128GB USB stick. I have 
been running this thing pretty much non-stop for ten years now. I have been running this script for 
less than 24 hours, and as of this moment, the largest prime number it has found is 209249. This script
on this device is not going to set any world records. I have made a few modifications for integrity and 
efficiency, but this is not the code that will find the largest prime number ever.

