# Chapter 04 visualizations

Files live in `notes/ch04/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) Inverse function reflection about $y=x$

- File: `figures/fig-inverse-reflection.tex`
- Use near: Inverse functions / inverse examples
- Caption idea: “Graphs of inverse functions are reflections across $y=x$.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-inverse-reflection.tex}
  \caption{A function and its inverse reflect across $y=x$.}
  \label{fig:inverse-reflection}
\end{figure}
```

### 2) Exponential vs logarithm

- File: `figures/fig-exp-log.tex`
- Use near: Derivative of exponential/logarithm
- Caption idea: “$\ln(x)$ is the inverse of $e^x$; both are monotone.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-exp-log.tex}
  \caption{The graphs of $e^x$ and $\ln x$.}
  \label{fig:exp-log}
\end{figure}
```

### 3) Restricting $\sin$ to get $\arcsin$

- File: `figures/fig-arcsin-restriction.tex`
- Use near: Arcsine / derivative of arcsine
- Caption idea: “Restrict $\sin$ to $[-\pi/2,\pi/2]$ to make it invertible.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-arcsin-restriction.tex}
  \caption{The restricted sine and its inverse $\arcsin$.}
  \label{fig:arcsin-restriction}
\end{figure}
```
