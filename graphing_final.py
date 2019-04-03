import datetime as dt
import time as t
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from pathlib import Path


def graphing_main(voltage):

    # Parameters
    x_len = 60         # Number of points to display
    yticks = np.arange(9,15,0.25)   # generate y axis
    ylim = [9,15]   # min max of y axis

    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = list(range(0, 60))
    ys = [0] * x_len
    ax.set_yticks(yticks)
    ax.set_ylim(ylim)

    # Create a blank line. We will update the line in animate
    line, = ax.plot(xs, ys)

    #format time
    def format_time(begin,str_len,s):
        t = dt.datetime.now()
        s = t.strftime('%Y-%m-%d %H{}%M{}%S.%f'.format(s,s))
        return s[begin:-(26-str_len)]

    # Add labels
    plt.title('Voltage over Time '+ format_time(0,13,':'))
    plt.xlabel('Seconds')
    plt.ylabel('Voltage (V)')

    # generate file names
    def gen_file_names():
        x_title = Path("C:/Users/Angus/Desktop/voltage logs/{} X.txt".format(format_time(0,13,'-')))
        y_title = Path("C:/Users/Angus/Desktop/voltage logs/{} Y.txt".format(format_time(0,13,'-')))
        return (x_title,y_title)

    # This function is called periodically from FuncAnimation
    def animate(i, ys):

        xt, yt = gen_file_names()

        # Add y to list
        ys.append(voltage.value)

        # Limit y list to set number of items
        ys = ys[-x_len:]

        # Update line with new Y values
        line.set_ydata(ys)

        with open(xt, "a") as X:
            X.write(format_time(11,13,':')+"\n")
        with open(yt, "a") as Y:
            Y.write(str(voltage.value)+"\n")

        return line,

    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig,
        animate,
        fargs=(ys,),
        interval=60000,
        blit=True)

    plt.show()    
