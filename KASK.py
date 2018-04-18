# -*- coding: utf-8 -*-
"""
Created on Wed May 27 07:26:50 2015

@author: a001819
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 12:31:42 2014

@author: a001819
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

fid = open('datauttag_SK.txt','r')

for i, row in enumerate(fid):
    if i==0:
        param = row.split('\t')
        my_dat = dict((par, []) for par in param)
        my_dat['my_t'] = []
        my_dat['uyear'] = []   #Skapa en lista med unika år
        my_dat['pl_time'] = [] #Skapa en lista med unika år till plottar
        
    else:
        split_row = row.split('\t')
        if float(split_row[15]) <= 10. and int(split_row[6]) <= 8 and int(split_row[6]) >= 6:
            for i, par in enumerate(param):
                value = split_row[i]
                try:
                    value = float(value)
                except:
                    pass
                if value == '':
                    value = np.nan
                elif par == 'Year':
                    #value = datetime.datetime(int(value),6,15)
                    value = int(value)
                    if value not in my_dat['uyear']:
                        my_dat['uyear'].append(value)
                        my_dat['pl_time'].append(datetime.date(value,6,15))                                   
#                elif par == '':

                my_dat[par].append(value)
            my_dat['my_t'].append(datetime.datetime(int(my_dat['Year'][-1]),int(my_dat['Month'][-1]),int(my_dat['Day'][-1]),int(my_dat['Hour'][-1]),int(my_dat['Minute'][-1])))
        

# Gör säsongsmedelvärden för varje år 
pp = 'Chla (ug/l)'
my_mean = {}
my_mean['chlmean'] = []
for j, val in enumerate(my_dat['uyear']):
    elem = [my_dat[pp][i] for i,x in enumerate(my_dat['Year']) if x == val]
    my_mean['chlmean'].append(np.mean(elem))
        

        
#Plotta data
'''
plotta chl mot DINw
lägsta kvartilen för syredata: np.percentile
tid som syrefritt
for i, val in enumerate(my_dat['my_t']):
print val
val.year
'''
#Data till plotten
fig, ax = plt.subplots()
plt.plot(my_dat['pl_time'],my_mean['chlmean'],'ro')

#Sätter grid
ax.grid(True)
years = mdates.YearLocator() 
ax.xaxis.set_major_locator(years)

#Sätter axlar
datemin = datetime.date(min(my_dat['uyear']), 1, 1)
datemax = datetime.date(max(my_dat['uyear']), 12, 31)
ax.set_xlim(datemin, datemax)
plt.title(pp)
plt.ylabel(u'(ug/l)')
plt.xlabel('Year')

#mp.plot(my_smean['Year'],my_smean['mean'],'.')
                
#mp.plot(my_dat['my_t'],my_dat[u'Chla (µg/l)'],'.') #O2 (ml/l)Chla (µg/l)'],'.') #PO4 (µmol/l)'],'.')
#mp.plot(my_dat['my_t'].sort())                
#mp.plot(my_dat[u'PO4 (µmol/l)'])

plt.show()        
        
#for pp in param:
#    my_dat[pp] = []
#    for i, row in enumerate(fid):
#        split_row = row.split('\t')
#        if i>0:
#            if float(split_row[15]) <= 10.:
#                my_dat[pp].append(float(split_row[8]))
#                try:
#                    my_dat[pp].append(float(split_row[pp]))
#                except:
#                    my_dat[pp].append(np.nan)
#
#



#mp.plot(to_plot)


#>>> import datetime
#>>> datetime.datetime.now()
#datetime.datetime(2015, 5, 27, 12, 2, 48, 893000)
#>>> datetime.datetime(2003,04,05)
#datetime.datetime(2003, 4, 5, 0, 0)
#>>> t=datetime.datetime(2003,04,05)
#>>> t.strftime('%Y--%m')
#'2003--04'
#>>> t.strftime('%Y-jgiopo-%m')
#'2003-jgiopo-04'
#>>> 