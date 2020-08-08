#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 08:47:34 2020

@author: miles
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
sns.set()
sns.despine()

#process data to get falcon winning rate
YEARS = np.array(range(2002, 2020 , 1)).astype(int) #year 2002-2019
rate_df = pd.read_csv("week4_data/falcon_winning_rate_1966_2019.csv", skiprows=lambda x: x in list(range(2, 38)) + [0, 56, 57, 58]) #keep years 2002-2019

wins, losses, ties = rate_df['Wins'], rate_df['Losses'], rate_df['Ties']
rate_df['winning_rate'] = (wins + 0.5 * ties) / (wins + ties + losses) #calculate winning rate
rate_df['Ranking'] = rate_df['Finish'].apply(lambda x: x[0]) #calculate ranking, not used

#process data of falcon franchise value
franchise = pd.read_csv('week4_data/falcon_franchise_value_2002_2019.csv').T.rename(columns={0: 'value'}) #read in franchise value data
 
#process data of Georgia state gdp 
g_gdp =  pd.read_csv('week4_data/GDP_GA_1997_2019.csv') #read in georgai state gdp file
all_gdp = g_gdp[g_gdp['Description'] == 'All industry total'] 
sports_gdp = g_gdp[g_gdp['Description'] == '    Performing arts, spectator sports, museums, and related activities']
g_gdp = all_gdp.append(sports_gdp).set_index("Description").rename(index={'All industry total': 'Total', '    Performing arts, spectator sports, museums, and related activities': 'Entertainment'})
g_gdp.index.name = None
g_gdp = g_gdp.T.iloc[12:] 
g_gdp.Total = g_gdp.Total.astype('float') #process
g_gdp.Entertainment.replace(to_replace='(NA)', value = np.nan, inplace=True) #replace NaN value with np.nan

#combine the dataframes
rate_dataf = rate_df.copy().set_index('Season').loc[:, ['winning_rate', 'Ranking']]
rate_dataf.index.name = None
rate_dataf.set_index(franchise.index, inplace=True)
df = pd.concat([rate_dataf, franchise, g_gdp], axis=1)


#plot winning rate
def plot1():
    ax1 = sns.lineplot(x=YEARS, y='winning_rate', data=rate_df)
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Winning Rate %')
    
    ax1.set(ylim=(0,1.2))
    plt.xticks(YEARS)
    ax1.set_xticklabels(labels=YEARS, rotation=45, ha='right')
    ax1.set_title('Atlanta Falcon Regular Season Winning Rate')
    plt.show()

#plot franchise value
def plot2():
    ax2 = sns.lineplot(x=YEARS, y='value', data=franchise)
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Value (million $)')
    
    plt.xticks(YEARS)
    ax2.set_xticklabels(labels=YEARS, rotation=45, ha='right')
    ax2.set_title('Atlanta Falcon Franchise Value')
    plt.show()
    
#plot georgia total gdp
def plot3():
    ax3 = sns.lineplot(x=YEARS, y='Total', data=g_gdp)
    ax3.set_xlabel('Years')
    ax3.set_ylabel('Total GDP Value (million $)')
    
    plt.xticks(YEARS)
    ax3.set_xticklabels(labels=YEARS, rotation=45, ha='right')
    ax3.set_title('Georgia State Total GDP')
    plt.show()

#plot georgia entertainment industry gdp
def plot4():
    ax4 = sns.lineplot(x=YEARS, y='Entertainment', data=g_gdp)
    ax4.set_xlabel('Years')
    ax4.set_ylabel('GDP Value (million $)')
    
    plt.xticks(YEARS)
    ax4.set_xticklabels(labels=YEARS, rotation=45, ha='right')
    ax4.set_title('Georgia State GDP on Performing Arts, Spectator Sports, Museums, and Related Activities')
    plt.show()

# f = plt.figure(figsize=(16,16))
# ax1 = f.add_subplot(221)
# ax4 = f.add_subplot(223)
# ax2 = f.add_subplot(222)
# ax3 = f.add_subplot(224)
def plot_all():
    plt.subplots(2,2,figsize=(16,12))
    plt.tight_layout(pad=6.0)
    plt.subplot(221)
    ax1 = sns.lineplot(x=YEARS, y='winning_rate', data=rate_df)
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Winning Rate %')
        
    ax1.set(ylim=(0,1.2))
    plt.xticks(YEARS)
    ax1.set_xticklabels(labels=YEARS, rotation=45, ha='right')
    ax1.set_title('Atlanta Falcon Regular Season Winning Rate')
    
    
    plt.subplot(222)
    ax2 = sns.lineplot(x=YEARS, y='value', data=franchise)
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Value (million $)')
    
    plt.xticks(YEARS)
    ax2.set_xticklabels(labels=YEARS, rotation=45, ha='right')
    ax2.set_title('Atlanta Falcon Franchise Value')
    
        
    plt.subplot(223)
    ax4 = sns.lineplot(x=YEARS, y='Entertainment', data=g_gdp)
    ax4.set_xlabel('Years')
    ax4.set_ylabel('GDP Value (million $)')
    
    plt.xticks(YEARS)
    ax4.set_xticklabels(labels=YEARS, rotation=45, ha='right')
    ax4.set_title('Georgia State GDP on Performing Arts, Spectator Sports, Museums, and Related Activities')
        
    plt.subplot(224)
    ax3 = sns.lineplot(x=YEARS, y='Total', data=g_gdp)
    ax3.set_xlabel('Years')
    ax3.set_ylabel('Total GDP Value (million $)')
    
    plt.xticks(YEARS)
    ax3.set_xticklabels(labels=YEARS, rotation=45, ha='right')
    ax3.set_title('Georgia State Total GDP')



