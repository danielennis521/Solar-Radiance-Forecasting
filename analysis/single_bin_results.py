import pandas as pd
import matplotlib.pyplot as plt

errors = pd.read_csv('forecast_errors.csv')
sarima_errors = errors[errors['SARIMA'] < 15000]['SARIMA']
holtwin_errors = errors[errors['Holt-Winters'] < 15000]['Holt-Winters']

plt.hist(sarima_errors, 20, alpha=0.6, label='SARIMA', density=True)
plt.hist(holtwin_errors, 20, alpha=0.6, label='Holt-Winters', density=True)
plt.legend()
plt.title('Distribution of Forecast Errors: SARIMA vs. Holt-Winters')
plt.xlabel('Total Error Per Forecast')
plt.show()

print('SARIMA mean error:', sarima_errors.mean())
print('SARIMA median error:', sarima_errors.median())
print('Holt-Winters mean error:', holtwin_errors.mean())
print('Holt-Winters median error:', holtwin_errors.median())