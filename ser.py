# https://sio2.mimuw.edu.pl/c/oij14-1/p/ser/

def draw_sercas(amount):
    heart = """
     @@@   @@@
    @   @ @   @
    @    @    @
    @         @
     @       @
      @     @
       @   @
        @ @
         @
         
    """
    print(heart * amount)

import datetime

H = int(input("Ile serc?: "))


begin = datetime.datetime.now()
draw_sercas(H)

print(begin)
print(datetime.datetime.now())
