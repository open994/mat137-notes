# Visualizations: conventions + LaTeX integration

This repo stores small, self-contained LaTeX figure snippets (TikZ/PGFPlots) alongside each chapter.

## Folder layout

- `notes/chXX/figures/*.tex`: individual figure snippets (each file is a `tikzpicture` or `axis` block; no surrounding `figure` environment)
- `notes/chXX/VISUALS.md`: which figures exist for the chapter + suggested captions + exact LaTeX snippets to include them

## One-time LaTeX setup

If your `notes/preamble.tex` does not already load TikZ/PGFPlots, add these packages:

```tex
% TikZ + PGFPlots (for figures in notes/chXX/figures)
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,angles,quotes}

\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
```

Notes:

- The figure files intentionally reuse the existing theme colors already defined in `preamble.tex`: `thmcolor`, `defcolor`, `excolor`.
- If you prefer a single switch to disable all visuals, you can wrap each `\input{...}` with a custom boolean (left to the integrator).

## How to include a figure snippet

In the chapter `.tex` where you want the figure:

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-some-name.tex}
  \caption{Your caption here.}
  \label{fig:some-label}
\end{figure}
```

If the figure is from another folder, use the relative path from the including file.
