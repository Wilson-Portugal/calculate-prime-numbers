#!/usr/bin/python3

# Wilson Portugal
# June 27, 2022
# modified July 2, 2022

import codecs
import os.path

precision_value = int(12)

prime_counter = int(0)
max_value = int(10 ** 12)
# maximum value of ten to the power of twelve is a one with 
# twelve zeroes, 1,000,000,000,000 (one trillion)
# use Decimal precision for large number (is this necessary?)
# Decimal precision in not only unneccesary but it is a huge
# contraint on resources and has been removed, July 2, 2000

prime_list_file = "prime_numbers_list_file.txt"

def read_prime_counter():
    """get next number after highest prime number"""
    # read the next prime counter from the prime numbers list 
    # file... the number will be the last number previously 
    # written to the file... I want to return that number 
    # plus one
    file = codecs.open(prime_list_file, "r", "utf-8")
    return_value = int(file.readlines()[-1].strip()) + 1
    file.close()
    return return_value

def init_prime_list_file():
    """initialize prime number file list file if not existing"""
    # check for the prime number list file and create it if it does not exist
    if os.path.exists(prime_list_file) == False:
        print("Prime List file does not exist, creating file")
        file = codecs.open(prime_list_file, "w", "utf-8")
        file.write(str(2)+"\n")
        file.close()

def check_for_prime(number_value):
    """check if a number is a prime number"""
    # the first thing i want to think about doing here is to open up my list of
    # known prime numbers, and try to divide my number value against each prime
    # number in the list... if my number value is a prime number, then it will
    # not divide evenly with any of the existing prime numbers... if it does
    # divide evenly by any prime number, then the number value is not a prime
    # number... to check if a number divides evenly, I use the modulus operator,
    # and if the return value is zero, the the number divides equally... for
    # more understanding of that statement, look up the modulus operator in
    # mathematics... another tweak i make to the code is that it does not have
    # to check all prime numbers, only prime numbers up to its square root...
    # to check this, if the number value divided by the prime number is less
    # than the prime number, then the checking of prime numbers has gone
    # beyond the square root and is no longer required to verify if the
    # number value is a prime number, the rest of the checking would be
    # not required, and the number value would be determinded as a prime
    # number... this saves a lot of steps of calculations...

    # create a flag variable and initialize to true, this will be set to
    # false if the number value is ever evenly divided by another prime
    # number
    prime_flag = True

    # do not check any numbers that are not integers
    if number_value != int(number_value):
        return

    # do not check any numbers less than two
    if number_value < 2:
        return

    # open prime list file for reading
    file = codecs.open(prime_list_file, "r", "utf-8")
    while True:
        # get the next prime number from the file
        prime_number = file.readline().strip()

        # check to see if file reader is at end of file
        if not prime_number:
            break;

        # find the remainder of dividing the number value by the
        # current prime number
        mod_value = int(number_value) % int(prime_number)
        if mod_value == 0:
            # if the number value is evenly divided by a prime number
            # then the number value is not a prime number... set the
            # flag to false and stop checking the number value, job
            # done
            prime_flag = False
            break;

        # check if the square root of the number value is greater than
        # the prime number being checked
        divided_value = float(int(number_value) / int(prime_number))
        if float(divided_value) < float(prime_number):
            # if the square root of the number value is greater than
            # the prime number being checked, then the number value
            # would be a prime number... set the flag an look no
            # further
            prime_flag = True
            break;

    # after all prime numbers that need to be checked have been checked,
    # close the prime number list file
    file.close()

    # if the prime number flag is set, then add the number value to the
    # prime number list file
    if prime_flag == True:
        file = codecs.open(prime_list_file, "a", "utf-8")
        file.write(str(number_value)+"\n")
        file.close
        print(str(number_value))

init_prime_list_file()
prime_counter = read_prime_counter()

while int(prime_counter) <= int(max_value):
    check_for_prime(prime_counter)
    # I am going to increment the prime counter variable by a step 
    # value of one instead of two... i know the practice is to 
    # increment it by a step value of two because no even values 
    # above two will be prime numbers... however, I am afraid 
    # that if the number starts off on an even number for any 
    # reason, then incrementing with a step value of two will 
    # kill the joy
    prime_counter = int(prime_counter) + 1
