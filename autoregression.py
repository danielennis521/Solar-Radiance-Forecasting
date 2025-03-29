
import numpy as np
import matplotlib.pyplot as plt



class AR_Model():

    def __init__(self, order):
        self.order = order
        self.coefficients = np.zeros(self.order)


    def train(self, x):
        # inputs:
        # x: the time series you want to fit the AR(self.order) model to
        #    note that we need len(x) >= self.order + 1 to be able to solve

        b = x[self.order:]
        A = [ x[self.order-i:-i] for i in range(1, self.order+1)]
        A = np.array(A)

        self.coefficients = np.linalg.lstsq(A.T, b, rcond=None)[0]

    
    def predict(self, x, num_steps=1, location=-1):
        # inputs:
        # x: time series you want to predict, must have len > self.order
        # num_steps: numer of steps foreward you want to predict
        # location: position in the series where you want to start the prediction
        #           i.e. location=-1, num_steps=1 predicts the next step after the
        #           end of the given time series 

        y = x.copy()

        for i in range(num_steps):
            y = np.append(y, y[-self.order:].dot(test_model.coefficients))

        return y[-num_steps:]



class ARIMA():

    def __init__(self):
        pass


    def train(self, x):
        pass


    def predict(self, x, num_steps=1, location=-1):
        pass



class SARIMA():

    def __init__(self):
        pass


    def train(self, x):
        pass


    def predict(self, x, num_steps=1, location=-1):
        pass



n = 100
t = np.linspace(0, 4, n)
x = np.sin(4*np.pi*t) + np.random.normal(0, 0.1, n)


order = 12
test_model = AR_Model(order)
test_model.train(x)
y = np.concatenate([x[:order], [x[i:i+order].dot(test_model.coefficients) for i in range(0, n-order)] ])
plt.plot(t, x)
plt.plot(t, y)
plt.show()

print(test_model.predict(x[:order], 5))