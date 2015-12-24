# Forex_Processing_Prototype
A prototype library to pull Foreign Currency exchange rates from Gain Capital's pubic records

This library is a prototype of a better concept (that will be released soon-ish), that can do the followin things:

1. Create a hierarchical folder structure in the executing directory, depending on two specific countries, for a specific year, month, and week. 
2. Dowload and extract Exchange rates between two specific countries, for a specific year, month, and week. 
3. Extract the Ask price or Bid price from the extracted data
4. Store the exchange rate data in a tabular format for easy datetime control, for use in things like temporal averaging.


In the example below, we have used the data provided on Gain Capital's website, for any two given currencies.
We have plotted the exchange rates between US Dollars and British Pounds for  for the last week of 
September 2015, we have plotted it for a day, an hour, and a minute.


**The performance of two portfolios with two different entropy constraints. **
![alt text](https://github.com/tommathewXC/Forex_Processing_Prototype/blob/master/daily.png "Daily data")

**The following is plot for the day of October 25th, 2015 at 4 PM**
![alt text](https://github.com/tommathewXC/Forex_Processing_Prototype/blob/master/daily.png "Hourly data")


**The following is plot for the day of October 25th, 2015 at 4:30 PM**
![alt text](https://github.com/tommathewXC/Forex_Processing_Prototype/blob/master/miunte.png "Minute Data")
