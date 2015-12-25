# Using statistical entropy as a measure of risk in Portfolio Optimization

The objective of this project was to use the signal entropy in stock data as a measure of risk,
for the application of picking the optimal portfolio.

## What is Entropy?

A random variable is one whose outcomes can only be found by observation, as they don't have
certain values. This introduces the notion of a probability of each possible value this variable
can take. A discrete variable is one that can take discrete values (duh). An example is the number
of possible outcomes from rolling two dice, or the number of outcomes expected when flipping a coin.
The other type of variable is called continuous. An example of this is the average height of all males
in North Korea. 

Now let's assume that there is a discrete random variable X, that is described by a probability 
distribution function p(X). The probability of a specific event Y, will then have the probability
p(Y), and the entropy of that event is -p(Y)*log(p(Y)). The total entropy in the variable is sum
of the entropies of all the events that can possibly occur.



Entropy is a measure of uncertainty in a signal. In thermodynamics, entropy is used to described
the number of available atomic energy states. In coding theory, entropy calculated using the base-2
logarithmic function gives the minimum number of bits required to code a random signal.

## Why entropy?

In finance, the entropy in the asset pricing data can be used to compute risk. The elegance of this is that
we can use the entropies of all the assets as a linear constraint, when posing the "optimal portfolio" 
problem as a mathematical optimization objective, specifically as a linear programming problem. The current
risk management strategy in optimization, is achieved by imposing a quadratic non-linear constraint on the
problem, which can be difficult to solve without Lagrange duality.


## What are we doing here?

For the engineering description, check out the report [here](https://github.com/tommathewXC/EntropyOptimizedPortfolio/blob/master/Documentation/An%20application%20of%20entropy%20as%20a%20risk%20constraint%20in%20Portfolio%20Optimization.docx)

The programmatic process is a follows:

1.	Pulled data manually from google finance's historical records.
2. 	Cleaned, and preprocessed the data.
3.	Built the probability distribution tables.
4.	Ran the linear program in MATLAB.

## How are we doing this?

1.	From [here](https://github.com/tommathewXC/EntropyOptimizedPortfolio/tree/master/Python%20files, run the 
	run main.py. Note that the cleaning process will create a text file with the tabulated stock data. These
	tables will be used in the next part.
2.	Compile [this](https://github.com/tommathewXC/EntropyOptimizedPortfolio/tree/master/C%2B%2B%20files) code, 
	after specifying the paths to your training and testing directories, and the path to the list of tables in
	your training directory.
3.	Run "entropylp.m", after loading all the files from [here](https://github.com/tommathewXC/EntropyOptimizedPortfolio/blob/master/Matlab%20files/entropylp.m)
	to your MATLAB environment.
	
## What are the pros with this technique?
	
	1. 	Entropy is an information theoretic measure that describes all the useful information in a statistical	
		variable. I find it a better measure of risk than entropy (personal opinion).
	2. 	This whole process is extremely easy to do.
	3.	The methods in linear programming is pretty well understood, and there is practically an infinite amount
		of resources to learn from.

## What are the cons with this technique?

	0. 	There are none. (jk)
	1.	The data layer of the python project assumes that the data is in csv format. Probably not 
		the most efficient way to store data.
	2.	There is a lot of references to absolute paths in the code base.
	3.	The data grabbing process is not automated (as of yet).
	4.	Lastly, and most importantly, the dependence on MATLAB. A very expensive con. However, 
		OCTAVE is a spiritual twin to MATLAB and is free.

		
## OK, let's see it in action.
	
Run the "entropylp.m" to get the following plots
	
	
**The performance of two portfolios with two different entropy constraints. **
![alt text](https://github.com/tommathewXC/Forex_Processing_Prototype/blob/master/daily.png "Daily data")

**The average return rate for different entropy constraint.**
![alt text](https://github.com/tommathewXC/Forex_Processing_Prototype/blob/master/daily.png "Hourly data")


**Performance over 50 months at a good entropy constraint**
![alt text](https://github.com/tommathewXC/Forex_Processing_Prototype/blob/master/miunte.png "Minute Data")
