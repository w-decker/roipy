# roipy

Plotting brain regions of interest (ROI) for demonstration purposes in Python

## Description

Have you ever wanted to plot a region of the brain to include in a talk or presentation? What about in a lecture? Some might arbitrarily highlight the area of the cortex in which they _think_ a particular region might fall. Others might scour the internet for images. Well...you won't need to do that any more. With `roipy`, you can plot exact regions of the brain using the [**Destrieux Atlas**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2937159/).

## Installation

This package is hosted on [PyPi](https://pypi.org/project/roipy/). You may use `pip` to install.

```bash
pip install roipy
```

## Usage

There are three types of brain plots included in `roipy`. A "univariate" plot, a "multivariate" plot and a "whole brain multivariate" plot. There are two methods for generating each plot:

1. Using the domain general class, `roipy.plotting.Plot()`
2. Executing each individual plotting method via its own specific function (e.g., `roipy.utils.plot_multivariate()`)

Below is an example of each methods implementation.

```python
# import
from roipy.plotting import Plot
from roipy.utils import plot_multivariate

# Domain general Plot()
P = Plot()
P.plot_multivariate(roi=[1,3,5,34], cmap='viridis')

#Individual function
plot_multivariate(roi=[1,3,5,34], shape='pial', view='lateral', hemi='left', cmap='viridis')

# Save the plot
import matplotlib.pyplot as plt
plt.savefig('brain.png')

```

The parameter `roi` is given a list of integers which correspond to the Destrieux surface atlas. 

You can also animate the plots with `roipy.animation.Anim()`. 

```python
# import
from roipy.animation import Anim
from roipy.plotting import Plot

# Plot() instance
P = Plot()

# Anim() instance
A = Anim()
a.animate(lambda frame: P.plot_multivariate(roi=[1,3,5,34], cmap='viridis'), fname='brain.gif', save=True)
```
>Admittedly, this is more complex as it requires use of the `lambda` function in Python. But, using `roipy.plotting.utils.plot_univariate`, you can devise your own animation style.

## Example brain

![brain](/brain.png)




