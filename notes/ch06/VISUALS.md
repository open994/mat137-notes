# Chapter 06 visualizations

Files live in `notes/ch06/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) Related rates: shadow (similar triangles)

- File: `figures/fig-related-rates-shadow.tex`
- Use near: Related rates: shadow problem
- Caption idea: “Similar triangles relate rates of change.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-related-rates-shadow.tex}
  \caption{Shadow geometry for a classic related-rates setup.}
  \label{fig:related-rates-shadow}
\end{figure}
```

### 2) Optimization: cylinder with radius $r$ and height $h$

- File: `figures/fig-optimization-cylinder.tex`
- Use near: Optimization problems involving surface area/volume
- Caption idea: “Label variables before differentiating.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-optimization-cylinder.tex}
  \caption{A cylinder labeled with radius $r$ and height $h$.}
  \label{fig:optimization-cylinder}
\end{figure}
```

### 3) Asymptotes: vertical + slant (rational function)

- File: `figures/fig-vertical-and-slant-asymptotes.tex`
- Use near: Asymptotes / slant asymptotes
- Caption idea: “Rational functions can approach a line as $|x|\to\infty$.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-vertical-and-slant-asymptotes.tex}
  \caption{A rational function with a vertical asymptote and a slant asymptote.}
  \label{fig:vertical-and-slant-asymptotes}
\end{figure}
```
