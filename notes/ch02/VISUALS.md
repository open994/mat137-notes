# Chapter 02 visualizations

Files live in `notes/ch02/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) Epsilon–delta picture for a limit

- File: `figures/fig-eps-delta-band.tex`
- Use near: Formal definition of limit / proving limits from the definition
- Caption idea: “A $\delta$-window in $x$ forces an $\varepsilon$-band in $y$.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-eps-delta-band.tex}
  \caption{An $\varepsilon$-band around $L$ and a $\delta$-window around $a$.}
  \label{fig:eps-delta-band}
\end{figure}
```

### 2) One-sided limits + jump discontinuity

- File: `figures/fig-one-sided-jump.tex`
- Use near: One-sided limits / types of discontinuity
- Caption idea: “Left-hand and right-hand behaviors can disagree.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-one-sided-jump.tex}
  \caption{A jump discontinuity with distinct one-sided limits.}
  \label{fig:one-sided-jump}
\end{figure}
```

### 3) Squeeze theorem picture

- File: `figures/fig-squeeze-theorem.tex`
- Use near: Squeeze theorem
- Caption idea: “If $g\le f\le h$ and $g,h\to L$, then $f\to L$.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-squeeze-theorem.tex}
  \caption{A function trapped between two functions with the same limit.}
  \label{fig:squeeze-theorem}
\end{figure}
```

### 4) Geometric plot for $\lim_{x\to 0} \sin x / x$

- File: `figures/fig-sinx-over-x.tex`
- Use near: The limit of $\sin(x)/x$
- Caption idea: “Near $0$, the ratio stays close to $1$.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-sinx-over-x.tex}
  \caption{The graph of $\sin(x)/x$ near $0$.}
  \label{fig:sinx-over-x}
\end{figure}
```
