# Chapter 09 visualizations

Files live in `notes/ch09/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) Substitution rule: interval mapping $x\mapsto u=g(x)$

- File: `figures/fig-substitution-interval-map.tex`
- Use near: Substitution rule / substitution for definite integrals
- Caption idea: “Changing variables maps an $x$-interval to a $u$-interval.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-substitution-interval-map.tex}
  \caption{Substitution as an interval mapping.}
  \label{fig:substitution-interval-map}
\end{figure}
```

### 2) Integration by parts: geometric/product-rule intuition

- File: `figures/fig-by-parts-rectangle.tex`
- Use near: Integration by parts statement
- Caption idea: “A rectangle’s area change splits into two strips.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-by-parts-rectangle.tex}
  \caption{A geometric intuition behind the product rule and integration by parts.}
  \label{fig:by-parts-rectangle}
\end{figure}
```

### 3) Partial fractions: one rational function as a sum of simpler ones

- File: `figures/fig-partial-fractions-decomposition.tex`
- Use near: Partial fractions (distinct factors / repeated factors)
- Caption idea: “Decomposition turns a complex integrand into easy pieces.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-partial-fractions-decomposition.tex}
  \caption{A rational function and its partial fraction pieces (qualitative shape).}
  \label{fig:partial-fractions-decomposition}
\end{figure}
```
