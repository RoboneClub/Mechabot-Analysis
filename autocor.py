from matplotlib.pyplot import get
import numpy as np
import pandas as pd

def get_resultant(X,Y,Z):
    """This function gets the resultant magnitudes of three arrays of vector quantities: X, Y, and Z."""
    resultant = []
    for i in range(len(X)):
        resultant.append((X[i]**2 + Y[i]**2 + Z[i] **2)**0.5)
    return resultant

def get_mean(arr):
    """This function uses numpy's mean funtion to calculate the mean of values in an array"""
    return np.mean(arr)

def get_sd(arr):
    """This function uses numpy's std funtion to calculate the standard deviation of values in an array"""
    return np.std(arr)

def sumnomeq(y,k):
    """This function calculates the sum of all iterations of the nominaor in the autocorrelation formula"""
    nomeq = []
    end = len(y) - k
    mean = get_mean(y)
    for i in range(0,end):
        nomeq.append((y[i] - mean) * ( y[i + k] - mean))
    return np.sum(nomeq)
def sumdenomeq(y):
    """This function calculates the sum of all iterations of the denominaor in the autocorrelation formula"""
    denomeq = []
    mean = get_mean(y)
    end = len(y) - 1
    for i in range(0,end):
        denomeq.append((y[i] - mean)**2)
    return np.sum(denomeq)
def autocor(y):
    """Autocorrelation of array y"""
    autocorarr = []
    counter = 0
    denom = sumdenomeq(y)
    for i in range (len(y)-1):
        autocorarr.append((sumnomeq(y,i)/denom))
        counter += 1
        print(f"Progress: {counter*100/len(y)}%")
    return autocorarr

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    """imports the data from the csv using pandas library"""
    data = pd.read_csv('data01.csv')
    """Takes only the time, magnetometer X, Y, and Z readings from the dataset:"""
    time = data.iloc[:,1].values
    MagnX = data.iloc[:,10].values
    MagnY = data.iloc[:,11].values
    MagnZ = data.iloc[:,12].values
    """sets Magn_resultant array to the resultant values of Magnetometer readings"""
    Magn_resultant = get_resultant(MagnX,MagnY,MagnZ)
    """Finds the mean of resultant Magnetometer readings"""
    Magn_mean = get_mean(Magn_resultant)
    """Finds the standard deviation of resultant Magnetometer readings"""
    Magn_sd = get_sd(Magn_resultant)

    autocorr_magn = autocor(MagnX)#np.load("autocorrelation_magn.npy",allow_pickle=True) 
    import plot
    plot.plot_2d(np.arange(0,len(MagnX),1),'record number',[np.append(autocorr_magn,autocorr_magn[-1])],'Autocorrelation',[MagnX],"Magn")

    plt.plot(np.arange(0,len(MagnX),1),Magn_resultant,label='MagnResultant')
    plt.plot(np.arange(0,len(MagnX),1),[Magn_mean]*len(MagnX),label='Mean')
    plt.plot(np.arange(0,len(MagnX),1),[Magn_sd]*len(MagnX),label='Numpy Standard Deviation')
    plt.plot(np.arange(0,len(MagnX),1),autocorr_magn+[autocorr_magn[-1]],label='Autocorrelation')
   
    """plots resultant magnetometer values, the mean, and the standard deviation"""
    plt.legend()
    plt.show()
