# File: Archimedes.py
# By: Thomas Welborn
# Created: 11/22/19
# Last Modified: 12/05/19
# Course: COSC 3312 Numerical Methods
# Instructor: Dr. Cooper
# Due: 12/05/19

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import random
import math



#get_2dRange gets the range for the radius and theta from the user
#@param none
#@return one-dimensional list: twoDRange, a list with exactly 4 values being the radius range for the first two, and theta range for the last two elements
def get_2dRange():
  radius_low = -1
  radius_hi = -2
  theta_low = -1
  theta_hi = -2
  while (radius_low > radius_hi) or (radius_low < 0) or (radius_hi < 0):
    radius_low = int( input("Please enter an integer equal to or greater than 0 for the lowest value of your radius range: "))
    radius_hi = int( input("Please enter an integer equal to or greater than 0 for the highest value of your radius range: "))
  while (theta_low > theta_hi) or (theta_low < 0) or (theta_hi < 0):
    theta_low = int( input("Please enter an integer equal to or greater than 0 for the lowest value of your theta range: "))
    theta_hi = int( input("Please enter an integer equal to or greater than 0 for the highest value of your theta range: "))

  twoDRange = [radius_low, radius_hi, theta_low, theta_hi]
  return twoDRange


#get_3dRange gets the range for the radius, theta, and phi from the user
#@param none
#@return one-dimensional list : threeDRange, a list with 6 elements being radius lower range value, radius upper range value, then the same for theta and phi
def get_3dRange():
  radius_low = -1
  radius_hi = -2
  theta_low = -1
  theta_hi = -2
  phi_low = -1
  phi_hi = -2
  while (radius_low > radius_hi) or (radius_low < 0) or (radius_hi < 0):
    radius_low = int( input("Please enter an integer equal to or greater than 0 for the lowest value of your radius range: "))
    radius_hi = int( input("Please enter an integer equal to or greater than 0 for the highest value of your radius range: "))
  while (theta_low > theta_hi) or (theta_low < 0) or (theta_hi < 0):
    theta_low = int( input("Please enter an integer equal to or greater than 0 for the lowest value of your theta range: "))
    theta_hi = int( input("Please enter an integer equal to or greater than 0 for the highest value of your theta range: "))
  while (phi_low > phi_hi) or (phi_low < 0) or (phi_hi < 0):
    phi_low = int( input("Please enter an integer equal to or greater than 0 for the lowest value of your phi range: "))
    phi_hi = int( input("Please enter an integer equal to or greater than 0 for the highest value of your phi range: "))

  threeDRange = [radius_low, radius_hi, theta_low, theta_hi, phi_low, phi_hi]
  return threeDRange




#this function displays a 2-d model of a evenly distributed circle according to the user inputs
#@param 1-dimensional list : twoDRange, contains the user-provided ranges for the radius and theta
#@return none
def make_2d(twoDRange):
  fig2 = plt.figure()
  for index in range(1000):
    #notice the random numbers generated multiple a random number that is between 0 and 1 by the upper range limit
    #this will actually generate a random number that is between 0 and the upper limit
    #becuase of this we need to take into account the lower range
    #that is why we add the lower range onto the end of it to make sure that only the numbers between low and high are taken
    #this same random number generation thought process was used for the 3-d method as well
    r = (random.random() * twoDRange[1]) + twoDRange[0]
    theta = (random.random() * twoDRange[3]) + twoDRange[2]
    x = math.sqrt(r) * math.cos(theta)
    y = math.sqrt(r)  * math.sin(theta)
    plt.scatter(x, y, color = 'green')
  plt.show()
  return

#this function displays a 3-d model of a evenly distributed sphere according to the user inputs
#@param 1-dimensional list : threeDRange, contains the user-provided ranges for the radius, theta, and phi values
#@return none
def make_3d(threeDRange):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection = '3d')
  for index in range(1000):
    r = (random.random() * threeDRange[1]) + threeDRange[0]
    theta = (random.random() * threeDRange[3]) + threeDRange[2]
    phi = (random.random() * threeDRange[5]) + threeDRange[4]
    x = math.pow(r, 1/3) * math.cos(theta) * math.sin(phi)
    y = math.pow(r, 1/3) * math.sin(theta) * math.sin(phi)
    z = math.pow(r, 1/3) * math.cos(phi)
    ax.scatter(x, y, z, color = 'green')
  plt.show()
  return



#make_default2D displays a 2-d circle based on the original ranges and values givien in class using the default ranges
#@param none
#@return none
def make_default2D():
  fig2 = plt.figure()
  #the next 2 lines were used during testing when I wanted to keep a variable constant
  #r = random.random()
  #theta = random.random() * 2 * math.pi
  for index in range(1000):
    r = random.random()
    theta = random.random() * 2 * math.pi
    #take the square root of the radius for more equally dispersed points because dimension=2
    x = math.sqrt(r) * math.cos(theta)
    y = math.sqrt(r)  * math.sin(theta)
    plt.scatter(x, y, color = 'green')
  plt.show()
  return

#make_default2D displays a 3-d hypersphere based on the original ranges and values givien in class using the default ranges
#@param none
#@return none
def make_default3D():
  fig = plt.figure()
  ax = fig.add_subplot(111, projection = '3d')
  #the next three lines I used to test when I wanted to keep a variable constant
  #r = random.random()
  #theta = random.random() * 2 * math.pi
  #phi = random.random() * math.pi
  for index in range(1000):
    r = random.random()
    theta = random.random() * 2 * math.pi
    phi = random.random() * math.pi
    #take the cubed root of the radius for more equally dispersed points because dimension=3
    x = math.pow(r, 1/3) * math.cos(theta) * math.sin(phi)
    y = math.pow(r, 1/3) * math.sin(theta) * math.sin(phi)
    z = math.pow(r, 1/3) * math.cos(phi)
    ax.scatter(x, y, z, color = 'green')
  plt.show()
  return

  



def main():
  np.random.seed(12345678)
  print("Here are the default 2-d and 3-d circle/sphere graph representations.")
  print("After you are done examining a graph, exit out of the window to continue to the next graph.")
  make_default2D()
  make_default3D()

  print(" ")
  print("Now we will begin the user-controlled part of the program. You may manipulate these graphs by changing the ranges in which the radius, theta, and phi values are pseudo-randomly generated from.")
  #initiates the boolean to true, will keep going as long as user wants
  user_boolean = True
  user_answer = " "

  while (user_boolean):
    print("We will now get your 2-d ranges.")
    print("------------------------------------------------------------------------")
    my2D_range = get_2dRange()
    print("------------------------------------------------------------------------")
    print("------------------------------------------------------------------------")
    print("We will now get your 3-d ranges.")
    print("------------------------------------------------------------------------")
    my3D_range = get_3dRange()
    print("------------------------------------------------------------------------")
    print("------------------------------------------------------------------------")
    print("Here is your 2-d graph.")
    make_2d(my2D_range)
    print("Here is your 3-d graph.")
    make_3d(my3D_range)
    print(" ")
    user_answer = input("Would you like to make another pair of graphs (y/n): ")
    if (user_answer == "y") or (user_answer == "Y"):
      user_boolean = True
    else:
      user_boolean = False

  print("Bye!")
main()
