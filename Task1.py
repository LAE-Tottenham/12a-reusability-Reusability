# Help! My code is too messy :( Please help me organise it and extract out the duplications.
# Define your reusable functions here:
import math
def calculate_hypotenuse(opp, adj):
    return math.sqrt(opp**2 + adj**2)

def get_triangle_sides():
    opp = float(input("Enter the opposite side length: "))
    adj = float(input("Enter the adjacent side length: "))
    return opp, adj


# Make sure each function only does ONE thing!!!!!!!!!!!
###########################################


def weird_calculation():
    opp1, adj1 = get_triangle_sides()
    hyp1 = calculate_hypotenuse(opp1, adj1)
    opp2, adj2 = get_triangle_sides()
    hyp2 = calculate_hypotenuse(opp2, adj2)
    opp3 = hyp1
    adj3 = hyp2
    hyp3 = calculate_hypotenuse(opp3, adj3)
    return hyp3

weird_answer = weird_calculation()
print(weird_answer)

# After you have written the reusable functions, answer the following:

# Questions:
# 1. What are the preconditions for your code not to break?

#That the user's input must be positive integers


# 2. Validate the user's input based on your preconditions.

#in the function get_triangle_sides a while loop can be added  to check that the user enters valid numbers.


# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.

#One benefit is that it reduces the code size, making it easier to read and understand by other people.
#Each function also has a specific purpose and the code would not be repeated multiple times.
#Each function can be tested independantly, improving the quality of the code.


# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
