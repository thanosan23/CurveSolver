# CurveSolver

Find the exponential curve of best fit.

## How to use
1. Enter in the data in `data.csv`
2. Run the program and the output will be the exponential curve of best fit.


## How does it work
This program takes advantage of the "log trick". By taking the log of the x and y data, and finding the best fit of the data, the exponential curve of best fit can be found.

```
y = b*x^m

log(y) = m*log(x)+log(b)
```
