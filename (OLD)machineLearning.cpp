/* This code originates from Eugiene Kanillar and can be found here
   https://www.section.io/engineering-education/an-introduction-to-machine-learning-using-c++/
   The code has been edited by Jesse White 
   THIS VERSION OF THE MACHINE LEARNING CODE IS NO LONGER USED BY THE FINAL DELIVERABLE
*/

#include<bits/stdc++.h>  // This header file contains all C++ libraries
using namespace std;   // stdout library for printing values 

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main()//Begin Main
{
/*Intialization Phase (We will instruct the program to follow a specific inclination in prices. In this case, we will expect the prices to lower.)*/
double trainingInit[] = {1, 2, 3, 4, 5};    // defining x values 
double trainingFollow[] = {1, 3, 3, 2, 5};    // defining y values 
vector<double>error;             // array to store all error values
double devi;
double b0 = 0;                   //initializing b0
double b1 = 0;                   //initializing b1
double learnRate = 0.01;         //initializing error rate
bool sell;

/*Training Phase*/
for (int i = 0; i < 20; i ++) {   // Since there are five values and four epochs are needed, run a for loop 20 times.
    int index = i % 5;              // This accesses the index after each epoch
    double p = b0 + b1 * trainingInit[index];  // calculating prediction
    devi = p - trainingFollow[index];              // calculating error
    b0 = b0 - learnRate * devi;         // updating b0
    b1 = b1 - learnRate * devi * trainingInit[index];// updating b1
    error.push_back(devi);
}

/*Testing Phase*/
/*(After the AI has been trained we will be able to input a value, like the last known price of Ethereum, and make a prediction of the next price)*/
cout<<"Enter a test x value: ";
double input;
cin>>input;
double pred=b0+b1*input;
cout<<"The value predicted by the model= "<<pred<<"\n";

/*Price Check (Sell high, buy low! If the predicted price is greater than the original price*/
if (pred >= input){ //Begin if comparison of original and predicted price
    sell = true;
    cout<<"The value of sell is = TRUE\n";
    cout<<endl;
}//End if comparison

//Because of the negative inclination of the training phase, "sell" should return as FALSE
else {//Begin else for comparison
    sell = false;
    cout<<"The value of sell is = FALSE\n";
    cout<<endl;
}//End else
}//End main
