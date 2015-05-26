from __future__ import division
from pylab import *
from scipy.misc import imsave


def convert_blue_to_bw(x):
    # red plane
    i = argwhere((x[:,:,0] > 0.3) & (x[:,:,0] < 0.7))
    x[i[:,0], i[:,1], 0:3] = 0.0

    # blue plane
    i = argwhere((x[:,:,2] > 0.3) & (x[:,:,2] < 0.7))
    x[i[:,0], i[:,1], 0:3] = 1.0
    return x
def strip_axes(x):
    x[:, 0:90, :] = 1
    x[-70:, :, :] = 1
    x[:90, :, :] = 1
    return x

names = [
        'results/thermal/2014-09-09thermal_sampleAt.png',
        'results/edge/2014-09-09edge_sampleAt.png',
]

for filename in names:
    x = imread(filename)
    if 'thermal' in filename: savePrefix = 'thermal'
    if 'square' in filename: savePrefix = 'square'
    if 'circle' in filename: savePrefix = 'circle'
    if 'edge' in filename: savePrefix = 'edge'

    if 'sampleAt' in filename:
        x = convert_blue_to_bw(x)
        imageType = 'sampleAt'
    x = strip_axes(x)
    W = 2
    x[0:W, :, 0:3] = 0
    x[:, 0:W, 0:3] = 0
    x[-W:, :, 0:3] = 0
    x[:, -W:, 0:3] = 0
    print savePrefix + '_' + imageType
    imsave('python_scripting/'+savePrefix + '_' + imageType + '.png', x)

    figure()
    imshow(x)
    show()

