from scipy.stats import chi2_contingency
import pandas as pd
import numpy as np


npi = pd.read_csv('npi_sample.csv')
print(npi.head(5))

special_authority_freq = pd.crosstab(npi['special'], npi['authority'])
print(special_authority_freq)

# Generate Contigency Table
special_authority_freq = pd.crosstab(npi.special, npi.authority)


# Generate Proportion from Contigency Table
special_authority_prop = special_authority_freq/len(npi)
authority_marginals = special_authority_prop.sum(axis=0)
special_marginals = special_authority_prop.sum(axis=1)


# Calculating the chi-square
chi2, pval, dof, expected = chi2_contingency(special_authority_freq)
print(expected)
print(chi2)
