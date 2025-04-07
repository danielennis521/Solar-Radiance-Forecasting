
import numpy as np


class harmonic_regression():

    def __init__(self):
        self.main_modes = []
        self.x = []


    def train(self, x, cutoff=0.1):
      
        b1 = np.array( [(2/n) * np.sum( x*np.cos(t * (2*np.pi) * (i/n)) ) for i in range(1, n//2)] )
        b2 = np.array( [(2/n) * np.sum( x*np.sin(t * (2*np.pi) * (i/n)) ) for i in range(1, n//2)] )
        b0 = (1/n)*np.sum(x)
        bn = (1/n)*np.sum(x* np.array([(-1)**i for i in range(n)]))

        b1 = np.insert(b1, 0, b0)
        b2 = np.insert(b2, 0, 0)
        b1 = np.insert(b1, -1, bn)
        b2 = np.insert(b2, -1, 0)

        A = np.sqrt(b1**2 + b2**2)

        self.main_modes = np.where(A > 0.1)[0]
        self.x = x
        self.b1 = b1
        self.b2 = b2
        self.n = n


    def update(self, x):
        pass


    def predict(self, numsteps):
        
        t = np.linspace(self.n, self.n+numsteps, numsteps)
        y = np.sum([b1[mode] * np.cos(t*2*np.pi*mode/n) 
            + b2[mode] * np.sin(t*2*np.pi*mode/n) for mode in main_modes], axis=0)
        
        return y


class DHR():

  def __init__(self):
    pass

  
