# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
#triangle_sides(), weird_calculation(), hyptenuse_calculation()

# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################
import math
def triangle_sides(triangle_num):
    while True:
        try:
            opp1 = float(input("Enter your triangle's opposite side length: "))
            if opp1 > 0:
                adj1 = float(input("Enter your triangle's adjacent side length: "))
                break
            else:
                print("Try again, you must enter a positive value")
        except ValueError:
            print("Enter a numeric value please")
    return opp1,adj1

def hypotenuse_calculation(opp1,adj1):
    return math.sqrt(opp1**2 + adj1**2)

def weird_calculation():
    opp1,adj1 = triangle_sides(1)
    hyp1 = hypotenuse_calculation(opp1,adj1)

    opp2,adj2 = triangle_sides(2)
    hyp2 = hypotenuse_calculation(opp2,adj2)

    hyp3 = hypotenuse_calculation(hyp1,hyp2)
   
    return hyp3

print(weird_calculation())


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# The lengths must be positive, the total of 2 sides of the triangle must be greater that the third side.

# 2. Validate the user's input based on your preconditions.
#def triangle_sides(triangle_num):
    #while True:
     #   try:
      #      opp1 = float(input("Enter your triangle's opposite side length: "))
       #     if opp1 > 0:
        #        adj1 = float(input("Enter your triangle's adjacent side length: "))
         #       break
          #  else:
               # print("Try again, you must enter a positive value")
       # except ValueError:
           # print("Enter a numeric value please")
   # return opp1,adj1
#
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
# It was useful as i didn't need to rewrite the code for the hypotenuse calculation, so it saved me time.
# Also, my code was shorter as i was able to use only 1 function to calculate the hypotenuse of 2 triangles.


# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
