![alt text][logo]

[logo]: logo-small.jpg

About
------

Tracktor is an OpenCV based object tracking software. The software is able to perform single-object tracking in 
noisy environments or multi-object tracking in clear environments. In addition to tracking multiple objects
simultaneously, tracktor is also able to maintain individual identities. I have provided three example notebooks
to help the user track objects in videos. Each example is provided because it shows how tracktor is able to solve
various tracking related problems while maintaining individual identities.

#### Example 1: Fish Track
This example shows how tracktor is able to track objects in noisy environments. The video shows tracking of a fish
alone in a tank. A falcon tube is dropped in the tank creating ripples and bubbles in the water. Tracktor is able
to track the focal fish despite these disturbances.

#### Example 2: Spider Track
This example depicts multiple object tracking where objects to be tracked vary considerably in size. The female
spider is about an order of magnitude (10x) larger than the male spider. In addition to tracking vastly differently
sized objects simultaneously, this example also shows how individual identity is maintained despite disturbances. At
00:01:00 into the video, a human enters the frame to examine the web. Despite numerous contours satisfying the tracking
conditions (seen in the tracked video as contours), tracktor is able to continue tracking focal spiders while
successfully maintaining their identities.

#### Example 3: Termite Track
This example consists of eight termits moving in a petridish. Tracktor is successfully able to track all eight termits
while maintaining individual identities. In addition to tracking and identifying numerous objects, tracktor is also 
shown to maintain identity when termites touch each other (during trophallaxis).

Installation
------------
Tracktor works on all operating systems (Windows, Linux and Mac). 
[Pip](https://pip.pypa.io/en/stable/) can be used to install all packages except [OpenCV](http://opencv.org/). OpenCV needs to be installed separately. For Mac users, try using [Homebrew](https://brew.sh/) for OpenCV. 

#### Dependencies

- [Python 2.7+](http://www.python.org)

- [numpy](http://www.numpy.org/)

- [pandas](https://pandas.pydata.org/)

- [scipy](http://www.scipy.org/)

- [scikit-learn](http://scikit-learn.org/stable/)

- [OpenCV 3.1+](http://opencv.org/)

- [jupyter](http://jupyter.org/)*

*Jupyter notebook is optional. However, I highly recommend it for interactive coding. All example notebooks are written here. 

Once installed, place tracktor.py in the same folder as your tracking notebook. Use python to run tracking. Examples are provided in jupyter notebooks.

Cite
----

If you use Tracktor, please cite it using this zenodo DOI:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1134016.svg)](https://doi.org/10.5281/zenodo.1134016)


Thank You for using and citing Tracktor!
