# Chapter 05 visualizations

Files live in `notes/ch05/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) Rolle’s theorem geometry

- File: `figures/fig-rolles-theorem.tex`
- Use near: Rolle's theorem
- Caption idea: “Same endpoints implies a horizontal tangent somewhere in between.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-rolles-theorem.tex}
  \caption{Rolle’s theorem: a horizontal tangent in the interior.}
  \label{fig:rolles-theorem}
\end{figure}
```

### 2) Mean Value Theorem geometry

- File: `figures/fig-mean-value-theorem.tex`
- Use near: Mean value theorem statement/motivation
- Caption idea: “A secant slope is attained by a tangent slope.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-mean-value-theorem.tex}
  \caption{Mean Value Theorem: a tangent parallel to the secant.}
  \label{fig:mean-value-theorem}
\end{figure}
```

### 3) Critical points and local extrema

- File: `figures/fig-critical-points.tex`
- Use near: Local extrema and critical points
- Caption idea: “Local maxima/minima occur at critical points (with caveats).”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-critical-points.tex}
  \caption{A smooth function with critical points at a local max and min.}
  \label{fig:critical-points}
\end{figure}
```
