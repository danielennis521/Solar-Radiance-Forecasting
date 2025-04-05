
import numpy as np
import matplotlib.pyplot as plt


class exponential_smoothing():

    def __init__(self, alpha=0.1):
        self.alpha = alpha


    def train(self, x, cost='least squares', method='Golden Section', iterations=10):
        # inputs:
        # x: the time series you want to fit
        # cost: form of the sum of residuals to be minimized
        # method: algorithm to be used in minimizing non-linear equation
        # iterations: max number of iterations for the solver to compute

        if cost == 'least squares':
            self.lstq_fit(x, method=method)
        elif cost == 'lad':
            self.lad_fit(x, method=method)
        else:
            raise Exception("invalid choice for method")


    def predict(self, x, num_steps=1, location=-1):
        pass


    def lstq_fit(self, x, iterations=10, tol=1e-6, method='Golden Section'):

        if method == 'Newton':
            n = len(x)
            self.alpha=0.1

            for k in range(iterations):
                
                # compute f and f'
                f = 0
                df = 0
                ddf = 0
                for i in range(n-1):
                    L = np.sum([self.alpha * (1-self.alpha)**j * x[i-j] for j in range(i)])
                    dL = np.sum([-x[i-j] * (1 - self.alpha)**(j-1) * (1 - self.alpha*(j + 1)) for j in range(i)])
                    ddL = np.sum([x[i-j] * (1-self.alpha)**2 * ((j-1)*(1-self.alpha*(j+1)) + (j+1)*(1-self.alpha)) for j in range(i)])

                    f += (x[i + 1] - L)**2
                    df += 2 * (x[i + 1] - L) * dL
                    ddf += 2*(dL**2 - (x[i + 1] - L)*ddL)
                
                # Newtons Method step
                self.alpha -= 4*1e-3*ddf*df
        
        elif method=='Golden Section':
            n = len(x)
            t = (np.sqrt(5) - 1)/2
            left = 0.0
            right = 1.1
            a1 = left + (1-t)*(right - left)
            a2 = left + t*(right - left)

            f_left = 0
            f_right = 0
            f1 = 0
            f2 = 0

            for i in range(n-1):
                L_left = np.sum([left * (1-left)**j * x[i-j] for j in range(i)])
                L_right = np.sum([right * (1-right)**j * x[i-j] for j in range(i)])
                L1 = np.sum([a1 * (1-a1)**j * x[i-j] for j in range(i)])
                L2 = np.sum([a2 * (1-a2)**j * x[i-j] for j in range(i)])

                f_left -= (x[i + 1] - L_left)**2
                f_right -= (x[i + 1] - L_right)**2
                f1 += (x[i + 1] - L1)**2
                f2 += (x[i + 1] - L2)**2

            for k in range(iterations):
                if f1 > f2:
                    left = a1
                    a1 = a2
                    f1 = f2
                    a2 = left + t*(right - left)

                    f2 = 0
                    for i in range(n-1):
                        L2 = np.sum([a2 * (1-a2)**j * x[i-j] for j in range(i)])
                        f2 += (x[i + 1] - L2)**2
                else:
                    right = a2
                    a2 = a1
                    f2 = f1
                    a1 = left + (1-t)*(right - left)
                    
                    f1 = 0
                    for i in range(n-1):
                        L1 = np.sum([a1 * (1-a1)**j * x[i-j] for j in range(i)])
                        f1 += (x[i + 1] - L1)**2

            self.alpha = (a1 + a2) / 2
        return 


    def lad_fit(self, x, iterations=10, tol=1e-6):
        
        n = len(x)
        self.alpha=1

        for i in range(iterations):
            
            # compute f and f'
            f = 0
            df = 0
            for i in range(n):
                for j in range(i):
                    pass
            
            # check convergence
            if df < tol:
                break

            # Newtons Method step
            self.alpha -= f/df

        return 



class holt_winters_smoothing():

    def __init__(self, alpha=0.1):
        self.alpha = alpha


    def train(self, x, method='least squares'):

        if method == 'least squares':
            self.lstq_fit(x)
        elif method == 'lad':
            self.lad_fit(x)
        pass


    def predict(self, x, num_steps=1, location=-1):
        pass


    def lstq_fit(self, x):
        pass


    def lad_fit(self, x):
        pass
