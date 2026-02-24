# Chapter 07 visualizations

Files live in `notes/ch07/figures/`.

## One-time setup

Ensure TikZ/PGFPlots are enabled as described in `notes/VISUALS-README.md`.

## Agent integration instructions (important)

- Do **not** edit `chapter.tex` automatically.
- Each `.tex` file in `figures/` is a *snippet* (a single `tikzpicture`). To include it in the notes, wrap it in a LaTeX `figure` environment in the appropriate section, and use `\input{figures/<name>.tex}`.
- Prefer placing these figures directly in Sections 7.7–7.8 (for the two examples) and near the discussion of lower/upper sums (Properties 2–3 / the “all lower sums vs all upper sums” picture).

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

### 4) Section 7.7 example: single-point spike (integrable)

- File: `figures/fig-single-point-spike.tex`
- Use near: Section 7.7, Example 7-9
- Caption idea: “Changing a function at one point does not affect its integral.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-single-point-spike.tex}
  \caption{The function $f$ equals $0$ everywhere except at $x=0$, where $f(0)=1$.}
  \label{fig:single-point-spike}
\end{figure}
```

### 5) Section 7.8 example: Dirichlet function (not integrable)

- File: `figures/fig-dirichlet-function.tex`
- Use near: Section 7.8, Example 7-10
- Caption idea: “Every subinterval has infimum $0$ and supremum $1$.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-dirichlet-function.tex}
  \caption{Dirichlet function intuition: on every interval, values $0$ and $1$ both occur (densely).}
  \label{fig:dirichlet-function}
\end{figure}
```

### 6) Lower vs upper sums on the real line (integrable vs not)

- File: `figures/fig-lower-upper-sums-numberline.tex`
- Use near: Properties 2–3 / the remark about “all lower sums left, all upper sums right”
- Caption idea: “Lower sums push up; upper sums push down; integrability means they meet.”

```tex
\begin{figure}[ht]
  \centering
  \input{figures/fig-lower-upper-sums-numberline.tex}
  \caption{Lower sums and upper sums viewed as numbers on the real line: meeting implies integrability; a gap implies non-integrability.}
  \label{fig:lower-upper-sums-numberline}
\end{figure}
```
