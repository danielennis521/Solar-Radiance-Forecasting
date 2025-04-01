
import autoregression as ar
import smoothing as sm
import harmonic_regression as hr
import pandas as pd
import h5pyd
import numpy as np

f = h5pyd.File("/nrel/nsrdb/v3/nsrdb_2012.h5")

# filter to the area of interest
coords = f['coordinates']
coords = pd.DataFrame({'latitude': coords[:, 0], 'longitude': coords[:, 1]}, index=range(0,coords.shape[0]))
index = coords.loc[(coords.latitude < 45.0) 
                 & (coords.latitude > 44.5)
                 & (coords.longitude < -93)
                 & (coords.longitude > -94)].index

coords = coords.iloc[index]
print(coords)


# filter to a time of interest
dates = f['datetime']
pd.DataFrame({'date': dates}, index=range(0,dates.shape[0]))
index = dates.loc[
                  ]

dates = dates.iloc[index]


# get the associated data
ghi = f['ghi']
print(ghi.shape)



# compute models for each forecasting method 

# at each half hour predict the next 4 hours of solar irradiance

#  compare results of each models prediction for the next 30 min 

# compare results of each models prediction for 4 hours from the current time
