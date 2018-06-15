library(ggplot2)
library(tidyverse)

# read data
df <- read.csv('collected_eeg_data.tsv',sep='\t',head=F)

# make long and turn values into numbers
dfl <- gather(df, electrode, measurement, V2:V6)
dfl$measurement <- as.numeric(dfl$measurement)

# plot
ggplot(dfl,aes(dfl$measurement)) + geom_histogram(binwidth=10) + facet_grid(electrode~.) + theme_minimal() + scale_x_continuous('value')
ggsave('histogram.png')
