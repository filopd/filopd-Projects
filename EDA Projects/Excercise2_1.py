"""
Write a function called Pumpkin that uses functions from thinkstats.py to compute the mean, variance and standard
deviation of the pumpkins weights in the previous section.
"""
import thinkstats_code.thinkstats as ts
import math as mt
"""
Pumpkin example with Seq: [1,1,1,3,3,591]
"""
list_data = [1,1,1,3,3,591]
mean = ts.Mean(list_data)
variance = ts.Var(list_data)
sdv = mt.sqrt(variance)

print("Sequence of Pumpkins:", list_data)
print("Mean is:", mean)
print("Variance:", variance)
print("Standard Deviation:", sdv)
