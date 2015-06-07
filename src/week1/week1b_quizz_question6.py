#!/usr/bin/env python
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    # Put your code here.
    #FV = PV (1+rate)**periods
    return present_value*(rate_per_period+1)**periods

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
  
print "$500 at 4% compounded 10 times a year for 3 years yields $", future_value(500, .04, 10, 10)
