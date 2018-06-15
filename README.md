# Rainbow muse

### `osc-monitor.py`
Reads an input OSC stream from e.g. a `Muse Monitor` mobile app to put out the eeg/accelerometer values. Requires `python-osc`, `phue` & `arrow` libraries.

#### Raw data that can be collected: EEG
The `osc-monitor.py` was run to collect ~ 60k EEG recordings. Data was saved in `collected_eeg_data.tsv` and subsequently plotted with `plot_histogram.R`. The resulting figure is in `histogram.png`

![](histogram.png)

#### Lighting up the Philips Hue
The connection to the Philips Hue is managed through `phue`. Each EEG reading is used to randomly set the color & brightness of the Hue lamp. 

[See an example on Twitter](https://twitter.com/gedankenstuecke/status/1007557614773813248).
