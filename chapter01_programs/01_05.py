# dispersion_plot : plot the position of specific words in the passage

from nltk.book import *
import matplotlib.pyplot as plt
#import numpy

print(f'\nPlot the positions of words in text4')

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

plt.show()
