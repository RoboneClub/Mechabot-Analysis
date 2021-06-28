import matplotlib.pyplot as plt


def plot_2d(x_axis,x_label,arr1,arr1_label,arr2,arr2_label,title=[""]*20):
    for m in range(len(arr1)):

        fig, ax1 = plt.subplots()

        color = 'tab:red'
        ax1.set_xlabel(x_label,size=15)
        ax1.set_ylabel(arr1_label, color=color,size = 15)
        ax1.plot(x_axis, arr1[m], color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

        color = 'tab:blue'
        ax2.set_ylabel(arr2_label, color=color,size=15)  # we already handled the x-label with ax1
        ax2.plot(x_axis, arr2[m], color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        plt.title(title[m],size=15,color='green')
        plt.show()
