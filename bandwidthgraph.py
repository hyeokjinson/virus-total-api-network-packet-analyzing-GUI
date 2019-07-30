import psutil
import platform
import datetime
import time
import uuid
import threading
import tkinter as tk
from tkinter import *
import socket
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
bandwidth = 0
matplotlib.use('TkAgg')
style.use('ggplot')
LARGE_FONT = ('Verdana', 12)
print(hex(uuid.getnode()))   # printing the value of unique MAC address using uuid and getnode() function
                             #hex converts integer value to hexadecimal
total = 0      # global variables
sent = 0
received = 0
                              # set x coordinates for time(seconds).
x = [-60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39,
     -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17,
     -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
                              # set y coordinates for badnwidth(mb)
y1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

f = Figure(figsize=(6, 5), dpi=120)
a = f.add_subplot(211)
a.plot(x, y1)
b = f.add_subplot(212)
b.plot(x, y2)

def animate(i):
   # print(y)
   y1.pop(0)
   y2.pop(0)
   y1.append(sent)
   y2.append(received)
   a.clear()
   a.plot(x, y1)
   b.clear()                           # Take away this line and run the program to see some cool art.
   b.plot(x, y2)
   b.set_xlabel('Time(s)')
   



                                                # we used os module to extract systen name function, in specfic HOSTNAME


                                                    #we used entryText.set to string variable from function into textbox

def monitor():
    old_value = 0
    sen_value = 0
    rec_value = 0
    while True:
        b_received = psutil.net_io_counters().bytes_recv
        b_sent = psutil.net_io_counters().bytes_sent
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value

        if sen_value:
            plot_y1 = b_sent - sen_value
            plot_y2 = b_received - rec_value

            plots(plot_y1, plot_y2)
        sen_value = b_sent
        rec_value = b_received

        time.sleep(1)
                                                        #time.sleep(1) pauses the program for the number of seconds set

thread1 = threading.Thread(target=monitor)


def convert_to_gbit(value):
    return value / 1024. / 1024. * 8


def send_stat(value):
    global total
    global bandwidth
    print("%0.3f" % convert_to_gbit(value))
    bandwidth = convert_to_gbit(value)
    total += bandwidth
    totalText.set('Total Bandwidth Used: ' + '%0.3f mb' % total)


def plots(sen, rec):
    global sent
    global received
    sent = convert_to_gbit(sen)
    received = convert_to_gbit(rec)


window = Tk()                       # BELOW IS THE GUI
T1 = tk.Text()
window.geometry("500x300")
window.title("Bandwidth Monitor")

graph_frame = Frame(window)
graph_frame.grid(row=0, column=0, rowspan=2)

canvas = FigureCanvasTkAgg(f, graph_frame)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0)
graph_label = tk.Label(graph_frame, text='Upload and Download mb/s', font=LARGE_FONT)
graph_label.grid(row=0, column=0, rowspan=1)

button_frame = Frame(window)
button_frame.grid(row=0, column=1)


button8 = tk.Button(button_frame, relief=GROOVE, text='Running', fg='green', width=14, command=thread1.start())
button8.grid(row=4, columnspan=2)

entryText = StringVar(window)             # Variables set for the text_boxes
totalText = StringVar(window)             #

total_textbox = Entry(button_frame, textvariable=totalText, state='readonly', width=100)
total_textbox.grid(row=5, column=0, columnspan=2)

display_textbox = Entry(button_frame, textvariable=entryText, state='readonly', width=100)
display_textbox.grid(row=6, column=0, columnspan=2)

ani = animation.FuncAnimation(f, animate, interval=1000)
window.mainloop()