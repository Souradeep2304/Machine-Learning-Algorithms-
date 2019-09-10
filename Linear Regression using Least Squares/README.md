# Implementing Linear Regression using Least Squares Technique
Linear regression is the technique in which we are going to estimate the value of a target variable based on a random input using the given set of values of independent and the correspondent target variables. Here we are going to use a single independent variable to estimate the prediction function.

##Estimation of the Prediction Function

The prediction function that we are going to use in this case is as follows:<br/>

Y=Theta0+(Theta1*X)<br/>

where Theta0 and Theta1 are the parameters so as the value of the cost fucntion is mimimum.<br/>
In least squares technique we are going to minimize the value of the cost function by mimizing the sum of square of errors which is the difference between original value of the target variable and the estimated one. From the mathematical derrivations we get **Theta1** as the value of standard deviation of y and x being divided by the value of standard deviation of X; and **Theta0** as the difference between the mean of the target variables and mean of input variables multiplied by size of the data set.s

