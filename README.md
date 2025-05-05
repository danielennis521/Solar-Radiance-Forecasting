# Introduction
Due to improvements in manufacturing and the development of more effective photovoltaic cells, solar energy has seen a rapid increase in popularity. From the data available from OurWorldInData
We can see that the amount of solar energy being produced has increased exponentially.

![global renewable energy production]()
https://ourworldindata.org/grapher/solar-energy-consumption?time=latest

Solar energy is likely to continue playing an important role in our transition towards cleaner energy production in the coming years. Since solar power generation is inherently intermittent
it is vital that we have systems that can store excess energy for later use and that we are able to reliably estimate the energy that will be produced in the future. When energy production
from intermittent sources falls sharply and unexpectedly the sudden spike in demand for energy from other sources can lead to steep price increases. 

# Time Series Forecasting Methods


# The Data
Data on the intensity of sunlight in a given region can be found at the National Renewable Energy Labs (NREL) National Solar Radiation Database (NRSDB), https://nsrdb.nrel.gov/ . The 
data cover all of the US and at a resoltion of 1km x 1km with snapshots being taken every 30 minutes. In order to access the data you'll need to set up an API key and follow the instructions
provided at https://github.com/NREL/hsds-examples/blob/master/notebooks/03_NSRDB_introduction.ipynb .

# Model Fitting
## Sarima Fit
For the SARIMA model we need to choose the number of previous observations to fit, the number of previous errors, and an order of differncing. Since our predictions are only looking ahead an hour to a day the nonstationarity due to seasonal shifts is not noticable so it is reasonable to not use any differencing, i.e. for shorter term forecasting a SARMA model is sufficient. The decay in the autocorrelation of our data can be used to determine how many previous observations we should consider in the autoregressive part of the SARMA model,

<img src="https://github.com/danielennis521/Solar-Radiance-Forecasting/blob/main/model%20fitting/sarima_autocorrelation.png" alt="ACF plot" width="450" height="325">

So it appears that around 8 previous observations is a reasonable number to use. While the ACF shows much older observations being significant we know this is because of seasonality. Looking at the PACF we see that again using 8 previous errors will be enough,

<img src="https://github.com/danielennis521/Solar-Radiance-Forecasting/blob/main/model%20fitting/sarima_pacf.png" alt="PACF plot" width="450" height="325">

since our data is in 30 minute intervals the length for the seasonality will be 48. All of this together gives us the information we need to build our model. We can use the statsmodel library to train on several different date ranges. The test predictions pictured below were generated from the sarima_fit.py file in the "model fitting" folder.

<img src="https://github.com/danielennis521/Solar-Radiance-Forecasting/blob/main/model%20fitting/sarima_single_bin_1.png" alt="SARIMA fit 1" width="750" height="300">
<img src="https://github.com/danielennis521/Solar-Radiance-Forecasting/blob/main/model%20fitting/sarima_single_bin_2.png" alt="SARIMA fit 2" width="750" height="300">

## Holt Winters Fit 
There are no parameters we need to fit for this model in the way that we had to for SARIMA. Instead we need to select the type of the model, specifically, the trend and seasonal components can either be addative or multiplicative. For this we'll simply test each method, measure the sum of absolute errors and compare,

<img src="https://github.com/danielennis521/Solar-Radiance-Forecasting/blob/main/model%20fitting/HW_test.png" alt="PACF plot" width="450" height="325">

This gives us the following sum of error magnitudes,
  
  trend-addative, seasonal-addative: 3557.39  
  trend-multiplicative, seasonal-multiplicative: 4203.60  
  trend-addative, seasonal-multiplicative: 5375.72  
  trend-multiplicative, seasonal-addative: 5930.04  
  
So we can see that choosing the addative model for all components is the clear winner

# Predictions and Comparison of the Models


# Conclusion
