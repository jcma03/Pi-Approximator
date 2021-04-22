def gcd(a, b):  #Uses Eulers Algorithm For finding the GCD of 2 numbers
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def newline():
    print("\n")

import math
import cmath
from random import randint
import time

em_constant = 0.57721566490153286060651209008240243104215933593992
golden_ratio = (1 + 5**0.5) / 2
gravity = 9.807

ran = 0
numbers_pulled = 0  # Counters, pretty self explanatory
coprime = 0
cofactor = 0

print("My goal is to get to Pi exactly! Help by using this program!")
time.sleep(3.14)  #Haha
print(
    "This program cacluates Pi and an ever growing list of constants by just using 10 million random numbers and our approximation of pi!"
)
time.sleep(3.14)
print(
    "The maths modules were only used to calcuate accuracy, not for the actual calculation! Upvote Please!"
)
time.sleep(3.14)
print("If number shows up weird, check number in relevant file!")

while numbers_pulled < 10000000:  # Makes sure only 10 million numbers are used
    x = randint(0, 10000000)
    y = randint(0, 10000000)
    result = gcd(x, y)  # Each pair of numbers go through this function
    if result == 1:
        coprime = coprime + 1
        numbers_pulled = numbers_pulled + 1
    else:
        cofactor = cofactor + 1
        numbers_pulled = numbers_pulled + 1

ran = ran + 1

print("cofactor:", cofactor, "coprime:", coprime, "Total:", numbers_pulled)

newline()

print("Now, for the calculation of pi")

variable_x = coprime / 10000000
print(
    coprime, "divided by a million =", variable_x)  # Uses the fact that pi squared = 6 divided by probability that a pair of numbers are coprime
variable_y = 6 / variable_x
print("Result divided into 6 =", variable_y)

pi = math.sqrt(variable_y)
print(pi)
accuracy = math.pi - pi  # Calculates accuracy of pi
print("Within:", accuracy, "of actual Pi!")
print("Using 10 million random numbers!")

newline()

tau = pi * 2
print("Therefore, we can deduce that our approximation of Tau would be:", tau)
accuracy2 = math.tau - tau
print("Correct within:", accuracy2, "of actual Tau!")
print("Using 10 million random numbers!")

newline()

e = (20 + pi)**(1 / pi)
print("Therefore, we can deduce that our approximation of e would be:", e)
accuracy3 = math.e - e
print("Correct within:", accuracy3, "of actual e!")
print("Using 10 million random numbers!")

newline()

root2 = 1 / (math.sin(pi / 4))
print("Therefore, we can deduce that our approximation of sqrt(2) would be:",
      root2)
accuracy4 = math.sqrt(2) - root2
print("Correct within:", accuracy4, "of the actual sqrt(2)!")
print("Using 10 million random numbers!")

newline()

phi = 2 * math.sin((3 * pi) / 10)
print("Therefore, we can deduce that our approximation of phi would be:", phi)
accuracy5 = golden_ratio - phi
print("Correct within:", accuracy5, "of actual phi!")
print("Using 10 million random numbers!")

newline()

EulerMasceroni = pi / (2 * e)
print(
    "Therefore, we can deduce that our approximation of the EulerMasceroni constant would be:",
    EulerMasceroni)
accuracy6 = em_constant - EulerMasceroni
print("Correct within:", accuracy6, "of the actual EulerMasceroni constant!")
print("Using 10 million random numbers!")

newline()

g = 4 * (pi**2) / (4)
print(
    "Therefore, we can deduce that our approximation of the gravity on earth constant would be:",
    g)
accuracy7 = gravity - g
print("Correct within:", accuracy7, "of the actual gravity on earth constant!")
print("Using 10 million random numbers!")

filePi = open("pi.py", "a")
filePi.write(str(pi))
filePi.write("\n")
filePi.close()

fileTau = open("tau.py", "a")
fileTau.write(str(tau))
fileTau.write("\n")
fileTau.close()

fileRan = open("ran.py", "a")
fileRan.write(str(ran))
fileRan.write("\n")
fileRan.close()

fileE = open("e.py", "a")
fileE.write(str(e))
fileE.write("\n")
fileE.close()

fileSqrt2 = open("root2.py", "a")
fileSqrt2.write(str(root2))
fileSqrt2.write("\n")
fileSqrt2.close()

filePhi = open("phi.py", "a")
filePhi.write(str(phi))
filePhi.write("\n")
filePhi.close()

fileEm = open("masceroni.py", "a")
fileEm.write(str(EulerMasceroni))
fileEm.write("\n")
fileEm.close()

fileG = open("g.py", "a")
fileG.write(str(g))
fileG.write("\n")
fileG.close()
