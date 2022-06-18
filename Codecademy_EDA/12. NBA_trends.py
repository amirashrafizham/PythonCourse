import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, chi2_contingency


nba = pd.read_csv('nba_games.csv')

# NUMERICAL AND CATEGORICAL ASSESSMENT
# ----------------------------------------------------------------------#
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]
print(nba_2010.head())


# Store Kicks and Nets data
Knicks_pts_2010 = nba_2010[nba_2010['fran_id'] == 'Knicks']
Nets_pts_2010 = nba_2010[nba_2010['fran_id'] == 'Nets']

Knicks_pts_2014 = nba_2014[nba_2014['fran_id'] == 'Knicks']
Nets_pts_2014 = nba_2014[nba_2014['fran_id'] == 'Nets']


# Calcualte mean difference of pts for 2010 and 2014

mean_diff_2010 = Knicks_pts_2010['pts'].mean() - Nets_pts_2010['pts'].mean()
mean_diff_2014 = Knicks_pts_2014['pts'].mean() - Nets_pts_2014['pts'].mean()


# Compare the mean points based on histogram
def hist_knicks_nets():
    plt.hist(Knicks_pts_2010.pts, label="Knicks", density=True, alpha=0.5)
    plt.hist(Nets_pts_2010.pts, label="Nets", density=True, alpha=0.5)
    plt.title('2010 data')
    plt.legend()
    plt.show()
    plt.close()
    print(f"Mean difference 2010: {mean_diff_2010}")

    plt.hist(Knicks_pts_2014.pts, label="Knicks", density=True, alpha=0.5)
    plt.hist(Nets_pts_2014.pts, label="Nets", density=True, alpha=0.5)
    plt.title('2014 data')
    plt.legend()
    plt.show()
    plt.close()
    print(f"Mean difference 2014: {mean_diff_2014}")


# Compare the mean points of Knicks and Nets based on boxplots
def boxplot_knicks_nets():
    nba_2010_knicks_nets = nba_2010[(nba_2010.fran_id ==
                                    'Knicks') | (nba_2010.fran_id == 'Nets')]

    nba_2014_knicks_nets = nba_2014[(nba_2014.fran_id ==
                                    'Knicks') | (nba_2014.fran_id == 'Nets')]

    sns.boxplot(data=nba_2010_knicks_nets, x='fran_id', y='pts')
    plt.title('2010 data')
    plt.show()
    plt.close()

    sns.boxplot(data=nba_2014_knicks_nets, x='fran_id', y='pts')
    plt.title('2014 data')
    plt.show()
    plt.close()


def boxplot_all_teams():
    sns.boxplot(data=nba_2010, x='fran_id', y='pts')
    plt.show()
    plt.close()

    sns.boxplot(data=nba_2014, x='fran_id', y='pts')
    plt.show()
    plt.close()

# CATEGORICAL AND CATEGORICAL ASSESSMENT
# ----------------------------------------------------------------------#


# Check if teams win more games away or home
location_result_freq = pd.crosstab(
    nba_2010['game_result'], nba_2010['game_location'])

print(location_result_freq)


# Convert into properties table
location_result_prop = location_result_freq/len(nba_2010)
print(location_result_prop)

# Calculating the chi-square statistic
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(chi2)


# NUMERICAL AND NUMERICAL ASSESSMENT
# ----------------------------------------------------------------------#

# Checking the covariance between forecast and point_diff for 2010 data
cov_forecast_pointdiff = np.cov(nba_2010['forecast'], nba_2010['point_diff'])
print(cov_forecast_pointdiff)

cov_sqfeet_beds = 228.2

# Using Pearson's correlation to establish the relationship
corr_forecast_pointdiff, p = pearsonr(
    nba_2010['forecast'], nba_2010['point_diff'])
print(corr_forecast_pointdiff)

# Checking the relationship using a Scatterplot
plt.scatter(x=nba_2010['forecast'], y=nba_2010['point_diff'])
plt.show()
