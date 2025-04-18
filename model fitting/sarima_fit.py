
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX 
import matplotlib.pyplot as plt

# determining parameters
train_start = 60*48 + 16
train_end = 74*48 + 16
solar_intensity = pd.read_csv('StLouisPark_Solar_Data.csv')
bin1 = solar_intensity[solar_intensity.columns[0]][train_start:train_end]

plt.plot(bin1)
plt.show()
plot_acf(bin1)
plt.show()
plot_pacf(bin1)
plt.show()

# test prediction 1
forecast_interval = 48
solar_arima = SARIMAX(endog=bin1, order=(8,0,2), seasonal_order=(1, 0, 1, 48))
results = solar_arima.fit(maxiter=200)
prediction = results.predict(len(bin1), len(bin1)+48)
observation = solar_intensity[solar_intensity.columns[0]][train_start:train_end+forecast_interval]


print(prediction)
plt.plot(prediction, color='blue', label='prediction')
plt.plot(observation, color='black', label='observation')
plt.legend()
plt.show()

# test prediction 2
train_start = 83*48 + 16
train_end = 97*48 + 16
bin1 = solar_intensity[solar_intensity.columns[0]][train_start:train_end]

forecast_interval = 48
solar_arima = SARIMAX(endog=bin1, order=(8,0,2), seasonal_order=(1, 0, 1, 48))
results = solar_arima.fit(maxiter=200)
prediction = results.predict(len(bin1), len(bin1)+48)
observation = solar_intensity[solar_intensity.columns[0]][train_start:train_end+forecast_interval]


print(prediction)
plt.plot(prediction, color='blue', label='prediction')
plt.plot(observation, color='black', label='observation')
plt.legend()
plt.show()
