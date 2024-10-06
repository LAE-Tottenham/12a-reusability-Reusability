# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
def triangle(opp1, adj1):
    import math
    hyp1 = math.sqrt(opp1**2 + adj1**2)
    return hyp1

def weird_calculation():
    import math
    hyplist = []
    for i in range(2):
        while True:
            try:
                opp1 = float(input("Enter your first triangle's opposite side length: "))
            except ValueError:
                print("Please enter a number.")
            else:
                break
        while True:
            try:
                adj1 = float(input("Enter your first triangle's adjacent side length: "))
            except ValueError:
                print("Please enter a number.")
            else:
                break
        hyp = triangle(opp1, adj1)
        hyplist.append(hyp)
    hyp1 = hyplist[0]
    hyp2 = hyplist[1]
    hyp3 = math.sqrt(hyp1**2 + hyp2**2)
    return hyp3

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
#   The triangle lengths have to be numbers and not variables
# 2. Validate the user's input based on your preconditions.
#   I did it.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
#   Because it meant we could use the function twice to get the 2 different values of the hypotenuse, which were then used to get the value of the third hypotenuse.
#   Because it shortened our code by a lot as the parts that needed to be done more than once were removed and put only once.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
