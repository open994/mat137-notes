# Chapter 14 visualizations

Files live in `notes/ch14/figures/`.

## Inventory (quick placement)

| Figure file | Concept | Suggested section |
|---|---|---|
| `fig-motivating-example-interval.tex` | concrete interval/endpoints behavior | A Motivating Example |
| `fig-radius-of-convergence.tex` | convergence interval $(a-R,a+R)$ | Definition of Power Series |
| `fig-taylor-approx-exp.tex` | Taylor polynomials approximating $e^x$ | Taylor Polynomials / Computing Maclaurin Series |
| `fig-taylor-remainder-band.tex` | qualitative remainder/error growth | Analytic Functions and Remainders / Estimation via Taylor Polynomials |
| `fig-log-series.tex` | $\ln(1+x)$ vs truncations | The Logarithm Series |

## Figures

### 0) Motivating example: interval of convergence with endpoint behavior

- File: `figures/fig-motivating-example-interval.tex`
- Use near: A motivating example
- Caption idea: “Inside the radius $3$ the series converges absolutely; endpoints behave differently.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-motivating-example-interval.tex}
  \caption{A typical power-series convergence picture: absolute inside, case-by-case at endpoints.}
  \label{fig:motivating-example-interval}
\end{figure}
```

### 1) Radius of convergence on the number line

- File: `figures/fig-radius-of-convergence.tex`
- Use near: Definition of power series
- Caption idea: “Converges inside $(a-R,a+R)$ and diverges outside (endpoints are special).”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-radius-of-convergence.tex}
  \caption{Radius of convergence for a power series centered at $a$.}
  \label{fig:radius-of-convergence}
\end{figure}
```

### 2) Taylor polynomials approximating $e^x$

- File: `figures/fig-taylor-approx-exp.tex`
- Use near: Taylor polynomials / Maclaurin series
- Caption idea: “Higher-degree Taylor polynomials match more derivatives at the center.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-taylor-approx-exp.tex}
  \caption{Taylor polynomial approximations to $e^x$ near $0$.}
  \label{fig:taylor-approx-exp}
\end{figure}
```

### 3) Remainder intuition: approximation error grows away from center

- File: `figures/fig-taylor-remainder-band.tex`
- Use near: Analytic functions and remainders / estimation via Taylor polynomials
- Caption idea: “Error is small near the center, larger farther away.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-taylor-remainder-band.tex}
  \caption{A qualitative “error band” around a Taylor approximation.}
  \label{fig:taylor-remainder-band}
\end{figure}
```

### 4) Logarithm series: $\ln(1+x)$ near $0$

- File: `figures/fig-log-series.tex`
- Use near: The logarithm series
- Caption idea: “The Maclaurin series matches $\ln(1+x)$ well for $|x|<1$.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-log-series.tex}
  \caption{Approximating $\ln(1+x)$ by truncating its power series.}
  \label{fig:log-series}
\end{figure}
```
