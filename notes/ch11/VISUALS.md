# Chapter 11 visualizations

Files live in `notes/ch11/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) Epsilon-neighborhood definition for sequence convergence

- File: `figures/fig-sequence-epsilon-neighborhood.tex`
- Use near: Limits of sequences (formal definition)
- Caption idea: “Eventually all terms lie inside the $\varepsilon$-neighborhood of $L$.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-sequence-epsilon-neighborhood.tex}
  \caption{Convergence of a sequence in an $\varepsilon$-neighborhood.}
  \label{fig:sequence-epsilon-neighborhood}
\end{figure}
```

### 2) Monotone bounded sequence converging to its supremum

- File: `figures/fig-monotone-bounded-convergence.tex`
- Use near: Monotonicity and boundedness / Monotone convergence theorem
- Caption idea: “Increasing + bounded above forces convergence.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-monotone-bounded-convergence.tex}
  \caption{A monotone increasing sequence bounded above converges.}
  \label{fig:monotone-bounded-convergence}
\end{figure}
```

### 3) Growth hierarchy: compare $n$, $n^2$, and $2^n$

- File: `figures/fig-growth-hierarchy.tex`
- Use near: The growth hierarchy
- Caption idea: “Eventually, exponentials dominate polynomials.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-growth-hierarchy.tex}
  \caption{Discrete comparison of common growth rates.}
  \label{fig:growth-hierarchy}
\end{figure}
```
