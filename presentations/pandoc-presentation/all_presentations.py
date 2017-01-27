"""
This script generates all possible presentations from {document}.pandoc

I looked into generating a Jupyter presentation from {doc}.pandoc, but no
luck. podoc and notedown didn't define custom slides.
"""
import os

filename = 'present.pandoc'  # .pandoc
formats = ['s5', 'slidy', 'slideous', 'dzslides', 'revealjs', 'beamer']

if False:
    os.system('notedown {0} > output/present.ipynb'.format(filename))
else:
    os.system('cd output; jupyter nbconvert --to slides present.ipynb')

for format_ in formats:
    filetype = 'pdf' if format_ == 'beamer' else 'html'
    args = '' if filetype == 'html' else '-H header.tex'
    command = ('pandoc -t {0} -s {3} {2} '
               '-o output/{0}.{1}'.format(format_, filetype, args, filename))

    print(command)
    os.system(command)
