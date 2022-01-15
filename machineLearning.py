# This code originates from Eugiene Kanillar and can be found here
# https://www.section.io/engineering-education/an-introduction-to-machine-learning-using-c++/

# It has been edited from C++ to Python for the sake of the project
# Final version made by Jesse White

#Set up historical data
trainingInit = (1, 2, 3, 4, 5)
trainingFollow = (1, 3, 3, 2, 5)

#Initialize an array to store error values
error = []

#Initialize values to be used in the training section of the module
devi = 0.0
b0 = 0.0
b1 = 0.0
learnRate = 0.01

#Train the system to follow a trend with historical data
for i in range(20):
    index = i % 5
    p = b0 + b1 * trainingInit[index]
    devi = p - trainingFollow[index]
    b0 = b0 - learnRate * devi
    b1 = b1 - learnRate * devi * trainingInit[index]
    error.append(devi)

#Take most recent price as input
x = input("Enter a test x value: ")

#Predict the next price value based on previous trends
pred = b0 + b1 * float(x)

print("The value predicted by the model= " + str(pred))

#Check the prices, both the most recent and predicted prices, and determine either buying or selling
if (pred >= float(x)):
    print("It is recommended that you SELL now.")
else:
    print("It is recommended that you BUY now.")
