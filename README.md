# Rainbow muse and Sound and Peace

## Sound and peace

Using the MUSE EEG headset, control:

* Beep sound of the laptop  
  - This can be used as a game to find out how peaceful can one sit. As the person moves his facial muscles while blinking or talking it is translated to large fluctuations in the
captured signals which in turn plays the beep sound. The lesser the number of beeps, the peaceful the subject was during the game.     

## Rainbow Muse

* Philips Hue LED Light (Also done in a different way in next section)  
  - Similarly, instead of beep sound, light can be controlled. In this project we used Philips Hue LED Light that was connected to a bridge which connected it to a WiFi. The Signal from EEG was captured from Muse headset that was connected to the laptop via WiFi. The laptop processes the signals and in turn send the signal to the bridge to control the intensity and colour of the LED light.  

Usage:

sudo python3 sound_and_peace.py <MUSE_NAME> <THRESHOLD> <DURATION> <SOUND_FLAG> <LIGHT_FLAG>

Parameters:  
MUSE_NAME: Unique identifier of the Muse Headset printer on it.  
DURATION:  Time (seconds) for which the Muse Headset whould record the brain signals.  
THRESHOLD: Puts a threshold on sum of standard deviations of the first 4 channels.  
 When this threshold is crossed, it results in the beep sound or light intensiy change.  
SOUND_FLAG: True if user wants to play the sound  
LIGHT_FLAG: True if user wants to change light's intensity  

eg.
sudo python3 sound_and_peace.py Muse-7039 80 60 True False

Note:
Duration is in seconds and Threshold is on the sum of standard deviations of the first 4 channels


----------------------------------------------------------------------------------------------------

## Using the `Muse Monitor` mobile app

### `osc-monitor.py`
Reads an input OSC stream from e.g. a `Muse Monitor` mobile app to put out the eeg/accelerometer values. Requires `python-osc`, `phue` & `arrow` libraries.

#### Raw data that can be collected: EEG
The `osc-monitor.py` was run to collect ~ 60k EEG recordings. Data was saved in `collected_eeg_data.tsv` and subsequently plotted with `plot_histogram.R`. The resulting figure is in `histogram.png`

![](histogram.png)

#### Lighting up the Philips Hue
The connection to the Philips Hue is managed through `phue`. Each EEG reading is used to randomly set the color & brightness of the Hue lamp.

[See an example on Twitter](https://twitter.com/gedankenstuecke/status/1007557614773813248).
