
import pandas as pd
import h5pyd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


f = h5pyd.File("/nrel/nsrdb/v3/nsrdb_2015.h5")
# for k in f:
#     dset = f[k]
#     print(f"{dset.name} {dset.shape}")

# filter to the area of interest
coords = f['coordinates']
coords = pd.DataFrame({'latitude': coords[:, 0], 'longitude': coords[:, 1]},index=range(0,coords.shape[0]))
space_index = coords.loc[(coords.latitude < 45.25) 
                 & (coords.latitude > 44.5)
                 & (coords.longitude < -93.75)
                 & (coords.longitude > -94)].index
coords = coords.iloc[space_index]


# filter to a time of interest
date_format = "%Y-%m-%d %H:%M:%S"
first_day = '2015-02-01 16:00:00'
last_day = '2015-06-01 16:00:00'

first_day = datetime.strptime(first_day, date_format)
last_day = datetime.strptime(last_day, date_format)

first_time_index = first_day.timetuple().tm_yday * 48
last_time_index = last_day.timetuple().tm_yday * 48

dates = [first_day + timedelta(minutes=30*i) for i in range(last_time_index - first_time_index)]

# get the associated data
ghi = f['ghi']
df = pd.DataFrame({i: ghi[first_time_index:last_time_index, i] for i in space_index})
df['datetime'] = dates
df.to_csv('StLouisPark_Solar_Data.csv', index = False)
