# create_prime_numbers_mpy.py
# Wilson Portugal
# July 6, 2022
# micropython 1.82

import io
import machine
import os
import time

FILENAME = 'prime_number_list.txt'
FIRST_PRIME = int(2)
MAX_VALUE = int(1000)

def current_time():
    ltime = time.localtime()
    year = str(ltime[0])
    month = ("00"+str(ltime[1]))[-2:]
    day = ("00"+str(ltime[2]))[-2:]
    hour = ("00"+str(ltime[3]))[-2:]
    minute = ("00"+str(ltime[4]))[-2:]
    second = ("00"+str(ltime[5]))[-2:]
    tz = int(hour) - int(time.gmtime()[3])
    if tz >= 0:
        tzs = "+"+("00"+str(tz))[-2:]
    else:
        tzs = ("00"+str(tz))[-2:]
    rv = year+"-"+month+"-"+day+" "+hour+":"+minute+":"+second+" "+tzs
    return rv

def init_prime_number():
    files = os.listdir()
    if FILENAME in files:
        os.remove(FILENAME)
    dt = current_time()
    file = io.open(FILENAME, "wt")
    file.write(str(FIRST_PRIME)+","+dt+"\n")
    file.close()

def check_for_prime(num_value):
    prime_flag = True

    if num_value != int(num_value):
        return
    
    if num_value < 2:
        return
    
    file = io.open(FILENAME, "rt")
    while True:
        prime_number = file.readline().strip().split(",")[0]
        if not prime_number:
            break

        mod_value = int(num_value) % int(prime_number)
        if mod_value == 0:
            prime_flag = False
            break

        divided_value = float(int(num_value) / int(prime_number))
        if float(divided_value) < float(prime_number):
            prime_flag = True
            break

    file.close()

    if prime_flag == True:
        dt = current_time()
        file = io.open(FILENAME, "at")
        file.write(str(num_value)+","+dt+"\n")
        file.close()

led = machine.Pin(25, machine.Pin.OUT)
led.value(1)

init_prime_number()
prime_counter = FIRST_PRIME

while int(prime_counter) <= int(MAX_VALUE):
    # print(prime_counter)
    check_for_prime(int(prime_counter))
    prime_counter = int(prime_counter) + 1

led.value(0)
