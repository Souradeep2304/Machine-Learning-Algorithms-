# Implementing Linear Regression using Gradient Descent
Linear regression is the technique in which we are going to estimate the value of a target variable based on a random input using the given set of values of independent and the correspondent target variables. Here we are going to use a single independent variable to estimate the prediction function.

## Estimation of the prediction fucntion using Gradient Descent

We will know that we have succeeded when our cost function is at the very bottom of the pits in our graph, i.e. when its value is the minimum. The red arrows show the minimum points in the graph.

The way we do this is by taking the derivative (the tangential line to a function) of our cost function. The slope of the tangent is the derivative at that point and it will give us a direction to move towards. We make steps down the cost function in the direction with the steepest descent. The size of each step is determined by the parameter α, which is called the learning rate.

For example, the distance between each 'star' in the graph above represents a step determined by our parameter α. A smaller α would result in a smaller step and a larger α results in a larger step. The direction in which the step is taken is determined by the partial derivative of J(θ0,θ1)J(\theta_0,\theta_1)J(θ0​,θ1​). Depending on where one starts on the graph, one could end up at different points. The image above shows us two different starting points that end up in two different places. 