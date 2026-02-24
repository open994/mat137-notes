# Chapter 07 visualizations

Files live in `notes/ch07/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) Riemann sum rectangles approximating area

- File: `figures/fig-riemann-rectangles.tex`
- Use near: Integrals as limits / Riemann sums
- Caption idea: “Rectangles approximate area; refining the partition improves accuracy.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-riemann-rectangles.tex}
  \caption{A right-endpoint Riemann sum approximation.}
  \label{fig:riemann-rectangles}
\end{figure}
```

### 2) Upper vs lower Darboux sums (same partition)

- File: `figures/fig-darboux-upper-lower.tex`
- Use near: Darboux integral / properties of Darboux sums
- Caption idea: “Lower sums increase; upper sums decrease as partitions refine.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-darboux-upper-lower.tex}
  \caption{Upper and lower sums on a fixed partition.}
  \label{fig:darboux-upper-lower}
\end{figure}
```

### 3) Visual intuition for a non-integrable “dense oscillation”

- File: `figures/fig-nonintegrable-dense-oscillation.tex`
- Use near: A non-integrable function
- Caption idea: “If oscillation persists at every scale, upper and lower sums may never meet.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-nonintegrable-dense-oscillation.tex}
  \caption{Dense oscillation intuition: upper sums stay high while lower sums stay low.}
  \label{fig:nonintegrable-dense-oscillation}
\end{figure}
```
