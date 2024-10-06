# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
def hyp():
    opp = input("Enter your triangle's opposite side: ") 
    while opp.isdigit() == False :
        print("That is not a valid number.")
        opp = input("Enter your triangle's opposite side: ")    
    adj = input("Enter your triangle's adjacent side length: ")
    while adj.isdigit() == False:
        print("That is not a valid number.")
        adj = input("Enter your triangle's adjacent side length: ")


    import math
    hyp1 = math.sqrt(int(opp)**2 + int(adj)**2)
    return hyp1
# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################

def weird_calculation():
    # get the length and width of the first triangle from the user
    count = 0
    while count < 2:
        if count == 0:
            hyp1 = hyp()
        else: 
            hyp2 = hyp()
        count = count + 1
    # create a third triangle with the hyp1 as the opp and hyp2 as the adj
    opp3 = hyp1
    adj3 = hyp2
    
    import math
    hyp3 = math.sqrt(opp3**2 + adj3**2)
    return hyp3

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
