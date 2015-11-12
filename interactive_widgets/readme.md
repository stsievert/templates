
Interative widgets in an Jupyter Notebook is pretty easy: good clear
documentation now exists.

However, Jupyter notebook widgets do not yet have the feature that they are
static *and* interactive. This means that they are self contained and can be
published in blog posts/etc.

For this functionality, I use the library [ipywidgets-unsupported] as IPython
does not yet support *static interactive* widgets. Related:
[ipython/ipythonwidgets issue #16]

The file `update_numbers.html` contains example code to have two sliders that
when a slider is moved, some MathJax text is updated. Adapt as you wish! Also,
note that this code is at the bottom of the script.

[ipython/ipythonwidgets issue #16]:https://github.com/ipython/ipywidgets/issues/16
