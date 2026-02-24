# Chapter 08 visualizations

Files live in `notes/ch08/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) The accumulation (area) function $A(x)=\int_a^x f(t)\,dt$

- File: `figures/fig-accumulation-function.tex`
- Use near: Functions defined by integrals / FTC Part One statement
- Caption idea: “Accumulated area changes at a rate equal to the integrand.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-accumulation-function.tex}
  \caption{Accumulated area from $a$ to $x$ under $f$.}
  \label{fig:accumulation-function}
\end{figure}
```

### 2) FTC as a “derivative–integral” inverse relationship (diagram)

- File: `figures/fig-ftc-commutative-diagram.tex`
- Use near: Summary and comparison
- Caption idea: “Differentiation and integration are inverse operations (under hypotheses).”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-ftc-commutative-diagram.tex}
  \caption{How FTC links accumulation and rates of change.}
  \label{fig:ftc-commutative-diagram}
\end{figure}
```

### 3) FTC Part Two intuition: net change equals signed area

- File: `figures/fig-net-change-signed-area.tex`
- Use near: FTC Part Two statement
- Caption idea: “Positive area adds; negative area subtracts.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-net-change-signed-area.tex}
  \caption{Net change as signed area under a rate function.}
  \label{fig:net-change-signed-area}
\end{figure}
```
