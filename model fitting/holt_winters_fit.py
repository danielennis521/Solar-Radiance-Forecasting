
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt
import numpy as np


# determining parameters
train_start = 73*48 + 20
train_end = 87*48 + 20
solar_intensity = pd.read_csv('StLouisPark_Solar_Data.csv')
bin1 = solar_intensity[solar_intensity.columns[0]][train_start:train_end]
bin1 = bin1 + 0.01
#bin1 = [np.max(b, 0) for b in bin1]

forecast_interval = 48

#1
solar_exp = ExponentialSmoothing(bin1, trend='mul', seasonal='mul', seasonal_periods=forecast_interval)
results = solar_exp.fit()

prediction = results.predict(len(bin1), len(bin1)+forecast_interval-1).to_numpy()
observation = solar_intensity[solar_intensity.columns[0]][train_end:train_end+forecast_interval].to_numpy()

res_mul_mul = np.sum(np.abs(prediction-observation)[:32])

#2
solar_exp = ExponentialSmoothing(bin1, trend='mul', seasonal='add', seasonal_periods=forecast_interval)
results2 = solar_exp.fit()

prediction2 = results2.predict(len(bin1), len(bin1)+forecast_interval-1).to_numpy()
observation = solar_intensity[solar_intensity.columns[0]][train_end:train_end+forecast_interval].to_numpy()

res_mul_add = np.sum(np.abs(prediction2-observation)[:32])

#3
solar_exp = ExponentialSmoothing(bin1, trend='add', seasonal='mul', seasonal_periods=forecast_interval)
results3 = solar_exp.fit()

prediction3 = results3.predict(len(bin1), len(bin1)+forecast_interval-1).to_numpy()
observation = solar_intensity[solar_intensity.columns[0]][train_end:train_end+forecast_interval].to_numpy()

res_add_mul = np.sum(np.abs(prediction3-observation)[:32])

#4
solar_exp = ExponentialSmoothing(bin1, trend='add', seasonal='add', seasonal_periods=forecast_interval)
results4 = solar_exp.fit()

prediction4 = results4.predict(len(bin1), len(bin1)+forecast_interval-1).to_numpy()
observation = solar_intensity[solar_intensity.columns[0]][train_end:train_end+forecast_interval].to_numpy()

res_add_add = np.sum(np.abs(prediction4-observation)[:32])


plt.plot(prediction[:32], color='blue', label='trend:mul, season:mul')
plt.plot(prediction2[:32], color='red', label='trend:mul, season:add')
plt.plot(prediction3[:32], color='green', label='trend:add, season:mul')
plt.plot(prediction4[:32], color='purple', label='trend:add, season:add')
plt.plot(observation[:32], color='black', label='observation')
plt.legend()
plt.show()

print(res_add_add)
print(res_mul_mul)
print(res_add_mul)
print(res_mul_add)
