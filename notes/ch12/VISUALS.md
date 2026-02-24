# Chapter 12 visualizations

Files live in `notes/ch12/figures/`.

## Inventory (quick placement)

| Figure file | Concept | Suggested section |
|---|---|---|
| `fig-p-integral-comparison.tex` | $p$-integral threshold | The $p$-Integral |
| `fig-unbounded-integrand-integrable.tex` | endpoint blow-up but finite area | Unbounded Integrands |
| `fig-comparison-test-area.tex` | comparison/limit-comparison intuition | The Basic Comparison Test / The Limit-Comparison Test |

## Figures

### 1) The $p$-integral: convergence depends on $p$

- File: `figures/fig-p-integral-comparison.tex`
- Use near: The $p$-Integral
- Caption idea: “For $p>1$, the tail area is finite; for $p\le 1$ it diverges.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-p-integral-comparison.tex}
  \caption{The $p$-integral threshold at $p=1$.}
  \label{fig:p-integral-comparison}
\end{figure}
```

### 2) Unbounded integrand at an endpoint (integrable singularity)

- File: `figures/fig-unbounded-integrand-integrable.tex`
- Use near: Unbounded integrands
- Caption idea: “A function can blow up but still have finite area.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-unbounded-integrand-integrable.tex}
  \caption{An improper integral converging despite an endpoint blow-up.}
  \label{fig:unbounded-integrand-integrable}
\end{figure}
```

### 3) Comparison test picture ($0\le f\le g$)

- File: `figures/fig-comparison-test-area.tex`
- Use near: The basic comparison test / limit-comparison test
- Caption idea: “If the bigger tail area is finite, the smaller tail area is too.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-comparison-test-area.tex}
  \caption{Area comparison intuition for improper integrals.}
  \label{fig:comparison-test-area}
\end{figure}
```
