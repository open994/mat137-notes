# Chapter 10 visualizations

Files live in `notes/ch10/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Figures

### 1) Volumes by slicing (disk method intuition)

- File: `figures/fig-disk-method-slice.tex`
- Use near: Volumes by slicing
- Caption idea: “A vertical slice rotates into a disk.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-disk-method-slice.tex}
  \caption{Disk method intuition: a slice rotates into a disk.}
  \label{fig:disk-method-slice}
\end{figure}
```

### 2) Volumes by slicing (washer method intuition)

- File: `figures/fig-washer-method-slice.tex`
- Use near: Volumes by slicing (regions between curves)
- Caption idea: “A slice rotates into a washer with outer and inner radii.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-washer-method-slice.tex}
  \caption{Washer method intuition: outer minus inner disk.}
  \label{fig:washer-method-slice}
\end{figure}
```

### 3) Cylindrical shells intuition

- File: `figures/fig-cylindrical-shells.tex`
- Use near: Cylindrical shells
- Caption idea: “A vertical strip rotates into a thin cylindrical shell.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-cylindrical-shells.tex}
  \caption{Shell method intuition: a strip rotates into a shell.}
  \label{fig:cylindrical-shells}
\end{figure}
```
