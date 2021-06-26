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

def get_magn_history(magn_resultant, decay = 0.0005):
    """This function simulates Magnetometer readings in the past"""
    history_magn = []
    for i in magn_resultant:
        arr = [i]
        for j in range(9):
            arr.append(arr[j] + arr[j]*decay)
        
        history_magn.append(np.flip(arr))
    return history_magn

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

    data = pd.read_csv('data01.csv')
    """imports the data from the csv using pandas library"""
    """Takes only the time, magnetometer X, Y, and Z readings from the dataset:"""
    time = data.iloc[:,1].values
    MagnX = data.iloc[:,10].values
    MagnY = data.iloc[:,11].values
    MagnZ = data.iloc[:,12].values
    plt.plot(np.arange(0,len(MagnX),1),MagnX,label='MagnX')
    plt.plot(np.arange(0,len(MagnX),1),MagnY,label='MagnY')
    plt.plot(np.arange(0,len(MagnX),1),MagnZ,label='MagnZ')
    """plots magnetometer X,Y, and Z readings"""
    plt.legend()
    plt.show()

    """calculates the resultant magnitude of the magnetic field"""
    Magn_resultant = get_resultant(MagnX,MagnY,MagnZ)
    """calculates the mean of magnetometer readings"""
    Magn_mean = get_mean(Magn_resultant)
    """calculates the standard deviation of magnetometer readings"""
    Magn_sd = get_sd(Magn_resultant)

    autocorr_magn = autocor(MagnX)#np.load("autocorrelation_magn.npy",allow_pickle=True) 
    import plot
    plot.plot_2d(np.arange(0,len(MagnX),1),'record number',[np.append(autocorr_magn,autocorr_magn[-1])],'Autocorrelation',[MagnX],"Magn")

    plt.plot(np.arange(0,len(MagnX),1),Magn_resultant,label='MagnResultant')
    plt.plot(np.arange(0,len(MagnX),1),[Magn_mean]*len(MagnX),label='Mean')
    plt.plot(np.arange(0,len(MagnX),1),[Magn_sd]*len(MagnX),label='Numpy Standard Deviation')
    """plots resultant magnetometer values, the mean, and the standard deviation"""
    plt.legend()
    plt.show()
    
    """ 

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('Magnetic Strength', color=color)
    ax1.plot(np.arange(0,len(MagnX),1), Magn_resultant, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Auto-correlation', color=color)  # we already handled the x-label with ax1
    ax2.plot(np.arange(0,len(MagnX),1), auto_correlation, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
    """
