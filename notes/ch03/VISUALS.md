# Chapter 03 visualizations

Files live in `notes/ch03/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) Secants approaching the tangent (derivative definition)

- File: `figures/fig-secant-to-tangent.tex`
- Use near: Definition of the derivative
- Caption idea: “As $h\to 0$, the secant slope approaches the tangent slope.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-secant-to-tangent.tex}
  \caption{Secant lines converging to the tangent line.}
  \label{fig:secant-to-tangent}
\end{figure}
```

### 2) A continuous but non-differentiable function ($|x|$ at $0$)

- File: `figures/fig-cusp-abs.tex`
- Use near: Non-differentiable functions / differentiability vs continuity
- Caption idea: “The corner prevents a unique tangent slope.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-cusp-abs.tex}
  \caption{A corner: continuous but not differentiable at the cusp.}
  \label{fig:cusp-abs}
\end{figure}
```

### 3) Derivative as instantaneous rate of change

- File: `figures/fig-rate-of-change.tex`
- Use near: Derivative as rate of change
- Caption idea: “Tangent slope is instantaneous velocity on a position–time graph.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-rate-of-change.tex}
  \caption{Slope of the tangent as instantaneous rate of change.}
  \label{fig:rate-of-change}
\end{figure}
```
