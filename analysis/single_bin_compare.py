import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX 
import matplotlib.pyplot as plt
import numpy as np


solar_intensity = pd.read_csv('StLouisPark_Solar_Data.csv')
bin1 = solar_intensity[solar_intensity.columns[0]]
n = len(bin1)


sarima_errors = []
holtwin_errors = []
starts = []
for i in range(300):
    print(i)
    # generate starting point
    a = np.random.randint(0, n-48*15)
    while True:
        if bin1[a] == 0 and bin1[a+1] > 0:
            break
        elif a<=0:
            a = np.random.randint(0, n-48*15)
        else:
            a -= 1


    # SARIMA Prediction
    forecast_interval = 48
    solar_arima = SARIMAX(endog=bin1[a: a + 14*48], order=(6,0,2), seasonal_order=(1, 0, 1, 48))
    results = solar_arima.fit(maxiter=200)
    s_prediction = results.predict(14*48, 15*48)
    observation = solar_intensity[solar_intensity.columns[0]][a + 14*48: a + 15*48]


    # Holt Winters Prediction
    solar_exp = ExponentialSmoothing(bin1[a: a + 14*48].to_numpy() + 0.01, trend='mul', seasonal='mul', seasonal_periods=forecast_interval)
    results = solar_exp.fit()

    hw_prediction = results.predict(14*48, 15*48-1)

    starts.append(a)
    sarima_errors.append(np.sum(np.abs(s_prediction-observation)[:32]))
    holtwin_errors.append(np.sum(np.abs(hw_prediction-observation)[:32]))


df = pd.DataFrame({'starts': starts, 'SARIMA':sarima_errors, 'Holt-Winters':holtwin_errors})
df.to_csv('forecast_errors.csv', index=False)


# plt.plot(hw_prediction, color='green', label='Holt-Winters')
# plt.plot(s_prediction.to_numpy(), color='blue', label='SARIMA')
# plt.plot(observation.to_numpy(), color='black', label='observation')
# plt.legend()
# plt.show()
