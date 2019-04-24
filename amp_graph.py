import datetime as dt
import time as t
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from pathlib import Path

def amp_main(amp):

    # amperage graph parameters
    x_len = 60         # Number of points to display
    yticks = np.arange(0,15,0.5)   # generate y axis
    ylim = [0,15]   # min max of y axis
    start = t.time()

    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = list(range(0, 60))
    ys = [0] * x_len
    ax.set_yticks(yticks)
    ax.set_ylim(ylim)

    # Create a blank line. We will update the line in animate
    line, = ax.plot(xs, ys)

    # Add labels
    plt.title('Amperage over Time')
    plt.xlabel('Seconds')
    plt.ylabel('Amps (A)')

    # This function is called periodically from FuncAnimation
    def animate(i, ys, start):

        # Add y to list
        ys.append(amp.value)

        # Limit y list to set number of items
        ys = ys[-x_len:]

        # Update line with new Y values
        line.set_ydata(ys)

        return line,

    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig,
        animate,
        fargs=(ys,start),
        interval=1000,
        blit=True)

    plt.show()    
