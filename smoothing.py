
import numpy as np



class exponential_smoothing():

    def __init__(self, alpha=0.1):
        self.alpha = alpha


    def train(self, x, method='least squares'):

        if method == 'least squares':
            self.lstq_fit(x)
        elif method == 'lad':
            self.lad_fit(x)
        else:
            raise Exception("invalid choice for method")


    def predict(self, x, num_steps=1, location=-1):
        pass


    def lstq_fit(self, x, iterations=10, tol=1e-6):
        
        n = len(x)
        self.alpha=0.1

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


    def lad_fit(self, x, iterations=10, tol=1e-6):
        
        n = len(x)
        self.alpha=0.1

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
