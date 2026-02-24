# Chapter 01 visualizations

Files live in `notes/ch01/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) Venn diagram: union vs intersection

- File: `figures/fig-venn-union-intersection.tex`
- Use near: Set union/intersection definitions
- Caption idea: “Union collects elements in either set; intersection collects elements in both.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-venn-union-intersection.tex}
  \caption{Union and intersection.}
  \label{fig:venn-union-intersection}
\end{figure}
```

### 2) Interval endpoints: open vs closed

- File: `figures/fig-interval-open-closed.tex`
- Use near: Interval notation
- Caption idea: “Filled dots mean endpoints included; hollow dots mean excluded.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-interval-open-closed.tex}
  \caption{Open/closed endpoints on a number line.}
  \label{fig:interval-open-closed}
\end{figure}
```

### 3) Quantifier dependence: “for all x, there exists y(x)”

- File: `figures/fig-quantifier-dependence.tex`
- Use near: Order of multiple quantifiers
- Caption idea: “The existential choice may depend on the universal variable.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-quantifier-dependence.tex}
  \caption{Quantifier order encodes dependence.}
  \label{fig:quantifier-dependence}
\end{figure}
```
