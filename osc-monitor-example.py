import argparse
from pythonosc import dispatcher
from pythonosc import osc_server
from matplotlib import pyplot as plt
import numpy as np
from phue import Bridge
import time
import random


def delta_handler(endpoint, args, ch1, ch2, ch3, ch4):
    print(endpoint)
    print(ch1)
    global x_counter
    plt.scatter(x_counter, ch1)
    plt.pause(0.05)
    x_counter += 1
    #h2.set_ydata(ch2)
    #redraw_figure()
    #h3.set_ydata(ch3)
    #redraw_figure()
    #h4.set_ydata(ch4)
    #redraw_figure()


def clench_detect(endpoint, value):
    if value == 1:
        print('clenched')
        lights = b.get_light_objects()
        for light in lights:
            if light.on:
                light.xy = [random.random(), random.random()]


def blink_detect(endpoint, value):
    if value == 1:
        print('blinked')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")
    parser.add_argument("--bridge",
                        default='192.168.0.23',
                        help="The Philipps bridge IP")

    args = parser.parse_args()
    try:
        b = Bridge(args.bridge)
    except:
        pass

    dispatcher = dispatcher.Dispatcher()
    # the one below gives you all the endpoints!
    #dispatcher.map("/*", print)
    dispatcher.map("/muse/elements/blink", blink_detect)
    dispatcher.map("/muse/elements/jaw_clench", clench_detect)

    t_start = time.time()
    x_counter = 1

    #dispatcher.map('/muse/elements/delta_absolute', delta_handler, 'foo')
    dispatcher.map('/muse/eeg', delta_handler, 'foo')

    server = osc_server.BlockingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
