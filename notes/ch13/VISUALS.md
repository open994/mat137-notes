# Chapter 13 visualizations

Files live in `notes/ch13/figures/`.

## Inventory (quick placement)

| Figure file | Concept | Suggested section |
|---|---|---|
| `fig-partial-sums-converge.tex` | partial sums $s_n$ approaching $S$ | Definition of Series / Tails of Series |
| `fig-geometric-series-area.tex` | geometric series as filling area | Geometric Series |
| `fig-divergence-test.tex` | terms not going to 0 | The Divergence Test |
| `fig-alternating-series-estimation.tex` | alternating sums + remainder bound | Alternating Series Estimation |

## Figures

### 1) Partial sums converge to the series value

- File: `figures/fig-partial-sums-converge.tex`
- Use near: Definition of series / tails of series
- Caption idea: “A series converges iff its partial sums converge.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-partial-sums-converge.tex}
  \caption{A convergent series’ partial sums approach a limit.}
  \label{fig:partial-sums-converge}
\end{figure}
```

### 2) Geometric series as shrinking areas

- File: `figures/fig-geometric-series-area.tex`
- Use near: Geometric series
- Caption idea: “Each term adds a fixed fraction of the remaining gap.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-geometric-series-area.tex}
  \caption{Geometric series visualized by filling a unit square.}
  \label{fig:geometric-series-area}
\end{figure}
```

### 3) Divergence test: terms not going to zero

- File: `figures/fig-divergence-test.tex`
- Use near: The divergence test
- Caption idea: “If $a_n\nrightarrow 0$, then $\sum a_n$ diverges.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-divergence-test.tex}
  \caption{A necessary condition for convergence: $a_n\to 0$.}
  \label{fig:divergence-test}
\end{figure}
```

### 4) Alternating series error bounded by first omitted term

- File: `figures/fig-alternating-series-estimation.tex`
- Use near: Alternating series estimation
- Caption idea: “Partial sums alternate around the limit; the error is small.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-alternating-series-estimation.tex}
  \caption{Alternating series estimation: the remainder is bounded by the next term.}
  \label{fig:alternating-series-estimation}
\end{figure}
```
