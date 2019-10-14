\abstract{
    This is an abstract
}

# Introduction

Modern machine has seen outstanding success recently.[^footnote] ...

[^footnote]:Footnote

Citation to \cite{cer2018}

\vspace{1em}

![](figs/img.png)

Here's a code example, really:

\begin{minted}{python}
import numpy as np

def relu(x):
    return np.maximum(x, 0)

x = np.linspace(-1, 1)
y = relu(x)
print(y.min(), y.max())  # 0.0, 1.0
\end{minted}
