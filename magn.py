import numpy as np
import pandas as pd



def get_resultant(X,Y,Z):
    resultant = []
    for i in range(len(X)):
        resultant.append((X[i]**2 + Y[i]**2 + Z[i] **2)**0.5)
    return resultant

def get_mean(arr):
    return np.mean(arr)

def get_sd(arr):
    return np.std(arr)


def autocorr(x):
    result = np.correlate(x, x, mode='full')
    index = int(len(result)/2)
    return result[index:]

def get_magn_history(magn_resultant, decay = 0.0005):
    history_magn = []
    for i in magn_resultant:
        arr = [i]
        for j in range(9):
            arr.append(arr[j] + arr[j]*decay)
        
        history_magn.append(np.flip(arr))
    return history_magn


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    data = pd.read_csv('data01.csv')
    time = data.iloc[:,1].values
    MagnX = data.iloc[:,10].values
    MagnY = data.iloc[:,11].values
    MagnZ = data.iloc[:,12].values
    plt.plot(np.arange(0,len(MagnX),1),MagnX,label='MagnX')
    plt.plot(np.arange(0,len(MagnX),1),MagnY,label='MagnY')
    plt.plot(np.arange(0,len(MagnX),1),MagnZ,label='MagnZ')
    plt.legend()
    plt.show()

    Magn_resultant = get_resultant(MagnX,MagnY,MagnZ)
    Magn_mean = get_mean(Magn_resultant)
    Magn_sd = get_sd(Magn_resultant)

    plt.plot(np.arange(0,len(MagnX),1),Magn_resultant,label='MagnResultant')
    plt.plot(np.arange(0,len(MagnX),1),[Magn_mean]*len(MagnX),label='Mean')
    plt.plot(np.arange(0,len(MagnX),1),[Magn_sd]*len(MagnX),label='Numpy Standard Deviation')
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
