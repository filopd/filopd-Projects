"""
Reusing code from survey.py and first.py, compute the standard deviation of gestation time for first babies and others.
Does it look like the spread is the same for the two groups? How big is the difference in the means compared
to these standard deviations? What does this comparison suggest about the statistical significance of the difference?
"""
import thinkstats_code.thinkstats as ts
import thinkstats_code.first as fp
import math as mt

def main(name, data_dir='.'):
    table, firsts, others = fp.MakeTables(data_dir)
    fp.ProcessTables(firsts, others)
    print("First Babies:")
    mean = ts.Mean(firsts.lengths)
    variance = ts.Var(firsts.lengths)
    sdv = mt.sqrt(variance)
    print(" Mean is:", mean)
    print(" Variance:", variance)
    print(" Standard Deviation:", sdv)
    print("\nOther than First Babies:")
    mean = ts.Mean(others.lengths)
    variance = ts.Var(others.lengths)
    sdv = mt.sqrt(variance)
    print(" Mean is:", mean)
    print(" Variance:", variance)
    print(" Standard Deviation:", sdv)
    print("\n\nDifference in ")
    print(" Mean is:", ts.Mean(firsts.lengths) - mean)
    print(" Standard Deviation:", mt.sqrt(ts.Var(firsts.lengths))- sdv)

if __name__ == '__main__':
    import sys

    main(*sys.argv)