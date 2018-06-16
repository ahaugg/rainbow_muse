from muselsl.stream import list_muses
import sys
from muselsl.muse import Muse
import time
import numpy as np
import os
from matplotlib import pyplot as plt

bell = 0
total_std_list = []
count = 0
def _start(address,threshold, duration):
    def save_eeg(new_samples, new_timestamps):
        channel_std = []
        global bell
        global total_std_list
        global count
        # eeg_samples.append(new_samples)
        # timestamps.append(new_timestamps)
        # print(new_samples.shape)
        for channel in range(new_samples.shape[0] - 1):
            channel_data = np.array(new_samples[channel,:])
            # print(channel_data)
            channel_std.append(np.std(channel_data))
        total_std = int(np.array(channel_std).sum())
        print('Count:',count)
        print(total_std)
        count +=1
        total_std_list.append(total_std)
        if total_std > threshold and not total_std == 0 :
            os.system("/usr/bin/canberra-gtk-play --id='bell'")
            bell += 1





    muse = Muse(address, save_eeg)
    muse.connect()
    muse.start()

    t_init = time.time()
    print('Start recording at time t=%.3f' % t_init)

    while (time.time() - t_init) < duration:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break

    muse.stop()
    muse.disconnect()



my_muse_name = sys.argv[1]
threshold = int(sys.argv[2])
duration = int(sys.argv[3])
my_muse_address = None
print('Finding Muse: ', my_muse_name)

muses_list = list_muses()

found = False

'''
Returns a  dictionary of type
[{'address': '00:55:DA:B0:4A:19', 'name': 'Muse-4A19'}]

'''

for muse in muses_list:
    if not found:
        for key, value in muse.items():
            print('In Loop Dictionary: %s, %s'%(key, value))

            if key == 'name' and value == my_muse_name:
                my_muse_name = value
                found =  True

            if key == 'address' and found == True:
                my_muse_address = value
                # found == True
                break


if found == True:
    print('Dictionary: %s, %s'%(my_muse_name, my_muse_address))
    # stream(my_muse_address)
    print('Starting stream')
    _start(my_muse_address,threshold,duration)


    # Note: Streaming is synchronous, so code here will not execute until the stream has been closed
    print('Stream has ended')
    print('Final Peace Score: ',(count - bell))
    # plt.plot(total_std_list)
    # plt.show()

else:
    print('Sorry Unable to find muse: %s'%my_muse_name)
