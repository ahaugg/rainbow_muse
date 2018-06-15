import muselsl, time

from muselsl.muse import Muse
from muselsl.stream import stream
from muselsl import view, record

from multiprocessing import Process


def print_stuff():
    print('hitting callback')



if __name__ == '__main__':
    MAC = '00:55:da:b0:4a:19'

    recording_path = 'E:/brains/andrew/rainbows/'

    aura_detector = Muse(MAC, callback_eeg=print_stuff)

    stream_process = Process(target=stream, args=(aura_detector,))
    stream_process.start()

    view()



