:::: center
::: minipage
These notes are for the University of Toronto course **MAT137: Calculus
with Proofs**. They are heavily adapted from the work of **Alfonso
Gracia-Saz** via the MAT137 YouTube channel lectures and related course
materials. Any remaining errors, omissions, or typos are the
responsibility of the compiler(s) of these notes.
:::
::::

# Logic, Definitions, Notation, and Proofs

## Sets and Set Notation {#sec:1.1}

*Before we do any calculus, we need a common language. We begin with the
most basic objects in mathematics---sets---and the notation we use to
talk about them.*

::: definition
[]{#def:1-1 label="def:1-1"} A *set* is a collection of objects. The
objects that belong to a set are called its *elements*.
:::

::: remark
A logician would rightly object that the definition above is not
rigorous enough for the purposes of logic and foundations. For our
purposes, however, it is good enough, and we keep it simple.
:::

A set is described by listing or characterising its elements inside
curly braces. For example,
$$A = \{\, x \in \mathbb{Z}: x \text{ is even}\,\}, \qquad
  B = \{4,\, 5,\, 6\}.$$ The set $A$ has infinitely many elements; the
set $B$ has exactly three.

::: definition
[]{#def:1-2 label="def:1-2"} Let $S$ and $T$ be sets.

1.  We write $x \in S$ to mean that $x$ is an element of $S$, and
    $x \notin S$ to mean that it is not.

2.  We write $S \subseteq T$ to mean that every element of $S$ is also
    an element of $T$; in this case $S$ is called a *subset* of $T$.

3.  We write $S \subsetneq T$ to mean that $S \subseteq T$ and
    $S \neq T$ (a *proper subset*).
:::

::: remark
The notation for "subset" is not universal. Some books use $\subset$ to
mean $\subseteq$ (subset, possibly equal), while other books use
$\subset$ to mean $\subsetneq$ (proper subset). Check the conventions in
whatever text you are reading. In these notes we use $\subseteq$ and
$\subsetneq$ exclusively, so there is no ambiguity.
:::

::: definition
[]{#def:1-3 label="def:1-3"} Let $S$ and $T$ be sets.

1.  The *union* $S \cup T$ is the set of elements belonging to $S$, to
    $T$, or to both.

2.  The *intersection* $S \cap T$ is the set of elements belonging to
    **both** $S$ and $T$.

3.  The *empty set* $\varnothing$ is the set with no elements:
    $\varnothing = \{\,\}$.
:::

::: example
[]{#ex:1-1 label="ex:1-1"} Let $C = \{2,\,4\}$ and $D = \{4,\,5\}$. Then
$$C \cup D = \{2,\,4,\,5\}, \qquad C \cap D = \{4\}.$$
:::

<figure id="fig:venn-union-intersection" data-latex-placement="ht">

<figcaption>Union and intersection.</figcaption>
</figure>

*Four sets of numbers appear so frequently that they have standard names
and symbols. Each is a subset of the next.*

::: definition
[]{#def:1-4 label="def:1-4"}

1.  $\mathbb{N}= \{0,\,1,\,2,\,3,\,\dots\}$ (the *natural numbers*).

2.  $\mathbb{Z}= \{\dots,\,-2,\,-1,\,0,\,1,\,2,\,\dots\}$ (the
    *integers*).

3.  $\mathbb{Q}= \left\{\,\dfrac{p}{q} : p,\,q \in \mathbb{Z},\; q \neq 0\,\right\}$
    (the *rational numbers*).

4.  $\mathbb{R}$ denotes the *real numbers*: informally, any number with
    a decimal expansion.

We have
$\mathbb{N}\subseteq \mathbb{Z}\subseteq \mathbb{Q}\subseteq \mathbb{R}$.
:::

::: remark
Some books start $\mathbb{N}$ at $1$ instead of $0$. Do not argue about
which convention is "right"; what matters is that you know which
convention is in force whenever you do mathematics or read a book.
:::

::: remark
There is a more formal and rigorous way to define $\mathbb{R}$, but that
construction is surprisingly deep and complicated; it is normally the
topic of an analysis course.
:::

## Set-Builder Notation and Intervals {#sec:1.2}

*We now introduce a powerful notation that lets us describe sets
precisely, even when an explicit list of elements is impossible.*

::: definition
[]{#def:1-5 label="def:1-5"} A set may be described by writing
$$\{\, x \in S : P(x) \,\} \qquad\text{or equivalently}\qquad \{\, x \in S \mid P(x) \,\},$$
which is read "the set of elements $x$ in $S$ **such that** $P(x)$." On
the left of the colon (or bar) we state **where** we draw our elements
from; on the right we state any **extra constraints**.
:::

::: remark
Use the colon or vertical bar to mean "such that" **only** inside
set-builder notation. Do not use it in other contexts.
:::

::: example
[]{#ex:1-2 label="ex:1-2"} Let
$A = \{\, x \in \mathbb{Z}: x^{2} < 6 \,\}$. Since the only integers
whose squares are less than $6$ are $-2,\,-1,\,0,\,1,\,2$, we have
$A = \{-2,\,-1,\,0,\,1,\,2\}$.
:::

::: example
[]{#ex:1-3 label="ex:1-3"} A second common usage: the left side gives
the **form** of the elements, and the right side explains the notation.
With $A$ as above,
$$B = \{\, 2x : x \in A \,\} = \{-4,\,-2,\,0,\,2,\,4\}.$$ Here $B$
consists of all elements of the form $2x$ where $x \in A$.
:::

*A particularly important family of sets built with set-builder notation
are the intervals.*

::: definition
[]{#def:1-6 label="def:1-6"} Let $a,\,b \in \mathbb{R}$ with $a \le b$.
$$\begin{align*}
  [a,\,b] &= \{\, x \in \mathbb{R}: a \le x \le b \,\}  &&\text{(closed interval)},\\
  (a,\,b) &= \{\, x \in \mathbb{R}: a < x < b \,\}       &&\text{(open interval)},\\
  [a,\,b) &= \{\, x \in \mathbb{R}: a \le x < b \,\},     &&\\
  (a,\,b] &= \{\, x \in \mathbb{R}: a < x \le b \,\}.     &&
\end{align*}$$ We also define unbounded intervals: $$\begin{align*}
  [a,\,\infty) &= \{\, x \in \mathbb{R}: x \ge a \,\}, &\qquad
  (a,\,\infty) &= \{\, x \in \mathbb{R}: x > a \,\},\\
  (-\infty,\,b] &= \{\, x \in \mathbb{R}: x \le b \,\}, &\qquad
  (-\infty,\,b) &= \{\, x \in \mathbb{R}: x < b \,\}.
\end{align*}$$
:::

::: remark
The symbol $\infty$ is **not** a number; it is never included as an
endpoint. The notation $(a,\infty)$ simply means "the set of all real
numbers greater than $a$, with no upper bound."
:::

<figure id="fig:interval-open-closed" data-latex-placement="ht">

<figcaption>Open/closed endpoints on a number line.</figcaption>
</figure>

## Mathematical Quantifiers {#sec:1.3}

*Many mathematical statements assert that something holds for **all**
objects, or that **there exists** an object with a certain property. The
two quantifier symbols make these assertions precise.*

::: definition
[]{#def:1-7 label="def:1-7"}

1.  The symbol $\forall$ is read "*for all*" or "*for every*."

2.  The symbol $\exists$ is read "*there exists*" or "*there is*."
:::

::: remark
In mathematics, "there exists" **always** means "there exists **at least
one**." It does not mean "there exists exactly one." For instance,
saying that an equation "has a solution" means it has at least one
solution. If you want to say exactly one, you must say so explicitly.
:::

::: example
[]{#ex:1-4 label="ex:1-4"} Consider the following statements.

1.  $\forall\, x \in \mathbb{R},\; x^{2} \ge 0$. This is **true**; every
    real number has a non-negative square.

2.  $\forall\, x \in \mathbb{Z},\; x > \pi$. This is **false**; for
    example, $x = 1$ is an integer with $1 < \pi$.
:::

::: example
[]{#ex:1-5 label="ex:1-5"} Consider the following statements.

1.  $\exists\, x \in \mathbb{R}$ such that $x^{2} = 5$. This is
    **true**; take $x = \sqrt{5}$ (or $x = -\sqrt{5}$).

2.  $\exists\, x \in \mathbb{R}$ such that $x^{2} = -1$. This is
    **false**; no real number has a negative square.
:::

::: remark
The connector "such that" adds no mathematical content; it simply makes
the sentence grammatically correct. Logicians often replace it with a
comma, but writing it out makes statements easier to read.
:::

::: remark
Writing "$x^{2} = 5$" by itself, with no quantifier and no prior
agreement about $x$, is **meaningless**: it is neither true nor false.
Such a fragment is sometimes called a *predicate* rather than a
*statement*. Every variable in a statement must be either quantified or
previously fixed. If you are ever tempted to begin a definition,
theorem, or proof with an equation or inequality involving an
unquantified variable---do not do it.
:::

## Order of Multiple Quantifiers {#sec:1.4}

*When a statement involves more than one quantifier, the order in which
they appear changes the meaning drastically. We illustrate with a pair
of statements that differ only in the order of their quantifiers, yet
one is true and the other is false.*

::: example
[]{#ex:1-6 label="ex:1-6"} Compare:

1.  $\forall\, x \in \mathbb{Z},\;\exists\, y \in \mathbb{Z}$ such that
    $x < y$.

2.  $\exists\, y \in \mathbb{Z}$ such that
    $\forall\, x \in \mathbb{Z},\; x < y$.
:::

::: remark
Before reading on, decide which statement is true and which is false,
and why.
:::

*In statement (b) we claim there is a **single** integer $y$ that is
greater than **every** integer $x$. The same $y$ must work for all $x$.
This is clearly false: there is no largest integer.*

*In statement (a) we claim that **for every** integer $x$, we can find
**some** integer $y$ with $x < y$. Crucially, we are allowed to use a
**different** $y$ for each $x$. Given any $x$, simply take $y = x + 1$.
So statement (a) is true.*

::: theorem
[]{#thm:1-1 label="thm:1-1"} For every integer $x$, there exists an
integer $y$ such that $x < y$.
:::

::: remark
The moral is that the order of quantifiers tells us **what depends on
what**. In (a), $y$ is allowed to depend on $x$; in (b), $y$ must be
chosen independently of $x$. As statements grow to involve many
quantifiers, keeping track of dependencies becomes essential.
:::

<figure id="fig:quantifier-dependence" data-latex-placement="ht">

<figcaption>Quantifier order encodes dependence.</figcaption>
</figure>

## Simple Proofs with Quantifiers {#sec:1.5}

*We now write proofs of some deliberately simple statements so that we
can see the building blocks clearly, before assembling them into more
complex proofs later.*

::: theorem
[]{#thm:1-2 label="thm:1-2"} Let $A = \{2,\,3,\,4\}$. Then for every
$x \in A$, we have $x > 0$.
:::

::: proof
*Proof.* We check each element of $A$ individually: $2 > 0$, $3 > 0$,
and $4 > 0$. ◻
:::

*What if the claim is false? To disprove a "for all" statement, we prove
its **negation**: a "there exists" statement.*

::: definition
[]{#def:1-8 label="def:1-8"} The *negation* of a statement $P$ is a
statement that is true exactly when $P$ is false.
:::

The negation of "$\forall\, x \in S,\; P(x)$" is "$\exists\, x \in S$
such that $\lnot P(x)$."

::: theorem
[]{#thm:1-3 label="thm:1-3"} It is false that every integer is positive.
Equivalently, there exists an integer $x$ with $x \le 0$.
:::

::: proof
*Proof.* Take $x = -6$. Then $x \in \mathbb{Z}$ and $x \le 0$. ◻
:::

*Next, a statement with **two** quantifiers, where the proof cannot
proceed by exhaustive checking because there are infinitely many cases.*

::: theorem
[]{#thm:1-4 label="thm:1-4"} For every integer $x$, there exists an
integer $y$ such that $x < y$.
:::

::: proof
*Proof.* Let $x$ be an integer (fixing an arbitrary value). Take
$y = x + 1$. Then $y$ is an integer, and $x < x + 1 = y$. ◻
:::

::: remark
The word "let" in a proof means we are **fixing** an **arbitrary** value
of the variable. "Arbitrary" because the proof must work for every
integer; "fix" because subsequent lines may refer to $x$ and it must
carry a definite meaning. In the statement of the theorem, $x$ is a
quantified variable with no intrinsic value. In the proof, once we write
"let $x$ be an integer," it becomes fixed and we may operate with it.
:::

::: remark
The structure here---fix the "for all" variable, then choose the "there
exists" variable, then verify---is a template we will reuse in much more
complex proofs, including proofs involving the definition of limit.
:::

## Quantifiers and the Empty Set {#sec:1.6}

*A common point of confusion arises when quantifiers are applied to the
empty set. There is a trap here.*

::: example
[]{#ex:1-7 label="ex:1-7"} Consider the two statements:

1.  $\forall\, x \in \varnothing,\; x > 0$.

2.  $\exists\, x \in \varnothing$ such that $x > 0$.

One is true and the other is false.
:::

::: remark
Before reading on, decide which is true and which is false.
:::

*Statement (a) is **true**.* To prove a "for all" statement, we must
check that **all** elements of the set satisfy the condition. The empty
set has zero elements, so there are zero elements to check; the
verification is vacuously complete. Conversely, to disprove it we would
need to find one element that fails, but the empty set contains no
elements at all, so we cannot.

*Statement (b) is **false**.* To prove a "there exists" statement, we
must exhibit at least one element with the desired property, and no
element of $\varnothing$ exists.

::: theorem
[]{#thm:1-5 label="thm:1-5"} For any property $P$, the statement
"$\forall\, x \in \varnothing,\; P(x)$" is true, and the statement
"$\exists\, x \in \varnothing$ such that $P(x)$" is false.
:::

::: remark
The specific condition ($x > 0$ in the example) is irrelevant. The
argument depends only on the set being empty.
:::

## Conditional Statements and Implication {#sec:1.7}

*Conditional statements---sentences of the form "if ..., then
..."---appear constantly in mathematics. We now pin down their precise
meaning, which is narrower than everyday English usage.*

::: definition
[]{#def:1-9 label="def:1-9"} A *conditional statement* has the form
$$\text{If } P, \text{ then } Q, \qquad\text{equivalently written}\qquad P \implies Q.$$
The symbol $\implies$ is read "*implies*." The statement means: whenever
$P$ is true, $Q$ must be true as well. **When $P$ is false, we make no
claim about $Q$ at all.**
:::

::: example
[]{#ex:1-8 label="ex:1-8"} "If $x > 10$, then $x > 6$" is true for all
real numbers $x$. Consider three cases:

1.  $x = 12$: $P$ is true, $Q$ is true. Compatible.

2.  $x = 8$: $P$ is false, $Q$ is true. Compatible (we don't care when
    $P$ is false).

3.  $x = 3$: $P$ is false, $Q$ is false. Also compatible.
:::

::: example
[]{#ex:1-9 label="ex:1-9"} Let $A \subseteq \mathbb{R}$ and suppose we
know that $x \in A \implies x > 0$.

1.  If $x \notin A$: no conclusion (the hypothesis is false).

2.  If $x > 0$: no conclusion (knowing $Q$ is true does not tell us
    about $P$).

3.  If $x \le 0$: we **can** conclude $x \notin A$. If $x$ were in $A$,
    it would have to be positive, contradicting $x \le 0$.
:::

::: theorem
[]{#thm:1-6 label="thm:1-6"} The implication $P \implies Q$ is logically
equivalent to its *contrapositive* $\lnot Q \implies \lnot P$.
:::

::: remark
$P \implies Q$ does **not** imply $\lnot P \implies \lnot Q$. That would
be the *inverse*, which is a different statement.
:::

::: definition
[]{#def:1-10 label="def:1-10"} We write $$P \iff Q$$ and read it "$P$
*if and only if* $Q$" (often abbreviated *iff*). It means that **both**
$P \implies Q$ and $Q \implies P$ hold. Equivalently, $P$ and $Q$ are
always both true or both false; we say $P$ and $Q$ are *equivalent*.
:::

::: example
[]{#ex:1-10 label="ex:1-10"} Let $n \in \mathbb{Z}$.

1.  "$n$ is even" does **not** imply "$n$ is a multiple of $4$" (take
    $n = 6$). However, "$n$ is a multiple of $4$" $\implies$ "$n$ is
    even."

2.  "$n$ is even" $\iff$ "$n + 1$ is odd." Both implications hold.
:::

::: remark
In casual English, "if" sometimes means "if and only if." In
mathematics, the two are **strictly distinguished**. Always check
whether a statement asserts one implication or both.
:::

::: example
[]{#ex:1-11 label="ex:1-11"} Is the following statement true or false?
$$\text{``If } 0 > 1, \text{ then } 478{,}871 \text{ is prime.''}$$ The
hypothesis $0 > 1$ is false. Since the "if" part is false, the entire
implication is **true**, regardless of whether $478{,}871$ is prime.
:::

::: remark
This may feel counterintuitive, but it follows directly from the
definition: an implication makes a promise only when the hypothesis is
true. When the hypothesis is false, the promise is vacuously kept.
:::

## Negation of Conditional Statements {#sec:1.8}

*A common and important fact: the negation of a conditional statement is
**never** another conditional statement. Understanding this is critical
for writing correct proofs.*

Let $A \subseteq \mathbb{R}$. Consider the conditional:
$$x \in A \implies x > 0.$$ What does this really say? It asserts that
**every** real number $x$ falls into one of three cases:

1.  $x \notin A$ and $x > 0$,

2.  $x \notin A$ and $x \le 0$,

3.  $x \in A$ and $x > 0$.

There is a **hidden quantifier**: the statement means
$\forall\, x \in \mathbb{R}$, if $x \in A$ then $x > 0$.

::: theorem
[]{#thm:1-7 label="thm:1-7"} The negation of
$$\forall\, x,\; (P(x) \implies Q(x))$$ is
$$\exists\, x \text{ such that } P(x) \text{ and } \lnot Q(x).$$
:::

In other words, the only way the conditional can fail is if there is
some $x$ for which the "if" part is **true** and the "then" part is
**false**.

::: remark
The negation of an "if...then" is **never** another "if...then." Also,
many conditional statements contain a **hidden, implicit** universal
quantifier. When you write the negation, you **must** write that
quantifier out explicitly.
:::

## Structure of a Correct Proof {#sec:1.9}

*We now look at a common **bad** proof, identify precisely what goes
wrong, and then write a correct proof of the same result. This
illustrates several principles that every proof must satisfy.*

::: theorem
[]{#thm:1-8 label="thm:1-8"} If $x,\,y \ge 0$, then
$$\sqrt{xy} \le \frac{x + y}{2}.$$
:::

*A common incorrect attempt proceeds as follows: start by writing the
desired inequality, square both sides, rearrange, and arrive at
$(x - y)^{2} \ge 0$. Since a square is non-negative, conclude that the
original inequality is true.*

::: remark
This "proof" is wrong for several reasons.

1.  It **assumes what it wants to prove**. The argument only shows: if
    the inequality holds, then $(x - y)^{2} \ge 0$. That tells us
    nothing about whether the inequality itself is true.

2.  The statement of the "theorem" was just a bare inequality with no
    quantifiers. A theorem must say **when** or **for which** values
    something is true.

3.  The inequality is **not** always true: when $x = y = -1$, the left
    side is $\sqrt{1} = 1$ and the right side is $-1$, so $1 \le -1$ is
    false. A correct proof must notice the need for $x, y \ge 0$.

4.  The proof contains no words, only algebra. In general, a proof must
    **explain** what is being done.
:::

::: proof
*Proof of [\[thm:1-8\]](#thm:1-8){reference-type="ref+label"
reference="thm:1-8"}.* Let $x,\,y \ge 0$. Since every square is
non-negative, $$(x - y)^{2} \ge 0.$$ Expanding and rearranging:
$$\begin{align*}
  x^{2} - 2xy + y^{2} &\ge 0, \\
  x^{2} + 2xy + y^{2} &\ge 4xy, \\
  (x + y)^{2} &\ge 4xy.
\end{align*}$$ Both sides are non-negative (since $x, y \ge 0$), so we
may take square roots of both sides:
$$\left\lvert x + y \right\rvert \ge 2\sqrt{xy}.$$ Since $x + y \ge 0$,
we have $\left\lvert x + y \right\rvert = x + y$, and therefore
$$\sqrt{xy} \le \frac{x + y}{2}.  \qedhere$$ ◻
:::

::: remark
You may wonder: how did we *come up with* starting from
$(x - y)^{2} \ge 0$? The answer is **rough work**. We first take the
desired inequality and manipulate it (not as a proof, but as
exploration) to discover what known fact it rests on. Once we find that
foundation, we write the actual proof **forward**: beginning from the
known fact and ending at the desired conclusion. The rough work is not
part of the proof; it is the process of *finding* the proof.
:::

::: remark
A correct proof has the following structure:

1.  The theorem states clearly **what** is being proved and **when** it
    holds.

2.  The proof begins with things that are **known** to be true.

3.  Each step follows logically from the previous ones.

4.  Whenever necessary, explanations accompany the algebra.

5.  The proof ends by concluding the desired result.
:::

## Writing Rigorous Definitions {#sec:1.10}

*We all have some geometric intuition for what it means for a function
to be "increasing"---a function that "always goes up." But "always goes
up" is not a mathematical definition. We now illustrate, step by step,
how to turn an intuitive idea into a precise, rigorous definition.*

::: remark
Some students believe that the definition of "increasing" is "positive
derivative." That is **wrong**. A function can be increasing even at a
point where it has a corner and no derivative at all. We need a
definition that captures every function we intuitively regard as
increasing, including such examples.
:::

*To formalise "always goes up," compare two input values $x_{1}$ and
$x_{2}$. If $x_{1} < x_{2}$, we want $f(x_{1}) < f(x_{2})$. But this
pair of inequalities by itself is not a definition; we need to specify
the function, the domain, and a quantifier.*

::: definition
[]{#def:1-11 label="def:1-11"} Let $I$ be an interval and let $f$ be a
function defined on $I$. We say $f$ is *increasing on $I$* if
$$\forall\, x_{1},\, x_{2} \in I, \quad x_{1} < x_{2} \implies f(x_{1}) < f(x_{2}).$$
:::

::: remark
Every piece of this definition is necessary:

1.  We define "increasing **on** $I$," not just "increasing," because a
    function can be increasing on one interval and not on another.

2.  The universal quantifier $\forall$ is required; without it, we would
    not know whether the condition applies to all pairs or just some.

3.  The conditional $\implies$ is required. Writing "$x_{1} < x_{2}$ and
    $f(x_{1}) < f(x_{2})$" (with "and" instead of "implies") would
    demand that *every* pair satisfies $x_{1} < x_{2}$, which is never
    true.

Without any one of these pieces, the definition would mean something
different, or nothing at all.
:::

## Verifying a Definition Directly {#sec:1.11}

*Once we have a definition, the definition itself tells us what a proof
should look like. We do not need to memorise a separate proof template:
the structure of the proof is contained in the structure of the
definition.*

::: theorem
[]{#thm:1-9 label="thm:1-9"} The function $f(x) = 3x + 7$ is increasing
on $\mathbb{R}$.
:::

*By [\[def:1-11\]](#def:1-11){reference-type="ref+label"
reference="def:1-11"}, what we want to show (WTS) is:*
$$\forall\, x_{1},\, x_{2} \in \mathbb{R}, \quad x_{1} < x_{2} \implies f(x_{1}) < f(x_{2}).$$

::: proof
*Proof.* Let $x_{1},\, x_{2} \in \mathbb{R}$ and assume $x_{1} < x_{2}$.
Multiplying both sides by $3$ (positive, so the inequality is
preserved): $$3x_{1} < 3x_{2}.$$ Adding $7$ to both sides:
$$3x_{1} + 7 < 3x_{2} + 7,$$ that is, $f(x_{1}) < f(x_{2})$. ◻
:::

::: remark
We did not need to memorise a method for proving that a function is
increasing. The definition of "increasing" dictated the proof structure:
fix arbitrary $x_{1}, x_{2}$; assume $x_{1} < x_{2}$; derive
$f(x_{1}) < f(x_{2})$. The same principle applies to **every**
mathematical definition.
:::

## Disproving via Definition Negation {#sec:1.12}

*We now prove that an example does **not** satisfy a definition, again
using nothing more than the definition itself---specifically, its
negation.*

::: theorem
[]{#thm:1-10 label="thm:1-10"} The function $g(x) = \cos x$ is not
increasing on $[0,\,\pi]$.
:::

*To say $g$ is **not** increasing on $[0,\,\pi]$ is to negate the
definition of increasing: there must exist a pair
$x_{1},\, x_{2} \in [0,\,\pi]$ with $x_{1} < x_{2}$ and
$g(x_{1}) \ge g(x_{2})$.*

::: proof
*Proof.* Take $x_{1} = 0$ and $x_{2} = \frac{\pi}{2}$. Then
$x_{1} < x_{2}$, but
$$g(x_{1}) = \cos 0 = 1 \ge 0 = \cos\frac{\pi}{2} = g(x_{2}).$$ Hence
$g$ is not increasing on $[0,\,\pi]$. ◻
:::

::: remark
The lesson applies to any concept: to show that something does **not**
satisfy a definition, negate the definition and prove the negation. No
special technique is needed beyond understanding the definition.
:::

## Proofs Involving Hypotheses {#sec:1.13}

*Most theorems take the form "if ..., then ...": there is a
**hypothesis** that we may assume, and a **conclusion** that we must
prove. We illustrate with a slightly more complex proof that uses the
definition of increasing together with hypotheses.*

::: theorem
[]{#thm:1-11 label="thm:1-11"} Let $f$ and $g$ be functions defined on
an interval $I$, and let $h = f + g$. If $f$ and $g$ are both increasing
on $I$, then $h$ is increasing on $I$.
:::

::: remark
The statement before the "if" is the *set-up*: it introduces the
notation. The "if" part is the *hypothesis*: something we are allowed to
**assume** during the proof. The "then" part is the *conclusion*: what
we must **prove**. Treat them very differently.
:::

::: proof
*Proof.* We want to show that $h$ is increasing on $I$,
i.e. $$\forall\, x_{1},\, x_{2} \in I, \quad x_{1} < x_{2} \implies h(x_{1}) < h(x_{2}).$$
Let $x_{1},\, x_{2} \in I$ with $x_{1} < x_{2}$. Since $f$ is increasing
on $I$, $$f(x_{1}) < f(x_{2}).$$ Since $g$ is increasing on $I$,
$$g(x_{1}) < g(x_{2}).$$ Adding these two inequalities:
$$f(x_{1}) + g(x_{1}) < f(x_{2}) + g(x_{2}),$$ that is,
$h(x_{1}) < h(x_{2})$. ◻
:::

::: remark
Notice how $f$ and $g$ were treated differently from $h$. For $f$ and
$g$, we **assumed** they were increasing (hypothesis) and **used** that
fact. For $h$, we **proved** it was increasing (conclusion). This is the
fundamental distinction between hypothesis and conclusion in a proof.
:::

## Proof by Induction {#sec:1.14}

*Proof by induction is a technique especially suited to theorems that
depend on a natural number $n$ and that cannot be checked one value at a
time (because there are infinitely many values), yet for which a direct
proof for all $n$ at once is not apparent.*

::: theorem
[]{#thm:1-12 label="thm:1-12"} For every natural number $n \ge 4$,
$$n! > 2^{n}.$$
:::

*We denote the statement "$n! > 2^{n}$" by $S_{n}$.*

::: definition
[]{#def:1-12 label="def:1-12"} A *proof by induction* of a statement
$S_{n}$ for all $n \ge n_{0}$ consists of two steps:

1.  **Base case.** Prove $S_{n_{0}}$.

2.  **Induction step.** Prove that for every $n \ge n_{0}$,
    $S_{n} \implies S_{n+1}$.

Together, these show that $S_{n}$ holds for every $n \ge n_{0}$.
:::

::: remark
In the induction step, we are **not** proving $S_{n}$ and we are **not**
proving $S_{n+1}$. We are proving an **implication**: *if* $S_{n}$ is
true, *then* $S_{n+1}$ must be true as well. By itself, the induction
step does not tell us whether any $S_{n}$ is true. Combined with the
base case, however, the chain of implications propagates truth from
$n_{0}$ onward:
$S_{n_{0}} \implies S_{n_{0}+1} \implies S_{n_{0}+2} \implies \cdots$.
:::

::: proof
*Proof of [\[thm:1-12\]](#thm:1-12){reference-type="ref+label"
reference="thm:1-12"}.* We proceed by induction on $n$.

**Base case** ($n = 4$). We have $4! = 24$ and $2^{4} = 16$, so
$4! > 2^{4}$.

**Induction step.** Let $n \ge 4$ and assume $n! > 2^{n}$ (induction
hypothesis). We want to show $(n+1)! > 2^{n+1}$.

Since $(n+1)! = (n+1) \cdot n!$ and $2^{n+1} = 2 \cdot 2^{n}$, we
compute: $$\begin{align*}
  (n+1) \cdot n! &> (n+1) \cdot 2^{n} &&\text{(by the induction hypothesis)} \\
                 &\ge 5 \cdot 2^{n}     &&\text{(since } n \ge 4 \text{ implies } n+1 \ge 5\text{)} \\
                 &> 2 \cdot 2^{n}        &&\text{(since } 5 > 2\text{)} \\
                 &= 2^{n+1}.
\end{align*}$$ Hence $(n+1)! > 2^{n+1}$, completing the induction
step. ◻
:::

::: remark
A common misunderstanding: the induction step is **not** "prove
$S_{n+1}$." It is "prove that $S_{n} \implies S_{n+1}$." We prove the
statement itself only for the base case. Everything else is an
implication.
:::

## Direct and Inductive Proofs {#sec:1.15}

*To illustrate that a theorem may have more than one proof, and that
different proof strategies are sometimes available, we prove the same
identity by two completely different methods.*

::: theorem
[]{#thm:1-13 label="thm:1-13"} For every positive integer $n$,
$$1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}.$$
:::

Let $S_{n} = 1 + 2 + \cdots + n$.

::: proof
*First proof (direct).* Write the sum in two ways: $$\begin{align*}
  S_{n} &= 1 + 2 + 3 + \cdots + n, \\
  S_{n} &= n + (n-1) + (n-2) + \cdots + 1.
\end{align*}$$ Adding term by term, each pair sums to $n + 1$ and there
are $n$ pairs: $$2S_{n} = n(n+1).$$ Therefore
$S_{n} = \dfrac{n(n+1)}{2}$. ◻
:::

::: proof
*Second proof (by induction).* We proceed by induction on $n$.

**Base case** ($n = 1$). $S_{1} = 1$ and $\dfrac{1 \cdot 2}{2} = 1$.

**Induction step.** Let $n$ be a positive integer and assume
$S_{n} = \dfrac{n(n+1)}{2}$ (induction hypothesis). Then
$$\begin{align*}
  S_{n+1} &= S_{n} + (n+1) \\
           &= \frac{n(n+1)}{2} + (n+1) &&\text{(by the induction hypothesis)} \\
           &= \frac{n(n+1) + 2(n+1)}{2} \\
           &= \frac{(n+1)(n+2)}{2},
\end{align*}$$ which is the formula with $n$ replaced by $n+1$. ◻
:::

::: remark
Both proofs are equally valid. The first is a direct proof: a single
algebraic trick works for all $n$ simultaneously, with no assumptions.
The second is an inductive proof: we prove the identity for $n = 1$,
then show that truth at $n$ implies truth at $n + 1$. Which proof is
"better" is a matter of taste.
:::

# Limits and Continuity

## Intuitive Idea of Limits {#sec:2.1}

*We begin not with a rigorous definition, but with examples---hand-wavy,
heuristic---just to gain some intuition about what the concept of
"limit" means. Once we are comfortable with the idea, we will introduce
the formal, rigorous definition in a later section.*

::: example
[]{#ex:2-1 label="ex:2-1"} Consider the function $f$ defined by
$$f(x) = \dfrac{x^{2} - 1}{x - 1}.$$ The domain is all of $\mathbb{R}$
except $1$; the value $f(1)$ is undefined. We may factor the numerator
and cancel:
$$\dfrac{x^{2} - 1}{x - 1} = \dfrac{(x-1)(x+1)}{x-1} = x + 1, \qquad x \neq 1.$$
Call $g(x) = x + 1$. Then $f$ and $g$ agree everywhere except at $1$:
$g(1) = 2$, while $f(1)$ is undefined. The graph of $f$ is the line
$y = x + 1$ with a **hole** at the point $(1, 2)$.

Looking at the graph, all the values of $f(x)$ for $x$ close to $1$
suggest that $f(1)$ "should be" $2$. We say that the *limit* of $f(x)$
as $x$ approaches $1$ is $2$, and write $$\lim_{x \to 1} f(x) = 2.$$
:::

::: example
[]{#ex:2-2 label="ex:2-2"} Consider the function
$$f(x) = \dfrac{1 - \sqrt{1 + x}}{x},$$ defined for $x \geq -1$,
$x \neq 0$. A table of values suggests that as $x$ approaches $0$,
$f(x)$ approaches $-\frac{1}{2}$. We can verify this algebraically by
multiplying numerator and denominator by the conjugate $1 + \sqrt{1+x}$:
$$\dfrac{1 - \sqrt{1+x}}{x} \cdot \dfrac{1 + \sqrt{1+x}}{1 + \sqrt{1+x}}
  = \dfrac{1 - (1+x)}{x\!\left(1 + \sqrt{1+x}\right)}
  = \dfrac{-1}{1 + \sqrt{1+x}}, \qquad x \neq 0.$$ The simplified
function equals $-\frac{1}{2}$ at $x = 0$, confirming
$\lim_{x \to 0} f(x) = -\frac{1}{2}$.
:::

*In both examples, the rough idea is the same. We summarise it
informally as follows.*

::: remark
The statement "$\lim_{x \to a} f(x) = L$" means, roughly, that if $x$ is
very close to $a$ but **not** equal to $a$, then $f(x)$ is very close to
$L$. This is **not** a definition; the formal definition will come in
[2.5](#sec:2.5){reference-type="ref+label" reference="sec:2.5"}.
:::

## Limits That Do Not Exist {#sec:2.2}

*Not every function has a limit at every point. In this section we
examine two ways a limit can fail to exist, and introduce the notation
$\lim_{x \to a} f(x) = \infty$.*

::: example
[]{#ex:2-3 label="ex:2-3"} Let
$h(x) = \sin\!\left(\dfrac{\pi}{2x}\right)$. The value $h(0)$ is
undefined. Evaluating at
$x = 1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \ldots$ gives
$$h(1) = 1,\quad h\!\left(\tfrac{1}{2}\right) = 0,\quad h\!\left(\tfrac{1}{3}\right) = -1,\quad h\!\left(\tfrac{1}{4}\right) = 0,\quad h\!\left(\tfrac{1}{5}\right) = 1,\quad \ldots$$
As $x$ approaches $0$, the function oscillates between $-1$ and $1$
without settling near any single number. Therefore $\lim_{x \to 0} h(x)$
**does not exist** (DNE).
:::

::: remark
For a limit to exist, the function must approach **one single number**.
Oscillation between two or more values prevents this.
:::

::: example
[]{#ex:2-4 label="ex:2-4"} Let $F(x) = \dfrac{1}{(x-1)^{2}}$. Then
$F(1)$ is undefined. When $x$ is close to $1$, $(x-1)^{2}$ is close to
$0$ but positive, so $F(x)$ grows arbitrarily large. We write
$$\lim_{x \to 1} F(x) = \infty.$$
:::

::: remark
The notation $\lim_{x \to a} f(x) = \infty$ does **not** mean the limit
exists. It means the limit does not exist **in a specific way**: $f(x)$
fails to approach any single real number because it grows without bound.
Infinity is **not** a real number.
:::

## One-Sided Limits {#sec:2.3}

*Sometimes a function approaches different values depending on the
direction from which we approach a point. This leads to the notion of
side limits.*

::: example
[]{#ex:2-5 label="ex:2-5"} Let
$G(x) = \dfrac{x^{2} + x}{\left\lvert x \right\rvert}$. Then $G(0)$ is
undefined. Breaking into cases: $$G(x) =
  \begin{cases}
    x + 1 & \text{if } x > 0, \\
    -x - 1 & \text{if } x < 0.
  \end{cases}$$ When $x$ is close to $0$ and positive, $G(x)$ is close
to $1$. When $x$ is close to $0$ and negative, $G(x)$ is close to $-1$.
Since the two values disagree, $\lim_{x \to 0} G(x)$ does not exist.
However, the *one-sided limits* do exist:
$$\lim_{x \to 0^{+}} G(x) = 1, \qquad
  \lim_{x \to 0^{-}} G(x) = -1.$$
:::

::: remark
The notation $\lim_{x \to a^{+}} f(x)$ means the limit as $x$ approaches
$a$ **from the right** (i.e. through values greater than $a$).
Similarly, $\lim_{x \to a^{-}} f(x)$ means the limit **from the left**.
Together, these are called the *side limits* or *one-sided limits*.
:::

*Let us summarise the different behaviours we have seen.*

::: remark
The limit of a function at a point may or may not exist.

1.  The limit **exists** and equals $L$ when $f(x)$ approaches $L$ as
    $x \to a$. It does not matter whether $f(a)$ is defined, undefined,
    or equal to $L$.

2.  The limit **does not exist**, and this can happen in several ways:

    - the limit is $\infty$ or $-\infty$ (vertical asymptote),

    - the two one-sided limits exist but differ (jump),

    - the function oscillates without settling (wild oscillation).
:::

<figure id="fig:one-sided-jump" data-latex-placement="ht">

<figcaption>A jump discontinuity with distinct one-sided
limits.</figcaption>
</figure>

## Absolute Values and Distance {#sec:2.4}

*This section is a short but essential preparation for the formal
definition of limit. We explain how to use absolute values and
inequalities to talk about distances, both geometrically and
algebraically.*

::: definition
[]{#def:2-1 label="def:2-1"} For any $x \in \mathbb{R}$,
$$\left\lvert x \right\rvert =
  \begin{cases}
    x & \text{if } x \geq 0, \\
    -x & \text{if } x < 0.
  \end{cases}$$ Geometrically, $\left\lvert x \right\rvert$ is the
*distance* between $x$ and $0$ on the real line. More generally,
$\left\lvert x - a \right\rvert$ is the distance between $x$ and $a$.
:::

::: theorem
[]{#thm:2-1 label="thm:2-1"} For all $x, y \in \mathbb{R}$:

1.  $\left\lvert xy \right\rvert = \left\lvert x \right\rvert\,\left\lvert y \right\rvert$
    (multiplicativity).

2.  $\left\lvert x + y \right\rvert \leq \left\lvert x \right\rvert + \left\lvert y \right\rvert$
    (triangle inequality).
:::

::: remark
The equality
$\left\lvert xy \right\rvert = \left\lvert x \right\rvert\,\left\lvert y \right\rvert$
holds for products, but the analogous statement for **sums** is
**false**: $\left\lvert x+y \right\rvert$ need not equal
$\left\lvert x \right\rvert+\left\lvert y \right\rvert$. Instead, we
only have the triangle inequality.
:::

*The key idea we need going forward is how to express "$x$ is close to
$a$" using inequalities. The following equivalences should become second
nature.*

::: proposition
[]{#thm:2-2 label="thm:2-2"} Let $a \in \mathbb{R}$ and $\delta > 0$.
The following statements are equivalent:

1.  $\left\lvert x - a \right\rvert < \delta$.

2.  The distance between $x$ and $a$ is less than $\delta$.

3.  $-\delta < x - a < \delta$.

4.  $a - \delta < x < a + \delta$.

5.  $x \in (a - \delta,\, a + \delta)$.
:::

::: remark
Every time you encounter one of these inequalities, you should be able
to convert it instantly to any of the other equivalent forms, and to the
geometric picture of $x$ lying in an open interval of radius $\delta$
centred at $a$. If you can do that, you are ready for the formal
definition of limit.
:::

## Formal Definition of Limit {#sec:2.5}

*We now transform the rough idea "if $x$ is close to $a$ but not $a$,
then $f(x)$ is close to $L$" into a rigorous statement. Every piece of
the definition is necessary; omitting or modifying any part would change
the meaning.*

::: definition
[]{#def:2-2 label="def:2-2"} Let $a, L \in \mathbb{R}$, and let $f$ be a
function defined at least on an open interval containing $a$, except
possibly at $a$ itself. We say $$\lim_{x \to a} f(x) = L$$ if for every
$\varepsilon> 0$ there exists a $\delta > 0$ such that for all
$x \in \mathbb{R}$,
$$0 < \left\lvert x - a \right\rvert < \delta \implies \left\lvert f(x) - L \right\rvert < \varepsilon.$$
:::

::: remark
The second line is an implication with a **hidden universal
quantifier**: it means "for every real number $x$, if
$0 < \left\lvert x - a \right\rvert < \delta$, then
$\left\lvert f(x) - L \right\rvert < \varepsilon$." It is a standard
convention to leave the "for all $x$" implicit. Write it explicitly if
it helps you avoid confusion.
:::

*Let us unpack the roles of $\varepsilon$ and $\delta$ by considering
functions that do and do not have limits.*

::: remark
Think of $\varepsilon$ as a challenge and $\delta$ as a response. We
require that for **every** $\varepsilon> 0$ (no matter how small), we
can **find** a $\delta > 0$ (depending on $\varepsilon$) that makes the
implication true. Making $\varepsilon$ smaller forces the graph into a
narrower horizontal band around $L$; if we can always respond with a
$\delta$ that keeps the graph inside this band, the limit is $L$.

For a function that does **not** have limit $L$, there will be some
small $\varepsilon$ for which **no** $\delta$ works: no matter how close
we restrict $x$ to $a$, the graph escapes the band.
:::

<figure id="fig:eps-delta-band" data-latex-placement="ht">

<figcaption>An <span class="math inline"><em>ε</em></span>-band around
<span class="math inline"><em>L</em></span> and a <span
class="math inline"><em>δ</em></span>-window around <span
class="math inline"><em>a</em></span>.</figcaption>
</figure>

::: remark
As an exercise, try to write rigorous
$(\varepsilon, \delta)$-definitions for the one-sided limits
$\lim_{x \to a^{+}} f(x) = L$ and $\lim_{x \to a^{-}} f(x) = L$, and for
$\lim_{x \to a} f(x) = \infty$. If you succeed, it means you truly
understand the formal definition.
:::

## Limits at Infinity {#sec:2.6}

*We now ask: when $x$ is very large, what happens to $f(x)$? This leads
to the notion of limit at infinity.*

::: definition
[]{#def:2-3 label="def:2-3"} Let $L \in \mathbb{R}$, and let $f$ be a
function defined at least on an interval $(p, \infty)$ for some
$p \in \mathbb{R}$. We say $$\lim_{x \to \infty} f(x) = L$$ if for every
$\varepsilon> 0$ there exists a real number $M$ such that for all $x$,
$$x > M \implies \left\lvert f(x) - L \right\rvert < \varepsilon.$$
:::

::: example
[]{#ex:2-6 label="ex:2-6"} Consider
$f(x) = \dfrac{x+1}{x} = 1 + \dfrac{1}{x}$. When $x$ is large,
$\frac{1}{x}$ is close to $0$, so $f(x)$ is close to $1$. Therefore
$\lim_{x \to \infty} f(x) = 1$.
:::

::: remark
When $\lim_{x \to \infty} f(x) = L$, the line $y = L$ is called a
*horizontal asymptote* of $f$ at $\infty$. A horizontal asymptote is
**not** a line that the graph "never touches." The graph may cross the
asymptote; it may even intersect it infinitely many times. What matters
is that eventually, as $x \to \infty$, $f(x)$ stays arbitrarily close to
$L$.
:::

::: remark
In the definition, the quantifier structure is: for every
$\varepsilon> 0$, there exists $M$ such that ...The important quantifier
is $\varepsilon$: we need the implication to hold for **all** positive
$\varepsilon$, but for each $\varepsilon$ we only need to find **one**
value of $M$. As $\varepsilon$ shrinks, $M$ may need to grow.
:::

## Proving Limits from the Definition {#sec:2.7}

*We now illustrate, with a simple example, how to prove that a function
has a specific limit directly from the
$(\varepsilon,\delta)$-definition. The emphasis is on the **structure**
of the proof: fix $\varepsilon$, choose $\delta$, assume the hypothesis,
derive the conclusion.*

::: theorem
[]{#thm:2-3 label="thm:2-3"} $\lim_{x \to 3} (2x + 1) = 7$.
:::

*Before writing the proof, we do rough work to discover the right choice
of $\delta$. We want to show that
$\left\lvert (2x+1) - 7 \right\rvert < \varepsilon$ whenever
$0 < \left\lvert x - 3 \right\rvert < \delta$. Observe:*
$$\left\lvert (2x+1) - 7 \right\rvert = \left\lvert 2x - 6 \right\rvert = 2\left\lvert x - 3 \right\rvert.$$
*If $\left\lvert x - 3 \right\rvert < \delta$, then
$2\left\lvert x-3 \right\rvert < 2\delta$. Setting
$2\delta = \varepsilon$, i.e. $\delta = \varepsilon/2$, will work.*

::: proof
*Proof.* Strategy: choose $\delta = \varepsilon/2$ and verify the
implication.

Let $\varepsilon> 0$. Take $\delta = \varepsilon/ 2 > 0$. Fix any
$x \in \mathbb{R}$ with $0 < \left\lvert x - 3 \right\rvert < \delta$.
Then $$\begin{align*}
  \left\lvert (2x + 1) - 7 \right\rvert
    &= \left\lvert 2x - 6 \right\rvert \\
    &= 2\left\lvert x - 3 \right\rvert \\
    &< 2\delta \\
    &= \varepsilon.
\end{align*}$$ Therefore
$\left\lvert (2x+1)-7 \right\rvert < \varepsilon$, as required. ◻
:::

## A Harder Epsilon-Delta Proof {#sec:2.8}

*The structure of the proof is the same as in
[2.7](#sec:2.7){reference-type="ref+label" reference="sec:2.7"}, but the
algebra is harder. The key new difficulty is that $\delta$ cannot simply
be $\varepsilon$ divided by something; we need to **bound** a factor
that depends on $x$.*

::: theorem
[]{#thm:2-4 label="thm:2-4"} $\lim_{x \to 4} (x^{2} + 1) = 17$.
:::

*Rough work. We want
$\left\lvert (x^{2}+1) - 17 \right\rvert < \varepsilon$ whenever
$0 < \left\lvert x-4 \right\rvert < \delta$. Observe:*
$$\left\lvert x^{2} - 16 \right\rvert = \left\lvert x-4 \right\rvert\,\left\lvert x+4 \right\rvert.$$
*The factor $\left\lvert x+4 \right\rvert$ depends on $x$, so we cannot
simply set $\delta = \varepsilon/ \left\lvert x+4 \right\rvert$---that
would make $\delta$ depend on $x$, which is not permitted. Instead, we
impose $\delta \leq 1$, which forces $x \in (3, 5)$ and hence
$\left\lvert x+4 \right\rvert < 9$. Then
$\left\lvert x^{2}-16 \right\rvert < 9\delta$, and choosing
$\delta \leq \varepsilon/9$ finishes the job.*

::: remark
In the structure of an $(\varepsilon, \delta)$-proof, $\delta$ is chosen
**before** $x$ is fixed, so $\delta$ may depend on $\varepsilon$ but
**never** on $x$. Allowing $\delta$ to depend on $x$ would change the
meaning of the statement entirely and would not establish anything about
limits.
:::

::: proof
*Proof.* Strategy: choose $\delta = \min\{1,\, \varepsilon/9\}$ and
verify.

Let $\varepsilon> 0$. Take
$\delta = \min\!\left\{1,\, \dfrac{\varepsilon}{9}\right\} > 0$. Fix any
$x \in \mathbb{R}$ with $0 < \left\lvert x - 4 \right\rvert < \delta$.

Since $\delta \leq 1$, we have $\left\lvert x - 4 \right\rvert < 1$, so
$3 < x < 5$ and therefore $7 < x + 4 < 9$. In particular,
$\left\lvert x + 4 \right\rvert < 9$.

Since $\delta \leq \varepsilon/9$, we have
$\left\lvert x - 4 \right\rvert < \varepsilon/9$. Therefore:
$$\begin{align*}
  \left\lvert (x^{2} + 1) - 17 \right\rvert
    &= \left\lvert x^{2} - 16 \right\rvert \\
    &= \left\lvert x - 4 \right\rvert\,\left\lvert x + 4 \right\rvert \\
    &< \dfrac{\varepsilon}{9} \cdot 9 \\
    &= \varepsilon.
\end{align*}$$ Thus
$\left\lvert (x^{2}+1)-17 \right\rvert < \varepsilon$, as required. ◻
:::

::: remark
The choice $\delta \leq 1$ is arbitrary; any positive constant would
work (producing a different but equally valid proof). The essential idea
is to first restrict $x$ to a bounded neighbourhood of $4$ so that
$\left\lvert x+4 \right\rvert$ can be bounded by a constant.
:::

## Proving a Limit Does Not Exist {#sec:2.9}

*To show that a limit does **not** exist, we negate the formal
definition. This requires four quantifiers and careful handling of
each.*

::: definition
[]{#def:2-4 label="def:2-4"} We say $\lim_{x \to \infty} h(x)$ does not
exist if for every $L \in \mathbb{R}$ there exists $\varepsilon> 0$ such
that for every $M \in \mathbb{R}$ there exists $x \in \mathbb{R}$
satisfying
$$x > M \quad\text{and}\quad \left\lvert h(x) - L \right\rvert \geq \varepsilon.$$
:::

::: remark
This definition is obtained by negating the definition of
$\lim_{x \to \infty} h(x) = L$ for every possible value of $L$. If you
find the four quantifiers intimidating, revisit the negation one
quantifier at a time:

- "for every $\varepsilon$" becomes "there exists $\varepsilon$,"

- "there exists $M$" becomes "for every $M$,"

- the hidden "for all $x$" becomes "there exists $x$,"

- the implication $P \Rightarrow Q$ becomes $P \wedge \neg Q$.
:::

::: theorem
[]{#thm:2-5 label="thm:2-5"} $\lim_{x \to \infty} \cos(\pi x)$ does not
exist.
:::

*Key observations: when $x$ is an even integer, $\cos(\pi x) = 1$; when
$x$ is an odd integer, $\cos(\pi x) = -1$. So $h(x) = \cos(\pi x)$ keeps
oscillating between $1$ and $-1$ for arbitrarily large $x$.*

::: proof
*Proof.* Strategy: fix an arbitrary $L$, choose
$\varepsilon= \frac{1}{2}$, and for any $M$ exhibit an integer $x > M$
with $\left\lvert \cos(\pi x) - L \right\rvert \geq \frac{1}{2}$.

Let $L \in \mathbb{R}$. Take $\varepsilon= \frac{1}{2}$. Let
$M \in \mathbb{R}$ be arbitrary.

Since $\varepsilon= \frac{1}{2}$, the open interval
$(L - \varepsilon,\, L + \varepsilon)$ has length $1$. Therefore it
cannot contain **both** $1$ and $-1$ (which are distance $2$ apart). At
least one of $1$ and $-1$ lies outside
$(L - \frac{1}{2},\, L + \frac{1}{2})$.

**Case 1:** $1 \notin (L - \frac{1}{2},\, L + \frac{1}{2})$. Choose any
even integer $x > M$. Then $\cos(\pi x) = 1$, so
$\left\lvert \cos(\pi x) - L \right\rvert = \left\lvert 1 - L \right\rvert \geq \frac{1}{2}$.

**Case 2:** $-1 \notin (L - \frac{1}{2},\, L + \frac{1}{2})$. Choose any
odd integer $x > M$. Then $\cos(\pi x) = -1$, so
$\left\lvert \cos(\pi x) - L \right\rvert = \left\lvert -1 - L \right\rvert \geq \frac{1}{2}$.

In either case, we have found $x > M$ with
$\left\lvert \cos(\pi x) - L \right\rvert \geq \varepsilon$. Since $L$
was arbitrary, the limit does not exist. ◻
:::

## The Limit Laws {#sec:2.10}

*Computing every limit from the $(\varepsilon, \delta)$-definition would
be tedious. The limit laws let us reduce complicated limits to simple
building blocks. Their importance cannot be overstated: once proven,
they free us from epsilon-delta arguments for a huge class of
functions.*

::: theorem
[]{#thm:2-6 label="thm:2-6"} Let $a, c \in \mathbb{R}$.

1.  $\lim_{x \to a} x = a$.

2.  $\lim_{x \to a} c = c$.
:::

::: remark
These are the two simplest $(\varepsilon, \delta)$-proofs one can write.
Try them as an exercise before proceeding.
:::

::: theorem
[]{#thm:2-7 label="thm:2-7"} Let $a, L, M \in \mathbb{R}$ and let $f, g$
be functions defined on an open interval containing $a$, except possibly
at $a$. Suppose $\lim_{x \to a} f(x) = L$ and $\lim_{x \to a} g(x) = M$.
Then:

1.  **Sum law:** $\lim_{x \to a} \bigl[f(x) + g(x)\bigr] = L + M$.

2.  **Product law:**
    $\lim_{x \to a} \bigl[f(x) \cdot g(x)\bigr] = L \cdot M$.

3.  **Quotient law:** If $M \neq 0$, then
    $\lim_{x \to a} \dfrac{f(x)}{g(x)} = \dfrac{L}{M}$.
:::

::: remark
The limit laws **only** apply when the individual limits **exist** as
real numbers. If even one of the limits does not exist, we cannot draw
any conclusion---positive or negative---about the sum, product, or
quotient. For example, $\lim_{x \to 0} x = 0$ and
$\lim_{x \to 0} \frac{3}{x}$ does not exist, yet
$\lim_{x \to 0} x \cdot \frac{3}{x} = 3$. Likewise, $\frac{1}{x}$ and
$\frac{2x-1}{x}$ both lack limits at $0$, yet their sum
$\frac{1}{x} + \frac{2x-1}{x} = \frac{2x}{x}$ has limit $2$.
:::

::: example
[]{#ex:2-7 label="ex:2-7"} To compute $\lim_{x \to 2} (x^{4} - 3x)$,
note that this polynomial is built from sums and products of $x$ and
constants. By [\[thm:2-6\]](#thm:2-6){reference-type="ref+label"
reference="thm:2-6"} and iterated application of the sum and product
laws: $$\lim_{x \to 2} (x^{4} - 3x) = 2^{4} - 3 \cdot 2 = 10.$$ The same
argument shows that for **any** polynomial $p$ and any
$a \in \mathbb{R}$, $\lim_{x \to a} p(x) = p(a)$.
:::

## Proof of the Sum Law {#sec:2.11}

*We prove the sum law from
[\[thm:2-7\]](#thm:2-7){reference-type="ref+label" reference="thm:2-7"}
as a model for how the limit laws are established. The key idea is the
triangle inequality: split the error of the sum into the errors of the
two summands, and make each one less than $\varepsilon/2$.*

::: proof
*Proof.* Strategy: use the hypotheses on $f$ and $g$ with
$\varepsilon/2$ to obtain $\delta_{1}$ and $\delta_{2}$, then set
$\delta = \min\{\delta_{1}, \delta_{2}\}$.

Let $h = f + g$. We wish to show $\lim_{x \to a} h(x) = L + M$.

Let $\varepsilon> 0$. Since $\lim_{x \to a} f(x) = L$, applying the
definition with $\varepsilon/2 > 0$ yields a $\delta_{1} > 0$ such that
$$0 < \left\lvert x - a \right\rvert < \delta_{1} \implies \left\lvert f(x) - L \right\rvert < \frac{\varepsilon}{2}.$$

Similarly, since $\lim_{x \to a} g(x) = M$, there exists
$\delta_{2} > 0$ such that
$$0 < \left\lvert x - a \right\rvert < \delta_{2} \implies \left\lvert g(x) - M \right\rvert < \frac{\varepsilon}{2}.$$

Take $\delta = \min\{\delta_{1}, \delta_{2}\} > 0$. Fix any
$x \in \mathbb{R}$ with $0 < \left\lvert x - a \right\rvert < \delta$.
Then $\left\lvert x - a \right\rvert < \delta_{1}$ and
$\left\lvert x - a \right\rvert < \delta_{2}$, so both conclusions above
hold. Therefore: $$\begin{align*}
  \left\lvert h(x) - (L + M) \right\rvert
    &= \left\lvert \bigl(f(x) - L\bigr) + \bigl(g(x) - M\bigr) \right\rvert \\
    &\leq \left\lvert f(x) - L \right\rvert + \left\lvert g(x) - M \right\rvert \\
    &< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} \\
    &= \varepsilon.
\end{align*}$$

Thus $\left\lvert h(x) - (L+M) \right\rvert < \varepsilon$, completing
the proof. ◻
:::

::: remark
Notice the different ways the definition of limit is used. For $h$, we
are **proving** the limit exists, so we must fix an arbitrary
$\varepsilon$ and produce $\delta$. For $f$ and $g$, we **assume** the
limits exist, so we may **choose** any $\varepsilon$ we like (here
$\varepsilon/2$) and are **guaranteed** the existence of a suitable
$\delta$.
:::

## The Squeeze Theorem {#sec:2.12}

*The squeeze theorem (also called the sandwich theorem) is a powerful
tool for computing limits of functions that are hard to handle directly
but can be trapped between two simpler functions with the same limit. We
motivate it with an example that also illustrates a common pitfall.*

::: example
[]{#ex:2-8 label="ex:2-8"} Compute
$\lim_{x \to 0} \bigl(x^{2} \sin(1/x)\bigr)$.

*A tempting but **incorrect** argument:* write the limit as a product
and apply the product law:
$$\lim_{x \to 0} x^{2} \cdot \lim_{x \to 0} \sin(1/x) = 0 \cdot (\cdots) = 0. \quad \textbf{WRONG!}$$
This fails because $\lim_{x \to 0} \sin(1/x)$ **does not exist** (the
function oscillates wildly), so the product law does not apply.
:::

::: remark
One cannot conclude anything by writing "$0$ times anything is $0$" in
the context of limits. The product law requires **both** individual
limits to exist. As a cautionary example: $\lim_{x \to 0} x = 0$ and
$\lim_{x \to 0} \frac{3}{x}$ does not exist, yet
$\lim_{x \to 0} x \cdot \frac{3}{x} = 3 \neq 0$.
:::

*The correct approach uses the fact that
$\left\lvert \sin(1/x) \right\rvert \leq 1$, so
$-x^{2} \leq x^{2}\sin(1/x) \leq x^{2}$ for all $x \neq 0$. Both
$-x^{2}$ and $x^{2}$ have limit $0$ at $x = 0$. The function
$x^{2}\sin(1/x)$ is "squeezed" between them and must also have limit
$0$.*

::: theorem
[]{#thm:2-8 label="thm:2-8"} Let $a, L \in \mathbb{R}$, and let
$f, g, h$ be functions defined on an open interval containing $a$,
except possibly at $a$. Suppose:

1.  $h(x) \leq g(x) \leq f(x)$ for all $x$ sufficiently close to $a$
    (but $x \neq a$),

2.  $\lim_{x \to a} h(x) = L$ and $\lim_{x \to a} f(x) = L$.

Then $\lim_{x \to a} g(x) = L$.
:::

<figure id="fig:squeeze-theorem" data-latex-placement="ht">

<figcaption>A function trapped between two functions with the same
limit.</figcaption>
</figure>

::: example
[]{#ex:2-9 label="ex:2-9"} Since $-1 \leq \sin(1/x) \leq 1$ for all
$x \neq 0$, $$-x^{2} \leq x^{2}\sin(1/x) \leq x^{2}.$$ Both
$\lim_{x \to 0}(-x^{2}) = 0$ and $\lim_{x \to 0} x^{2} = 0$. By the
squeeze theorem ([\[thm:2-8\]](#thm:2-8){reference-type="ref+label"
reference="thm:2-8"}), $\lim_{x \to 0} x^{2}\sin(1/x) = 0$.
:::

## Proof of the Squeeze Theorem {#sec:2.13}

*We now prove [\[thm:2-8\]](#thm:2-8){reference-type="ref+label"
reference="thm:2-8"}. The proof follows the same pattern as the proof of
the sum law: use the hypotheses on $f$ and $h$ to find $\delta_{1}$ and
$\delta_{2}$, then combine them.*

::: proof
*Proof.* Strategy: for a given $\varepsilon$, use the limits of $f$ and
$h$ to obtain $\delta_{1}$ and $\delta_{2}$, then set
$\delta = \min\{\delta_{1}, \delta_{2}, p\}$, where $p$ controls the
region where the inequalities hold.

By hypothesis (i), there exists $p > 0$ such that for all $x$ with
$0 < \left\lvert x - a \right\rvert < p$, $$h(x) \leq g(x) \leq f(x).$$

Let $\varepsilon> 0$. Since $\lim_{x \to a} f(x) = L$, there exists
$\delta_{1} > 0$ such that
$$0 < \left\lvert x - a \right\rvert < \delta_{1} \implies \left\lvert f(x) - L \right\rvert < \varepsilon.$$
In particular, $f(x) < L + \varepsilon$.

Since $\lim_{x \to a} h(x) = L$, there exists $\delta_{2} > 0$ such that
$$0 < \left\lvert x - a \right\rvert < \delta_{2} \implies \left\lvert h(x) - L \right\rvert < \varepsilon.$$
In particular, $h(x) > L - \varepsilon$.

Take $\delta = \min\{\delta_{1}, \delta_{2}, p\} > 0$. Fix any $x$ with
$0 < \left\lvert x - a \right\rvert < \delta$. Then
$\left\lvert x-a \right\rvert < \delta_{2}$ gives
$h(x) > L - \varepsilon$; $\left\lvert x-a \right\rvert < p$ gives
$g(x) \geq h(x)$; $\left\lvert x-a \right\rvert < p$ also gives
$g(x) \leq f(x)$; and $\left\lvert x-a \right\rvert < \delta_{1}$ gives
$f(x) < L + \varepsilon$. Combining:
$$L - \varepsilon< h(x) \leq g(x) \leq f(x) < L + \varepsilon.$$
Therefore $\left\lvert g(x) - L \right\rvert < \varepsilon$, as
required. ◻
:::

## Definition of Continuity {#sec:2.14}

*When we say a function is "continuous," we mean, informally, that its
graph can be sketched without lifting the pen from the paper. We now
make this precise.*

::: definition
[]{#def:2-5 label="def:2-5"} Let $a \in \mathbb{R}$, and let $f$ be a
function defined at least on an open interval containing $a$. We say $f$
is *continuous at $a$* if $$\lim_{x \to a} f(x) = f(a).$$ Equivalently,
this means three things:

1.  $\lim_{x \to a} f(x)$ exists (and is a real number),

2.  $f(a)$ is defined,

3.  the limit equals the value.

If $f$ is not continuous at $a$, we say it is *discontinuous* at $a$.
:::

::: definition
[]{#def:2-6 label="def:2-6"} Under the same hypotheses, $f$ is
continuous at $a$ if and only if for every $\varepsilon> 0$ there exists
$\delta > 0$ such that for all $x$,
$$\left\lvert x - a \right\rvert < \delta \implies \left\lvert f(x) - f(a) \right\rvert < \varepsilon.$$
:::

::: remark
Comparing [\[def:2-6\]](#def:2-6){reference-type="ref+label"
reference="def:2-6"} with
[\[def:2-2\]](#def:2-2){reference-type="ref+label" reference="def:2-2"},
the key difference is that we **no longer exclude** the case $x = a$.
For the definition of limit, the value at $a$ is irrelevant, so we write
$0 < \left\lvert x - a \right\rvert$ to exclude it. For continuity, we
**need** $f(a)$ to be the right value, so we allow $x = a$.
:::

::: remark
Roughly speaking:

- Limit: if $x$ is close to $a$ **but not** $a$, then $f(x)$ is close to
  $L$.

- Continuity: if $x$ is close to $a$, **including** $a$, then $f(x)$ is
  close to $f(a)$.

This distinction is the source of all subtleties when composing limits
versus composing continuous functions (see
[2.16](#sec:2.16){reference-type="ref+label" reference="sec:2.16"}).
:::

::: definition
[]{#def:2-7 label="def:2-7"}

1.  $f$ is *continuous on the open interval $(a, b)$* if $f$ is
    continuous at every point of $(a, b)$.

2.  $f$ is *continuous on the closed interval $[a, b]$* if $f$ is
    continuous on $(a, b)$, and in addition
    $$\lim_{x \to a^{+}} f(x) = f(a) \qquad\text{and}\qquad \lim_{x \to b^{-}} f(x) = f(b).$$

3.  If we say "$f$ is continuous" without specifying where, we mean
    *continuous on its domain*.
:::

::: remark
A function may be "continuous" (meaning continuous on its domain) and
yet fail to be continuous at a point not in its domain. For instance,
$f(x) = 1/x$ is continuous (on $\mathbb{R}\setminus \{0\}$), but it is
**not** continuous at $0$ (which is not in its domain). This is not a
contradiction; it is a consequence of the precise definitions.
:::

## Continuity of Elementary Functions {#sec:2.15}

*The following theorem is extremely useful: it tells us that almost
every function we encounter in practice is continuous on its domain, so
computing limits at points in the domain reduces to simple evaluation.*

::: theorem
[]{#thm:2-9 label="thm:2-9"} Any function built from polynomials, roots,
trigonometric functions, exponentials, logarithms, and absolute values
by means of addition, subtraction, multiplication, division, and
composition is continuous on its domain.
:::

::: remark
These functions are sometimes called *elementary functions*. The word
"elementary" does not mean "simple"; it is just the name for this class.
:::

::: example
[]{#ex:2-10 label="ex:2-10"} To compute
$\lim_{x \to 1} \dfrac{\sqrt{x^{3} + \sin x}}{e^{x} + 2}$, note that
this function is elementary and $x = 1$ is in its domain. Therefore
$$\lim_{x \to 1} \dfrac{\sqrt{x^{3} + \sin x}}{e^{x} + 2} = \dfrac{\sqrt{1 + \sin 1}}{e + 2}.$$
:::

::: remark
[\[thm:2-9\]](#thm:2-9){reference-type="ref+label" reference="thm:2-9"}
only applies **on the domain**. If the point in question is **not** in
the domain, one cannot simply "plug in." For example, $\sin(x)/x$ is not
defined at $0$, so the theorem does not tell us the limit there; a
separate argument is needed (see
[2.18](#sec:2.18){reference-type="ref+label" reference="sec:2.18"}).
:::

*How is [\[thm:2-9\]](#thm:2-9){reference-type="ref+label"
reference="thm:2-9"} proved? The strategy proceeds in two steps.*

**Step 1.** Prove that the "basic" building blocks---constant functions,
$f(x) = x$, $e^{x}$, $\ln x$, $\sin x$, and
$\left\lvert x \right\rvert$---are each continuous on their domains.

**Step 2.** Prove that sums, products, quotients, and compositions of
continuous functions are continuous.

For Step 2, sums, products, and quotients follow immediately from the
limit laws ([\[thm:2-7\]](#thm:2-7){reference-type="ref+label"
reference="thm:2-7"}). For instance:

::: proof
*Proof that the sum of continuous functions is continuous.* Strategy:
apply the sum law.

Let $f$ and $g$ be continuous at $a$. By definition,
$\lim_{x \to a} f(x) = f(a)$ and $\lim_{x \to a} g(x) = g(a)$. By the
sum law ([\[thm:2-7\]](#thm:2-7){reference-type="ref+label"
reference="thm:2-7"}):
$$\lim_{x \to a}\bigl[f(x) + g(x)\bigr] = f(a) + g(a) = (f + g)(a).$$

Hence $f + g$ is continuous at $a$. ◻
:::

*Composition requires a separate argument, which is the subject of the
next section.*

## Limits and Composition of Functions {#sec:2.16}

*One might expect that "the limit of a composition is the composition of
the limits," just as for sums and products. Surprisingly, this is
**false** in general. Understanding why it fails---and when it can be
salvaged---illuminates the crucial difference between limits and
continuity.*

::: remark
Recall the key distinction:

- $\lim_{x \to a} f(x) = L$: if $x$ is close to $a$ **but not** $a$,
  then $f(x)$ is close to $L$.

- $f$ continuous at $a$: if $x$ is close to $a$ **including** $a$, then
  $f(x)$ is close to $f(a)$.

Continuity has a symmetry between input and output that the limit
definition lacks. In a composition, the **output** of one function
becomes the **input** of the next, and this asymmetry causes trouble.
:::

::: remark
Before reading further, try to construct a function $f$ such that
$\lim_{x \to 0} f(x) = 0$ but $\lim_{x \to 0} f(f(x)) = 1$. This feels
counterintuitive, but it can be done with a simple piecewise function.
:::

*Here is the false statement, stated explicitly so that you know to
avoid it.*

::: remark
The following is **not** a theorem. Assuming $\lim_{x \to a} f(x) = L$
and $\lim_{y \to L} g(y) = M$, one **cannot** conclude that
$\lim_{x \to a} g(f(x)) = M$.
:::

*We now state the results that **are** true.*

::: theorem
[]{#thm:2-10 label="thm:2-10"} If $f$ is continuous at $a$ and $g$ is
continuous at $f(a)$, then $g \circ f$ is continuous at $a$.
:::

::: proof
*Proof.* Strategy: concatenate the two continuity implications.

Since $f$ is continuous at $a$: if $x$ is close to $a$, then $f(x)$ is
close to $f(a)$. Since $g$ is continuous at $f(a)$: if $y$ is close to
$f(a)$, then $g(y)$ is close to $g(f(a))$. Setting $y = f(x)$, we
obtain: if $x$ is close to $a$, then $g(f(x))$ is close to $g(f(a))$.
This says exactly that $g \circ f$ is continuous at $a$.

More formally: let $\varepsilon> 0$. Since $g$ is continuous at $f(a)$,
there exists $\eta > 0$ such that
$\left\lvert y - f(a) \right\rvert < \eta \implies \left\lvert g(y) - g(f(a)) \right\rvert < \varepsilon$.
Since $f$ is continuous at $a$, for this $\eta > 0$ there exists
$\delta > 0$ such that
$\left\lvert x - a \right\rvert < \delta \implies \left\lvert f(x) - f(a) \right\rvert < \eta$.
Combining:
$\left\lvert x - a \right\rvert < \delta \implies \left\lvert g(f(x)) - g(f(a)) \right\rvert < \varepsilon$. ◻
:::

::: theorem
[]{#thm:2-11 label="thm:2-11"} Suppose $\lim_{x \to a} f(x) = L$,
$\lim_{y \to L} g(y) = M$, and in addition $f(x) \neq L$ for all $x$ in
some open interval about $a$ (except possibly $x = a$). Then
$\lim_{x \to a} g(f(x)) = M$.
:::

::: theorem
[]{#thm:2-12 label="thm:2-12"} Suppose $\lim_{x \to a} f(x) = L$ and $g$
is **continuous** at $L$. Then $\lim_{x \to a} g(f(x)) = g(L)$.
:::

::: remark
Both
[\[thm:2-11,thm:2-12\]](#thm:2-11,thm:2-12){reference-type="ref+label"
reference="thm:2-11,thm:2-12"} add an extra hypothesis to the false
"theorem" in order to make it true.
[\[thm:2-11\]](#thm:2-11){reference-type="ref+label"
reference="thm:2-11"} strengthens the condition on $f$ (requiring
$f(x) \neq L$ near $a$), while
[\[thm:2-12\]](#thm:2-12){reference-type="ref+label"
reference="thm:2-12"} strengthens the condition on $g$ (upgrading from
"having a limit" to "being continuous"). Either fix suffices because
each repairs the mismatch between the "then" clause of one hypothesis
and the "if" clause of the other.
:::

## Types of Discontinuity {#sec:2.17}

*When a function is discontinuous at a point, it is traditional to
classify the discontinuity as removable or non-removable. The
classification tells us whether the function can be "fixed" by
redefining it at a single point.*

::: definition
[]{#def:2-8 label="def:2-8"} A function $f$ has a *removable
discontinuity* at $a$ if $\lim_{x \to a} f(x)$ exists but $f$ is not
continuous at $a$ (either because $f(a)$ is undefined or because $f(a)$
differs from the limit).
:::

::: definition
[]{#def:2-9 label="def:2-9"} A function $f$ has a *non-removable
discontinuity* at $a$ if $\lim_{x \to a} f(x)$ does not exist.
:::

::: example
[]{#ex:2-11 label="ex:2-11"} The function $h(x) = \dfrac{\sin x}{x}$ is
undefined at $0$, but $\lim_{x \to 0} h(x) = 1$ (see
[2.18](#sec:2.18){reference-type="ref+label" reference="sec:2.18"}).
Define a new function $$H(x) =
  \begin{cases}
    \dfrac{\sin x}{x} & \text{if } x \neq 0, \\[6pt]
    1 & \text{if } x = 0.
  \end{cases}$$ Then $H$ is continuous at $0$. We have "removed" the
discontinuity by filling the hole in the graph.
:::

::: remark
A removable discontinuity can always be fixed: define (or redefine) the
function at the point to equal the limit, and the result is continuous.
A non-removable discontinuity **cannot** be fixed by redefining the
function at a single point. Examples of non-removable discontinuities
include jumps (the two one-sided limits exist but differ), vertical
asymptotes, and wild oscillations.
:::

::: remark
In physics and applied mathematics, removable discontinuities are often
silently removed. When a physicist writes $\sin(x)/x$, they usually mean
the function $H$ above, with the hole filled in. In a pure-mathematics
course, we are more careful about the distinction.
:::

## The Limit of $\sin(x)/x$ {#sec:2.18}

*This is a classic proof using nothing but high-school geometry and the
squeeze theorem. It is a beautiful argument that relies on comparing the
areas of two triangles and a circular sector.*

::: theorem
[]{#thm:2-13 label="thm:2-13"}
$\displaystyle\lim_{x \to 0} \dfrac{\sin x}{x} = 1$.
:::

<figure id="fig:sinx-over-x" data-latex-placement="ht">

<figcaption>The graph of <span
class="math inline">sin (<em>x</em>)/<em>x</em></span> near <span
class="math inline">0</span>.</figcaption>
</figure>

*We begin by establishing a geometric inequality. Consider the unit
circle with a central angle $x \in (0, \frac{\pi}{2})$, and compare
three regions:*

1.  The triangle with vertices at the origin, the point
    $(\cos x, \sin x)$, and $(\cos x, 0)$ has area
    $\frac{1}{2}\cos x \sin x$.

2.  The circular sector of radius $1$ and angle $x$ has area
    $\frac{1}{2}x$.

3.  The triangle with vertices at the origin, $(1, 0)$, and
    $(1, \tan x)$ has area $\frac{1}{2}\tan x$.

::: lemma
[]{#lem:2-1 label="lem:2-1"} For $0 < x < \frac{\pi}{2}$,
$$\cos x \leq \dfrac{\sin x}{x} \leq \dfrac{1}{\cos x}.$$
:::

::: proof
*Proof.* Strategy: use the area comparison, then divide through by
$\sin x$ and take reciprocals.

Since the triangle (i) is contained in the sector (ii), which is
contained in triangle (iii):
$$\frac{1}{2}\cos x \sin x \;\leq\; \frac{1}{2}x \;\leq\; \frac{1}{2}\tan x = \frac{1}{2}\,\dfrac{\sin x}{\cos x}.$$
Multiplying through by $\dfrac{2}{\sin x} > 0$ gives
$$\cos x \;\leq\; \dfrac{x}{\sin x} \;\leq\; \dfrac{1}{\cos x}.$$ Taking
reciprocals (and reversing the inequalities) yields
$$\cos x \;\leq\; \dfrac{\sin x}{x} \;\leq\; \dfrac{1}{\cos x}.$$ The
derivation assumes $0 < x < \frac{\pi}{2}$. Since all three functions
$\cos x$, $\frac{\sin x}{x}$, and $\frac{1}{\cos x}$ are **even**, the
same inequalities hold for $-\frac{\pi}{2} < x < 0$. ◻
:::

::: proof
*Proof of [\[thm:2-13\]](#thm:2-13){reference-type="ref+label"
reference="thm:2-13"}.* Strategy: apply the squeeze theorem.

By [\[lem:2-1\]](#lem:2-1){reference-type="ref+label"
reference="lem:2-1"}, for
$0 < \left\lvert x \right\rvert < \frac{\pi}{2}$,
$$\cos x \;\leq\; \dfrac{\sin x}{x} \;\leq\; \dfrac{1}{\cos x}.$$ Since
$\cos$ is continuous at $0$ with $\cos 0 = 1$,
$$\lim_{x \to 0} \cos x = 1 \qquad\text{and}\qquad \lim_{x \to 0} \dfrac{1}{\cos x} = 1.$$
By the squeeze theorem
([\[thm:2-8\]](#thm:2-8){reference-type="ref+label"
reference="thm:2-8"}),
$\displaystyle\lim_{x \to 0} \dfrac{\sin x}{x} = 1$. ◻
:::

## Techniques for Computing Limits {#sec:2.19}

*We review the basic toolkit for computing limits at a point. Mastering
these techniques requires practice beyond what a single section can
provide, but this summary identifies what to try first.*

**Method 1: Direct evaluation.** If the function is continuous at the
point, evaluate.

::: example
[]{#ex:2-12 label="ex:2-12"}
$\displaystyle\lim_{x \to 2} \dfrac{x^{2} + 1}{\sqrt{x + 2}} = \dfrac{4 + 1}{\sqrt{4}} = \dfrac{5}{2}.$
:::

**Method 2: Algebraic manipulation.** If the function is not defined at
the point (often revealed by the indeterminate form $0/0$), try to
simplify. Common techniques include factoring, multiplying by
conjugates, and cancellation. The manipulations need only be valid
**near** the point, not **at** it.

::: example
[]{#ex:2-13 label="ex:2-13"} Compute
$\displaystyle\lim_{x \to 2} \dfrac{x^{2} - 4}{x - 2}$.

Attempting to evaluate gives $0/0$. Factor:
$$\dfrac{x^{2} - 4}{x - 2} = \dfrac{(x-2)(x+2)}{x-2} = x + 2, \qquad x \neq 2.$$
The simplified function is continuous at $2$, so the limit is $4$.
:::

::: example
[]{#ex:2-14 label="ex:2-14"} Compute
$\displaystyle\lim_{x \to 0} \dfrac{\sqrt{1 + x} - 1}{x}$.

Multiply numerator and denominator by the conjugate $\sqrt{1+x} + 1$:
$$\dfrac{\sqrt{1+x} - 1}{x} \cdot \dfrac{\sqrt{1+x}+1}{\sqrt{1+x}+1}
  = \dfrac{(1+x) - 1}{x(\sqrt{1+x}+1)}
  = \dfrac{1}{\sqrt{1+x} + 1}.$$ This is continuous at $0$, so the limit
is $\frac{1}{2}$.
:::

**Method 3: Reduction to a known limit.** Transform the expression into
one whose limit is already known, such as
$\lim_{x \to 0} \frac{\sin x}{x} = 1$.

::: example
[]{#ex:2-15 label="ex:2-15"} Compute
$\displaystyle\lim_{x \to 0} \dfrac{\sin(2x)}{x}$.

Write $\dfrac{\sin(2x)}{x} = 2 \cdot \dfrac{\sin(2x)}{2x}$. As
$x \to 0$, $2x \to 0$, so $\dfrac{\sin(2x)}{2x} \to 1$. Therefore the
limit is $2$.
:::

::: example
[]{#ex:2-16 label="ex:2-16"} Compute
$\displaystyle\lim_{x \to 0} \dfrac{\sin(2x)}{\sin(3x)}$.

Multiply and divide to create the standard form:
$$\dfrac{\sin(2x)}{\sin(3x)}
  = \dfrac{\sin(2x)}{2x} \cdot \dfrac{3x}{\sin(3x)} \cdot \dfrac{2}{3}.$$
Each ratio has limit $1$ as $x \to 0$, so the limit is $\dfrac{2}{3}$.
:::

::: example
[]{#ex:2-17 label="ex:2-17"} Compute
$\displaystyle\lim_{x \to 0} \dfrac{1 - \cos x}{x^{2}}$.

Multiply and divide by $1 + \cos x$:
$$\dfrac{1 - \cos x}{x^{2}} \cdot \dfrac{1 + \cos x}{1 + \cos x}
  = \dfrac{1 - \cos^{2} x}{x^{2}(1 + \cos x)}
  = \dfrac{\sin^{2} x}{x^{2}} \cdot \dfrac{1}{1 + \cos x}
  = \left(\dfrac{\sin x}{x}\right)^{\!2} \cdot \dfrac{1}{1 + \cos x}.$$
As $x \to 0$, $\left(\dfrac{\sin x}{x}\right)^{2} \to 1$ and
$\dfrac{1}{1 + \cos x} \to \dfrac{1}{2}$. Therefore the limit is
$\dfrac{1}{2}$.
:::

::: remark
These methods can be combined. More advanced methods exist---notably
L'Hôpital's rule (which requires derivatives) and Taylor series (which
requires power series)---but they belong to later chapters.
:::

## Limits at Infinity of Rational Functions {#sec:2.20}

*For rational functions and related expressions, limits at infinity are
computed by factoring out the highest power of $x$ and using the fact
that $\lim_{x \to \infty} 1/x = 0$.*

::: theorem
[]{#thm:2-14 label="thm:2-14"} The limit of a polynomial as
$x \to \infty$ is determined by its leading term. Specifically, if
$p(x) = a_{n}x^{n} + \cdots + a_{0}$ with $a_{n} \neq 0$, then
$$\lim_{x \to \infty} p(x) = \lim_{x \to \infty} a_{n}x^{n}.$$
:::

::: proof
*Proof.* Strategy: factor out $x^{n}$ and use
$\lim_{x \to \infty} 1/x = 0$.

Write
$$p(x) = x^{n}\!\left(a_{n} + \dfrac{a_{n-1}}{x} + \cdots + \dfrac{a_{0}}{x^{n}}\right).$$
As $x \to \infty$, each term $a_{k}/x^{n-k} \to 0$ for $k < n$, so the
factor in parentheses approaches $a_{n}$. Therefore $p(x)$ behaves like
$a_{n} x^{n}$. ◻
:::

::: example
[]{#ex:2-18 label="ex:2-18"}
$\displaystyle\lim_{x \to \infty} (2x^{3} - x^{2} + 5)$. The leading
term is $2x^{3} \to \infty$. So the limit is $\infty$.
:::

::: example
[]{#ex:2-19 label="ex:2-19"} Compute
$\displaystyle\lim_{x \to \infty} \dfrac{2x^{2} + 3}{3x^{2} - x + 1}$.

Factor out $x^{2}$ from both numerator and denominator:
$$\dfrac{2x^{2} + 3}{3x^{2} - x + 1}
  = \dfrac{x^{2}(2 + 3/x^{2})}{x^{2}(3 - 1/x + 1/x^{2})}
  = \dfrac{2 + 3/x^{2}}{3 - 1/x + 1/x^{2}}
  \;\xrightarrow{x \to \infty}\; \dfrac{2}{3}.$$
:::

::: example
[]{#ex:2-20 label="ex:2-20"} Compute
$\displaystyle\lim_{x \to \infty} \dfrac{x^{2} + \sqrt{x^{4} + 1}}{\sqrt{x^{4} + x^{2}} + x}$.

Factor $x^{4}$ inside each square root: $$\begin{align*}
  \dfrac{x^{2} + \sqrt{x^{4}(1 + 1/x^{4})}}{\sqrt{x^{4}(1 + 1/x^{2})} + x}
  &= \dfrac{x^{2} + x^{2}\sqrt{1 + 1/x^{4}}}{x^{2}\sqrt{1 + 1/x^{2}} + x} \\
  &= \dfrac{x^{2}\!\left(1 + \sqrt{1 + 1/x^{4}}\right)}{x^{2}\!\left(\sqrt{1 + 1/x^{2}} + 1/x\right)} \\
  &\xrightarrow{x \to \infty}\; \dfrac{1 + 1}{\sqrt{1} + 0} = 2.
\end{align*}$$ Alternatively, $\dfrac{1+1}{\sqrt{1}} = 2$ can also be
written as $\sqrt{2} \cdot \sqrt{2} = 2$. In either case the limit is
$2$.
:::

::: remark
The rule of thumb is: identify the dominant term (highest power of $x$)
in the numerator and denominator, factor it out, and simplify. This
method extends naturally to expressions involving roots: a term
$\sqrt{x^{2k}}$ behaves like $x^{k}$ for large positive $x$.
:::

## The Extreme Value Theorem {#sec:2.21}

*We now state a deep theorem guaranteeing that continuous functions on
closed intervals attain their maximum and minimum. The theorem does
**not** tell us how to find these extreme values---only that they
exist.*

::: definition
[]{#def:2-10 label="def:2-10"} Let $f$ be a function and
$I \subseteq \mathbb{R}$. We say $f$ has a *maximum on $I$* if there
exists $c \in I$ such that $f(x) \leq f(c)$ for all $x \in I$. The value
$f(c)$ is the maximum, attained *at* $c$. The definition of *minimum* is
analogous, with the inequality reversed.
:::

::: remark
The maximum is a value (the output $f(c)$); it occurs **at** a point $c$
in the domain. If we say "the maximum of $f$" without specifying the set
$I$, we mean the maximum on the entire domain of $f$.
:::

*Let us build intuition for when a maximum is guaranteed to exist by
examining some examples of functions that lack one.*

::: example
[]{#ex:2-21 label="ex:2-21"} The function $f(x) = x$ on the open
interval $(0, 1)$ has no maximum: $f$ gets arbitrarily close to $1$ but
never attains it, because $1 \notin (0,1)$.
:::

::: example
[]{#ex:2-22 label="ex:2-22"} A function with a vertical asymptote on a
half-open interval may fail to have a maximum because it is unbounded.
:::

::: remark
These examples suggest two necessary ingredients: the domain should
include its endpoints (a **closed** interval), and the function should
not blow up (it should be **continuous**).
:::

::: theorem
[]{#thm:2-15 label="thm:2-15"} If $f$ is continuous on the closed and
bounded interval $[a, b]$, then $f$ has a maximum and a minimum on
$[a, b]$.
:::

::: remark
This theorem is easy to state and use but **difficult to prove**. A
rigorous proof requires a careful treatment of the completeness of
$\mathbb{R}$ and is typically presented in a real analysis course. For
our purposes, the extensive examples above should make the statement
plausible.
:::

::: remark
Both hypotheses---continuity of $f$ and closedness/boundedness of the
interval---are essential. Removing either one can produce a function
without a maximum or minimum.
:::

::: remark
Can you construct a function that is **continuous** on the half-open
interval $(0, 1]$ and has **neither** a maximum **nor** a minimum? Hint:
sketch the graph first, then find an equation.
:::

## The Intermediate Value Theorem {#sec:2.22}

*The intermediate value theorem formalises something you already
believe: if a continuous function is negative at one point and positive
at another, it must be zero somewhere in between.*

::: example
[]{#ex:2-23 label="ex:2-23"} Consider the equation $x^{5} + 9x - 6 = 0$.
Let $f(x) = x^{5} + 9x - 6$. Then $f(0) = -6 < 0$ and $f(1) = 4 > 0$.
Since $f$ is a polynomial and hence continuous, the function must cross
zero somewhere in $(0, 1)$. By evaluating $f(0.5) < 0$, we can narrow
the root to $(0.5, 1)$, and so on.
:::

::: remark
This equation cannot be solved exactly using radicals (a fact provable
via Galois theory). Nevertheless, the intermediate value theorem
guarantees the existence of a solution, and successive bisection can
approximate it to any desired accuracy.
:::

::: theorem
[]{#thm:2-16 label="thm:2-16"} Let $f$ be continuous on the closed
interval $[a, b]$. If $M$ is any real number between $f(a)$ and $f(b)$,
then there exists $c \in (a, b)$ such that $f(c) = M$.
:::

*In the special case $M = 0$: if $f(a)$ and $f(b)$ have opposite signs
and $f$ is continuous on $[a, b]$, then $f$ has a root in $(a, b)$.*

::: remark
Like the extreme value theorem, the intermediate value theorem is easy
to understand and believe but **hard to prove** rigorously. A formal
proof relies on the completeness of $\mathbb{R}$ and belongs to a course
in real analysis. For us, what matters is:

1.  understanding the statement,

2.  recognising that it is a property of **continuous** functions (it
    can fail for discontinuous ones),

3.  knowing when we are using it.
:::

::: remark
Continuity is essential. A step function, for instance, can jump from a
negative value to a positive value without ever equalling zero.
:::

# Derivatives

## Definition of the Derivative {#sec:3.1}

*We want to define the "slope of a curve" at a point, but we only know
how to define the slope of a line. We might try to define derivative as
the slope of the tangent line, but what is a tangent line? Every naïve
definition of one of these concepts seems to rely on another equally
undefined concept. The only way to break the circle is to use limits.*

*Consider a curve---the graph of a function $f$---and two points $P$ and
$Q$ on the curve with $x$-coordinates $a$ and $b$, respectively. The
slope of the line through $P$ and $Q$ is $\frac{f(b)-f(a)}{b-a}$. Now
keep $P$ fixed and slide $Q$ toward $P$. As $Q$ approaches $P$, the line
through them becomes the tangent line at $P$. This motivates taking a
limit.*

::: definition
[]{#def:3-1 label="def:3-1"} Let $f$ be a function defined at least on
an open interval containing $a$. The *derivative of $f$ at $a$* is
$$f'(a) = \lim_{x \to a} \dfrac{f(x) - f(a)}{x - a},$$ provided this
limit exists. Equivalently, setting $h = x - a$,
$$f'(a) = \lim_{h \to 0} \dfrac{f(a+h) - f(a)}{h}.$$ These two
expressions are entirely the same; it is simply a change of variable.
:::

::: definition
[]{#def:3-2 label="def:3-2"} We say that $f$ is *differentiable at $a$*
when the limit in [\[def:3-1\]](#def:3-1){reference-type="ref+label"
reference="def:3-1"} exists. We say that $f$ is *differentiable*
(without qualification) when $f$ is differentiable at every point in its
domain.
:::

::: definition
[]{#def:3-3 label="def:3-3"} Let $f$ be differentiable at $a$. The
*tangent line* to the graph of $f$ at the point $(a, f(a))$ is the line
through $(a, f(a))$ with slope $f'(a)$. Its equation is
$$y = f(a) + f'(a)(x - a).$$
:::

::: remark
Notice that this definition of tangent line relies on the derivative,
which we defined independently using a limit. The tangent line is fully
determined by a point and a slope, and the derivative supplies that
slope.
:::

<figure id="fig:secant-to-tangent" data-latex-placement="ht">

<figcaption>Secant lines converging to the tangent line.</figcaption>
</figure>

::: example
[]{#ex:3-1 label="ex:3-1"} Consider a function $f$ whose graph is given.
To compute $f'(0)$, find the point on the graph with $x$-coordinate $0$
and draw the tangent line there. If that line has slope $2$, then
$f'(0) = 2$. Similarly, if the tangent line at the point with
$x$-coordinate $-1$ is horizontal, then $f'(-1) = 0$.
:::

## Derivatives from the Definition {#sec:3.2}

*We now illustrate how to compute a derivative directly from the limit
definition. This is the foundational method; later, differentiation
rules will spare us the effort of returning to the definition each
time.*

::: example
[]{#ex:3-2 label="ex:3-2"} Let $f(x) = 4x - x^{2}$. Compute $f'(1)$ from
the definition.

Using the $h$-form of the definition: $$\begin{align*}
  f'(1)
  &= \lim_{h \to 0} \dfrac{f(1+h) - f(1)}{h} \\
  &= \lim_{h \to 0} \dfrac{\bigl[4(1+h) - (1+h)^{2}\bigr] - \bigl[4(1) - 1^{2}\bigr]}{h} \\
  &= \lim_{h \to 0} \dfrac{4 + 4h - 1 - 2h - h^{2} - 3}{h} \\
  &= \lim_{h \to 0} \dfrac{2h - h^{2}}{h} \\
  &= \lim_{h \to 0} (2 - h) \\
  &= 2.
\end{align*}$$ After all cancellations we are left with a continuous
function, and evaluating at $h = 0$ gives $f'(1) = 2$.
:::

::: remark
Computing derivatives from the definition is tedious for any function
more complicated than a simple polynomial. The **differentiation
rules**, introduced in [3.4](#sec:3.4){reference-type="ref+label"
reference="sec:3.4"}, provide a much faster method. We still need to
prove them from the definition, but once proven, they can be reused
indefinitely.
:::

## Derivative as Rate of Change {#sec:3.3}

*The derivative has a second fundamental interpretation: rate of change.
To motivate it, consider a familiar example---velocity.*

*Suppose you are driving at $180\,\text{km/h}$. What does that mean? It
does not literally mean you will drive $180\,\text{km}$ in the next
hour; your velocity may change. A better interpretation: over a very
small time interval $\Delta t$, you travel approximately
$180\,\text{km/h}\cdot\Delta t$, and this approximation improves as
$\Delta t$ shrinks. There is a limit lurking here. It is impossible to
define velocity---or any instantaneous rate of change---without limits.*

::: definition
[]{#def:3-4 label="def:3-4"} Let $x$ denote the position of a particle
as a function of time $t$.

1.  The *average velocity* between times $t_{1}$ and $t_{2}$ is
    $$\dfrac{\Delta x}{\Delta t} = \dfrac{x(t_{2}) - x(t_{1})}{t_{2} - t_{1}}.$$

2.  The *instantaneous velocity* at time $t_{1}$ is
    $$\left.\dfrac{dx}{dt}\right|_{t=t_{1}} = \lim_{t_{2} \to t_{1}} \dfrac{x(t_{2}) - x(t_{1})}{t_{2} - t_{1}} = \lim_{\Delta t \to 0} \dfrac{\Delta x}{\Delta t}.$$
:::

::: remark
The notation $\frac{dx}{dt}$ does **not** mean a number $dx$ divided by
a number $dt$. The symbols $dx$ and $dt$ are not numbers. Rather,
$\frac{dx}{dt}$ denotes the limit of $\frac{\Delta x}{\Delta t}$ as
$\Delta t \to 0$. We call it the *derivative of $x$ with respect to
$t$*.
:::

::: definition
[]{#def:3-5 label="def:3-5"} More generally, if $Q$ is a physical
quantity that depends on another quantity $x$, the *instantaneous rate
of change of $Q$ with respect to $x$* is
$$\dfrac{dQ}{dx} = \lim_{\Delta x \to 0} \dfrac{\Delta Q}{\Delta x}.$$
:::

::: remark
The two notions of derivative---$f'(a)$ for an abstract function, and
$\frac{dx}{dt}$ for a physical quantity---are the **same concept**. If
position $x$ is given by a function $f(t)$, then
$$\dfrac{dx}{dt}\bigg|_{t = t_{1}}
  = \lim_{t_{2} \to t_{1}} \dfrac{f(t_{2}) - f(t_{1})}{t_{2} - t_{1}}
  = f'(t_{1}).$$ Whether we think of derivative as slope, as
instantaneous rate of change, or as instantaneous velocity, we always
arrive at the same limit.
:::

<figure id="fig:rate-of-change" data-latex-placement="ht">

<figcaption>Slope of the tangent as instantaneous rate of
change.</figcaption>
</figure>

## Basic Differentiation Rules {#sec:3.4}

*Computing every derivative from the definition is slow and often messy.
The differentiation rules let us compute derivatives of common functions
quickly. Each rule must be proved from the definition, but once proved
it can be reused without limit.*

*Here are the basic rules, presented first in a "lazy" form that
suppresses hypotheses. A precise statement of the product rule follows
as an illustration of what the "proper" version looks like.*

::: theorem
[]{#thm:3-1 label="thm:3-1"} Let $f$ and $g$ be differentiable
functions, and let $c$ be a real constant.

1.  **Constant rule.** $\dfrac{d}{dx}[c] = 0$.

2.  **Power rule.** For every $c \in \mathbb{R}$,
    $\dfrac{d}{dx}\!\left[x^{c}\right] = c\,x^{c-1}$.

3.  **Sum rule.** $(f + g)' = f' + g'$.

4.  **Constant multiple rule.** $(c \cdot f)' = c \cdot f'$.

5.  **Product rule.** $(f \cdot g)' = f'\,g + f\,g'$.

6.  **Quotient rule.**
    $\left(\dfrac{f}{g}\right)' = \dfrac{f'\,g - f\,g'}{g^{2}}$,
    provided $g \neq 0$.
:::

::: theorem
[]{#thm:3-2 label="thm:3-2"} Let $a \in \mathbb{R}$, and let $f$ and $g$
be functions defined on an open interval containing $a$. Define
$h = f \cdot g$. If $f$ and $g$ are both differentiable at $a$, then $h$
is also differentiable at $a$, and
$$h'(a) = f'(a)\,g(a) + f(a)\,g'(a).$$
:::

::: remark
The **if--then** structure matters. The product rule requires both $f$
and $g$ to be differentiable individually. If one or both are not
differentiable, the formula does not apply, although the product may
still have a derivative that must be computed by other means (e.g., the
definition).
:::

::: example
[]{#ex:3-3 label="ex:3-3"} Compute the derivative of
$p(x) = 3x^{4} - 5x^{2} + 7x - 2$.

A polynomial is a sum of terms, each a constant times a power. By the
sum and constant multiple rules, $$\begin{align*}
  p'(x)
  &= 3 \cdot 4x^{3} - 5 \cdot 2x + 7 \cdot 1 - 0 \\
  &= 12x^{3} - 10x + 7.
\end{align*}$$
:::

::: example
[]{#ex:3-4 label="ex:3-4"} Compute the derivative of
$q(x) = \dfrac{x - 1}{x^{2} + x}$.

By the quotient rule: $$\begin{align*}
  q'(x)
  &= \dfrac{(1)(x^{2} + x) - (x - 1)(2x + 1)}{(x^{2} + x)^{2}} \\
  &= \dfrac{x^{2} + x - 2x^{2} - x + 2x + 1}{(x^{2} + x)^{2}} \\
  &= \dfrac{-x^{2} + 2x + 1}{(x^{2} + x)^{2}}.
\end{align*}$$
:::

::: example
[]{#ex:3-5 label="ex:3-5"} The power rule works for **all** real
exponents, not only positive integers.

1.  Writing $\frac{1}{x^{3}} = x^{-3}$, we get
    $\dfrac{d}{dx}\!\left[x^{-3}\right] = -3x^{-4} = -\dfrac{3}{x^{4}}$.

2.  Writing $\sqrt{x} = x^{1/2}$, we get
    $\dfrac{d}{dx}\!\left[x^{1/2}\right] = \dfrac{1}{2}\,x^{-1/2} = \dfrac{1}{2\sqrt{x}}$.
:::

## Differentiability and Continuity {#sec:3.5}

*One of the first theoretical results about derivatives is that
differentiability is a stronger condition than continuity: every
differentiable function is continuous, but not conversely. We first give
an informal argument explaining why, and then a formal proof.*

::: theorem
[]{#thm:3-3 label="thm:3-3"} Let $c \in \mathbb{R}$, and let $f$ be a
function defined on an open interval containing $c$. If $f$ is
differentiable at $c$, then $f$ is continuous at $c$.
:::

::: remark
The converse is **false**. There exist functions that are continuous at
a point but not differentiable there. See
[3.9](#sec:3.9){reference-type="ref+label" reference="sec:3.9"} for
examples.
:::

*Before the formal proof, here is an informal explanation. Continuity
means $\lim_{x \to c} f(x) = f(c)$, or equivalently
$\lim_{x \to c}[f(x) - f(c)] = 0$. When we try to compute $f'(c)$ from
continuity alone, the defining limit $\frac{f(x)-f(c)}{x-c}$ gives the
indeterminate form $\frac{0}{0}$, which may or may not exist. But if $f$
is not even continuous at $c$, the numerator does not approach $0$ while
the denominator does, and the limit can never exist. So non-continuity
forces non-differentiability.*

::: proof
*Proof.* We show that $\lim_{x \to c}[f(x) - f(c)] = 0$.

Multiply and divide by $x - c$: $$\begin{align*}
  \lim_{x \to c}\bigl[f(x) - f(c)\bigr]
  &= \lim_{x \to c}\left[\dfrac{f(x) - f(c)}{x - c} \cdot (x - c)\right] \\
  &= \left(\lim_{x \to c} \dfrac{f(x) - f(c)}{x - c}\right) \cdot \left(\lim_{x \to c}(x - c)\right) \\
  &= f'(c) \cdot 0 \\
  &= 0.
\end{align*}$$

The product law for limits applies because both individual limits exist:
the first is $f'(c)$ (by the hypothesis of differentiability), and the
second is $0$. We are **not** claiming that $0$ times "anything" is $0$;
we are using the fact that $0$ times a **number** is $0$.

Since $\lim_{x \to c}[f(x) - f(c)] = 0$, we conclude
$\lim_{x \to c} f(x) = f(c)$, and $f$ is continuous at $c$. ◻
:::

## Proof of the Product Rule {#sec:3.6}

*We now prove the product rule formally. The key trick is to add and
subtract a carefully chosen term in order to factor out the derivatives
of $f$ and $g$ separately.*

::: proof
*Proof of [\[thm:3-2\]](#thm:3-2){reference-type="ref+label"
reference="thm:3-2"}.* We compute $h'(a)$ from the definition.

Write $h(x) = f(x)\,g(x)$, so $$\begin{align*}
  h'(a)
  &= \lim_{x \to a} \dfrac{h(x) - h(a)}{x - a} \\
  &= \lim_{x \to a} \dfrac{f(x)\,g(x) - f(a)\,g(a)}{x - a}.
\end{align*}$$ Add and subtract $f(a)\,g(x)$ in the numerator:
$$\begin{align*}
  &= \lim_{x \to a} \dfrac{f(x)\,g(x) - f(a)\,g(x) + f(a)\,g(x) - f(a)\,g(a)}{x - a} \\
  &= \lim_{x \to a} \left[\dfrac{f(x) - f(a)}{x - a}\cdot g(x) + f(a) \cdot \dfrac{g(x) - g(a)}{x - a}\right].
\end{align*}$$ Apply the limit laws (sum and product of limits):
$$\begin{align*}
  &= \left(\lim_{x \to a} \dfrac{f(x)-f(a)}{x-a}\right)\!\left(\lim_{x \to a} g(x)\right) + f(a)\!\left(\lim_{x \to a}\dfrac{g(x)-g(a)}{x-a}\right) \\
  &= f'(a)\,g(a) + f(a)\,g'(a).
\end{align*}$$

Three individual limits were used. The first is $f'(a)$, which exists by
hypothesis. The third is $g'(a)$, which exists by hypothesis. The second
is $\lim_{x \to a} g(x) = g(a)$; this holds because $g$ is
differentiable at $a$, and differentiability implies continuity
([\[thm:3-3\]](#thm:3-3){reference-type="ref+label"
reference="thm:3-3"}). ◻
:::

## Proof of the Power Rule {#sec:3.7}

*The power rule states that $\frac{d}{dx}[x^{c}] = c\,x^{c-1}$ for every
real number $c$. A proof for all real exponents requires heavy machinery
(in particular, logarithmic differentiation). Here we present a proof
for the case when $c$ is a positive integer, using induction.*

::: theorem
[]{#thm:3-4 label="thm:3-4"} For every positive integer $n$,
$$\dfrac{d}{dx}\!\left[x^{n}\right] = n\,x^{n-1}.$$
:::

::: proof
*Proof.* We proceed by induction on $n$.

**Base case** ($n = 1$). Define $f(x) = x$. By the definition of
derivative, $$\begin{align*}
  f'(x) &= \lim_{h \to 0} \dfrac{(x+h) - x}{h} = \lim_{h \to 0} \dfrac{h}{h} = \lim_{h \to 0} 1 = 1 = 1 \cdot x^{0}.
\end{align*}$$ So the formula holds when $n = 1$.

**Induction step.** Fix a positive integer $n$ and assume
$$\dfrac{d}{dx}\!\left[x^{n}\right] = n\,x^{n-1}.$$ We must show the
formula holds for $n + 1$. Write $x^{n+1} = x^{n} \cdot x$ and apply the
product rule: $$\begin{align*}
  \dfrac{d}{dx}\!\left[x^{n+1}\right]
  &= \dfrac{d}{dx}\!\left[x^{n}\right] \cdot x + x^{n} \cdot \dfrac{d}{dx}[x] \\
  &= n\,x^{n-1} \cdot x + x^{n} \cdot 1 \\
  &= n\,x^{n} + x^{n} \\
  &= (n+1)\,x^{n}.
\end{align*}$$

This is exactly the power-rule formula with exponent $n + 1$. By
induction, the formula holds for every positive integer $n$. ◻
:::

## Higher-Order Derivatives {#sec:3.8}

*Since the derivative of a function is itself a function, we can
differentiate again, and again, and so on. There are two standard
systems of notation for these repeated derivatives, and it is useful to
be comfortable with both.*

::: definition
[]{#def:3-6 label="def:3-6"} Let $f$ be a function. Its successive
derivatives are denoted:

1.  $f'$ --- the first derivative (or simply the derivative),

2.  $f''$ --- the second derivative,

3.  $f'''$ --- the third derivative,

4.  $f^{(n)}$ --- the $n$th derivative, for any positive integer $n$.

Each is defined whenever the preceding derivative exists and is itself
differentiable.
:::

::: remark
The parentheses around $n$ in $f^{(n)}$ are essential. Without them,
$f^{n}$ is ambiguous: for trigonometric functions, $\sin^{2} x$
conventionally means $(\sin x)^{2}$; in other contexts, a superscript
may denote iterated composition. With the parentheses, $f^{(n)}$
unambiguously means the $n$th derivative.
:::

::: definition
[]{#def:3-7 label="def:3-7"} If $y$ is a function of $x$, we write
$$\dfrac{dy}{dx},\quad \dfrac{d^{2}y}{dx^{2}},\quad \dfrac{d^{3}y}{dx^{3}},\quad \ldots,\quad \dfrac{d^{n}y}{dx^{n}}$$
for the first, second, third, ..., $n$th derivatives of $y$ with respect
to $x$. Think of $\frac{d}{dx}$ as an *operator*;
$\frac{d^{n}y}{dx^{n}}$ means "apply the operator $\frac{d}{dx}$ to $y$
a total of $n$ times."
:::

::: remark
The placement of the exponents in $\frac{d^{n}y}{dx^{n}}$ is deliberate.
The $n$ in the numerator records the number of differentiations applied
to $y$; the $n$ in the denominator records that all differentiations
were with respect to $x$. This notation also keeps track of physical
dimensions. For example, if $x$ is position measured in metres and $t$
is time in seconds, then velocity $\frac{dx}{dt}$ has units
$\text{m}/\text{s}$ and acceleration $\frac{d^{2}x}{dt^{2}}$ has units
$\text{m}/\text{s}^{2}$.
:::

::: example
[]{#ex:3-6 label="ex:3-6"} Let $f(x) = x^{7}$. Then
$$f'(x) = 7x^{6},\quad f''(x) = 42x^{5},\quad f'''(x) = 210x^{4},\quad \ldots,\quad f^{(7)}(x) = 7!,\quad f^{(8)}(x) = 0.$$
After seven applications of the power rule, all powers of $x$ are
exhausted and every subsequent derivative is $0$.
:::

## Non-Differentiable Functions {#sec:3.9}

*We know from [\[thm:3-3\]](#thm:3-3){reference-type="ref+label"
reference="thm:3-3"} that every differentiable function is continuous.
Any discontinuous function is therefore automatically
non-differentiable. More interesting are functions that are continuous
yet still fail to be differentiable. We examine two specific ways this
can occur.*

*Recall: $f$ is not differentiable at $a$ when the limit
$\lim_{x \to a}\frac{f(x)-f(a)}{x-a}$ does not exist. Like any limit, it
may fail to exist for various reasons. We focus on two:*

1.  *the two one-sided limits exist but are different (a **corner**),
    or*

2.  *the limit is $\pm\infty$ (a **vertical tangent line**).*

::: definition
[]{#def:3-8 label="def:3-8"} A function $f$ has a *corner* at $x = a$ if
$f$ is continuous at $a$, but the limit
$$\lim_{x \to a} \dfrac{f(x) - f(a)}{x - a}$$ does not exist because the
left-hand and right-hand limits are different (both finite).
:::

::: example
[]{#ex:3-7 label="ex:3-7"} Let $f(x) = \left\lvert x \right\rvert$. We
test differentiability at $0$:
$$\lim_{x \to 0} \dfrac{\left\lvert x \right\rvert - 0}{x - 0} = \lim_{x \to 0} \dfrac{\left\lvert x \right\rvert}{x}.$$
$$\begin{align*}
  \lim_{x \to 0^{+}} \dfrac{\left\lvert x \right\rvert}{x} &= \lim_{x \to 0^{+}} \dfrac{x}{x} = 1, \\
  \lim_{x \to 0^{-}} \dfrac{\left\lvert x \right\rvert}{x} &= \lim_{x \to 0^{-}} \dfrac{-x}{x} = -1.
\end{align*}$$ Since the one-sided limits disagree, $f'(0)$ does not
exist. The graph has a corner at the origin: the slope from the right is
$1$ and the slope from the left is $-1$.
:::

<figure id="fig:cusp-abs" data-latex-placement="ht">

<figcaption>A corner: continuous but not differentiable at the
corner.</figcaption>
</figure>

::: definition
[]{#def:3-9 label="def:3-9"} A function $f$ has a *vertical tangent
line* at $x = a$ if $f$ is continuous at $a$ and
$$\lim_{x \to a} \dfrac{f(x) - f(a)}{x - a} = +\infty \quad\text{or}\quad -\infty.$$
:::

::: example
[]{#ex:3-8 label="ex:3-8"} Let $g(x) = x^{1/3}$. We check
differentiability at $0$:
$$\lim_{x \to 0} \dfrac{x^{1/3} - 0}{x - 0} = \lim_{x \to 0} \dfrac{1}{x^{2/3}} = +\infty.$$
The derivative at $0$ does not exist; the graph has a vertical tangent
line at the origin.
:::

::: remark
For $x \neq 0$, the power rule gives $g'(x) = \frac{1}{3}\,x^{-2/3}$,
and one may verify that $\lim_{x \to 0} g'(x) = +\infty$ as well. It is
possible to prove (using L'Hôpital's rule) that if
$\lim_{x \to a} f'(x) = \pm\infty$, then
$\lim_{x \to a}\frac{f(x)-f(a)}{x-a} = \pm\infty$ also. In practice,
computing $\lim_{x \to a} f'(x)$ is often easier.
:::

::: remark
A vertical tangent line is **not** the same as a vertical asymptote. A
vertical asymptote occurs when the function itself is undefined at a
point and $\lim_{x \to a} f(x) = \pm\infty$. A vertical tangent line
occurs when $f$ is continuous at $a$ but the *derivative* tends to
$\pm\infty$. Do not confuse the two.
:::

## Chain Rule Examples {#sec:3.10}

*The chain rule is the differentiation rule for compositions of
functions. Before stating it formally, we build intuition through
examples.*

::: example
[]{#ex:3-9 label="ex:3-9"} Compute
$\dfrac{d}{dx}\!\left[\sqrt{x^{3}+1}\right]$.

The derivative of $\sqrt{x}$ is $\frac{1}{2\sqrt{x}}$. By the chain
rule, replace the argument $x$ with $x^{3}+1$, then multiply by the
derivative of the inner function:
$$\dfrac{d}{dx}\!\left[\sqrt{x^{3}+1}\right]
  = \dfrac{1}{2\sqrt{x^{3}+1}} \cdot 3x^{2}
  = \dfrac{3x^{2}}{2\sqrt{x^{3}+1}}.$$
:::

::: example
[]{#ex:3-10 label="ex:3-10"} Compute
$\dfrac{d}{dx}\!\left[\sin(6x)\right]$.

The derivative of $\sin(x)$ is $\cos(x)$. By the chain rule:
$$\dfrac{d}{dx}\!\left[\sin(6x)\right] = \cos(6x) \cdot 6 = 6\cos(6x).$$
:::

::: example
[]{#ex:3-11 label="ex:3-11"} Compute
$\dfrac{d}{dx}\!\left[(x^{2}+1)^{100}\right]$.

Rather than expanding the polynomial, apply the chain rule. The
derivative of $x^{100}$ is $100x^{99}$, so:
$$\dfrac{d}{dx}\!\left[(x^{2}+1)^{100}\right]
  = 100(x^{2}+1)^{99} \cdot 2x
  = 200x\,(x^{2}+1)^{99}.$$
:::

::: remark
In each example, identify the "outer" and "inner" functions, take the
derivative of the outer as if the inner were the variable, and then
multiply by the derivative of the inner. Practice this pattern on
several compositions before moving on.
:::

## Chain Rule Statement and Proof {#sec:3.11}

*We now state the chain rule precisely, discuss the notation carefully,
and attempt a proof.*

*Some students find calculations with specific functions easy but become
confused when the chain rule is written for abstract functions $f$ and
$g$. The key is to be strict about distinguishing the **name** of a
function (e.g., $f$) from its **value** at a point (e.g., $f(x)$). The
name of the composed function is $f \circ g$; its value at $x$ is
$f(g(x))$.*

::: theorem
[]{#thm:3-5 label="thm:3-5"} Let $a \in \mathbb{R}$, and let $f$ and $g$
be functions such that $g$ is defined on an open interval containing $a$
and $f$ is defined on an open interval containing $g(a)$. If $g$ is
differentiable at $a$ and $f$ is differentiable at $g(a)$, then
$f \circ g$ is differentiable at $a$ and
$$(f \circ g)'(a) = f'\!\bigl(g(a)\bigr) \cdot g'(a).$$
:::

::: example
[]{#ex:3-12 label="ex:3-12"} Revisiting $\sqrt{x^{3}+1}$: set
$g(x) = x^{3}+1$ and $f(u) = \sqrt{u}$. Then $f(g(x)) = \sqrt{x^{3}+1}$,
and
$$(f \circ g)'(x) = f'\!\bigl(g(x)\bigr) \cdot g'(x) = \dfrac{1}{2\sqrt{x^{3}+1}} \cdot 3x^{2}.$$
Here $f'(u) = \frac{1}{2\sqrt{u}}$, evaluated at $u = g(x) = x^{3}+1$,
gives $f'(g(x)) = \frac{1}{2\sqrt{x^{3}+1}}$.
:::

*It is natural to try to prove the chain rule by writing the derivative
from the definition and factoring in a suggestive way. The following
argument is instructive, despite a gap that prevents it from being fully
rigorous.*

::: proof
*Proof attempt.* By the definition of derivative, $$\begin{align*}
  (f \circ g)'(a)
  &= \lim_{x \to a} \dfrac{f(g(x)) - f(g(a))}{x - a}.
\end{align*}$$ Multiply and divide by $g(x) - g(a)$: $$\begin{align*}
  &= \lim_{x \to a} \dfrac{f(g(x)) - f(g(a))}{g(x) - g(a)} \cdot \dfrac{g(x) - g(a)}{x - a}.
\end{align*}$$ If both limits exist and the product law applies, the
second factor tends to $g'(a)$. For the first factor, setting
$u = g(x)$, as $x \to a$ we have $u \to g(a)$ (since differentiability
implies continuity), and the limit becomes $f'(g(a))$.

**Gap.** In the second step we divided by $g(x) - g(a)$. We know
$x \neq a$, but $g(x)$ may equal $g(a)$ for values of $x$ arbitrarily
close to $a$, causing division by zero. For "most" functions encountered
in practice this does not happen, but pathological examples exist. A
fully rigorous proof avoids this division entirely; such proofs
typically use more sophisticated tools and are usually presented in a
multivariable-calculus or analysis course. ◻
:::

::: remark
In Leibniz notation, with $u = g(x)$ and $y = f(u)$, the chain rule
reads $$\dfrac{dy}{dx} = \dfrac{dy}{du} \cdot \dfrac{du}{dx}.$$ This is
suggestive---it looks as if we "cancel the $du$ "---but remember that
$\frac{dy}{du}$ is not a fraction of numbers. The notation is a
convenient mnemonic, not a cancellation.
:::

## Trigonometric Derivatives {#sec:3.12}

*We derive the derivatives of the six trigonometric functions. The
strategy is to do the hard work only once---prove the derivative of
$\sin$ from the definition---and then obtain the rest using algebraic
identities, the chain rule, and the quotient rule.*

::: theorem
[]{#thm:3-6 label="thm:3-6"}

1.  $\dfrac{d}{dx}[\sin x] = \cos x$.

2.  $\dfrac{d}{dx}[\cos x] = -\sin x$.

3.  $\dfrac{d}{dx}[\tan x] = \sec^{2} x$.

4.  $\dfrac{d}{dx}[\cot x] = -\csc^{2} x$.

5.  $\dfrac{d}{dx}[\sec x] = \sec x \tan x$.

6.  $\dfrac{d}{dx}[\csc x] = -\csc x \cot x$.
:::

::: remark
The derivatives of $\cos$, $\cot$, and $\csc$ are obtained from those of
$\sin$, $\tan$, and $\sec$ by inserting a minus sign and swapping
$\sin \leftrightarrow \cos$, $\tan \leftrightarrow \cot$,
$\sec \leftrightarrow \csc$. Memorise the first three; the other three
can be re-derived in seconds.
:::

*The proof strategy is as follows. **Step 1:** Prove
$\frac{d}{dx}[\sin x] = \cos x$ directly from the definition, using two
previously established limits. **Step 2:** Write
$\cos x = \sin\!\left(\frac{\pi}{2} - x\right)$ and apply the chain
rule. **Step 3:** Express the remaining four functions as quotients of
$\sin$ and $\cos$, and use the quotient rule.*

::: proof
*Proof of *(i)*.* We compute $\frac{d}{dx}[\sin x]$ from the definition.

By the angle-addition formula
$\sin(x+h) = \sin x \cos h + \cos x \sin h$: $$\begin{align*}
  \dfrac{d}{dx}[\sin x]
  &= \lim_{h \to 0} \dfrac{\sin(x+h) - \sin x}{h} \\
  &= \lim_{h \to 0} \dfrac{\sin x \cos h + \cos x \sin h - \sin x}{h} \\
  &= \lim_{h \to 0} \left[\sin x \cdot \dfrac{\cos h - 1}{h} + \cos x \cdot \dfrac{\sin h}{h}\right].
\end{align*}$$ For the purpose of this limit, $x$ is fixed, so $\sin x$
and $\cos x$ are constants. By the limit laws: $$\begin{align*}
  &= \sin x \cdot \lim_{h \to 0} \dfrac{\cos h - 1}{h} + \cos x \cdot \lim_{h \to 0} \dfrac{\sin h}{h} \\
  &= \sin x \cdot 0 + \cos x \cdot 1 \\
  &= \cos x.
\end{align*}$$

The two key limits, $\lim_{h \to 0}\frac{\sin h}{h} = 1$ and
$\lim_{h \to 0}\frac{\cos h - 1}{h} = 0$, were established earlier using
only geometry and trigonometry, with no reliance on derivatives. ◻
:::

::: remark
Derive the formulas for $\frac{d}{dx}[\cos x]$, $\frac{d}{dx}[\tan x]$,
and $\frac{d}{dx}[\sec x]$ using the chain rule and quotient rule. These
are quick exercises and worth doing at least once.
:::

::: remark
It is tempting to compute $\lim_{h \to 0}\frac{\sin h}{h}$ using
L'Hôpital's rule. But L'Hôpital's rule requires knowing
$\frac{d}{dx}[\sin x] = \cos x$, which in turn requires knowing that
$\lim_{h \to 0}\frac{\sin h}{h} = 1$. Using L'Hôpital's rule here is
circular. This limit must be established by elementary means first.
:::

## Implicit Differentiation {#sec:3.13}

*Implicit differentiation is not a new rule; it is a clever application
of the chain rule. When a relation between $x$ and $y$ is given
implicitly---that is, not solved for $y$---we can still compute
$\frac{dy}{dx}$ by differentiating both sides with respect to $x$,
treating $y$ as an unknown function of $x$.*

To build intuition, consider the equation of a circle: $x^2 + y^2 = 25$.
We could solve for $y$ explicitly as $y = \pm\sqrt{25 - x^2}$ and
differentiate using the chain rule. However, this requires handling the
positive and negative cases separately and dealing with messy square
roots.

Instead, we can differentiate the original equation directly. The key is
to remember that $y$ is a function of $x$. When we differentiate a term
with $y$, we must apply the chain rule.

::: example
[]{#ex:3-13-simple label="ex:3-13-simple"} Find $\frac{dy}{dx}$ for the
circle $x^2 + y^2 = 25$.

Differentiate both sides with respect to $x$: $$\begin{align*}
  \frac{d}{dx}[x^2 + y^2] &= \frac{d}{dx}[25] \\
  2x + 2y \frac{dy}{dx} &= 0
\end{align*}$$ Notice the $2y \frac{dy}{dx}$ term: the derivative of the
outside function $(\cdot)^2$ is $2y$, and we multiply by the derivative
of the inside function $y$, which is $\frac{dy}{dx}$.

Now, isolate $\frac{dy}{dx}$: $$\begin{align*}
  2y \frac{dy}{dx} &= -2x \\
  \frac{dy}{dx} &= -\frac{2x}{2y} = -\frac{x}{y}
\end{align*}$$ This gives us a formula for the slope at any point
$(x, y)$ on the circle.
:::

### General Technique Outline {#general-technique-outline .unnumbered}

From this intuition, we can generalize the process of implicit
differentiation into four concrete steps:

1.  **Differentiate both sides** of the equation with respect to $x$.
    Treat $y$ as a differentiable function of $x$, applying the chain
    rule whenever differentiating terms involving $y$.

2.  **Collect all terms** containing $\frac{dy}{dx}$ on one side of the
    equation and move all other terms to the opposite side.

3.  **Factor out** $\frac{dy}{dx}$ from the terms containing it.

4.  **Solve for** $\frac{dy}{dx}$ by dividing both sides by the factored
    expression.

Let's apply this to a more complex curve where solving for $y$
explicitly would be nearly impossible.

::: example
[]{#ex:3-13-complex label="ex:3-13-complex"} Find the slope of the
tangent line to the curve $$2x^3 + x^2y - xy^3 = 2$$ at the point
$(1, 1)$.

**Step 1: Differentiate both sides with respect to $x$.** We
differentiate each term carefully, using the product rule for $x^2y$ and
$xy^3$. Writing $y'$ for $\frac{dy}{dx}$:

- $\frac{d}{dx}[2x^3] = 6x^2$

- $\frac{d}{dx}[x^2y] = 2xy + x^2 y'$ (Product rule: derivative of $x^2$
  times $y$, plus $x^2$ times derivative of $y$)

- $\frac{d}{dx}[-xy^3] = -y^3 - 3xy^2 y'$ (Product rule and chain rule)

- $\frac{d}{dx}[2] = 0$

Putting it all together: $$\begin{align*}
  6x^2 + 2xy + x^2 y' - y^3 - 3xy^2 y' &= 0
\end{align*}$$

**Step 2: Substitute the point $(1, 1)$ to find the slope.** Since we
only need the slope at a specific point, we can substitute $x = 1$ and
$y = 1$ immediately. This is often much easier than solving for $y'$
algebraically first. $$\begin{align*}
  6(1)^2 + 2(1)(1) + (1)^2 y' - (1)^3 - 3(1)(1)^2 y' &= 0 \\
  6 + 2 + y' - 1 - 3y' &= 0
\end{align*}$$

**Step 3 & 4: Collect terms and solve for $y'$.** $$\begin{align*}
  7 - 2y' &= 0 \\
  2y' &= 7 \\
  y' &= \frac{7}{2}
\end{align*}$$ The slope of the tangent line at $(1, 1)$ is
$\frac{7}{2}$.
:::

::: remark
Implicit differentiation is useful even when one *could* solve for $y$
explicitly. Keeping the equation implicit typically leads to simpler
calculations. The technique works because, near the point of interest,
$y$ is locally a function of $x$ (by the implicit function theorem), and
the chain rule applies to every occurrence of $y$.
:::

# Transcendental Functions

## Functions and Their Components {#sec:4.1}

*There are a few concepts related to the notion of function that can get
confusing. Strictly speaking, they all have very precise definitions,
but in some contexts we relax those definitions, abuse notation, and use
the terms to mean something slightly different. Sometimes students may
learn the same theorem in two apparently contradictory ways, depending
on whether it appears in a calculus class or in a linear algebra class.
There is no contradiction once we understand the conventions.*

::: definition
[]{#def:4-1 label="def:4-1"} A *function* consists of three pieces:

1.  A set of inputs called the *domain*.

2.  A set of potential outputs called the *codomain*.

3.  A *rule* that matches each input in the domain to exactly one output
    in the codomain.

If the function is named $f$, the domain is $A$, and the codomain is
$B$, we write $f\colon A \to B$. For each $x \in A$, the symbol $f(x)$
denotes the corresponding element of $B$.
:::

::: remark
The **name** of the function is $f$, **not** $f(x)$. The expression
$f(x)$ is an element in the codomain, not the function itself.
:::

::: definition
[]{#def:4-2 label="def:4-2"} Let $f\colon A \to B$ be a function. The
*range* (or *image*) of $f$ is the set of **actual** outputs:
$$\operatorname{Range}(f) = \{f(x) : x \in A\}.$$ The range is always a
subset of the codomain, but need not equal it.
:::

::: remark
The codomain is chosen beforehand; the range is determined after the
rule is defined. To specify a function, one needs only the domain, the
codomain, and the rule. The range can be computed from this information.
:::

*In calculus, we adopt conventions that simplify the way we talk about
functions.*

::: remark
In single-variable calculus, it is common to define a function by giving
only the rule (usually an equation). By default, we assume:

1.  The domain is the **largest subset** of $\mathbb{R}$ on which the
    rule makes sense.

2.  The codomain is $\mathbb{R}$.

For example, the function defined by $g(x) = \frac{1}{x^{2}}$ implicitly
has domain $\mathbb{R}\setminus \{0\}$ and codomain $\mathbb{R}$.
:::

::: remark
This convention saves time because we only work with one specific type
of function, but in other areas of mathematics---such as abstract
algebra---domains and codomains may not even be sets of numbers, and one
must specify them carefully.
:::

::: remark
Two functions with the same domain, the same rule, and the same range,
but **different codomains**, are strictly speaking different functions.
In calculus, we often treat the codomain as irrelevant and identify such
functions. In other areas of mathematics, this distinction can be
important.
:::

::: remark
The names introduced here---domain, codomain, range---are the most
commonly used names in mathematics. However, in some areas of computer
science, the word "range" is used to mean codomain, and "image" is used
for what we call range. When working with others, make sure you agree on
notation.
:::

## Inverse Functions {#sec:4.2}

*The idea behind the inverse of a function is simple: swap inputs and
outputs. If we reverse all the arrows in the diagram of a function, we
obtain its inverse---provided the result is again a function.*

::: definition
[]{#def:4-3 label="def:4-3"} Let $f\colon A \to B$ be a function. The
*inverse* of $f$ is a function $f^{-1}\colon B \to A$ defined by
$$x = f^{-1}(y) \quad \Longleftrightarrow \quad y = f(x),
  \qquad \text{for all } x \in A \text{ and all } y \in B.$$
:::

*Two things can go wrong when we try to construct an inverse. First, an
element of the codomain might not be in the range, leaving it with no
preimage. Second, two different inputs might produce the same output,
forcing the inverse to be "multi-valued." We give names to functions
that avoid each of these failures.*

::: definition
[]{#def:4-4 label="def:4-4"} A function $f\colon A \to B$ is
*surjective* (or *onto*) when the range equals the full codomain:
$$\text{for every } y \in B, \text{ there exists } x \in A \text{ such that } f(x) = y.$$
:::

::: definition
[]{#def:4-5 label="def:4-5"} A function $f\colon A \to B$ is *injective*
(or *one-to-one*) when different inputs produce different outputs:
$$\text{for all } x_1, x_2 \in A, \quad x_1 \neq x_2 \;\Longrightarrow\; f(x_1) \neq f(x_2).$$
Equivalently, $f(x_1) = f(x_2) \;\Longrightarrow\; x_1 = x_2$.
:::

::: theorem
[]{#thm:4-1 label="thm:4-1"} A function $f\colon A \to B$ has an inverse
if and only if $f$ is both injective and surjective.
:::

*This is the rigorous story. In calculus, however, we take a shortcut,
entirely bypassing the surjectivity problem.*

::: remark
In calculus, we almost always shrink the codomain to match the range
without saying so explicitly. This is why most calculus textbooks almost
never use the words "codomain" or "surjective." Under this convention, a
function has an inverse if and only if it is **injective**.
:::

::: definition
[]{#def:4-6 label="def:4-6"} Let $f$ be a one-to-one function with
domain $A$ and range $C$. The *inverse function* $f^{-1}$ has domain $C$
and range $A$, and is defined by
$$x = f^{-1}(y) \quad \Longleftrightarrow \quad y = f(x),
  \qquad \text{for all } x \in A \text{ and all } y \in C.$$
Equivalently, $f$ and $f^{-1}$ satisfy the composition identities
$$f^{-1}\!\bigl(f(x)\bigr) = x \quad \text{for all } x \in A,
  \qquad
  f\!\bigl(f^{-1}(y)\bigr) = y \quad \text{for all } y \in C.$$
:::

## Inverse Function Examples {#sec:4.3}

*Let us study several examples of pairs of inverse functions. These
illustrate the general theory, and the last example previews the
subtlety that arises with inverse trigonometric functions.*

::: example
[]{#ex:4-1 label="ex:4-1"} Let $f(x) = 2x + 1$. The domain and range are
both $\mathbb{R}$, so an inverse exists. From the definition,
$$y = 2x + 1 \quad \Longrightarrow \quad x = \frac{y - 1}{2},$$ so
$f^{-1}(y) = \dfrac{y - 1}{2}$. One can verify the composition
identities directly: $$\begin{align*}
  f^{-1}\!\bigl(f(x)\bigr) &= \frac{(2x + 1) - 1}{2} = x, \\
  f\!\bigl(f^{-1}(y)\bigr) &= 2 \cdot \frac{y - 1}{2} + 1 = y.
\end{align*}$$
:::

::: example
[]{#ex:4-2 label="ex:4-2"} The exponential function $e^{x}$ and the
natural logarithm $\ln(x)$ are inverses of each other. Their defining
relation is
$$y = e^{x} \quad \Longleftrightarrow \quad x = \ln(y), \qquad y > 0.$$
The domain of $e^{x}$ is $\mathbb{R}$ and its range is $(0,\infty)$; the
domain of $\ln$ is $(0,\infty)$ and its range is $\mathbb{R}$.

This statement can be used to **define** one function from the other. In
high school, one typically takes the exponential as given and defines
$\ln$ through the relation above. In analysis, it is common to start
with $\ln$ (constructed as an integral) and define $e^{x}$ as its
inverse.

The graphs of $e^{x}$ and $\ln(x)$ are reflections of each other across
the line $y = x$. This is a general property: switching from a function
to its inverse swaps the roles of $x$ and $y$, which is geometrically a
reflection across the diagonal.

The composition identities are
$$\ln(e^{x}) = x \quad \text{for all } x \in \mathbb{R},
  \qquad
  e^{\ln(y)} = y \quad \text{for all } y > 0.$$
:::

::: example
[]{#ex:4-3 label="ex:4-3"} Consider $f(x) = x^{2}$. This function is
**not** one-to-one: $f(3) = f(-3) = 9$. Therefore $f$ does not have an
inverse.

However, we can *restrict* $f$ to the smaller domain $[0, \infty)$. The
restriction is one-to-one and its range is $[0, \infty)$, so it has an
inverse. That inverse is the square root: $$g(x) = \sqrt{x}.$$ Note that
$g$ is **not** the inverse of the original $f$; it is the inverse of the
*restriction* of $f$ to $[0, \infty)$.

This is reflected in the composition identities. We have
$\sqrt{x^{2}} = x$ only when $x \geq 0$; in general,
$\sqrt{x^{2}} = \left\lvert x \right\rvert$.
:::

::: remark
If we have a function that is not one-to-one, we can restrict it to a
smaller domain and construct an inverse of the restriction. The
definition of the inverse and the properties it satisfies must then be
modified accordingly. This idea becomes essential when defining inverse
trigonometric functions.
:::

<figure id="fig:inverse-reflection" data-latex-placement="ht">

<figcaption>A function and its inverse reflect across <span
class="math inline"><em>y</em> = <em>x</em></span>.</figcaption>
</figure>

## Derivatives of Inverse Functions {#sec:4.4}

*If a function is differentiable and has an inverse, must the inverse
also be differentiable? The answer is: not necessarily, unless we add an
extra condition.*

*Consider a differentiable, one-to-one function $f$ whose graph has a
horizontal tangent at some point $P$. Reflecting the graph across the
diagonal $y = x$ to obtain the graph of $f^{-1}$ turns that horizontal
tangent into a vertical tangent at the corresponding point $Q$. A
vertical tangent has infinite slope, so $f^{-1}$ is not differentiable
there. This is the only obstruction.*

::: theorem
[]{#thm:4-2 label="thm:4-2"} Let $f$ be a function defined on an
interval $I$. If $f$ has an inverse, $f$ is differentiable, and $f'$ is
never zero on $I$, then $f^{-1}$ is also differentiable.
:::

::: remark
This result should not be confused with the **Inverse Function Theorem**
from multivariable calculus, which is a much more powerful and more
complicated statement. The theorem above is a simpler, single-variable
result.
:::

*Once we know both $f$ and $f^{-1}$ are differentiable, we can find the
derivative of $f^{-1}$ by differentiating the identity
$f\!\bigl(f^{-1}(y)\bigr) = y$.*

::: theorem
[]{#thm:4-3 label="thm:4-3"} Under the hypotheses of
[\[thm:4-2\]](#thm:4-2){reference-type="ref+label" reference="thm:4-2"},
for $y$ in the domain of $f^{-1}$,
$$\bigl(f^{-1}\bigr)'(y) = \frac{1}{f'\!\bigl(f^{-1}(y)\bigr)}.$$
Equivalently, setting $x = f^{-1}(y)$ (so that $y = f(x)$),
$$\bigl(f^{-1}\bigr)'(y) = \frac{1}{f'(x)}.$$
:::

::: proof
*Proof.* We know that $f\!\bigl(f^{-1}(y)\bigr) = y$ for all $y$ in the
domain of $f^{-1}$. Differentiating both sides with respect to $y$ and
applying the chain rule on the left gives
$$f'\!\bigl(f^{-1}(y)\bigr) \cdot \bigl(f^{-1}\bigr)'(y) = 1.$$

Setting $x = f^{-1}(y)$, this becomes
$f'(x) \cdot \bigl(f^{-1}\bigr)'(y) = 1$, and solving yields
$$\bigl(f^{-1}\bigr)'(y) = \frac{1}{f'(x)}.$$ Note that $f$ and $f^{-1}$
are evaluated at **different** points: $f'$ is evaluated at $x$, while
$\bigl(f^{-1}\bigr)'$ is evaluated at $y = f(x)$. ◻
:::

## Derivative of the Exponential {#sec:4.5}

*We now try to compute the derivative of an exponential function from
the limit definition, and in the process discover a defining property of
the number $e$.*

There are many exponential functions, one for each positive base $a$. If
$a > 1$, then $a^{x}$ is increasing; if $0 < a < 1$, then $a^{x}$ is
decreasing. In either case, the domain is $\mathbb{R}$ and the range is
$(0,\infty)$.

::: proposition
[]{#thm:4-4 label="thm:4-4"} Fix a positive number $a$ and define
$f(x) = a^{x}$. Then $$f'(x) = \lim_{h \to 0} \frac{a^{x+h} - a^{x}}{h}
         = a^{x} \cdot \lim_{h \to 0} \frac{a^{h} - 1}{h}.$$ The limit
$L_{a} = \lim_{h \to 0} \frac{a^{h} - 1}{h}$ depends only on $a$, not on
$x$. Therefore the derivative of $a^{x}$ is a **constant multiple** of
itself: $$\frac{d}{dx}\bigl[a^{x}\bigr] = L_{a} \cdot a^{x}.$$
:::

::: definition
[]{#def:4-7 label="def:4-7"} We define $e$ to be the unique positive
real number for which $L_{e} = 1$, i.e.,
$$\lim_{h \to 0} \frac{e^{h} - 1}{h} = 1.$$ Equivalently, $e$ is the
unique base for which the exponential is its own derivative:
$$\frac{d}{dx}\bigl[e^{x}\bigr] = e^{x}.$$
:::

::: remark
This derivation, while illuminating, assumes several things that require
justification: that the limit $L_{a}$ exists for every positive $a$,
that there exists a value of $a$ for which $L_{a} = 1$, and indeed that
$a^{x}$ is well-defined for arbitrary real $x$. These issues are
addressed in [4.6](#sec:4.6){reference-type="ref+label"
reference="sec:4.6"}. Nevertheless, the derivation is helpful for
understanding where the number $e$ comes from and why exponentials have
the derivative they do.
:::

## Defining Exponentials Rigorously {#sec:4.6}

*It may surprise you to learn that defining exponentials rigorously is
much harder than what you were told in high school. For most practical
purposes this is not something to worry about too much, but it is
interesting to know that it is a genuinely difficult problem.*

Recall the high-school definition of logarithms: $\log_{a}(x) = y$ means
$a^{y} = x$. This defines the logarithm as the *inverse* of the
exponential, so it is only valid if exponentials are already
well-defined.

*Let us review how powers are defined, starting with rational
exponents.*

::: remark
Let $a > 0$. Powers with rational exponents are built in stages:

1.  **Positive integer exponents.** $a^{n}$ ($n \in \mathbb{Z}^{+}$) is
    defined as iterated multiplication.

2.  **Reciprocal exponents.** $a^{1/n}$ is defined as $\sqrt[n]{a}$, the
    unique positive number whose $n$-th power is $a$.

3.  **General positive rationals.** $a^{n/m}$ is defined as
    $\bigl(a^{n}\bigr)^{1/m}$, using steps (i) and (ii).

4.  **Zero exponent.** $a^{0} = 1$.

5.  **Negative exponents.** $a^{-c} = \dfrac{1}{a^{c}}$ for $c > 0$.

This defines $a^{c}$ for every rational $c$. There are no difficulties
so far.
:::

::: remark
How do we define $a^{c}$ when $c$ is irrational? For example, what is
$2^{\pi}$? We cannot use iterated multiplication, roots, or quotients to
define it. There is no easy way around this: one must enter "serious
analysis territory" to even say what $2^{\pi}$ means.
:::

*One natural idea is to approximate $\pi$ by rational numbers---$3$,
$3.1$, $3.14$, $3.141$, ...---compute $2^{c}$ for each, and define
$2^{\pi}$ as the limit of the resulting sequence. This is probably what
early mathematicians were implicitly assuming. But it is surprisingly
hard to prove that (a) the limit exists, and (b) it does not depend on
the choice of rational approximation.*

The key identity $$a^{c} = e^{c \ln(a)}$$ reduces exponentials with
arbitrary base to exponentials with base $e$. It therefore suffices to
define $e^{x}$ (or equivalently $\ln(x)$) rigorously.

::: remark
In analysis, there are at least three common approaches:

1.  **Differential equations.** Define $e^{x}$ as the unique solution to
    the initial value problem $y' = y$, $y(0) = 1$. The Picard--Lindelöf
    theorem guarantees existence and uniqueness. This is natural but
    expensive: the theorem itself is sophisticated.

2.  **Power series.** Define
    $e^{x} = \sum_{n=0}^{\infty} \frac{x^{n}}{n!}$. This generalises
    beautifully to complex numbers, but proving the algebraic properties
    of the exponential from this definition requires the full theory of
    power series.

3.  **Integral definition of $\ln$.** Define
    $\ln(x) = \int_{1}^{x} \frac{1}{t} \,dt$ for $x > 0$, and then
    define $e^{x}$ as the inverse of $\ln$. This requires only the
    Fundamental Theorem of Calculus, making it by far the most
    accessible approach.
:::

::: remark
A full rigorous construction proving all the details is the province of
an analysis course. The goal here is simply to understand *why* defining
exponentials is not trivial; every calculus student should appreciate
this.
:::

## Derivative of the Logarithm {#sec:4.7}

*We know that the derivative of $e^{x}$ is itself. How can this help us
find the derivative of $\ln(x)$? Since $e^{x}$ and $\ln(x)$ are
inverses, the identity $e^{\ln(x)} = x$ provides a relation between the
two functions. Differentiating both sides will yield a relation between
their derivatives.*

::: theorem
[]{#thm:4-5 label="thm:4-5"} For all $x > 0$,
$$\frac{d}{dx}\bigl[\ln(x)\bigr] = \frac{1}{x}.$$
:::

::: proof
*Proof.* Start from $e^{\ln(x)} = x$. Differentiate both sides with
respect to $x$. On the left, the chain rule gives
$$e^{\ln(x)} \cdot \frac{d}{dx}\bigl[\ln(x)\bigr] = 1.$$

Since $e^{\ln(x)} = x$, this becomes
$$x \cdot \frac{d}{dx}\bigl[\ln(x)\bigr] = 1.$$ Solving gives
$\dfrac{d}{dx}\bigl[\ln(x)\bigr] = \dfrac{1}{x}$. ◻
:::

::: remark
This same trick---differentiating a composition identity---can be used
to find the derivative of **any** function, provided we know the
derivative of its inverse.
:::

<figure id="fig:exp-log" data-latex-placement="ht">

<figcaption>The graphs of <span
class="math inline"><em>e</em><sup><em>x</em></sup></span> and <span
class="math inline">ln <em>x</em></span>.</figcaption>
</figure>

## Derivatives of General Exponentials {#sec:4.8}

*We know the derivative of $e^{x}$, but what about $a^{x}$ for an
arbitrary positive base $a$? A common strategy in mathematics: reduce
the general problem to a special case we have already solved.*

::: theorem
[]{#thm:4-6 label="thm:4-6"} For every $a > 0$,
$$\frac{d}{dx}\bigl[a^{x}\bigr] = a^{x} \ln(a).$$
:::

::: proof
*Proof.* Any positive number $a$ can be written as $a = e^{\ln(a)}$.
Therefore $$a^{x} = \bigl(e^{\ln(a)}\bigr)^{x} = e^{x \ln(a)}.$$

The derivative of $e^{x \ln(a)}$ with respect to $x$ is, by the chain
rule, $$e^{x \ln(a)} \cdot \ln(a) = a^{x} \ln(a).$$ ◻
:::

::: remark
When $a = e$, we get $\ln(e) = 1$, and the formula reduces to
$\frac{d}{dx}[e^{x}] = e^{x}$, recovering the known identity.
:::

::: remark
You already know that $\frac{d}{dx}[\ln(x)] = \frac{1}{x}$. What is the
derivative of $\log_{a}(x)$ for an arbitrary positive base $a \neq 1$?
As a hint, use the change-of-base identity
$\log_{a}(x) = \frac{\ln(x)}{\ln(a)}$.
:::

## Logarithmic Differentiation {#sec:4.9}

*We use logarithmic differentiation to compute the derivative of a
function that is raised to the power of another function---a situation
in which neither the power rule nor the exponential rule directly
applies.*

::: example
[]{#ex:4-4 label="ex:4-4"} Let $f(x) = \bigl(\cos(x)\bigr)^{\sin(x)}$.
This expression is **not** simply a power (like $x^{3}$), because the
base depends on $x$. Nor is it simply an exponential (like $2^{x}$),
because the exponent also depends on $x$.

*Neither the power rule nor the exponential derivative rule applies on
its own. We need a different strategy.*

**Method 1: Rewrite as an exponential with base $e$.** Using the
identity $u^{v} = e^{v \ln u}$,
$$f(x) = e^{\sin(x) \cdot \ln(\cos(x))}.$$ Differentiating using the
chain rule, $$\begin{align*}
  f'(x)
  &= e^{\sin(x) \cdot \ln(\cos(x))} \cdot \frac{d}{dx}\bigl[\sin(x) \cdot \ln(\cos(x))\bigr] \\
  &= \bigl(\cos(x)\bigr)^{\sin(x)} \cdot \left[\cos(x) \cdot \ln(\cos(x)) + \sin(x) \cdot \frac{-\sin(x)}{\cos(x)}\right].
\end{align*}$$

**Method 2: Logarithmic differentiation.** Take logarithms of both
sides:
$$\ln\!\bigl(f(x)\bigr) = \sin(x) \cdot \ln\!\bigl(\cos(x)\bigr).$$ The
exponent has disappeared. Differentiate both sides using implicit
differentiation on the left and the product rule on the right:
$$\frac{f'(x)}{f(x)} = \cos(x) \cdot \ln(\cos(x)) + \sin(x) \cdot \frac{-\sin(x)}{\cos(x)}.$$
Solving for $f'(x)$ recovers the same answer as Method 1.
:::

::: remark
The two methods are the **same method in disguise**. Method 2
(logarithmic differentiation) is often more convenient because taking
logarithms turns products into sums, quotients into differences, and
powers into products, simplifying the expression before differentiation.
:::

## Power Rule for Real Exponents {#sec:4.10}

*In an earlier chapter we proved the power rule for positive integer
exponents. We now prove it for **any** real exponent, using logarithms.*

::: theorem
[]{#thm:4-7 label="thm:4-7"} For any $c \in \mathbb{R}$ and for all
$x > 0$, $$\frac{d}{dx}\bigl[x^{c}\bigr] = c\, x^{c-1}.$$
:::

::: remark
It may feel like overkill to use logarithms to prove the power
rule---are powers not more "basic" than logarithms? For *rational*
exponents, alternative proofs exist that avoid logarithms entirely. But
for *real* exponents, the identity $x^{c} = e^{c \ln(x)}$ is not merely
a useful trick; it is **the definition** of a power with a real
exponent.
:::

::: proof
*Proof.* For $x > 0$, write $x^{c} = e^{c \ln(x)}$. By the chain rule,
$$\begin{align*}
  \frac{d}{dx}\bigl[x^{c}\bigr]
  &= \frac{d}{dx}\bigl[e^{c \ln(x)}\bigr] \\
  &= e^{c \ln(x)} \cdot \frac{c}{x} \\
  &= x^{c} \cdot \frac{c}{x} \\
  &= c\, x^{c-1}.
\end{align*}$$ ◻
:::

::: remark
This proof works for **all** exponents at once---natural, rational,
real, and even complex. The price is that we must first develop the
theory of logarithms and establish the derivative formulas for $e^{x}$
and $\ln(x)$. The proof only *looks* short because the hard work was
done beforehand.
:::

## Logarithm Notation {#sec:4.11}

*There is a notational controversy surrounding logarithms. All
mathematicians agree that the natural logarithm---logarithm in base
$e$---is the most important, but we cannot agree on what to call it.*

If one fixes a favourite base $b$, then exponentials and logarithms in
any other base can be expressed in terms of base $b$. So why not choose
the *best* base and use it exclusively?

Mathematicians realised early that the base $e$ is special:

- Exponentials with base $e$ arise naturally as limits.

- The functions $e^{x}$ and $\ln(x)$ have **simpler derivatives** than
  exponentials or logarithms in any other base.

- $e^{x}$ and $\ln(x)$ have elegant power-series expansions.

Natural logarithm is natural, and it is the only logarithm one should
ever use.

::: remark
Historically, the decimal system made logarithms in base $10$ (the
"common logarithm") the most useful for hand computation using log
tables and slide rules. The notation $\log(x)$ without a base came to
mean $\log_{10}(x)$. Today, nobody computes by hand, and modern
mathematicians argue that $\log$ should be reserved for the natural
logarithm. Engineers and many calculus textbooks continue to use $\ln$.

In summary: whenever you see $\ln(x)$ or $\log(x)$ without a specified
base, both *probably* mean logarithm in base $e$. When reading a book or
working with others, check which convention is in use.
:::

## The Arcsine Function {#sec:4.12}

*Some books and most calculators call this function "sine inverse." We
prefer the name "arcsine" because arcsine is **not** the inverse
function of sine---the situation is more subtle.*

The function $\sin\colon \mathbb{R}\to [-1,1]$ is **not** one-to-one:
for example, $\sin(0) = \sin(\pi) = 0$. Therefore sine does not have an
inverse function.

::: definition
[]{#def:4-8 label="def:4-8"} The function *arcsine* is defined as the
inverse of the **restriction** of sine to the interval
$\bigl[-\frac{\pi}{2},\, \frac{\pi}{2}\bigr]$. Equivalently,
$$x = \arcsin(y) \quad \Longleftrightarrow \quad y = \sin(x),
  \qquad \text{for all } x \in \left[-\frac{\pi}{2},\, \frac{\pi}{2}\right] \text{ and all } y \in [-1,1].$$
The domain of $\arcsin$ is $[-1,1]$ and its range is
$\bigl[-\frac{\pi}{2},\, \frac{\pi}{2}\bigr]$.
:::

::: remark
The choice of the interval $\bigl[-\frac{\pi}{2},\, \frac{\pi}{2}\bigr]$
is a convention. We could have restricted sine to any interval on which
it is one-to-one and preserves the full range $[-1,1]$. The symmetric
interval around $0$ is the standard choice, but it is arbitrary.
:::

<figure id="fig:arcsin-restriction" data-latex-placement="ht">

<figcaption>The restricted sine and its inverse <span
class="math inline">arcsin </span>.</figcaption>
</figure>

Since $\arcsin$ and the restriction of $\sin$ are inverses, the
composition identities hold on the correct domains:
$$\arcsin\!\bigl(\sin(x)\bigr) = x \quad \text{for all } x \in \left[-\frac{\pi}{2},\, \frac{\pi}{2}\right],
  \qquad
  \sin\!\bigl(\arcsin(y)\bigr) = y \quad \text{for all } y \in [-1,1].$$

::: remark
These identities are **not** true outside the specified domains. For
instance, $\sin(\arcsin(2))$ is undefined, and
$\arcsin(\sin(2)) \neq 2$.
:::

::: example
[]{#ex:4-5 label="ex:4-5"} What is $\arcsin\!\left(\frac{1}{2}\right)$?
Call the answer $t$. Then $\sin(t) = \frac{1}{2}$ and
$t \in \bigl[-\frac{\pi}{2},\, \frac{\pi}{2}\bigr]$. The only such angle
is $t = \frac{\pi}{6}$.
:::

::: example
[]{#ex:4-6 label="ex:4-6"} What is $\arcsin\!\bigl(\sin(2)\bigr)$? Since
$2 \notin \bigl[-\frac{\pi}{2},\, \frac{\pi}{2}\bigr]$, we cannot simply
say the answer is $2$.

Let $t = \arcsin(\sin(2))$. By definition, $\sin(t) = \sin(2)$ and
$t \in \bigl[-\frac{\pi}{2},\, \frac{\pi}{2}\bigr]$. This is a
trigonometry problem. From the symmetry of the sine graph, the distance
from $\frac{\pi}{2}$ to $t$ equals the distance from $2$ to
$\frac{\pi}{2}$:
$$\frac{\pi}{2} - t = 2 - \frac{\pi}{2} \quad \Longrightarrow \quad t = \pi - 2.$$
Therefore $\arcsin(\sin(2)) = \pi - 2$.
:::

::: remark
What is $\arcsin(\sin(6))$? Hint: the answer is neither $6$ nor
$\pi - 6$.
:::

## Derivative of Arcsine {#sec:4.13}

*We use the same strategy as for $\ln$: differentiate a composition
identity relating $\sin$ and $\arcsin$, then solve for the unknown
derivative.*

::: theorem
[]{#thm:4-8 label="thm:4-8"} For all $x \in (-1,1)$,
$$\frac{d}{dx}\bigl[\arcsin(x)\bigr] = \frac{1}{\sqrt{1 - x^{2}}}.$$
:::

::: proof
*Proof.* Start from $\sin\!\bigl(\arcsin(x)\bigr) = x$. Differentiating
both sides with respect to $x$ and applying the chain rule on the left
gives
$$\cos\!\bigl(\arcsin(x)\bigr) \cdot \frac{d}{dx}\bigl[\arcsin(x)\bigr] = 1.$$

Solving yields $\frac{d}{dx}[\arcsin(x)] = \frac{1}{\cos(\arcsin(x))}$.

It remains to simplify $\cos(\arcsin(x))$. Let $\theta = \arcsin(x)$, so
$\sin(\theta) = x$. Using the identity
$\cos^{2}(\theta) = 1 - \sin^{2}(\theta)$,
$$\cos(\theta) = \pm\sqrt{1 - x^{2}}.$$ Since
$\theta \in \bigl[-\frac{\pi}{2},\, \frac{\pi}{2}\bigr]$ by definition
of $\arcsin$, we have $\cos(\theta) \geq 0$, so we choose the positive
sign. Therefore
$$\frac{d}{dx}\bigl[\arcsin(x)\bigr] = \frac{1}{\sqrt{1 - x^{2}}}.$$ ◻
:::

::: remark
The positive sign arises specifically because $\arcsin$ was defined
using the restriction of $\sin$ to
$\bigl[-\frac{\pi}{2},\, \frac{\pi}{2}\bigr]$, where $\cos$ is
non-negative. A different restriction could yield a different sign.
:::

## Arctangent and Arccosine {#sec:4.14}

*Having defined $\arcsin$ and computed its derivative, we now do the
same for $\arctan$ and $\arccos$. The ideas are identical, so we proceed
more quickly.*

::: definition
[]{#def:4-9 label="def:4-9"} The function $\tan$ is not one-to-one on
its natural domain. We restrict it to
$\bigl(-\frac{\pi}{2},\, \frac{\pi}{2}\bigr)$ (an **open** interval,
since $\tan$ is undefined at the endpoints). The *arctangent* function
is the inverse of this restriction:
$$x = \arctan(y) \quad \Longleftrightarrow \quad y = \tan(x),
  \qquad \text{for all } x \in \left(-\frac{\pi}{2},\, \frac{\pi}{2}\right) \text{ and all } y \in \mathbb{R}.$$
The domain of $\arctan$ is $\mathbb{R}$ and its range is
$\bigl(-\frac{\pi}{2},\, \frac{\pi}{2}\bigr)$.
:::

::: remark
Notice that the restriction interval for $\arctan$ is *open*, in
contrast to the *closed* interval
$\bigl[-\frac{\pi}{2},\, \frac{\pi}{2}\bigr]$ used for $\arcsin$. Since
the range of $\tan$ on $\bigl(-\frac{\pi}{2},\, \frac{\pi}{2}\bigr)$ is
all of $\mathbb{R}$, the domain of $\arctan$ is $\mathbb{R}$.
:::

::: definition
[]{#def:4-10 label="def:4-10"} The function $\cos$ is not one-to-one on
$\mathbb{R}$. We restrict it to $[0,\pi]$, and define the *arccosine*
function as the inverse of this restriction:
$$x = \arccos(y) \quad \Longleftrightarrow \quad y = \cos(x),
  \qquad \text{for all } x \in [0,\pi] \text{ and all } y \in [-1,1].$$
The domain of $\arccos$ is $[-1,1]$ and its range is $[0,\pi]$.
:::

::: remark
For $\arccos$, we cannot choose a domain for $\cos$ that is symmetric
about $0$---that would not produce a one-to-one function. The interval
$[0,\pi]$ is the standard choice.
:::

::: remark
Can you sketch the graphs of $\arctan$ and $\arccos$? For each, reflect
the graph of the restricted trigonometric function across the line
$y = x$.
:::

::: theorem
[]{#thm:4-9 label="thm:4-9"}

1.  $\dfrac{d}{dx}\bigl[\arcsin(x)\bigr] = \dfrac{1}{\sqrt{1 - x^{2}}}$,
    for $x \in (-1,1)$.

2.  $\dfrac{d}{dx}\bigl[\arccos(x)\bigr] = \dfrac{-1}{\sqrt{1 - x^{2}}}$,
    for $x \in (-1,1)$.

3.  $\dfrac{d}{dx}\bigl[\arctan(x)\bigr] = \dfrac{1}{1 + x^{2}}$, for
    all $x \in \mathbb{R}$.
:::

::: remark
The derivative of $\arccos$ is the same as that of $\arcsin$ but with an
additional **minus sign**. The particular signs arise from the specific
restrictions chosen; different restrictions could produce different
results.
:::

::: remark
It is worth memorising the derivatives of $\arcsin$ and $\arctan$ in
particular. They appear frequently in integration, where one recognises
integrands of the form $\frac{1}{\sqrt{1-x^{2}}}$ or $\frac{1}{1+x^{2}}$
as derivatives of inverse trigonometric functions.
:::

::: remark
One could similarly define arcsecant, arccosecant, and arccotangent, but
in practice these three functions are rarely used. For most purposes,
$\arcsin$, $\arccos$, and $\arctan$ suffice.
:::

# The Mean Value Theorem and Applications

## Motivation for the MVT {#sec:5.1}

*The Mean Value Theorem is perhaps the most interesting result in
calculus. And yet, when you look at the statement, at first sight it
appears not very interesting, technical, boring... honestly, it appears
useless. So why do we care? Or should we care?*

The goal of the Mean Value Theorem is to help us obtain information
about a function using something about its derivative. When we know
something about the derivative, what can we say about the function?

Consider the following natural question. We know that constant functions
have zero derivative. Are those the only ones? Are there other functions
with zero derivative? It appears not, and we would like to prove this.

::: theorem
[]{#thm:5-1 label="thm:5-1"} Let $f$ be a function defined on an open
interval $(a,b)$. If $f'(x) = 0$ for every $x \in (a,b)$, then $f$ is
constant.
:::

*This is the simplest example of a theorem in which we use something
about the derivative to conclude something about the function. Since it
is the simplest, let us try to prove it first... Surprisingly, we do not
even know how to start! Despite looking very simple, this is not easy to
prove.*

::: remark
Pause and try to prove
[\[thm:5-1\]](#thm:5-1){reference-type="ref+label" reference="thm:5-1"}.
There is no clear way to do it. In fact, we do not know **any** way to
prove this simple theorem without using the Mean Value Theorem.
:::

Here is a partial list of results that all rely on the Mean Value
Theorem:

- If a function has zero derivative, it must be constant.

- If a function has positive derivative, it must be increasing.

- All integration methods (finding antiderivatives up to a constant).

- L'Hôpital's Rule.

- The Fundamental Theorem of Calculus.

- Taylor's Theorem and Taylor series with remainder.

- Equality of mixed partial derivatives in multivariable calculus.

**Everything** important in calculus, whether big or small, requires the
Mean Value Theorem to prove it.

*But reaching the Mean Value Theorem is quite an investment. Before we
are ready to state and prove it, we need a simplified version called
Rolle's Theorem, which is interesting on its own but whose main purpose
is as a stepping stone. And in order to prove Rolle's Theorem, we need
two other results: the Extreme Value Theorem, which we already know, and
the Local Extreme Value Theorem, which we will study next.*

::: remark
Should you care about the Mean Value Theorem? It depends on your goals.
If you just want to *use* calculus tools, you can skip it---you will
never use it directly. But if you want to *prove* the theorems and
understand why they are true, then you absolutely need the MVT, since
there is little or nothing you can prove without it.
:::

## Local Extrema and Critical Points {#sec:5.2}

*Before defining local extremum, let us look at an example. Consider a
function $f$ defined on $[0,5]$. This function has a minimum of $1$ at
$x = 3$ and a maximum of $5$ at $x = 5$ (an endpoint---nothing wrong
with that). But there is a third interesting point: the value there is
$3$, and the function takes values greater than $3$ elsewhere, so it is
not a maximum. However, if we stay close to that point, it looks like a
maximum. We call it a *local* maximum.*

::: definition
[]{#def:5-1 label="def:5-1"} Let $f$ be a function with domain $I$, and
let $c \in I$.

1.  We say $f$ has a *maximum* at $c$ when $f(x) \leq f(c)$ for all
    $x \in I$.

2.  We say $f$ has a *local maximum* at $c$ when there exists
    $\delta > 0$ such that
    $$\left\lvert x - c \right\rvert < \delta \;\Longrightarrow\; f(x) \leq f(c).$$

Analogous definitions hold for *minimum* and *local minimum*.
:::

::: remark
Some terminology:

- The word *extremum* means "maximum or minimum."

- Some authors say *global extremum* instead of simply *extremum* to
  emphasise the contrast with local extremum. The two phrases mean the
  same thing.

- The plurals are *extrema*, *maxima*, and *minima* (irregular Latin
  plurals).
:::

::: remark
According to the definition above, endpoints **never** count as local
extrema, because the function needs to be defined on both sides of $c$.
This convention is used by the majority of calculus textbooks, and we
adopt it here. However, the majority of analysis textbooks use a
different convention that *does* include endpoints. When reading other
sources, be sure to check which convention is in use. There is one
specific point later where this distinction is very important.
:::

*Now that we have our definitions, let us move towards the Local Extreme
Value Theorem. What can we say about the derivative of a function at a
local extremum? Looking at graphs, the tangent line at a local extremum
appears to be horizontal (derivative zero)... unless the function has a
corner, in which case the derivative does not exist. These seem to be
the only two options.*

::: theorem
[]{#thm:5-2 label="thm:5-2"} Let $f$ be a function with domain an
interval $I$, and let $c$ be an interior point of $I$. If $f$ has a
local extremum at $c$, then $f'(c) = 0$ or $f'(c)$ does not exist.
:::

::: remark
Given the definition of local extremum that we use (which excludes
endpoints), the hypothesis that $c$ is an interior point is already
implicit. We state it explicitly anyway, to emphasise it. If one uses
the alternative definition that allows endpoints, then this hypothesis
is **essential** and must not be omitted.
:::

::: definition
[]{#def:5-2 label="def:5-2"} Let $f$ be a function defined on an
interval $I$. We say that $c$ is a *critical point* of $f$ when $c$ is
an interior point of $I$ and either $f'(c) = 0$ or $f'(c)$ does not
exist.
:::

With this terminology,
[\[thm:5-2\]](#thm:5-2){reference-type="ref+label" reference="thm:5-2"}
simply says that **local extrema are always critical points**.

::: remark
The converse is **not** true. A critical point is not always a local
extremum.
:::

<figure id="fig:critical-points" data-latex-placement="ht">

<figcaption>A smooth function with critical points at a local max and
min.</figcaption>
</figure>

## Proof of the Local EVT {#sec:5.3}

*We now prove the Local Extreme Value Theorem stated in
[5.2](#sec:5.2){reference-type="ref+label" reference="sec:5.2"}. The
argument treats the case of a local maximum; the case of a local minimum
is entirely analogous (reverse the inequalities).*

::: proof
*Proof of [\[thm:5-2\]](#thm:5-2){reference-type="ref+label"
reference="thm:5-2"} (local maximum case).* Suppose $f$ has a local
maximum at an interior point $c$. The derivative, if it exists, is
$$f'(c) = \lim_{x \to c} \frac{f(x) - f(c)}{x - c}.$$ We wish to show
that either this limit does not exist or it equals zero. Assume the
limit exists; we show it must be zero.

Consider the **denominator**. When $x \to c^{+}$, the quantity $(x - c)$
is positive. When $x \to c^{-}$, it is negative.

Consider the **numerator**. Since $f$ has a local maximum at $c$, we
have $f(x) \leq f(c)$ for all $x$ sufficiently close to $c$. Therefore
$f(x) - f(c) \leq 0$ for $x$ near $c$, regardless of the side of
approach.

Combining:

- From the right: the quotient $\dfrac{f(x) - f(c)}{x - c}$ is
  $\dfrac{(\leq 0)}{(> 0)} \leq 0$, so the right-hand limit is $\leq 0$.

- From the left: the quotient is $\dfrac{(\leq 0)}{(< 0)} \geq 0$, so
  the left-hand limit is $\geq 0$.

Since we assumed the full limit exists, the two one-sided limits must
exist and be equal. A quantity that is both $\leq 0$ and $\geq 0$ must
be zero. Therefore $f'(c) = 0$. ◻
:::

::: remark
We needed $c$ to be an interior point because we examined the limit from
both sides. If $c$ were an endpoint, the argument would fail.
:::

::: remark
Write the proof for a local minimum. It is very similar: change the
direction of the inequalities in the numerator. Everything else works
the same way.
:::

## Finding Global Extrema {#sec:5.4}

*The Local Extreme Value Theorem is not only a stepping stone towards
the Mean Value Theorem; it is also useful on its own. Here we
illustrate, with an example, how to use it to find the global maximum
and minimum of a function.*

::::: example
[]{#ex:5-1 label="ex:5-1"} Find the extrema (and local extrema) of
$$f(x) = x^{3} - 3x^{2} - 9x + 35 \qquad \text{on } [-4, 4].$$

**Step 1.** The function $f$ is continuous on the closed, bounded
interval $[-4, 4]$. By the Extreme Value Theorem, $f$ must have a
maximum and a minimum on this interval.

::: remark
Some students like to skip this first step, but it is **essential**.
Without it, everything else fails: the function might not even have a
maximum or a minimum.
:::

**Step 2.** Since $f$ has a maximum and a minimum, each must occur at an
**endpoint** or at an **interior point**. If it occurs at an interior
point, it is also a local extremum, so by
[\[thm:5-2\]](#thm:5-2){reference-type="ref+label" reference="thm:5-2"}
it must be a critical point.

Therefore, the plan is:

1.  Find all endpoints and critical points.

2.  Evaluate $f$ at each of these candidate points.

3.  The largest value is the maximum; the smallest is the minimum.

::: remark
This method only works for a **continuous function on a closed, bounded
interval**. Otherwise, the function may not have a maximum or minimum,
and applying this method carelessly may give the wrong answer.
:::

**Calculations.** The endpoints are $x = -4$ and $x = 4$. For the
critical points, compute the derivative:
$$f'(x) = 3x^{2} - 6x - 9 = 3(x + 1)(x - 3).$$ Since $f$ is a
polynomial, $f'$ exists everywhere, so the critical points are the
solutions of $f'(x) = 0$: namely $x = -1$ and $x = 3$.

Evaluating $f$ at all four candidate points: $$\begin{array}{c|cccc}
  x   & -4  & -1 & 3   & 4  \\ \hline
  f(x) & -41 & 40 & 8  & 15
\end{array}$$ The largest value is $f(-1) = 40$, so $f$ has a **maximum
of $40$ at $x = -1$**. The smallest value is $f(-4) = -41$, so $f$ has a
**minimum of $-41$ at $x = -4$**.

From this information, we can also guess the shape of the graph: $f$ has
a local maximum at $x = -1$ and a local minimum at $x = 3$. Strictly
speaking, this last observation is not yet fully rigorous, but
geometrically it makes perfect sense. We will learn how to argue this
rigorously when we study monotonicity.
:::::

## Rolle's Theorem {#sec:5.5}

*Rolle's Theorem is an intermediate step that will allow us to prove the
Mean Value Theorem. That is the main reason to study it. By itself, the
theorem may appear a bit dry and uninteresting, but it will lead us to
something much more important.*

::: theorem
[]{#thm:5-3 label="thm:5-3"} Let $f$ be defined on a closed, bounded
interval $[a,b]$. Suppose:

1.  $f$ is continuous on $[a,b]$,

2.  $f$ is differentiable on $(a,b)$,

3.  $f(a) = f(b)$.

Then there exists at least one $c \in (a,b)$ such that $f'(c) = 0$.
:::

<figure id="fig:rolles-theorem" data-latex-placement="ht">

<figcaption>Rolle’s theorem: a horizontal tangent in the
interior.</figcaption>
</figure>

*Before writing the proof, let us understand **why** each hypothesis is
needed.*

::: remark
**Why hypothesis (iii)?** If $f(a) = f(b)$, the graph must go up and
come back down (or vice versa), forcing a local extremum with derivative
zero. Without this condition, the function could be monotone and have no
point with zero derivative.

**Why hypothesis (ii)?** Even with $f(a) = f(b)$, the function could
have a local extremum at a corner, where the derivative does not exist.

**Why hypothesis (i)?** Even with differentiability on the interior and
equal endpoint values, a jump discontinuity at an endpoint can destroy
the conclusion.
:::

::: remark
One might ask: "Why not simply require differentiability on the full
closed interval $[a,b]$?" That would also make the theorem true.
However, it is good practice to state theorems with hypotheses as
**weak** as possible, because then the theorem applies in more
situations and is therefore more useful.
:::

::: proof
*Proof of Rolle's Theorem.* Since $f$ is continuous on the closed,
bounded interval $[a,b]$, the Extreme Value Theorem guarantees that $f$
attains a maximum and a minimum on $[a,b]$.

**Case 1:** At least one extremum (maximum or minimum) occurs at an
interior point $c \in (a,b)$. Then $f$ has a local extremum at $c$. By
the Local Extreme Value Theorem
([\[thm:5-2\]](#thm:5-2){reference-type="ref+label"
reference="thm:5-2"}), $f'(c)$ is either zero or does not exist. Since
$f$ is differentiable on $(a,b)$, we conclude $f'(c) = 0$.

**Case 2:** Both the maximum and the minimum occur at endpoints. Since
$f(a) = f(b)$, the maximum value and the minimum value are both equal to
$f(a)$. Therefore $f$ is constant on $[a,b]$, so $f'(c) = 0$ for every
$c \in (a,b)$.

In both cases, there exists $c \in (a,b)$ with $f'(c) = 0$. ◻
:::

::: remark
All three hypotheses were used in the proof: continuity on $[a,b]$ to
invoke the Extreme Value Theorem, differentiability on $(a,b)$ to
conclude $f'(c) = 0$ (rather than merely "does not exist"), and
$f(a) = f(b)$ to handle the case when both extrema occur at endpoints.
:::

## Counting Zeroes of Functions {#sec:5.6}

*The main reason we learned Rolle's Theorem is as a stepping stone to
the Mean Value Theorem. Nevertheless, it has applications of its own.
Here is one: it can help us count the number of zeroes of a function.*

::: definition
[]{#def:5-3 label="def:5-3"} We say that $c$ is a *zero* of a function
$f$ when $f(c) = 0$.
:::

::: remark
We say $c$ is a zero of the **function** $f$, and a solution of the
**equation** $f(x) = 0$. A function by itself is not an equation.
:::

The strategy for counting zeroes of a function uses two steps:

1.  Use the **Intermediate Value Theorem** to show that $f$ has *at
    least* a certain number of zeroes.

2.  Use **Rolle's Theorem** to show that $f$ has *at most* a certain
    number of zeroes.

If the two bounds agree, we know the exact count.

*The key observation linking Rolle's Theorem to zeroes is the
following.*

::: theorem
[]{#thm:5-4 label="thm:5-4"} Let $f$ be continuous and differentiable on
an interval $I$. Then the number of zeroes of $f$ on $I$ is at most the
number of zeroes of $f'$ on $I$, plus one.
:::

::: proof
*Proof.* Suppose $f$ has $n$ zeroes on $I$, say
$x_{1} < x_{2} < \cdots < x_{n}$. On each sub-interval
$[x_{k}, x_{k+1}]$ ($k = 1, \ldots, n-1$), the function $f$ satisfies
the hypotheses of Rolle's Theorem: it is continuous on
$[x_{k}, x_{k+1}]$, differentiable on $(x_{k}, x_{k+1})$, and
$f(x_{k}) = f(x_{k+1}) = 0$.

Therefore, for each $k$, there exists $c_{k} \in (x_{k}, x_{k+1})$ with
$f'(c_{k}) = 0$. Since $c_{1} < c_{2} < \cdots < c_{n-1}$, the
derivative $f'$ has at least $n - 1$ zeroes.

Equivalently, if $f'$ has $m$ zeroes, then $f$ has at most $m + 1$
zeroes. ◻
:::

::: example
[]{#ex:5-2 label="ex:5-2"} How many zeroes does
$g(x) = x^{6} + x^{2} + x - 2$ have?

**Lower bound (IVT).** The function $g$ is a polynomial, hence
continuous on $\mathbb{R}$. We compute:
$$g(-2) = 64 + 4 - 2 - 2 = 64 > 0, \qquad g(0) = -2 < 0, \qquad g(1) = 1 + 1 + 1 - 2 = 1 > 0.$$
Since $g$ changes sign from positive to negative on $(-2, 0)$ and from
negative to positive on $(0, 1)$, the IVT guarantees at least **two**
zeroes.

**Upper bound (Rolle's Theorem and
[\[thm:5-4\]](#thm:5-4){reference-type="ref+label"
reference="thm:5-4"}).** Compute: $$\begin{align*}
  g'(x)  &= 6x^{5} + 2x + 1, \\
  g''(x) &= 30x^{4} + 2.
\end{align*}$$ Since $x^{4} \geq 0$ for all $x$, we have
$g''(x) \geq 2 > 0$ for all $x$. So $g''$ has **zero** zeroes.

By [\[thm:5-4\]](#thm:5-4){reference-type="ref+label"
reference="thm:5-4"} applied to $g'$: the number of zeroes of $g'$ is at
most $0 + 1 = 1$.

By [\[thm:5-4\]](#thm:5-4){reference-type="ref+label"
reference="thm:5-4"} applied to $g$: the number of zeroes of $g$ is at
most $1 + 1 = 2$.

Since $g$ has at least two zeroes and at most two zeroes, $g$ has
**exactly two** zeroes.
:::

## The Mean Value Theorem {#sec:5.7}

*We have been working towards this theorem for a while: the Extreme
Value Theorem, the Local Extreme Value Theorem, and Rolle's Theorem were
all stepping stones. The Mean Value Theorem itself will appear not very
interesting at first, but we care about it because it has many powerful
applications.*

Recall Rolle's Theorem
([\[thm:5-3\]](#thm:5-3){reference-type="ref+label"
reference="thm:5-3"}): if $f$ is continuous on $[a,b]$, differentiable
on $(a,b)$, and $f(a) = f(b)$, then there exists $c \in (a,b)$ with
$f'(c) = 0$.

*For the Mean Value Theorem, we keep the first two hypotheses (they hold
for most common functions) but remove the third. The question is: with
only continuity and differentiability, what conclusion can we still
draw?*

*Consider a function satisfying the first two hypotheses, but with
$f(a) \neq f(b)$. Draw the line through the points $(a, f(a))$ and
$(b, f(b))$. Imagine "tilting" the picture so that this line becomes
horizontal. From the tilted perspective, the endpoint values are equal,
so Rolle's Theorem applies and there is a point where the tangent line
is horizontal---that is, parallel to the line through the endpoints.
Returning to the original picture, we conclude there exists a point
where the slope of the tangent line equals the slope of the secant line
through $(a, f(a))$ and $(b, f(b))$.*

::: theorem
[]{#thm:5-5 label="thm:5-5"} Let $f$ be defined on a closed, bounded
interval $[a,b]$. Suppose:

1.  $f$ is continuous on $[a,b]$,

2.  $f$ is differentiable on $(a,b)$.

Then there exists at least one $c \in (a,b)$ such that
$$f'(c) = \frac{f(b) - f(a)}{b - a}.$$
:::

<figure id="fig:mean-value-theorem" data-latex-placement="ht">

<figcaption>Mean Value Theorem: a tangent parallel to the
secant.</figcaption>
</figure>

::: remark
The Mean Value Theorem does **not** merely assert that the equation
$f'(c) = \dfrac{f(b) - f(a)}{b - a}$ holds. It says: **if** the
hypotheses are satisfied, **then** there **exists** a value
$c \in (a,b)$ making the equation true. The full logical
structure---hypotheses, existential quantifier, and equation---is the
theorem.
:::

::: remark
Like Rolle's Theorem and the Intermediate Value Theorem, the MVT is a
pure **existence** result. It guarantees that at least one such $c$
exists, but it does not tell us how to find it.
:::

## Proof of the MVT {#sec:5.8}

*The idea of the proof is to reduce the Mean Value Theorem to Rolle's
Theorem. We construct a new function $h$ that measures the vertical
distance between the graph of $f$ and the secant line through
$(a, f(a))$ and $(b, f(b))$. Since $h(a) = h(b) = 0$, Rolle's Theorem
applies to $h$.*

::: proof
*Proof of the Mean Value Theorem
([\[thm:5-5\]](#thm:5-5){reference-type="ref+label"
reference="thm:5-5"}).* Let $$m = \frac{f(b) - f(a)}{b - a}$$ be the
slope of the secant line through $(a, f(a))$ and $(b, f(b))$.

Define a new function $h$ on $[a,b]$ by
$$h(x) = f(x) - f(a) - m(x - a).$$

We verify the hypotheses of Rolle's Theorem for $h$ on $[a,b]$:

1.  $h$ is continuous on $[a,b]$, since $f$ is continuous and $m(x - a)$
    is a polynomial.

2.  $h$ is differentiable on $(a,b)$, since $f$ is differentiable and
    $m(x - a)$ is a polynomial.

3.  $h(a) = f(a) - f(a) - m \cdot 0 = 0$, and
    $$h(b) = f(b) - f(a) - m(b - a) = f(b) - f(a) - \bigl(f(b) - f(a)\bigr) = 0.$$
    So $h(a) = h(b) = 0$.

By Rolle's Theorem, there exists $c \in (a,b)$ such that $h'(c) = 0$.

Now observe that for any $x \in (a,b)$, $$h'(x) = f'(x) - m.$$ Therefore
$h'(c) = 0$ gives $f'(c) = m$, which is exactly
$$f'(c) = \frac{f(b) - f(a)}{b - a}. \qedhere$$ ◻
:::

*After all this work, we have a proof of the Mean Value Theorem. We are
now ready to start profiting from it!*

## Zero Derivative Implies Constant {#sec:5.9}

*This is our first application of the Mean Value Theorem. We return to
the problem raised at the very beginning: proving that constant
functions are the only functions with zero derivative. This seems
obvious, but it genuinely requires the Mean Value Theorem.*

::: theorem
[]{#thm:5-6 label="thm:5-6"} Let $f$ be defined on a closed interval
$[a,b]$. If $f$ is continuous on $[a,b]$ and $f'(x) = 0$ for every
$x \in (a,b)$, then $f$ is constant on $[a,b]$.
:::

::: proof
*Proof.* We must show that $f(x_{1}) = f(x_{2})$ for every
$x_{1}, x_{2} \in [a,b]$.

Fix arbitrary $x_{1}, x_{2} \in [a,b]$. Without loss of generality,
assume $x_{1} < x_{2}$. (If $x_{1} = x_{2}$, there is nothing to prove.)

We apply the Mean Value Theorem to $f$ on the interval $[x_{1}, x_{2}]$.
The hypotheses are satisfied: $f$ is continuous on
$[x_{1}, x_{2}] \subseteq [a,b]$, and $f$ is differentiable on
$(x_{1}, x_{2}) \subseteq (a,b)$.

By the MVT, there exists $c \in (x_{1}, x_{2})$ such that
$$f'(c) = \frac{f(x_{2}) - f(x_{1})}{x_{2} - x_{1}}.$$ But $f'(c) = 0$
by hypothesis, so $f(x_{2}) - f(x_{1}) = 0$, that is,
$f(x_{1}) = f(x_{2})$. ◻
:::

::: theorem
[]{#thm:5-7 label="thm:5-7"} Let $f$ be defined on an open interval
$(a,b)$. If $f'(x) = 0$ for every $x \in (a,b)$, then $f$ is constant on
$(a,b)$.
:::

::: remark
The proof is a slight modification of the proof of
[\[thm:5-6\]](#thm:5-6){reference-type="ref+label" reference="thm:5-6"}.
Try to write it yourself.
:::

::: example
[]{#ex:5-3 label="ex:5-3"} Prove that there exists a constant $C$ such
that $$\arctan\!\sqrt{\frac{1-x}{1+x}} = C - \frac{1}{2}\arcsin x,$$
find the value of $C$, and determine for which values of $x$ the
identity holds.

**Solution.** In principle, this is a problem in trigonometry that could
be solved with identities. But calculus makes it faster.

Proving the identity is equivalent to proving that the function
$$F(x) = \arctan\!\sqrt{\frac{1-x}{1+x}} + \frac{1}{2}\arcsin x$$ is
constant. After checking the domain (which turns out to be $(-1, 1]$),
we compute the derivative. The calculation requires some work, but after
simplification, one obtains $F'(x) = 0$ for all $x \in (-1, 1)$.

By [\[thm:5-6\]](#thm:5-6){reference-type="ref+label"
reference="thm:5-6"} (noting that $F$ is continuous on $(-1, 1]$ and
differentiable on $(-1, 1)$), the function $F$ is constant on $(-1, 1]$.

To find $C$, evaluate at $x = 0$:
$$C = F(0) = \arctan(1) + \frac{1}{2}\arcsin(0) = \frac{\pi}{4}.$$ The
identity holds for all $x \in (-1, 1]$.
:::

## Antiderivatives and Integration {#sec:5.10}

*This is our second application of the Mean Value Theorem. It explains
why integration is possible---more precisely, why adding a constant
"$+ C$" to one antiderivative produces *all* antiderivatives.*

::: example
[]{#ex:5-4 label="ex:5-4"} Find all functions $f$ whose derivative is
$x^{2}$. By trial and error, $\frac{1}{3}x^{3}$ works. Adding any
constant still works: $\frac{1}{3}x^{3} + C$ is also a solution. But
could there be other solutions that are **not** of this form?
:::

*The answer is no, and we must prove it. The proof is short, now that we
have the Mean Value Theorem.*

::: corollary
[]{#thm:5-8 label="thm:5-8"} Let $f$ and $g$ be defined on an open
interval $(a,b)$. If $f'(x) = g'(x)$ for all $x \in (a,b)$, then there
exists a constant $C$ such that $f(x) = g(x) + C$ for all $x \in (a,b)$.
:::

::: proof
*Proof.* Define $h(x) = f(x) - g(x)$. Then $h'(x) = f'(x) - g'(x) = 0$
for all $x \in (a,b)$. By
[\[thm:5-7\]](#thm:5-7){reference-type="ref+label" reference="thm:5-7"},
$h$ is constant, so there exists $C \in \mathbb{R}$ with $h(x) = C$ for
all $x$. That is, $f(x) = g(x) + C$. ◻
:::

::: remark
Returning to [\[ex:5-4\]](#ex:5-4){reference-type="ref+label"
reference="ex:5-4"}: if $f'(x) = x^{2}$, then $f'(x) = g'(x)$ where
$g(x) = \frac{1}{3}x^{3}$. By
[\[thm:5-8\]](#thm:5-8){reference-type="ref+label" reference="thm:5-8"},
there exists a constant $C$ such that $f(x) = \frac{1}{3}x^{3} + C$.
These are **all** the solutions.
:::

*This bears repeating, because it is very important. Without the Mean
Value Theorem, we could only say that any function of the form
$\frac{1}{3}x^{3} + C$ is *a* solution. Thanks to the Mean Value
Theorem, we can say these are **all** the solutions. This idea is at the
core of every integration method: find one antiderivative, add "$+ C$,"
and you have found them all. The MVT is therefore at the foundation of
all integration theorems.*

## Monotonicity and Derivatives {#sec:5.11}

*This is our third application of the Mean Value Theorem: the
relationship between the sign of the derivative and whether a function
is increasing or decreasing.*

::: remark
Saying that a function is increasing is **not** the same thing as saying
it has positive derivative. These two concepts are related, but they are
**not the same**. A function can be increasing everywhere yet have
derivative zero at a point, or have a corner where the derivative does
not exist, or even be discontinuous at infinitely many points. Positive
derivative is not the *definition* of increasing.
:::

::: definition
[]{#def:5-4 label="def:5-4"} Let $f$ be a function defined on an
interval $I$.

1.  $f$ is *increasing* on $I$ when, for every $x_{1}, x_{2} \in I$,
    $$x_{1} < x_{2} \;\Longrightarrow\; f(x_{1}) < f(x_{2}).$$

2.  $f$ is *non-decreasing* on $I$ when, for every $x_{1}, x_{2} \in I$,
    $$x_{1} < x_{2} \;\Longrightarrow\; f(x_{1}) \leq f(x_{2}).$$

Analogous definitions hold for *decreasing* and *non-increasing*
(reverse the second inequality).
:::

::: remark
This terminology is not universal. Some books use "strictly increasing"
for what we call "increasing," and "increasing" for what we call
"non-decreasing." When reading other sources or working with others,
make sure you agree on the definitions.
:::

::: theorem
[]{#thm:5-9 label="thm:5-9"} Let $f$ be defined on an open interval
$(a,b)$. If $f'(x) > 0$ for every $x \in (a,b)$, then $f$ is increasing
on $(a,b)$.
:::

::: theorem
[]{#thm:5-10 label="thm:5-10"} Let $f$ be defined on a closed, bounded
interval $[a,b]$. If $f$ is continuous on $[a,b]$ and $f'(x) > 0$ for
every $x \in (a,b)$, then $f$ is increasing on $[a,b]$.
:::

::: remark
The proofs of
[\[thm:5-9,thm:5-10\]](#thm:5-9,thm:5-10){reference-type="ref+label"
reference="thm:5-9,thm:5-10"} are direct applications of the Mean Value
Theorem, following the same pattern as the proof of
[\[thm:5-6\]](#thm:5-6){reference-type="ref+label" reference="thm:5-6"}.
Fix $x_{1} < x_{2}$ in the interval, apply the MVT on $[x_{1}, x_{2}]$,
and use $f'(c) > 0$ to conclude $f(x_{2}) - f(x_{1}) > 0$. Try writing
them out.
:::

Here is a summary of the results linking the sign of the derivative to
monotonicity on an open interval $(a,b)$:

::: center
  **Derivative condition**               **Conclusion**
  ----------------------------------- -- ------------------------------
  $f'(x) = 0$ for all $x \in (a,b)$      $f$ is constant on $(a,b)$
  $f'(x) > 0$ for all $x \in (a,b)$      $f$ is increasing on $(a,b)$
  $f'(x) < 0$ for all $x \in (a,b)$      $f$ is decreasing on $(a,b)$
:::

At an isolated point where the derivative is zero or does not exist, the
function could be increasing, decreasing, or have a local extremum. The
derivative at a single point does not determine the local behaviour; one
must examine the sign of the derivative on intervals.

## Intervals of Monotonicity {#sec:5.12}

*Let us illustrate, with an example, how to find the intervals where a
function is increasing or decreasing using the theorems of the previous
section.*

:::::: example
[]{#ex:5-5 label="ex:5-5"} Find the intervals on which
$f(x) = 8x^{5} + 5x^{4} - 20x^{3}$ is increasing or decreasing.

::: remark
Pause and try to solve this problem before reading the solution.
:::

**Step 1: Compute and factor the derivative.**
$$f'(x) = 40x^{4} + 20x^{3} - 60x^{2} = 20x^{2}(2x + 3)(x - 1).$$

**Step 2: Find the critical points.** Setting $f'(x) = 0$ gives $x = 0$,
$x = -\frac{3}{2}$, and $x = 1$.

**Step 3: Determine the sign of $f'$ on each sub-interval.** Since $f'$
is a product of three factors $20x^{2}$, $(2x+3)$, and $(x-1)$, we
analyse the sign of each:

::: center
               $\bigl(-\infty,-\tfrac{3}{2}\bigr)$   $-\frac{3}{2}$   $\bigl(-\tfrac{3}{2},0\bigr)$   $0$   $(0,1)$   $1$   $(1,\infty)$
  ----------- ------------------------------------- ---------------- ------------------------------- ----- --------- ----- --------------
  $20x^{2}$                    $+$                        $+$                      $+$                $0$     $+$     $+$       $+$
  $2x+3$                       $-$                        $0$                      $+$                $+$     $+$     $+$       $+$
  $x-1$                        $-$                        $-$                      $-$                $-$     $-$     $0$       $+$
  $f'(x)$                      $+$                        $0$                      $-$                $0$     $-$     $0$       $+$
:::

**Step 4: Conclude monotonicity.**

- On $\bigl(-\infty, -\frac{3}{2}\bigr)$, $f'(x) > 0$, so $f$ is
  increasing.

- On $\bigl(-\frac{3}{2}, 0\bigr)$ and $(0, 1)$, $f'(x) < 0$, so $f$ is
  decreasing on each.

- On $(1, \infty)$, $f'(x) > 0$, so $f$ is increasing.

Since $f$ is continuous at the critical points, we may include them in
the intervals of monotonicity (by
[\[thm:5-10\]](#thm:5-10){reference-type="ref+label"
reference="thm:5-10"} and its decreasing analogue):

- $f$ is **increasing** on $\bigl(-\infty, -\frac{3}{2}\bigr]$.

- $f$ is **decreasing** on $\bigl[-\frac{3}{2}, 1\bigr]$ (since $f'<0$
  on $\bigl(-\frac{3}{2},0\bigr) \cup (0,1)$ and $f'(0) = 0$, the
  function is decreasing on the entire interval
  $\bigl[-\frac{3}{2},1\bigr]$).

- $f$ is **increasing** on $[1, \infty)$.

**Step 5: Classify the critical points.**

At $x = -\frac{3}{2}$: the derivative is zero, the function is
increasing to the left and decreasing to the right, so $f$ has a **local
maximum**.

At $x = 1$: the derivative is zero, the function is decreasing to the
left and increasing to the right, so $f$ has a **local minimum**.

At $x = 0$: the derivative is zero, but the function is decreasing on
both sides. This is **not** a local extremum; it is an *inflection
point* (with a horizontal tangent line).

::: remark
We include $x = 1$ in both the decreasing interval
$\bigl[-\frac{3}{2}, 1\bigr]$ and the increasing interval $[1, \infty)$.
This is not a contradiction: a function is increasing or decreasing on
an *interval*, not at a *point*.
:::
::::::

# Further Applications of Derivatives and Limits

## A Related Rates Problem {#sec:6.1}

*A related rates problem is an application of calculus to a real-life
situation where there are multiple quantities that depend on each other,
and we need to find a relation between their derivatives. Here is our
first example.*

::: example
[]{#ex:6-1 label="ex:6-1"} A plane flying horizontally at an altitude of
$10\,\text{km}$ passes directly above a radar station. A bit later, the
radar station measures that the distance between the plane and the
station is $20\,\text{km}$ and is increasing at a rate of
$1000\,\text{km/h}$. What is the speed of the plane?
:::

::: remark
Pause and try to solve the problem. Even if you cannot fully solve it,
spending time understanding the question, getting started, and sketching
a picture will make the following explanation much more useful.
:::

**Step 1: Modelling.** We transform the word problem into a calculus
question. Begin by drawing a picture. The radar station is on the
ground, and the plane flies horizontally above it.

Introduce variables:

- Let $h = 10\,\text{km}$ be the altitude of the plane (a **constant**).

- Let $z$ be the distance between the radar station and the plane (this
  is what the radar measures).

- Let $x$ be the horizontal position of the plane.

Both $x$ and $z$ depend on time $t$. We **want** $\dfrac{dx}{dt}$ at the
instant when $z = 20\,\text{km}$ and
$\dfrac{dz}{dt} = 1000\,\text{km/h}$.

Since the radar station, the point directly below the plane, and the
plane itself form a right triangle, the Pythagorean theorem gives the
relation $$z^{2} = x^{2} + h^{2}.$$

**Step 2: Solving.** We need a relation between $\dfrac{dx}{dt}$ and
$\dfrac{dz}{dt}$. Differentiate both sides of the relation with respect
to $t$ (using the chain rule):
$$2z\,\frac{dz}{dt} = 2x\,\frac{dx}{dt}.$$ Solving for the desired
quantity: $$\frac{dx}{dt} = \frac{z}{x}\,\frac{dz}{dt}.$$ We know
$z = 20$ and $\dfrac{dz}{dt} = 1000$, and we can solve for $x$ from the
original equation:
$$x = \sqrt{z^{2} - h^{2}} = \sqrt{20^{2} - 10^{2}} = \sqrt{300} = 10\sqrt{3}\,\text{km}.$$
Substituting:
$$\frac{dx}{dt} = \frac{20}{10\sqrt{3}}\cdot 1000 = \frac{2000}{\sqrt{3}}\,\text{km/h}.$$
The speed of the plane is $\dfrac{2000}{\sqrt{3}}\,\text{km/h}$.

## Related Rates: Shadow Problem {#sec:6.2}

*Here is a second example of a related rates problem. The modelling step
is the key: we must identify what is constant, what depends on time,
find an equation relating the quantities, and then differentiate
implicitly.*

::: example
[]{#ex:6-2 label="ex:6-2"} A prisoner runs in a straight line towards
the wall of a prison. A spotlight on the ground, $30\,\text{m}$ from the
wall, points at the prisoner. The prisoner is $1.8\,\text{m}$ tall. How
fast is the height of the shadow on the wall changing when the prisoner
is $20\,\text{m}$ from the wall and running at $8\,\text{m/s}$?
:::

::: remark
Pause and try to solve this problem. Even if you cannot fully solve it,
drawing a picture and understanding the statement will make the
explanation much more useful.
:::

**Step 1: Modelling.** Draw a picture with the spotlight on the ground,
the wall, and the prisoner between them. Introduce variables:

- $a = 30\,\text{m}$: the distance from the spotlight to the wall
  (**constant**).

- $h = 1.8\,\text{m}$: the height of the prisoner (**constant**).

- $x$: the distance from the prisoner to the spotlight (depends on
  time).

- $y$: the height of the shadow on the wall (depends on time).

We **want** $\dfrac{dy}{dt}$ at the instant when $x = 10\,\text{m}$
(since the prisoner is $20\,\text{m}$ from the wall and $a = 30$) and
$\dfrac{dx}{dt} = 8\,\text{m/s}$.

By similar triangles (the triangle with height $h$ and base $x$, and the
triangle with height $y$ and base $a$): $$\frac{h}{x} = \frac{y}{a}.$$

**Step 2: Solving.** Differentiate both sides implicitly with respect to
$t$. Since $h$ and $a$ are constants:
$$h\cdot\biggl(-\frac{1}{x^{2}}\biggr)\frac{dx}{dt} = \frac{1}{a}\,\frac{dy}{dt}.$$
Solving: $$\frac{dy}{dt} = -\frac{ah}{x^{2}}\,\frac{dx}{dt}.$$
Substituting:
$$\frac{dy}{dt} = -\frac{(30)(1.8)}{10^{2}}\cdot 8 = -4.32\,\text{m/s}.$$

The rate of change is negative, confirming that the shadow height is
*decreasing* as the prisoner approaches the wall.

<figure id="fig:related-rates-shadow" data-latex-placement="ht">

<figcaption>Shadow geometry for a classic related-rates
setup.</figcaption>
</figure>

## Optimization: Minimizing Surface Area {#sec:6.3}

*An optimization problem is an application of calculus to a physical
situation where we want to make a certain quantity as large or as small
as possible.*

::: example
[]{#ex:6-3 label="ex:6-3"} We want to build an open box (four side walls
and a bottom, no top) with a square base. The volume must be
$500\,\text{cm}^{3}$. What dimensions minimize the total surface area
(and hence the material cost)?
:::

::: remark
Pause and try to solve the problem before continuing. Even a partial
attempt will make the explanation much more useful.
:::

**Step 1: Modelling.** Let $x$ be the side length of the square base and
$y$ the height. The total surface area (bottom plus four sides) is
$$S = x^{2} + 4xy.$$ The volume constraint is $x^{2}y = 500$, so
$y = \dfrac{500}{x^{2}}$. Substituting:
$$S(x) = x^{2} + \frac{2000}{x}, \qquad x > 0.$$

**Step 2: Solving.** The function $S$ is differentiable on $(0,\infty)$.
Compute the derivative:
$$S'(x) = 2x - \frac{2000}{x^{2}} = \frac{2(x^{3} - 1000)}{x^{2}}.$$
Setting $S'(x) = 0$ gives $x^{3} = 1000$, i.e. $x = 10$. This is the
only critical point.

::: remark
Many students stop here and declare the answer, but we are looking for
the **minimum**, not just a critical point. We must justify that the
minimum actually occurs at $x = 10$.
:::

When $x < 10$, we have $S'(x) < 0$ (decreasing), and when $x > 10$, we
have $S'(x) > 0$ (increasing). Therefore $S$ decreases all the way to
$x = 10$ and increases afterwards, so the global minimum occurs at
$x = 10$.

The optimal dimensions are $x = 10\,\text{cm}$ and
$y = \dfrac{500}{100} = 5\,\text{cm}$.

<figure id="fig:optimization-cylinder" data-latex-placement="ht">

<figcaption>A cylinder labeled with radius <span
class="math inline"><em>r</em></span> and height <span
class="math inline"><em>h</em></span>.</figcaption>
</figure>

## Optimization with Endpoints {#sec:6.4}

*In this example, the domain is a closed and bounded interval, so we can
appeal to the Extreme Value Theorem.*

::: example
[]{#ex:6-4 label="ex:6-4"} A woman at point $A$ on one side of a
straight river, $3\,\text{km}$ wide, wants to reach point $B$,
$8\,\text{km}$ downstream on the opposite side. She can row at
$6\,\text{km/h}$ and run at $8\,\text{km/h}$. Where should she land to
reach $B$ as soon as possible?
:::

::: remark
Pause and try to set up the problem: draw a picture, introduce a
variable for the landing point, and write a formula for the total travel
time.
:::

**Step 1: Modelling.** Let $C$ be the point where she lands, and let $x$
be the distance from the point directly across from $A$ to $C$. Then the
rowing distance is $\sqrt{x^{2} + 9}$ and the running distance is
$8 - x$. The total time is
$$T(x) = \frac{\sqrt{x^{2} + 9}}{6} + \frac{8 - x}{8}, \qquad x \in [0, 8].$$

**Step 2: Solving.** The function $T$ is continuous on the closed,
bounded interval $[0,8]$. By the Extreme Value Theorem, $T$ has a
minimum, and this minimum occurs either at a critical point or at an
endpoint.

::: remark
We **must** include endpoints. If she could row much faster than she
could run, the optimal path would be directly from $A$ to $B$ ($x = 8$).
If she could run much faster, going straight across ($x = 0$) would be
optimal. So the minimum *could* be an endpoint, and we cannot dismiss
them.
:::

Computing the derivative and setting it to zero, after some algebra we
find one critical point inside the domain:
$$x = \frac{9}{\sqrt{7}}\,\text{km}.$$ Compare the three candidate
values: $$\begin{array}{c|ccc}
  x & 0 & \dfrac{9}{\sqrt{7}} & 8 \\[6pt] \hline \\[-6pt]
  T(x) & 1.5\,\text{h} & 1 + \dfrac{\sqrt{7}}{8} \approx 1.33\,\text{h} & \dfrac{\sqrt{73}}{6} \approx 1.42\,\text{h}
\end{array}$$ The smallest value is at the critical point. She should
land $\dfrac{9}{\sqrt{7}}\,\text{km}$ downstream.

## Indeterminate Forms {#sec:6.5}

*Before introducing L'Hôpital's Rule, we must understand what an
indeterminate form is---and, just as importantly, what it is **not**.*

Consider the limit $\displaystyle\lim_{x \to 0}\frac{f(x)}{g(x)}$ where
both $f$ and $g$ are continuous and $f(0) = g(0) = 0$. Substituting
gives $\frac{0}{0}$, which is not a number. We have an *indeterminate
form*.

::: definition
[]{#def:6-1 label="def:6-1"} We say that a limit
$\displaystyle\lim_{x \to a}\frac{f(x)}{g(x)}$ has the indeterminate
form $\frac{0}{0}$ when $\lim_{x \to a}f(x) = 0$ and
$\lim_{x \to a}g(x) = 0$. This means that, **based on this information
alone**, we cannot determine the value of the limit.
:::

To see why, consider these three examples, all of type $\frac{0}{0}$ as
$x \to 0$: $$\lim_{x \to 0}\frac{2x}{x} = 2, \qquad
  \lim_{x \to 0}\frac{x^{2}}{x} = 0, \qquad
  \lim_{x \to 0}\frac{x}{x^{3}} = \infty.$$ The same hypotheses yield
different answers each time.

::: remark
Three important clarifications:

1.  We are talking about **limits**. We are never actually dividing zero
    by zero. For each value of $x$, we have something *close to* zero
    divided by something *close to* zero.

2.  Indeterminate form does **not** mean the limit is undefined or does
    not exist. It only means we do not yet know the answer and must do
    more work.

3.  Indeterminate forms arise because of a **tension** between two parts
    of the function. In $\frac{0}{0}$, the numerator "thinks" the
    quotient should be zero, while the denominator "thinks" it should be
    $\pm\infty$. The outcome depends on which approaches zero faster.
:::

The most common indeterminate forms are:
$$\frac{0}{0},\quad \frac{\pm\infty}{\pm\infty},\quad 0\cdot\infty,\quad \infty - \infty,\quad 0^{0},\quad \infty^{0},\quad 1^{\pm\infty}.$$

::: remark
Why is $\dfrac{1}{0}$ not on the list? Because we *can* draw a
conclusion: if $\lim f(x) = 1$ and $\lim g(x) = 0$, then
$\lim\left\lvert \frac{f(x)}{g(x)} \right\rvert = \infty$. The exact
answer ($+\infty$ or $-\infty$) depends on the **sign** of the
denominator near the point, but we are not stuck---we can say something.
:::

::: example
[]{#ex:6-5 label="ex:6-5"} Compute
$\displaystyle\lim_{x \to 3^{+}}\frac{1}{(x - 3)(2 - x)}$.

This is of the form $\frac{1}{0}$. As $x \to 3^{+}$: $(x-3) > 0$ and
$(2-x) < 0$, so the denominator is negative. Therefore the limit is
$-\infty$.
:::

## L'Hôpital's Rule {#sec:6.6}

*L'Hôpital's Rule is a powerful tool for computing limits that produce
indeterminate forms of type $\frac{0}{0}$ or
$\frac{\pm\infty}{\pm\infty}$. It tells us that, under certain
conditions, we may replace the numerator and denominator by their
derivatives.*

::: theorem
[]{#thm:6-1 label="thm:6-1"} Let $f$ and $g$ be functions, and let $a$
be a real number (or $\pm\infty$). Suppose:

1.  The limit $\displaystyle\lim_{x \to a}\frac{f(x)}{g(x)}$ is an
    indeterminate form of type $\dfrac{0}{0}$ or
    $\dfrac{\pm\infty}{\pm\infty}$.

2.  $f$ and $g$ are differentiable for $x$ near $a$ (but not necessarily
    at $a$).

3.  $g(x) \neq 0$ and $g'(x) \neq 0$ for $x$ near $a$ (but not
    necessarily at $a$).

4.  $\displaystyle\lim_{x \to a}\frac{f'(x)}{g'(x)}$ exists, or equals
    $+\infty$, or equals $-\infty$.

Then
$$\lim_{x \to a}\frac{f(x)}{g(x)} = \lim_{x \to a}\frac{f'(x)}{g'(x)}.$$
The theorem also holds for one-sided limits.
:::

::: remark
Condition (iv) is the one we often forget, but it is essential. If
$\lim \dfrac{f'}{g'}$ does not exist (and is not $\pm\infty$), then
L'Hôpital's Rule gives **no information** about $\lim\dfrac{f}{g}$. The
original limit may still exist.
:::

::: remark
The proof relies on a variant of the Mean Value Theorem and is quite
long (there are separate cases for $\frac{0}{0}$ and
$\frac{\infty}{\infty}$, and for each type of limit). It appears in
every standard calculus textbook.
:::

## L'Hôpital's Rule Examples {#sec:6.7}

*Let us work through several examples, from beginning to end, to see how
L'Hôpital's Rule is used in practice.*

::: example
[]{#ex:6-6 label="ex:6-6"} Compute
$\displaystyle\lim_{x \to \infty}\frac{x}{\ln x}$.

As $x \to \infty$: numerator $\to \infty$, denominator $\to \infty$.
This is $\dfrac{\infty}{\infty}$, so L'Hôpital's Rule applies.
Differentiating:
$$\lim_{x \to \infty}\frac{x}{\ln x} \stackrel{\text{L'H}}{=} \lim_{x \to \infty}\frac{1}{1/x} = \lim_{x \to \infty} x = \infty.$$
The second limit is $\infty$, so the use of L'Hôpital was legal, and the
original limit is $\infty$.
:::

::: example
[]{#ex:6-7 label="ex:6-7"} Compute
$\displaystyle\lim_{x \to 0}\frac{\cos x - \cos(2x)}{xe^{x} - x}$.

As $x \to 0$: numerator $\to 1 - 1 = 0$, denominator $\to 0 - 0 = 0$.
This is $\dfrac{0}{0}$. Apply L'Hôpital:
$$\stackrel{\text{L'H}}{=} \lim_{x \to 0}\frac{-\sin x + 2\sin(2x)}{e^{x} + xe^{x} - 1}.$$
As $x \to 0$: numerator $\to 0$, denominator $\to 1 + 0 - 1 = 0$. Still
$\dfrac{0}{0}$. Apply L'Hôpital again:
$$\stackrel{\text{L'H}}{=} \lim_{x \to 0}\frac{-\cos x + 4\cos(2x)}{2e^{x} + xe^{x}}.$$
Now as $x \to 0$: numerator $\to -1 + 4 = 3$, denominator
$\to 2 + 0 = 2$. The limit is $\dfrac{3}{2}$, which is a number;
therefore both applications of L'Hôpital were legal, and the original
limit is $\dfrac{3}{2}$.
:::

::: example
[]{#ex:6-8 label="ex:6-8"} Compute
$\displaystyle\lim_{x \to 1}\frac{x^{3} - 2x + 1}{x^{2} + 3x + 2}$.

As $x \to 1$: numerator $\to 1 - 2 + 1 = 0$, denominator
$\to 1 + 3 + 2 = 6$. This is $\dfrac{0}{6}$, which is **not** an
indeterminate form. We simply evaluate:
$$\lim_{x \to 1}\frac{x^{3} - 2x + 1}{x^{2} + 3x + 2} = \frac{0}{6} = 0.$$
:::

::: remark
In [\[ex:6-8\]](#ex:6-8){reference-type="ref+label" reference="ex:6-8"}
we are **not allowed** to use L'Hôpital's Rule because there is no
indeterminate form. If you try to use it anyway, you will get a wrong
answer.
:::

## Failure of L'Hôpital's Rule {#sec:6.8}

*L'Hôpital's Rule is very powerful, but it cannot always be used. Here
is an example where it fails silently---if we do not notice, we get a
wrong answer.*

::: example
[]{#ex:6-9 label="ex:6-9"} Compute
$\displaystyle\lim_{x \to \infty}\frac{x + \sin x}{2x + \cos x}$.

**Checking the form.** As $x \to \infty$, $\sin x$ oscillates between
$-1$ and $1$, but $x + \sin x \geq x - 1 \to \infty$, so the numerator
has limit $\infty$. By the same reasoning, the denominator has limit
$\infty$. We have $\dfrac{\infty}{\infty}$.

**Attempting L'Hôpital.** Differentiating:
$$\lim_{x \to \infty}\frac{1 + \cos x}{2 - \sin x}.$$ The function
$\dfrac{1 + \cos x}{2 - \sin x}$ is *periodic* with period $2\pi$. A
periodic, non-constant function never has a limit at infinity. Therefore
this limit **does not exist** (and is not $\pm\infty$).

By Condition (iv) of [\[thm:6-1\]](#thm:6-1){reference-type="ref+label"
reference="thm:6-1"}, L'Hôpital's Rule does not apply. It gives no
information.
:::

*So how do we compute the original limit? Without L'Hôpital, we can use
a direct argument.*

Divide numerator and denominator by $x$:
$$\frac{x + \sin x}{2x + \cos x} = \frac{1 + \frac{\sin x}{x}}{2 + \frac{\cos x}{x}}.$$
By the Squeeze Theorem, $\dfrac{\sin x}{x} \to 0$ and
$\dfrac{\cos x}{x} \to 0$ as $x \to \infty$ (since $\sin x$ and $\cos x$
are bounded). Therefore
$$\lim_{x \to \infty}\frac{x + \sin x}{2x + \cos x} = \frac{1 + 0}{2 + 0} = \frac{1}{2}.$$

::: remark
The limit *does* exist and equals $\frac{1}{2}$, even though L'Hôpital's
Rule could not detect it. This situation is uncommon, but it is
important to know that it can happen.
:::

## The Zero-Times-Infinity Form {#sec:6.9}

*L'Hôpital's Rule applies only to quotients. When we encounter
$0\cdot\infty$, we must first rewrite the product as a quotient.*

:::: example
[]{#ex:6-10 label="ex:6-10"} Compute
$\displaystyle\lim_{x \to \infty} x\bigl(1 - e^{2/x}\bigr)$.

::: remark
Pause and try to compute this limit. At least, try to understand what
the difficulty is.
:::

As $x \to \infty$: the first factor has limit $\infty$, and
$e^{2/x} \to e^{0} = 1$, so the second factor has limit $0$. We have
$\infty \cdot 0$, an indeterminate form.

**Do not** be tempted to say this is $0$.

Rewrite $x$ as $\dfrac{1}{1/x}$:
$$x\bigl(1 - e^{2/x}\bigr) = \frac{1 - e^{2/x}}{1/x}.$$ Now as
$x \to \infty$: numerator $\to 0$ and denominator $\to 0$. This is
$\dfrac{0}{0}$, and we may apply L'Hôpital:
$$\stackrel{\text{L'H}}{=} \lim_{x \to \infty}\frac{-e^{2/x}\cdot(-2/x^{2})}{-1/x^{2}} = \lim_{x \to \infty}\frac{2e^{2/x}\cdot(1/x^{2})}{1/x^{2}} = \lim_{x \to \infty} 2e^{2/x}\cdot(-1) = -2.$$
Wait---let us be more careful. Differentiating the numerator:
$$\frac{d}{dx}\bigl(1 - e^{2/x}\bigr) = -e^{2/x}\cdot\Bigl(-\frac{2}{x^{2}}\Bigr) = \frac{2e^{2/x}}{x^{2}}.$$
Differentiating the denominator:
$$\frac{d}{dx}\Bigl(\frac{1}{x}\Bigr) = -\frac{1}{x^{2}}.$$ Therefore:
$$\lim_{x \to \infty}\frac{2e^{2/x}/x^{2}}{-1/x^{2}} = \lim_{x \to \infty}(-2e^{2/x}) = -2.$$
Since $-2$ is a number, the use of L'Hôpital was legal, and the original
limit is $-2$.
::::

::: remark
This trick always works for $0 \cdot \infty$: if $\lim f = 0$ and
$\lim g = \infty$, rewrite $f\cdot g$ as $\dfrac{f}{1/g}$ (giving
$\frac{0}{0}$) or as $\dfrac{g}{1/f}$ (giving $\frac{\infty}{\infty}$).
:::

## The Infinity-Minus-Infinity Form {#sec:6.10}

*There is no single trick that works for all limits of the form
$\infty - \infty$. The strategy is to manipulate the expression
algebraically until it becomes a product or quotient to which we can
apply other tools.*

::: example
[]{#ex:6-11 label="ex:6-11"} Compute
$\displaystyle\lim_{x \to \infty}\bigl(\sqrt{x^{2} - x} - x\bigr)$.

As $x \to \infty$, the square root behaves like $x$ (since the leading
term inside is $x^{2}$), so both $\sqrt{x^{2}-x}$ and $x$ go to
$\infty$. We have $\infty - \infty$.

**Do not** be tempted to say this is $0$.

**Method 1 (factoring, then L'Hôpital).** Factor $x^{2}$ inside the
square root:
$$\sqrt{x^{2}-x} - x = x\sqrt{1-\frac{1}{x}} - x = x\Bigl(\sqrt{1-\frac{1}{x}} - 1\Bigr).$$
Now $\lim x = \infty$ and $\lim\bigl(\sqrt{1-1/x}-1\bigr) = 0$, so we
have $\infty\cdot 0$. Convert to a quotient:
$$\frac{\sqrt{1 - 1/x} - 1}{1/x}.$$ As $x \to \infty$, both numerator
and denominator approach $0$. Apply L'Hôpital:
$$\stackrel{\text{L'H}}{=} \lim_{x \to \infty}\frac{\dfrac{1}{2\sqrt{1 - 1/x}}\cdot\dfrac{1}{x^{2}}}{-\dfrac{1}{x^{2}}} = \lim_{x \to \infty}\frac{-1}{2\sqrt{1 - 1/x}} = -\frac{1}{2}.$$

**Method 2 (conjugate).** Multiply and divide by the conjugate
$\sqrt{x^{2}-x}+x$:
$$\sqrt{x^{2}-x} - x = \frac{(\sqrt{x^{2}-x})^{2} - x^{2}}{\sqrt{x^{2}-x}+x} = \frac{x^{2}-x-x^{2}}{\sqrt{x^{2}-x}+x} = \frac{-x}{\sqrt{x^{2}-x}+x}.$$
Factor $x$ from the denominator:
$$\frac{-x}{x\bigl(\sqrt{1-1/x}+1\bigr)} = \frac{-1}{\sqrt{1-1/x}+1} \to \frac{-1}{1+1} = -\frac{1}{2}.$$
Both methods give $-\dfrac{1}{2}$.
:::

## The One-to-Infinity Form {#sec:6.11}

*Of all indeterminate forms, $1^{\infty}$ is probably the most
controversial---the one students argue about the most. Let us explain
why it really is indeterminate, and why our intuition may be off.*

When we write $1^{\infty}$, we do **not** mean "the number $1$ raised to
the power infinity." We mean numbers *close to* $1$ raised to very large
exponents.

::: proposition
[]{#thm:6-2 label="thm:6-2"} $1^{\infty}$ is an indeterminate form:
limits of the type $\lim f(x)^{g(x)}$ with $\lim f = 1$ and
$\lim g = \infty$ can take any positive value.
:::

::: proof
*Proof.* Let $c$ be any nonzero real number, and consider
$$\lim_{x \to 0^{+}} (e^{x})^{c/x}.$$ Here
$\lim_{x \to 0^{+}} e^{x} = 1$ and $\lim_{x \to 0^{+}} c/x = \pm\infty$
(depending on the sign of $c$). So this is of type $1^{\pm\infty}$. But
$$(e^{x})^{c/x} = e^{xc/x} = e^{c},$$ which is constant, so the limit is
$e^{c}$. By choosing different values of $c$, we obtain any positive
number. ◻
:::

*Why is it hard to accept that $1^{\infty}$ is indeterminate? If the
base were the **constant** $1$, then $1^{x} = 1$ for all $x$, and the
limit would certainly be $1$. But the base is not constant---it is a
function approaching $1$. If the base is slightly greater than $1$, the
exponent pushes the result towards $\infty$; if slightly less, towards
$0$. The base wants the answer to be $1$; the exponent wants it to be
$\infty$ or $0$. That tension is what makes it indeterminate.*

## Exponential Indeterminate Forms {#sec:6.12}

*The exponential indeterminate forms ($0^{0}$, $\infty^{0}$,
$1^{\infty}$, $1^{-\infty}$) all require the same trick: take a
logarithm to convert the power into a product or quotient, compute the
limit of the logarithm, then exponentiate.*

::: example
[]{#ex:6-12 label="ex:6-12"} Compute
$\displaystyle\lim_{x \to 0^{+}} (1 - x)^{1/x}$.

As $x \to 0$: the base $(1-x) \to 1$ and the exponent $1/x \to \infty$.
This is $1^{\infty}$.

**Do not** say the answer is $1$.

**Step 1: Compute the limit of the logarithm.** Let
$F(x) = (1-x)^{1/x}$. Then
$$\ln F(x) = \frac{1}{x}\ln(1-x) = \frac{\ln(1-x)}{x}.$$ As $x \to 0$:
numerator $\to \ln 1 = 0$ and denominator $\to 0$. This is
$\dfrac{0}{0}$. Apply L'Hôpital:
$$\lim_{x \to 0^{+}}\frac{\ln(1-x)}{x} \stackrel{\text{L'H}}{=} \lim_{x \to 0^{+}}\frac{-1/(1-x)}{1} = \lim_{x \to 0^{+}}\frac{-1}{1-x} = -1.$$

**Step 2: Recover the original limit.** Since $\ln F(x) \to -1$ and the
exponential function is continuous:
$$\lim_{x \to 0^{+}} F(x) = \lim_{x \to 0^{+}} e^{\ln F(x)} = e^{-1} = \frac{1}{e}.$$
:::

::: remark
The same strategy works for all exponential indeterminate forms:

1.  Set $F(x) = f(x)^{g(x)}$ and compute $\ln F(x) = g(x)\ln f(x)$.

2.  Compute $\lim \ln F(x)$ (this will be a product or quotient, to
    which L'Hôpital may apply).

3.  Conclude $\lim F(x) = e^{\lim \ln F(x)}$.
:::

## Concavity and Inflection Points {#sec:6.13}

*The concavity of a function refers to the shape of its graph. There are
several equivalent ways to define it for nice (differentiable)
functions. We will discuss three approaches, all of which agree when the
function is differentiable.*

*As motivation, consider the family of graphs $y = x^{a}$ for various
values of $a$. When $a > 1$ the curves look like deformed parabolas, all
with the same "shape." When $a < 1$ (and $a > 0$) they have a different
shape. We say these two families have different *concavity*.*

We call curves of the first type *concave up* and curves of the second
type *concave down*.

::: remark
Some older textbooks (and the French mathematical tradition) use
*concave* and *convex* instead of *concave up* and *concave down*, but
which is which may depend on the author. We prefer *concave up* and
*concave down*.
:::

Three candidate definitions for concave up:

1.  **Secant segments above the graph.** For any two points on the
    graph, the segment of the secant line between them lies above the
    graph.

2.  **Tangent lines below the graph.** At every point, the tangent line
    lies below the graph.

3.  **Slopes increasing.** The derivative $f'$ is an increasing
    function.

(For concave down, reverse "above" and "below," and replace "increasing"
by "decreasing.")

For differentiable functions, all three are **equivalent**. The proof
relies on the Mean Value Theorem. Definition (3) is the simplest and is
the one used by most calculus textbooks.

::: definition
[]{#def:6-2 label="def:6-2"} Let $f$ be differentiable on an interval
$I$.

1.  $f$ is *concave up* on $I$ when $f'$ is increasing on $I$.

2.  $f$ is *concave down* on $I$ when $f'$ is decreasing on $I$.
:::

::: definition
[]{#def:6-3 label="def:6-3"} An interior point $c$ of the domain of $f$
is called an *inflection point* if $f$ changes concavity at $c$: there
exists an interval centred at $c$ such that $f$ is concave up on one
side and concave down on the other.
:::

*Inflection points are to concavity what local extrema are to
monotonicity. A local extremum is where the function changes from
increasing to decreasing (or vice versa); an inflection point is where
it changes from concave up to concave down (or vice versa).*

At an inflection point, the tangent line *crosses* the graph---it lies
above the graph on one side and below on the other.

::: theorem
[]{#thm:6-3 label="thm:6-3"} Let $f$ be twice differentiable on an open
interval $I$.

1.  If $f''(x) > 0$ for all $x \in I$, then $f$ is concave up on $I$.

2.  If $f''(x) < 0$ for all $x \in I$, then $f$ is concave down on $I$.
:::

::: theorem
[]{#thm:6-4 label="thm:6-4"} If $f$ is twice differentiable on an
interval and has an inflection point at an interior point $c$, then
$f''(c) = 0$.
:::

::: remark
The converse of [\[thm:6-4\]](#thm:6-4){reference-type="ref+label"
reference="thm:6-4"} is **not** true. $f''(c) = 0$ does **not** imply
that $c$ is an inflection point. These are merely **candidate** points,
just as $f'(c)=0$ gives candidates for local extrema. More generally,
$f''(c) = 0$ or $f''(c)$ does not exist gives the candidates for
inflection points.
:::

## Curve Sketching with Derivatives {#sec:6.14}

*We now illustrate, with a detailed example, how to use the first and
second derivatives to study the monotonicity, concavity, and shape of a
function.*

Before we begin, recall the tools at our disposal. On an open interval:

- $f' > 0 \implies f$ is increasing;$f' < 0 \implies f$ is decreasing.

- $f'' > 0 \implies f$ is concave up;$f'' < 0 \implies f$ is concave
  down.

On a closed interval, we require the derivative condition only on the
interior, plus continuity at the endpoints. Candidates for local extrema
satisfy $f' = 0$ or $f'$ DNE; candidates for inflection points satisfy
$f'' = 0$ or $f''$ DNE.

::: example
[]{#ex:6-13 label="ex:6-13"} Let $f(x) = x^{6}(x+3)^{3}$. Find the
intervals of increase/decrease, local extrema, intervals of concavity,
inflection points, and sketch the graph.

**First derivative.** After computation and factoring:
$$f'(x) = 3x^{5}(x+3)^{2}(3x+6) = 9x^{5}(x+3)^{2}(x+2).$$ The zeros of
$f'$ are $x = 0$, $x = -3$, and $x = -2$. We determine the sign of $f'$
on each subinterval by tracking which factors change sign:

- For $x > 0$: $f'(x) > 0$.

- At $x = 0$: the factor $x^{5}$ changes sign, so $f'$ changes sign.

- At $x = -2$: the factor $(x+2)$ changes sign.

- At $x = -3$: the factor $(x+3)^{2}$ does **not** change sign (even
  exponent).

**Sign chart for $f'$:** $$\begin{array}{c|ccccccc}
              & (-\infty,-3) & -3 & (-3,-2) & -2 & (-2,0) & 0 & (0,\infty) \\ \hline
  f'          & +            & 0  & +       & 0  & -      & 0 & +
\end{array}$$

Therefore $f$ is increasing on $(-\infty, -2]$ (the sign at $-3$ does
not change, so we join the intervals), decreasing on $[-2, 0]$, and
increasing on $[0, \infty)$.

At $x = -2$ (increasing $\to$ decreasing): **local maximum**.\
At $x = 0$ (decreasing $\to$ increasing): **local minimum**.

**Second derivative.** After computation and factoring:
$$f''(x) = \cdots = 9x^{4}(x+3)(2x+3)(2x+5) \cdot (\text{positive constant}).$$
The zeros of $f''$ are at $x = 0$, $x = -3$, $x = -\frac{3}{2}$, and
$x = -\frac{5}{2}$. Tracking which factors change sign:

- $x^{4}$: even power, no sign change at $0$.

- $(x+3)$: changes sign at $-3$.

- $(2x+3)$: changes sign at $-\frac{3}{2}$.

- $(2x+5)$: changes sign at $-\frac{5}{2}$.

**Concavity:**

- $(-\infty, -3)$: concave down.

- $(-3, -\frac{5}{2})$: concave up.

- $(-\frac{5}{2}, -\frac{3}{2})$: concave down.

- $(-\frac{3}{2}, \infty)$: concave up.

**Inflection points** occur at $x = -3$, $x = -\frac{5}{2}$, and
$x = -\frac{3}{2}$ (where concavity changes).

**Special points:**

- $x = -3$: inflection point with horizontal tangent ($f'(-3) = 0$),
  function increasing on both sides.

- $x = -\frac{5}{2}$: inflection point, function increasing with
  positive slope.

- $x = -2$: local maximum.

- $x = -\frac{3}{2}$: inflection point, function decreasing with
  negative slope.

- $x = 0$: local minimum.

Using the monotonicity and concavity information together on each
subinterval, we sketch the graph, paying attention to the shape near
each special point.
:::

## Asymptotes {#sec:6.15}

*An asymptote is a line that becomes arbitrarily close to a curve as we
move away from the origin in some direction. This single idea unifies
vertical, horizontal, and slant asymptotes.*

::: definition
[]{#def:6-4 label="def:6-4"} A line $L$ is an *asymptote* of a curve $C$
if the distance between $L$ and $C$ approaches $0$ as we move along $C$
in some direction away from the origin.
:::

::: remark
If you learned in high school that "an asymptote is a line the curve
approaches but never touches," the "never touches" part is
**incorrect**. A graph may cross its asymptote, even infinitely many
times, and the line is still an asymptote as long as the distance tends
to $0$.
:::

A function may have multiple asymptotes. For instance, a single graph
can have one horizontal asymptote as $x \to -\infty$, two vertical
asymptotes, and a slant asymptote as $x \to +\infty$.

#### Vertical Asymptotes {#vertical-asymptotes .unnumbered}

::: definition
[]{#def:6-5 label="def:6-5"} The line $x = a$ is a *vertical asymptote*
of $f$ if at least one of the following holds:
$$\lim_{x \to a^{+}}f(x) = \pm\infty, \qquad \lim_{x \to a^{-}}f(x) = \pm\infty.$$
:::

#### Horizontal Asymptotes {#horizontal-asymptotes .unnumbered}

::: definition
[]{#def:6-6 label="def:6-6"} The line $y = L$ is a *horizontal
asymptote* of $f$ if
$$\lim_{x \to +\infty}f(x) = L \qquad\text{or}\qquad \lim_{x \to -\infty}f(x) = L.$$
:::

#### Slant (Oblique) Asymptotes {#slant-oblique-asymptotes .unnumbered}

::: definition
[]{#def:6-7 label="def:6-7"} The line $y = mx + b$ is a *slant
asymptote* of $f$ if
$$\lim_{x \to +\infty}\bigl[f(x) - (mx + b)\bigr] = 0 \qquad\text{or}\qquad \lim_{x \to -\infty}\bigl[f(x) - (mx + b)\bigr] = 0.$$
:::

::: remark
One may view a horizontal asymptote as a special case of a slant
asymptote (with $m = 0$).
:::

<figure id="fig:vertical-and-slant-asymptotes"
data-latex-placement="ht">

<figcaption>A rational function with a vertical asymptote and a slant
asymptote.</figcaption>
</figure>

## Asymptotes of Rational Functions {#sec:6.16}

*We illustrate, with a detailed example, how to find all asymptotes of a
rational function.*

::: example
[]{#ex:6-14 label="ex:6-14"} Find all asymptotes of
$$f(x) = \frac{x^{3} + 1}{x^{3} - 2x^{2}} = \frac{x^{3}+1}{x^{2}(x-2)}.$$

**Vertical asymptotes.** The function is rational, continuous wherever
the denominator is nonzero. The denominator vanishes at $x = 0$ and
$x = 2$.

**At $x = 0$:** As $x \to 0$, the numerator approaches $1$ (positive)
and the factor $(x-2)$ approaches $-2$ (negative). The factor $x^{2}$ is
positive on both sides and vanishes. So the full function is negative
near $0$:
$$\lim_{x \to 0^{+}}f(x) = -\infty, \qquad \lim_{x \to 0^{-}}f(x) = -\infty.$$
Vertical asymptote: $x = 0$.

**At $x = 2$:** The numerator approaches $9$ (positive), $x^{2}$
approaches $4$ (positive), and $(x-2)$ changes sign:
$$\lim_{x \to 2^{+}}f(x) = +\infty, \qquad \lim_{x \to 2^{-}}f(x) = -\infty.$$
Vertical asymptote: $x = 2$.

**Horizontal asymptotes.** Compute limits at $\pm\infty$ by factoring
the leading term:
$$\frac{x^{3}+1}{x^{3}-2x^{2}} = \frac{x^{3}(1+1/x^{3})}{x^{3}(1-2/x)} = \frac{1+1/x^{3}}{1-2/x} \to \frac{1}{1} = 1.$$
The same holds for $x \to -\infty$. Horizontal asymptote: $y = 1$ (on
both sides).

This function has **no** slant asymptotes (since horizontal asymptotes
exist on both sides).
:::

::: remark
The asymptotes alone are not enough to sketch the graph precisely. For a
complete sketch, we should also compute the first derivative (for
monotonicity) and find intercepts. But whatever the graph looks like, it
must respect the asymptotic behaviour found above.
:::

## Slant Asymptote Computation {#sec:6.17}

*Not every function with asymptotes has horizontal ones. Here is an
example with a slant asymptote that is neither vertical nor horizontal.*

::: example
[]{#ex:6-15 label="ex:6-15"} Find all asymptotes of
$$g(x) = x + 2 + \frac{1}{e^{x^{2}} + 1}.$$

**Vertical asymptotes.** The domain is all of $\mathbb{R}$: the
denominator $e^{x^{2}}+1$ is always positive. Since $g$ is continuous on
$\mathbb{R}$, there are **no** vertical asymptotes.

**Horizontal asymptotes.** As $x \to \pm\infty$, $x^{2} \to \infty$, so
$e^{x^{2}} \to \infty$ and $\dfrac{1}{e^{x^{2}}+1} \to 0$. Therefore
$$\lim_{x \to \pm\infty}g(x) = \lim_{x \to \pm\infty}\bigl(x+2\bigr) = \pm\infty.$$
There are **no** horizontal asymptotes.

**Slant asymptote.** We observed that $g(x) \approx x+2$ for large
$\left\lvert x \right\rvert$. Check:
$$g(x) - (x+2) = \frac{1}{e^{x^{2}}+1} \to 0 \quad \text{as } x \to +\infty \text{ (and as } x \to -\infty\text{)}.$$
Since this difference tends to $0$, the line $y = x + 2$ is a **slant
asymptote** on both sides.

Moreover, $\dfrac{1}{e^{x^{2}}+1} > 0$ always, so the graph lies
*slightly above* the line $y = x+2$.
:::

## Slant Asymptotes via L'Hôpital {#sec:6.18}

*This example is significantly harder than the previous ones. The
function has **two different** slant asymptotes, one as $x \to +\infty$
and one as $x \to -\infty$. The computation requires L'Hôpital's Rule.*

::: example
[]{#ex:6-16 label="ex:6-16"} Find the slant asymptote of
$h(x) = x\arctan(x)$ as $x \to +\infty$.

**Conjecture.** Since
$\displaystyle\lim_{x \to \infty}\arctan(x) = \frac{\pi}{2}$, the
function $h(x) \approx \frac{\pi}{2}\,x$ for large $x$. Perhaps
$y = \frac{\pi}{2}\,x$ is the asymptote?

**Testing the conjecture.** Compute:
$$h(x) - \frac{\pi}{2}\,x = x\biggl(\arctan(x) - \frac{\pi}{2}\biggr).$$
As $x \to \infty$: the first factor $\to \infty$ and the second $\to 0$.
This is $\infty \cdot 0$. Convert to a quotient:
$$\frac{\arctan(x) - \frac{\pi}{2}}{1/x}.$$ Numerator $\to 0$,
denominator $\to 0$: we have $\dfrac{0}{0}$. Apply L'Hôpital:
$$\stackrel{\text{L'H}}{=} \lim_{x \to \infty}\frac{\dfrac{1}{1+x^{2}}}{-\dfrac{1}{x^{2}}} = \lim_{x \to \infty}\frac{-x^{2}}{1+x^{2}} = -1.$$
So
$\displaystyle\lim_{x \to \infty}\bigl[h(x) - \tfrac{\pi}{2}\,x\bigr] = -1 \neq 0$.
The line $y = \frac{\pi}{2}\,x$ is **not** an asymptote.

**Correcting the conjecture.** Since the difference approaches $-1$, we
can write:
$$h(x) - \biggl(\frac{\pi}{2}\,x - 1\biggr) \to 0 \quad\text{as } x \to \infty.$$
Therefore the slant asymptote as $x \to +\infty$ is
$y = \dfrac{\pi}{2}\,x - 1$.
:::

::: remark
The function $h(x) = x\arctan(x)$ has a **second**, different slant
asymptote as $x \to -\infty$. The process is similar. Try to find it:
consider $\displaystyle\lim_{x \to -\infty}\arctan(x) = -\frac{\pi}{2}$
and repeat the argument. You will obtain a different line.
:::

::: remark
Even if nobody has taught you a systematic algorithm for finding slant
asymptotes, you can still find them as long as you understand the
definition: the line $y = mx+b$ is a slant asymptote precisely when
$\lim\bigl[f(x) - (mx+b)\bigr] = 0$. Be willing to try a conjecture,
test it, and adjust if necessary.
:::

# The Definition of the Integral

## Geometric Motivation {#sec:7.1}

*The definition of the integral is quite long, and we will not reach it
in this section. Rather, we introduce the main ideas we will need. In a
later section we formalize these ideas into the actual definition.*

*We begin with a geometric interpretation.* Consider a function $f$ that
is positive and continuous on an interval $[a,b]$. The region between
the graph of $f$ and the $x$-axis is shaded, and we would like to define
the *area* of this region to be the integral.

::: definition
[]{#def:7-1 label="def:7-1"} The expression $$\int_{a}^{b} f(x)\,dx$$ is
read "the integral from $a$ to $b$ of $f(x)$, with respect to $x$,"
where $f$ is a function and $a,b$ are real numbers. It is sometimes
abbreviated as $\int_{a}^{b} f$. We call this a *definite integral*; it
is a number.
:::

::: remark
For now, the symbol $\,dx$ is merely a piece of notation indicating that
the variable of integration is $x$. We will later give it more meaning.
:::

::: remark
This is **not** a formal definition, because we do not yet know what the
area of an arbitrary region is. In general, we only know how to compute
the area of very simple shapes such as rectangles and triangles. We take
this geometric picture as **motivation** for what we want the integral
to represent.
:::

*We now spend some time trying to come up with a method to calculate the
area of an arbitrary region. Once we have that method, we will use the
resulting calculation as the definition of integral.*

There are three key steps in this construction.

**Step 1: Estimate with rectangles.** The simplest shape whose area we
know is the rectangle. Given the region under $f$ over $[a,b]$, we draw
a rectangle contained in the region, whose height is the minimum value
$m$ of $f$ on $[a,b]$, and a rectangle containing the region, whose
height is the maximum value $M$. Then
$$m(b-a) \;\le\; \int_{a}^{b} f(x)\,dx\;\le\; M(b-a).$$ These are very
rough estimates unless $f$ is nearly constant.

**Step 2: Cut into slices.** We improve the estimation by dividing the
region into vertical slices. For example, we cut the interval into four
sub-intervals and estimate each slice separately with a rectangle below
(under-estimate) and a rectangle above (over-estimate). The resulting
approximation is better: the error is smaller.

**Step 3: Take more and thinner slices.** As we increase the number of
slices and make them very thin, the estimation becomes better and
better.

*We now have a plan: cut into slices, approximate each slice with
rectangles, and then, in the limit, take many very thin slices. However,
we are not ready for the formal definition yet. We need two tools
first.*

1.  **Sigma notation.** When we use many slices and approximate each one
    with a rectangle, we must sum the areas of all those rectangles. The
    so-called sigma notation makes writing long, complicated sums much
    easier.

2.  **Supremum and infimum.** We have casually used the maximum and
    minimum of $f$ for the heights of the rectangles, but many nice
    functions do not attain maximum or minimum values. The notions of
    supremum and infimum are similar to maximum and minimum, but more
    versatile; they will replace the maximum and minimum in the formal
    definition.

## Sigma Notation {#sec:7.2}

*Sigma notation is a convenient notation for writing complicated sums in
a compact way.*

::: example
[]{#ex:7-1 label="ex:7-1"} The sum
$\dfrac{1}{3}+\dfrac{1}{4}+\dfrac{1}{5}+\dfrac{1}{6}+\dfrac{1}{7}$ can
be written in sigma notation as $$\sum_{i=3}^{7}\frac{1}{i}.$$ Each term
has the form $\frac{1}{i}$, where $i$ ranges from $3$ to $7$ in steps of
$1$. The letter $i$ under the $\Sigma$ indicates the *summation index*,
$i=3$ is the first value, and $7$ is the last value.
:::

More generally, we write the sum $a_1 + a_2 + \cdots + a_N$ as
$$\sum_{i=1}^{N} a_i,$$ where $a_i$ is any expression depending on an
integer $i$. This notation is especially useful when $a_i$ is
complicated.

::: remark
The summation index is a *dummy index*: it does not carry any intrinsic
meaning. We could equally write $\displaystyle\sum_{k=1}^{N} a_k$ and it
would denote exactly the same sum. Any letter (or symbol) may be used,
as long as it is not already in use for something else.
:::

::: example
[]{#ex:7-2 label="ex:7-2"} Let $k$ be a fixed constant. Compute each of
the following:

1.  $\displaystyle\sum_{i=1}^{3}\frac{i}{k}$,

2.  $\displaystyle\sum_{k=1}^{3}\frac{i}{k}$,

3.  $\displaystyle\sum_{\mu=1}^{3}\frac{i}{k}$.

**Solution.**

1.  The summation index is $i$. For the purpose of the sum, $k$ is a
    constant: $$\frac{1}{k}+\frac{2}{k}+\frac{3}{k} = \frac{6}{k}.$$

2.  The summation index is $k$. For the purpose of the sum, $i$ is a
    constant: $$\frac{i}{1}+\frac{i}{2}+\frac{i}{3} = \frac{11i}{6}.$$

3.  The summation index is $\mu$. Both $i$ and $k$ are constants, so the
    quantity $\frac{i}{k}$ does not change from term to term:
    $$\frac{i}{k}+\frac{i}{k}+\frac{i}{k} = \frac{3i}{k}.$$
:::

We conclude with two basic algebraic properties of sums.

::: proposition
[]{#thm:7-1 label="thm:7-1"} Let $c$ be a constant and let $a_i,b_i$
depend on the index $i$. Then:

1.  **Constant factor:**
    $\displaystyle\sum_{i=1}^{N} c\,a_i = c\sum_{i=1}^{N} a_i$.

2.  **Sum rule:**
    $\displaystyle\sum_{i=1}^{N}(a_i + b_i) = \sum_{i=1}^{N} a_i + \sum_{i=1}^{N} b_i$.
:::

::: remark
These are not new results. The first is the distributive property ("take
a common factor"), and the second follows from commutativity and
associativity of addition. They are simply old facts expressed in the
new notation.
:::

## Supremum and Infimum of Sets {#sec:7.3}

*The supremum and infimum are concepts similar to the maximum and
minimum, but more useful. In this section we define them for sets; in
the next section we extend the concepts to functions.*

*The notion of maximum is often insufficient. Let us explain why with an
example.*

::: example
[]{#ex:7-3 label="ex:7-3"} The closed interval $[0,2]$ has a maximum:
the number $2$, which is the largest element in the set. However, the
open interval $(0,2)$ does **not** have a maximum, because $2$ is not in
the set. Yet $2$ still "behaves like a maximum" in some sense. We need a
concept that describes what the number $2$ is to both $[0,2]$ and
$(0,2)$.
:::

::: definition
[]{#def:7-2 label="def:7-2"} A number $c$ is the *maximum* of a set $A$
when $c \in A$ and $x \le c$ for every $x \in A$.
:::

::: definition
[]{#def:7-3 label="def:7-3"} Let $A$ be a set of real numbers. A number
$c$ is an *upper bound* of $A$ when $x \le c$ for every $x \in A$.
:::

::: example
[]{#ex:7-4 label="ex:7-4"} For both $[0,2]$ and $(0,2)$, the number $2$
is an upper bound. But it is not the only one: $2.1$, $\pi$, and $100$
are all upper bounds. On the other hand, the set of integers
$\mathbb{Z}$ has no upper bound at all.
:::

*What is special about the number $2$? Of all the upper bounds of
$[0,2]$ or $(0,2)$, the number $2$ is the **smallest**. This is the key
idea.*

::: definition
[]{#def:7-4 label="def:7-4"} A number $c$ is the *supremum* (or *least
upper bound*) of a set $A$ when:

1.  $c$ is an upper bound of $A$, and

2.  every upper bound $b$ of $A$ satisfies $b \ge c$.

We write $c = \sup A$.
:::

::: example
[]{#ex:7-5 label="ex:7-5"} Both $[0,2]$ and $(0,2)$ have $\sup = 2$. The
set $\mathbb{Z}$ does not have a supremum, because it does not have an
upper bound to begin with.
:::

::: remark
When the supremum of a set happens to be an element of the set, then it
is the maximum. The closed interval $[0,2]$ has maximum $2$. The open
interval $(0,2)$ does not have a maximum. Neither does $\mathbb{Z}$.
:::

::: definition
[]{#def:7-5 label="def:7-5"} A set $A$ is *bounded above* when it has at
least one upper bound.
:::

::: remark
By reversing the direction of all inequalities in the definitions above,
define: *lower bound*, *infimum* (greatest lower bound), *minimum*, and
*bounded below*.
:::

::: definition
[]{#def:7-6 label="def:7-6"} Let $A$ be a set of real numbers.

1.  A number $c$ is a *lower bound* of $A$ when $c \le x$ for every
    $x \in A$.

2.  A number $c$ is the *infimum* (or *greatest lower bound*) of $A$,
    written $c = \inf A$, when $c$ is a lower bound of $A$ and every
    lower bound $b$ of $A$ satisfies $b \le c$.

3.  A number $c$ is the *minimum* of $A$ when $c \in A$ and $c$ is the
    infimum of $A$.

4.  $A$ is *bounded below* when it has at least one lower bound.

5.  $A$ is *bounded* when it is both bounded above and bounded below.
:::

::: theorem
[]{#thm:7-2 label="thm:7-2"} If a set $A \subseteq \mathbb{R}$ is
non-empty and bounded above, then $A$ has a supremum.
:::

::: remark
This result is perhaps the most important property of the real numbers.
It is the main difference between $\mathbb{R}$ and $\mathbb{Q}$. In an
analysis course, where one constructs $\mathbb{R}$ rigorously, proving
this property is a fundamental step. For now, we accept it without
proof; some authors treat it as an **axiom**.
:::

::: remark
State the analogous result for lower bounds: if a set $A$ is non-empty
and bounded below, then $A$ has an infimum.
:::

## Supremum and Infimum of Functions {#sec:7.4}

*In the previous section we defined the supremum and infimum of a set.
In this section we extend these concepts to functions. The idea is
actually simple: the supremum (or infimum) of a function is just the
supremum (or infimum) of its range.*

::: definition
[]{#def:7-7 label="def:7-7"} Let $f$ be a function defined on a domain
$I$. The *supremum of $f$ on $I$* is
$$\sup_{x \in I} f(x) \;=\; \sup\bigl\{\, f(x) : x \in I \,\bigr\},$$
i.e. the supremum of the range of $f$ restricted to $I$. If the domain
$I$ is not specified, it is understood to be the full domain of $f$.
:::

::: remark
Every other concept --- upper bound, maximum, infimum, minimum, bounded
above, bounded below --- extends to functions in exactly the same way:
we apply the set-theoretic definition to the range of the function.
:::

::: example
[]{#ex:7-6 label="ex:7-6"} Consider a function $f$ whose graph passes
through the values $-1$ and $1$ on the interval $[-2,2]$, with range
$[-1,1]$. Then $$\sup_{x \in [-2,2]} f(x) = \sup[-1,1] = 1.$$
:::

::: example
[]{#ex:7-7 label="ex:7-7"} Let $g$ be a function whose graph on $[0,2]$
approaches but never reaches the value $1$ from below, and attains the
value $-1$ at some point. Then $g$ is bounded on $[0,2]$, with
$\sup_{[0,2]} g = 1$ (but $g$ has no maximum), and $\inf_{[0,2]} g = -1$
(which is also a minimum).
:::

We mention two important theorems connecting supremum and maximum for
functions.

::: theorem
[]{#thm:7-3 label="thm:7-3"} If $f$ is bounded above on a non-empty
domain $I$, then $\sup_{x \in I} f(x)$ exists.
:::

This is an immediate consequence of the Least Upper Bound Principle for
sets ([\[thm:7-2\]](#thm:7-2){reference-type="ref+label"
reference="thm:7-2"}).

::: theorem
[]{#thm:7-4 label="thm:7-4"} If $f$ is continuous on a closed, bounded
interval $[a,b]$, then $f$ attains a maximum and a minimum on $[a,b]$.
:::

::: remark
These two theorems are related. Both provide a sufficient condition
guaranteeing that a function has a supremum (first theorem) or, more
strongly, a maximum (second theorem).
:::

## The Darboux Integral {#sec:7.5}

*We now take the ideas from [7.1](#sec:7.1){reference-type="ref+label"
reference="sec:7.1"} and convert them into a formal, rigorous
definition. Throughout this section, $f$ is a bounded function defined
on a closed interval $[a,b]$. We assume **only** that $f$ is bounded ---
we do not need continuity or any other hypothesis.*

*We recall the plan: cut the region into slices, approximate with
rectangles below and above, and then "take the limit" by making the
slices very thin.*

### Step 1: Partitions {#step-1-partitions .unnumbered}

::: definition
[]{#def:7-8 label="def:7-8"} A *partition* of the interval $[a,b]$ is a
finite set $P \subseteq [a,b]$ that contains both endpoints $a$ and $b$.
:::

In other words, $P$ consists of $a$, $b$, and finitely many other points
from $[a,b]$.

::: example
[]{#ex:7-8 label="ex:7-8"} The set $\{0, 0.2, 0.5, 0.9, 1\}$ is a
partition of $[0,1]$.
:::

Every partition determines a way to split $[a,b]$ into consecutive
sub-intervals. When we write a partition
$P = \{x_0, x_1, x_2, \ldots, x_n\}$, we adopt the convention that the
points are listed in increasing order:
$$a = x_0 < x_1 < x_2 < \cdots < x_n = b.$$

### Step 2: Lower and Upper Sums {#step-2-lower-and-upper-sums .unnumbered}

Given a partition $P = \{x_0, x_1, \ldots, x_n\}$ of $[a,b]$, on each
sub-interval $[x_{i-1}, x_i]$ we define: $$\begin{align*}
  m_i &= \inf_{x \in [x_{i-1},\, x_i]} f(x), \\[4pt]
  M_i &= \sup_{x \in [x_{i-1},\, x_i]} f(x), \\[4pt]
  \Delta x_i &= x_i - x_{i-1}.
\end{align*}$$

::: remark
We use the *infimum* rather than the minimum for $m_i$ because not every
bounded function attains its minimum. Since $f$ is bounded on $[a,b]$,
it is bounded on every sub-interval, so the infimum and supremum exist
by the Least Upper Bound Principle
([\[thm:7-2\]](#thm:7-2){reference-type="ref+label"
reference="thm:7-2"}).
:::

::: definition
[]{#def:7-9 label="def:7-9"} Let $f$ be a bounded function on $[a,b]$
and $P$ a partition of $[a,b]$. The *$P$-lower sum* and *$P$-upper sum*
of $f$ are $$L_P(f) = \sum_{i=1}^{n} m_i\,\Delta x_i,
  \qquad
  U_P(f) = \sum_{i=1}^{n} M_i\,\Delta x_i.$$
:::

*Geometrically, $L_P(f)$ is the total area of the rectangles **below**
the graph of $f$ (the under-estimate), and $U_P(f)$ is the total area of
the rectangles **above** the graph (the over-estimate).*

<figure id="fig:darboux-upper-lower" data-latex-placement="ht">

<figcaption>Upper and lower sums on a fixed partition.</figcaption>
</figure>

### Step 3: Lower and Upper Integrals {#step-3-lower-and-upper-integrals .unnumbered}

*The integral must be a number lying between all lower sums and all
upper sums. We need every lower sum to be at most every upper sum; this
will be proved in [7.6](#sec:7.6){reference-type="ref+label"
reference="sec:7.6"}. Assuming this fact, we proceed.*

::: lemma
[]{#lem:7-1 label="lem:7-1"} For any two partitions $P$ and $Q$ of
$[a,b]$, $$L_P(f) \le U_Q(f).$$ That is, every lower sum is less than or
equal to every upper sum.
:::

The proof is given in [7.6](#sec:7.6){reference-type="ref+label"
reference="sec:7.6"}.

*As we use finer partitions, the lower sums increase and the upper sums
decrease, each approaching the area we want to compute. Rather than
taking a "limit" of partitions (which are not numbers), we proceed more
elegantly: we define two integrals, one from each side.*

::: definition
[]{#def:7-10 label="def:7-10"} Let $f$ be a bounded function on $[a,b]$.
The *lower integral* of $f$ is
$$\underline{\int}_{a}^{b} f \;=\; \sup\bigl\{\, L_P(f) : P \text{ is a partition of } [a,b] \,\bigr\},$$
and the *upper integral* of $f$ is
$$\overline{\int}_{a}^{b} f \;=\; \inf\bigl\{\, U_P(f) : P \text{ is a partition of } [a,b] \,\bigr\}.$$
:::

::: remark
The set of lower sums is non-empty (there is at least one partition) and
bounded above (by any upper sum, via
[\[lem:7-1\]](#lem:7-1){reference-type="ref+label"
reference="lem:7-1"}), so the supremum exists. Similarly, the set of
upper sums is non-empty and bounded below, so the infimum exists.
:::

Since every lower sum is at most every upper sum, it follows that
$$\underline{\int}_{a}^{b} f \;\le\; \overline{\int}_{a}^{b} f.$$

::: definition
[]{#def:7-11 label="def:7-11"} A bounded function $f$ on $[a,b]$ is
*integrable* on $[a,b]$ when
$$\underline{\int}_{a}^{b} f \;=\; \overline{\int}_{a}^{b} f.$$ In this
case, the common value is called the *integral of $f$ from $a$ to $b$*,
denoted $$\int_{a}^{b} f(x)\,dx.$$ If the lower and upper integrals are
not equal, we say $f$ is *non-integrable* on $[a,b]$, and the integral
is undefined.
:::

::: theorem
[]{#thm:7-5 label="thm:7-5"} Every continuous function on a closed
interval $[a,b]$ is integrable on $[a,b]$.
:::

::: remark
The proof is quite technical and is typically covered in an analysis
course. If $f$ is not continuous, it may or may not be integrable.
:::

## Properties of Darboux Sums {#sec:7.6}

*We now list and justify three important properties of lower and upper
sums. Throughout this section, $f$ is a bounded function on $[a,b]$.*

::: proposition
[]{#thm:7-6 label="thm:7-6"} For any partition $P$ of $[a,b]$,
$$L_P(f) \le U_P(f).$$
:::

::: proof
*Proof.* On each sub-interval $[x_{i-1}, x_i]$, the infimum $m_i$ is at
most the supremum $M_i$, so $m_i\,\Delta x_i \le M_i\,\Delta x_i$.
Summing over all sub-intervals gives $L_P(f) \le U_P(f)$. ◻
:::

*Can we compare lower and upper sums for **different** partitions? There
is a sense in which some partitions are "better" than others.*

::: definition
[]{#def:7-12 label="def:7-12"} Given two partitions $P$ and $Q$ of
$[a,b]$, we say $Q$ is *finer than* $P$ (or $Q$ is a *refinement* of
$P$) when $P \subseteq Q$.
:::

::: remark
Being finer does not merely mean having more points. $Q$ must contain
**all** the points of $P$, plus possibly additional ones.
:::

*What happens when we add a single extra point to a partition? The extra
point splits one sub-interval into two, creating an extra slice. The
lower sum increases (or stays the same), because the infimum on a
smaller sub-interval is at least as large as the infimum on the original
sub-interval. Adding several points one at a time produces the same
effect.*

::: proposition
[]{#thm:7-7 label="thm:7-7"} Let $P$ and $Q$ be partitions of $[a,b]$
with $Q$ finer than $P$. Then
$$L_P(f) \le L_Q(f) \quad\text{and}\quad U_Q(f) \le U_P(f).$$ That is,
finer partitions produce larger lower sums and smaller upper sums.
:::

*What if we have two partitions and neither is finer than the other? We
cannot, in general, compare their lower sums or their upper sums
individually, but we can always compare **any** lower sum with **any**
upper sum.*

::: proposition
[]{#thm:7-8 label="thm:7-8"} For any two partitions $P$ and $Q$ of
$[a,b]$, $$L_P(f) \le U_Q(f).$$
:::

::: proof
*Proof.* Define $R = P \cup Q$. Then $R$ is a partition that is finer
than both $P$ and $Q$. By Property 2
([\[thm:7-7\]](#thm:7-7){reference-type="ref+label"
reference="thm:7-7"}): $$L_P(f) \le L_R(f) \le U_R(f) \le U_Q(f).$$

The middle step uses Property 1
([\[thm:7-6\]](#thm:7-6){reference-type="ref+label"
reference="thm:7-6"}). ◻
:::

::: remark
Property 3 is exactly [\[lem:7-1\]](#lem:7-1){reference-type="ref+label"
reference="lem:7-1"}, which we assumed when defining the integral in
[7.5](#sec:7.5){reference-type="ref+label" reference="sec:7.5"}. The
three properties together fully justify the picture: all lower sums sit
to the left, all upper sums sit to the right, the lower integral lies
between them on the left, and the upper integral lies between them on
the right.
:::

<figure id="fig:lower-upper-sums-numberline" data-latex-placement="ht">

<figcaption>Lower sums and upper sums viewed as numbers on the real
line: meeting implies integrability; a gap implies
non-integrability.</figcaption>
</figure>

## An Integrable Function {#sec:7.7}

*We illustrate how to use the definition of integral to prove that a
function is integrable.*

::: example
[]{#ex:7-9 label="ex:7-9"} Define $f \colon [-1,1] \to \mathbb{R}$ by
$$f(x) = \begin{cases} 1 & \text{if } x = 0, \\ 0 & \text{if } x \ne 0. \end{cases}$$
We will show that $f$ is integrable on $[-1,1]$ and
$\displaystyle\int_{-1}^{1} f(x)\,dx= 0$.
:::

**Lower sums.** Let $P$ be any partition of $[-1,1]$. On every
sub-interval, the infimum of $f$ is $0$ (regardless of whether $0$ is
one of the partition points). Therefore $L_P(f) = 0$ for every partition
$P$. Hence $$\underline{\int}_{-1}^{1} f = \sup\{0\} = 0.$$

**Upper sums.** Let $P$ be an arbitrary partition of $[-1,1]$. The
supremum of $f$ on a sub-interval is $1$ if the sub-interval contains
$0$, and $0$ otherwise. Exactly one sub-interval (or two, if $0 \in P$)
contributes, and the corresponding upper rectangle has height $1$ and
some positive width $w$. Therefore $U_P(f) = w$.

The width $w$ can be made arbitrarily small (by placing partition points
close to $0$), but it must remain positive. With the simplest partition
$P = \{-1,1\}$, we get $w = 2$. Thus
$$\bigl\{\, U_P(f) : P \text{ is a partition of } [-1,1] \bigr\} = (0, 2].$$
Hence $$\overline{\int}_{-1}^{1} f = \inf(0,2] = 0.$$

Since the lower and upper integrals are both $0$, the function $f$ is
integrable on $[-1,1]$ and $\displaystyle\int_{-1}^{1} f(x)\,dx= 0$.

<figure id="fig:single-point-spike" data-latex-placement="ht">

<figcaption>The function <span class="math inline"><em>f</em></span>
equals <span class="math inline">0</span> everywhere except at <span
class="math inline"><em>x</em> = 0</span>, where <span
class="math inline"><em>f</em>(0) = 1</span>.</figcaption>
</figure>

## A Non-Integrable Function {#sec:7.8}

*We now illustrate how to use the definition of integral to prove that a
function is non-integrable.*

::: example
[]{#ex:7-10 label="ex:7-10"} Define $g \colon [0,1] \to \mathbb{R}$ by
$$g(x) = \begin{cases} 1 & \text{if } x \in \mathbb{Q}, \\ 0 & \text{if } x \notin \mathbb{Q}. \end{cases}$$
We will show that $g$ is **not** integrable on $[0,1]$.
:::

<figure id="fig:dirichlet-function" data-latex-placement="ht">

<figcaption>Dirichlet function intuition: on every interval, values
<span class="math inline">0</span> and <span
class="math inline">1</span> both occur (densely).</figcaption>
</figure>

The entire argument rests on one key observation.

::: remark
For any real numbers $a < b$, the interval $(a,b)$ contains both
rational and irrational numbers.
:::

::: remark
Pause and convince yourself that this observation is true, because the
rest of the argument depends on it.
:::

Consider any partition $P$ of $[0,1]$, and look at any sub-interval
$[x_{i-1},x_i]$. Since this sub-interval contains both a rational number
(where $g = 1$) and an irrational number (where $g = 0$), we have:
$$m_i = \inf_{[x_{i-1},\,x_i]} g = 0, \qquad M_i = \sup_{[x_{i-1},\,x_i]} g = 1.$$
Therefore: $$L_P(g) = \sum_{i=1}^{n} 0 \cdot \Delta x_i = 0, \qquad
  U_P(g) = \sum_{i=1}^{n} 1 \cdot \Delta x_i = \sum_{i=1}^{n} \Delta x_i = 1.$$
This is true for **all** partitions. Hence
$$\underline{\int}_{0}^{1} g = \sup\{0\} = 0, \qquad
  \overline{\int}_{0}^{1} g = \inf\{1\} = 1.$$ Since $0 \ne 1$, the
function $g$ is not integrable on $[0,1]$.

<figure id="fig:nonintegrable-dense-oscillation"
data-latex-placement="ht">

<figcaption>Dense oscillation intuition: upper sums stay high while
lower sums stay low.</figcaption>
</figure>

::: remark
There are alternative ways to define the integral. In the *Lebesgue*
theory of integration, the Dirichlet function *is* integrable (with
integral $0$). The Lebesgue integral is more powerful but more complex;
it is beyond the scope of this course.
:::

## Integrals as Limits {#sec:7.9}

*Can we compute the lower or upper integral of a function as a limit of
lower or upper sums? It looks like we should be able to, but it is not
clear how: a limit as **what** approaches **what**?*

*A limit as the partitions "become finer"? We cannot naïvely take the
limit as the number of points in the partition approaches infinity,
because we also need the width of every sub-interval to approach $0$.*

::: definition
[]{#def:7-13 label="def:7-13"} Given a partition
$P = \{x_0, x_1, \ldots, x_n\}$ of $[a,b]$, the *norm* (or *mesh*) of
$P$ is $$\left\lVert P \right\rVert = \max_{1 \le i \le n} \Delta x_i,$$
the largest of the widths of the sub-intervals.
:::

::: remark
The norm is a measure of how "good" a partition is. If
$\left\lVert P \right\rVert$ is small, then **all** sub-intervals have
small width, hence all the approximating rectangles are very thin.
:::

::: theorem
[]{#thm:7-9 label="thm:7-9"} Let $f$ be a bounded function on $[a,b]$.
Then
$$\underline{\int}_{a}^{b} f \;=\; \lim_{\left\lVert P \right\rVert\to 0} L_P(f).$$
More precisely: for every $\varepsilon> 0$, there exists $\delta > 0$
such that for every partition $P$ of $[a,b]$ with
$\left\lVert P \right\rVert < \delta$,
$$\left|\; \underline{\int}_{a}^{b} f - L_P(f) \;\right| < \varepsilon.$$
Similarly,
$\displaystyle\overline{\int}_{a}^{b} f = \lim_{\left\lVert P \right\rVert\to 0} U_P(f)$.
:::

*In practice, however, considering all partitions is still cumbersome.
The following theorem allows us to use a single convenient sequence of
partitions.*

::: theorem
[]{#thm:7-10 label="thm:7-10"} Let $f$ be a bounded function on $[a,b]$,
and let $(P_n)_{n=1}^{\infty}$ be a sequence of partitions of $[a,b]$
such that $\left\lVert P_n \right\rVert \to 0$ as $n \to \infty$. Then
$$\underline{\int}_{a}^{b} f = \lim_{n \to \infty} L_{P_n}(f),
  \qquad
  \overline{\int}_{a}^{b} f = \lim_{n \to \infty} U_{P_n}(f).$$
:::

::: example
The simplest choice is the *uniform partition* $P_n$ that breaks $[a,b]$
into $n$ sub-intervals of equal length $\dfrac{b-a}{n}$. Then
$\left\lVert P_n \right\rVert = \dfrac{b-a}{n} \to 0$.
:::

::: remark
This expression is a limit in the familiar sense: a limit as a certain
number ($n$) approaches infinity. For studying the theory of
integration, the original definition (as a supremum/infimum) is both
simpler and more useful --- it makes it easier to prove further
properties and theorems. But it is good to know that the integral can
also be interpreted as a limit.
:::

## Riemann Sums {#sec:7.10}

*Riemann sums are an alternative way to calculate the integral of a
function. They are not very convenient for proving theorems, but they
are often useful for computations.*

Throughout this section, $f$ is a bounded, integrable function on
$[a,b]$.

*So far, we have estimated the area of each slice with a rectangle whose
height is the infimum (lower sum) or the supremum (upper sum) of $f$ on
that sub-interval. What if, instead, we choose a **random** point on the
graph of $f$ over each sub-interval and use the value of $f$ at that
point as the height of the rectangle?*

::: definition
[]{#def:7-14 label="def:7-14"} Let $f$ be a bounded function on $[a,b]$,
let $P = \{x_0, x_1, \ldots, x_n\}$ be a partition of $[a,b]$, and for
each $i = 1, \ldots, n$, choose a *sample point*
$x_i^{*} \in [x_{i-1}, x_i]$. The *Riemann sum* for $f$ and $P$ (with
these sample points) is
$$S_P^{*}(f) = \sum_{i=1}^{n} f(x_i^{*})\,\Delta x_i.$$
:::

::: remark
We say "*a* Riemann sum," not "*the* Riemann sum." Even for a fixed
function and partition, the Riemann sum depends on the choice of sample
points $x_i^{*}$. The star in $S_P^{*}$ indicates this dependence.
:::

::: remark
Since $m_i \le f(x_i^{*}) \le M_i$ on each sub-interval, every Riemann
sum satisfies $$L_P(f) \le S_P^{*}(f) \le U_P(f).$$
:::

<figure id="fig:riemann-rectangles" data-latex-placement="ht">

<figcaption>A right-endpoint Riemann sum approximation.</figcaption>
</figure>

::: theorem
[]{#thm:7-11 label="thm:7-11"} Let $f$ be bounded and integrable on
$[a,b]$. Let $(P_n)$ be a sequence of partitions of $[a,b]$, each having
$n$ sub-intervals, with $\left\lVert P_n \right\rVert \to 0$, and for
each $P_n$, choose sample points $x_i^{*}$ on each sub-interval. Then
$$\int_{a}^{b} f(x)\,dx= \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^{*})\,\Delta x_i.$$
:::

::: proof
*Proof.* From [\[thm:7-10\]](#thm:7-10){reference-type="ref+label"
reference="thm:7-10"}, we know
$L_{P_n}(f) \to \displaystyle\int_{a}^{b} f$ and
$U_{P_n}(f) \to \displaystyle\int_{a}^{b} f$ as $n \to \infty$ (using
the fact that $f$ is integrable, so the lower and upper integrals both
equal the integral). Since
$L_{P_n}(f) \le S_{P_n}^{*}(f) \le U_{P_n}(f)$, the Squeeze Theorem
gives $S_{P_n}^{*}(f) \to \displaystyle\int_{a}^{b} f$. ◻
:::

::: remark
**This method requires knowing in advance that $f$ is integrable.** If
$f$ is continuous on $[a,b]$, then $f$ is integrable by
[\[thm:7-5\]](#thm:7-5){reference-type="ref+label" reference="thm:7-5"},
and Riemann sums may be used. For an arbitrary bounded function whose
integrability is unknown, the limit of Riemann sums may fail to exist or
may depend on the choices made.
:::

*Suggestive notation.* The Riemann sum formula
$$\sum_{i=1}^{n} f(x_i^{*})\,\Delta x_i \;\xrightarrow{n\to\infty}\; \int_{a}^{b} f(x)\,dx$$
suggests that in the limit, the sum $\displaystyle\sum$ turns into the
integral $\displaystyle\int$, and the finite width $\Delta x$ turns into
the "infinitesimally small" $\,dx$. This is why some authors say $\,dx$
represents an infinitesimally small width.

::: example
[]{#ex:7-11 label="ex:7-11"} We compute
$\displaystyle\int_{0}^{1} x\,dx$ using Riemann sums. (The function
$f(x) = x$ is continuous, hence integrable.)

Choose the uniform partition
$P_n = \bigl\{0,\,\frac{1}{n},\,\frac{2}{n},\,\ldots,\,1\bigr\}$, which
has $n$ sub-intervals of equal width $\Delta x_i = \frac{1}{n}$. On each
sub-interval, choose the right endpoint as the sample point:
$x_i^{*} = \frac{i}{n}$. The Riemann sum is
$$S_{P_n}^{*}(f) = \sum_{i=1}^{n} \frac{i}{n}\cdot\frac{1}{n} = \frac{1}{n^{2}}\sum_{i=1}^{n} i = \frac{1}{n^{2}}\cdot\frac{n(n+1)}{2} = \frac{n+1}{2n}.$$
Taking the limit:
$$\int_{0}^{1} x\,dx= \lim_{n\to\infty}\frac{n+1}{2n} = \frac{1}{2}.$$
This agrees with the fact that the region under $f(x)=x$ on $[0,1]$ is a
triangle of area $\frac{1}{2}$.
:::

::: remark
Riemann sums may look like a simpler way to compute integrals than the
original definition, but they only work if we know the function is
integrable. For developing the theory of integration and proving
theorems, the original definition via lower and upper integrals is more
useful.
:::

## Properties of Definite Integrals {#sec:7.11}

*We now list the five most important properties of definite integrals.
They are all geometrically intuitive. To be rigorous, each should be
proved from the definition, but we omit the proofs here.*

### Linearity {#linearity .unnumbered}

::: theorem
[]{#thm:7-12 label="thm:7-12"} Let $f$ and $g$ be bounded functions on
$[a,b]$.

1.  **Sum rule.** If $f$ and $g$ are both integrable on $[a,b]$, then
    $f+g$ is integrable on $[a,b]$ and
    $$\int_{a}^{b}\bigl(f(x)+g(x)\bigr)\,dx= \int_{a}^{b} f(x)\,dx+ \int_{a}^{b} g(x)\,dx.$$

2.  **Constant multiple.** If $f$ is integrable on $[a,b]$ and
    $c \in \mathbb{R}$, then $cf$ is integrable on $[a,b]$ and
    $$\int_{a}^{b} c\,f(x)\,dx= c\int_{a}^{b} f(x)\,dx.$$
:::

::: remark
If $f$ or $g$ is non-integrable, the sum $f+g$ may or may not be
integrable, and the equation does not apply. This is analogous to the
situation with limit laws and differentiation rules.
:::

### Additivity over Intervals {#additivity-over-intervals .unnumbered}

::: theorem
[]{#thm:7-13 label="thm:7-13"} Let $f$ be a bounded function on $[a,c]$
with $a < b < c$. If $f$ is integrable on $[a,b]$ and on $[b,c]$, then
$f$ is integrable on $[a,c]$ and
$$\int_{a}^{c} f(x)\,dx= \int_{a}^{b} f(x)\,dx+ \int_{b}^{c} f(x)\,dx.$$
:::

*So far, we have only defined $\displaystyle\int_{a}^{b} f$ when
$a < b$. The following convention extends the definition.*

::: definition
[]{#def:7-15 label="def:7-15"} If $f$ is integrable on $[a,b]$ (with
$a < b$), we define $$\int_{b}^{a} f(x)\,dx= -\int_{a}^{b} f(x)\,dx.$$
In addition, for any $a$, $$\int_{a}^{a} f(x)\,dx= 0.$$
:::

::: remark
With these conventions, the identity
$$\int_{a}^{c} f(x)\,dx= \int_{a}^{b} f(x)\,dx+ \int_{b}^{c} f(x)\,dx$$
holds for **all** orderings of $a$, $b$, and $c$ (as long as $f$ is
integrable where needed). For instance, taking $a = c$ gives
$\displaystyle\int_{a}^{b} f + \int_{b}^{a} f = 0$, confirming that
$\displaystyle\int_{b}^{a} f = -\int_{a}^{b} f$.
:::

### Geometric Interpretation: Signed Area {#geometric-interpretation-signed-area .unnumbered}

*Our original motivation defined the integral as the area of the region
between the graph of $f$ and the $x$-axis, but we always assumed $f$ was
positive. The definition of the integral makes no such assumption --- it
works for any bounded function. So what does the integral represent when
$f$ is not positive?*

::: remark
For a **negative** function, the integral equals **minus** the area of
the region between the graph and the $x$-axis. This is because the
heights of the rectangles in the lower and upper sums are values of $f$,
which are negative.
:::

For a function that takes both positive and negative values on $[a,b]$,
we split the region between the graph and the $x$-axis into the part
above the axis and the part below. Then:
$$\int_{a}^{b} f(x)\,dx= (\text{area above the }x\text{-axis}) - (\text{area below the }x\text{-axis}).$$

::: remark
Areas are always positive, but definite integrals may be positive,
negative, or zero.
:::

### Comparison {#comparison .unnumbered}

::: theorem
[]{#thm:7-14 label="thm:7-14"} If $f$ and $g$ are integrable on $[a,b]$
and $f(x) \le g(x)$ for all $x \in [a,b]$, then
$$\int_{a}^{b} f(x)\,dx\le \int_{a}^{b} g(x)\,dx.$$
:::

::: remark
This also makes sense geometrically: when $f$ and $g$ are non-negative,
the region under the graph of $f$ is contained in the region under the
graph of $g$, so its area is no larger.
:::

::: remark
Practically everything one needs to do with definite integrals rests on
these five properties. To a certain extent, if one is not concerned with
rigorous definitions and proofs, one could forget the formal definition
and take these properties as a starting point.
:::

# The Fundamental Theorem of Calculus

## Antiderivatives and Indefinite Integrals {#sec:8.1}

*There are two different things that we call integrals. We use very
similar notation, but they mean something very different.*

The first is the *definite integral*,
$\displaystyle\int_{a}^{b} f(x)\,dx$, which we have already defined. It
is a **number**, and geometrically it represents area.

The second is the *indefinite integral*, written $$\int f(x)\,dx,$$
without limits of integration. This is something new.

::: definition
[]{#def:8-1 label="def:8-1"} Let $f$ be a function defined on an
interval $I$. A function $F$ is an *antiderivative* of $f$ on $I$ if
$F'(x) = f(x)$ for every $x \in I$.
:::

::: remark
We say "*an* antiderivative" because in general there will be more than
one. Every function can only have one derivative, if it has one, but it
can have many antiderivatives.
:::

::: definition
[]{#def:8-2 label="def:8-2"} The *indefinite integral*
$\displaystyle\int f(x)\,dx$ denotes the collection of **all**
antiderivatives of $f$.
:::

*So these two objects are quite different. The definite integral is a
number; the indefinite integral is a collection of functions. The
definite integral means area; the indefinite integral means
antiderivative. A priori, these two things have nothing to do with each
other. But we use very similar notation, and that is because they
**are** related --- by the Fundamental Theorem of Calculus, which will
come in a few sections. For now, they are two separate things.*

::: example
[]{#ex:8-1 label="ex:8-1"} Compute $\displaystyle\int x^{2}\,dx$.

**Solution.** We seek all antiderivatives of $x^{2}$. We can guess: the
function $\dfrac{1}{3}x^{3}$ works, since
$$\frac{d}{dx}\!\left(\frac{1}{3}x^{3}\right) = \frac{1}{3}\cdot 3x^{2} = x^{2}.$$
Adding any constant $C$ also works, because $\dfrac{d}{dx}(C) = 0$.
Moreover, these are *all* of the antiderivatives: by a consequence of
the Mean Value Theorem, if two functions have the same derivative on an
interval then they differ by a constant. Therefore
$$\int x^{2}\,dx= \frac{1}{3}x^{3} + C.$$
:::

::: remark
Without the Mean Value Theorem result that two functions sharing the
same derivative must differ by a constant, we could only say that we
found *some* antiderivatives, not *all* of them.
:::

### Guess and check {#guess-and-check .unnumbered}

*There are many so-called integration techniques --- substitution,
integration by parts, and so on --- which are methods for computing
antiderivatives. But by far the most important integration technique is
**guess and check**.*

The method is exactly what it sounds like: make a guess for what the
antiderivative should look like, take its derivative to check, and
modify as necessary.

::: example
[]{#ex:8-2 label="ex:8-2"} Compute $\displaystyle\int (2x+7)^{11}\,dx$.

**Solution.** We want a function whose derivative is $(2x+7)^{11}$. The
power rule suggests trying $(2x+7)^{12}$. Differentiating by the chain
rule:
$$\frac{d}{dx}\!\left[(2x+7)^{12}\right] = 12(2x+7)^{11}\cdot 2 = 24(2x+7)^{11}.$$
This is our target, but with an extra factor of $24$. Dividing by $24$
fixes this:
$$\frac{d}{dx}\!\left[\frac{1}{24}(2x+7)^{12}\right] = \frac{1}{24}\cdot 24(2x+7)^{11} = (2x+7)^{11}.$$
Therefore $$\int (2x+7)^{11}\,dx= \frac{1}{24}(2x+7)^{12} + C.$$
:::

::: remark
This method, even though it seems rudimentary, is very powerful. All the
integration techniques one learns later --- substitution, integration by
parts, and so on --- are just sophisticated forms of guessing and
checking that make the guessing part easier.
:::

::: remark
At this point, many textbooks present a table of elementary
antiderivatives. But you do not need those formulas: if you know the
differentiation rules and are comfortable with guess and check, you can
solve all standard antiderivative problems without memorising anything
new. Moreover, since you can check your answers by differentiating, you
will know whether they are right.
:::

## Functions Defined by Integrals {#sec:8.2}

*We already know two notions of integral: the definite integral (a
number) and the indefinite integral (a collection of antiderivatives).
We now introduce a way to use integrals to define new functions.*

::: definition
[]{#def:8-3 label="def:8-3"} Let $I$ be an interval, let $a \in I$ be a
fixed point, and let $f$ be an integrable function on $I$. We define a
new function $F$ by $$F(x) = \int_{a}^{x} f(t)\,dt.$$ For each value of
$x \in I$, the expression $\displaystyle\int_{a}^{x} f(t)\,dt$ is a
definite integral and hence a number; we call that number $F(x)$.
:::

*Strictly speaking, this is not a new concept: it is just a definite
integral where the upper endpoint of the interval becomes the variable
of a new function. However, the first time one sees this, it can be
confusing how it relates to and differs from an ordinary definite
integral, and in particular why we use the notation that we use. Let us
break this down carefully.*

::: example
[]{#ex:8-3 label="ex:8-3"} Consider a function $f$ whose graph is drawn
in the $ty$-plane. Fix $a = 1$ and define
$$F(x) = \int_{1}^{x} f(t)\,dt.$$ Then:

- $F(2) = \displaystyle\int_{1}^{2} f(t)\,dt$ is the area under $f$ from
  $t=1$ to $t=2$.

- $F(3) = \displaystyle\int_{1}^{3} f(t)\,dt$ is the area under $f$ from
  $t=1$ to $t=3$.

- $F(4) = \displaystyle\int_{1}^{4} f(t)\,dt$ is the area under $f$ from
  $t=1$ to $t=4$.

In each case the left endpoint is fixed at $1$, but the right endpoint
varies. For each choice of $x$, we obtain a number $F(x)$. This is a
valid way to define a function.
:::

<figure id="fig:accumulation-function" data-latex-placement="ht">

<figcaption>Accumulated area from <span
class="math inline"><em>a</em></span> to <span
class="math inline"><em>x</em></span> under <span
class="math inline"><em>f</em></span>.</figcaption>
</figure>

::: remark
Notice that we do **not** use $x$ as the variable of integration; we use
$t$ (or any other letter). The reason is that $x$ already has a role: it
is the endpoint of the interval, and hence the variable of the new
function $F$.

Recall that for a definite integral with fixed endpoints, the
integration variable is a dummy variable:
$$\int_{a}^{b} f(x)\,dx= \int_{a}^{b} f(t)\,dt= \int_{a}^{b} f(s)\,ds,$$
and we may use any letter we like, **except** $a$ or $b$, since they
already have a meaning.

The same principle applies here. In the expression
$F(x) = \displaystyle\int_{a}^{x} f(t)\,dt$, the integration variable
may be $t$, $s$, $u$, or any letter **except** $a$ or $x$. In
particular, **never** write $$F(x) = \int_{a}^{x} f(x)\,dx.$$ This is
ambiguous and technically wrong, because $x$ would have two different
meanings in the same expression: the endpoint and the variable of
integration.
:::

*Now that we understand how to use integrals to define new functions,
what can we say about them? There is a theorem --- the Fundamental
Theorem of Calculus --- that ties together the notions of definite
integral, indefinite integral, and functions defined as integrals. It
has two parts.*

- **Part One** answers: what important property does a function defined
  as an integral always have?

- **Part Two** answers: how can we quickly compute definite integrals?

## FTC Part One: Statement {#sec:8.3}

*The Fundamental Theorem of Calculus establishes connections between
definite integrals and antiderivatives --- two concepts that are defined
separately and in principle are different, but are related through this
theorem. We now state the first part.*

::: theorem
[]{#thm:8-1 label="thm:8-1"} Let $I$ be an interval, let $a \in I$, and
let $f$ be a function with domain $I$. Define
$$F(x) = \int_{a}^{x} f(t)\,dt.$$ If $f$ is continuous on $I$, then $F$
is differentiable on $I$ and
$$F'(x) = f(x) \quad \text{for every } x \in I.$$ In other words, $F$ is
an antiderivative of $f$.
:::

::: remark
Note that continuity of $f$ already guarantees integrability, so the
integral defining $F$ makes sense and $F$ is well-defined.
:::

*We can summarise this theorem in words: a function defined as an
integral is an antiderivative. This is the connection between the notion
of antiderivative and the notion of integral, which were defined
separately.*

The theorem is often recorded as the single equation
$$\frac{d}{dx}\int_{a}^{x} f(t)\,dt= f(x).$$ Both sides are functions of
$x$, not of $t$. The variable $t$ is merely the variable of integration;
it disappears.

::: remark
If you attempt to change an $x$ into a $t$, or vice versa, on one side
of this equation, the result will not only be wrong --- it will be
**meaningless**.
:::

::: remark
In the following examples, pause after reading each question and try to
solve it before reading the solution. You do not need any extra tools;
everything you need is contained in
[\[thm:8-1\]](#thm:8-1){reference-type="ref+label" reference="thm:8-1"}.
Any answer watched (or read) without first attempting the problem is a
learning opportunity wasted.
:::

::: example
[]{#ex:8-4 label="ex:8-4"} Define
$F(x) = \displaystyle\int_{1}^{x} e^{-t^{2}}\,dt$. Find $F'(2)$.

**Solution.** By [\[thm:8-1\]](#thm:8-1){reference-type="ref+label"
reference="thm:8-1"}, $F'(x) = e^{-x^{2}}$. Therefore $F'(2) = e^{-4}$.
:::

::: example
[]{#ex:8-5 label="ex:8-5"} Construct a function $g$ such that
$$g'(x) = \frac{1}{1 + x^{2} + x^{10}} \quad \text{and} \quad g(2) = 5.$$

**Solution.** By [\[thm:8-1\]](#thm:8-1){reference-type="ref+label"
reference="thm:8-1"}, an antiderivative of the given function is
obtained by writing an integral. We choose the lower limit $a = 2$ so
that we can control the value at $2$:
$$g(x) = \int_{2}^{x} \frac{1}{1 + t^{2} + t^{10}}\,dt+ 5.$$ Then
$g'(x) = \dfrac{1}{1 + x^{2} + x^{10}}$ by the theorem, and
$g(2) = 0 + 5 = 5$.
:::

::: example
[]{#ex:8-6 label="ex:8-6"} Define
$G(x) = \displaystyle\int_{-4}^{x^{2}} \frac{1}{1+t^{2}}\,dt$. Find
$G'(x)$.

**Solution.** Let
$F(x) = \displaystyle\int_{-4}^{x} \frac{1}{1+t^{2}}\,dt$. By
[\[thm:8-1\]](#thm:8-1){reference-type="ref+label" reference="thm:8-1"},
$F'(x) = \dfrac{1}{1+x^{2}}$. Observe that $G(x) = F(x^{2})$, so by the
chain rule, $$G'(x) = F'(x^{2})\cdot 2x = \frac{2x}{1 + x^{4}}.$$
:::

::: example
[]{#ex:8-7 label="ex:8-7"} Define
$H(x) = \displaystyle\int_{x^{3}+1}^{x^{2}+2x} e^{-t^{2}}\,dt$. Find
$H'(x)$.

**Solution.** We split the integral at a convenient point, say $0$:
$$H(x) = \int_{0}^{x^{2}+2x} e^{-t^{2}}\,dt- \int_{0}^{x^{3}+1} e^{-t^{2}}\,dt.$$
(We reversed the limits on the second integral, introducing a minus
sign.) Define
$$F(u) = \int_{0}^{u} e^{-t^{2}}\,dt, \quad \text{so that} \quad F'(u) = e^{-u^{2}}.$$
Then $H(x) = F\!\left(x^{2}+2x\right) - F\!\left(x^{3}+1\right)$. By the
chain rule, $$\begin{align*}
  H'(x) &= F'\!\left(x^{2}+2x\right)\cdot(2x+2) - F'\!\left(x^{3}+1\right)\cdot 3x^{2} \\
         &= (2x+2)\,e^{-(x^{2}+2x)^{2}} - 3x^{2}\,e^{-(x^{3}+1)^{2}}.
\end{align*}$$
:::

## FTC Part One: Proof {#sec:8.4}

*The proof of [\[thm:8-1\]](#thm:8-1){reference-type="ref+label"
reference="thm:8-1"} is perhaps a bit long, but it is not too abstract.*

::: proof
*Proof.* Fix $x \in I$. We wish to show that $F'(x) = f(x)$.

**Step 1: Rewrite the difference quotient.** By the definition of
derivative, $$F'(x) = \lim_{h \to 0} \frac{F(x+h) - F(x)}{h}.$$
Substituting the definition of $F$, $$\frac{F(x+h) - F(x)}{h}
  = \frac{1}{h}\left[\int_{a}^{x+h} f(t)\,dt- \int_{a}^{x} f(t)\,dt\right]
  = \frac{1}{h}\int_{x}^{x+h} f(t)\,dt,$$ where the last step uses the
additive property of integrals. Therefore it suffices to show
$$\lim_{h \to 0} \frac{1}{h}\int_{x}^{x+h} f(t)\,dt= f(x). \tag{$\ast$}$$

**Step 2: Geometric intuition.** For small $h > 0$, the integral
$\displaystyle\int_{x}^{x+h} f(t)\,dt$ represents a thin vertical strip
of area under the graph of $f$. This strip is approximately a rectangle
of width $h$ and height $f(x)$, so its area is roughly $f(x)\cdot h$.
Dividing by $h$ gives approximately $f(x)$, and this approximation
improves as $h \to 0$.

**Step 3: Rigorous bounding (for $h > 0$).** Define
$$M_{h} = \sup_{t \in [x,\,x+h]} f(t), \qquad m_{h} = \inf_{t \in [x,\,x+h]} f(t).$$
Then
$$m_{h}\cdot h \;\le\; \int_{x}^{x+h} f(t)\,dt\;\le\; M_{h}\cdot h,$$
and dividing by $h > 0$,
$$m_{h} \;\le\; \frac{1}{h}\int_{x}^{x+h} f(t)\,dt\;\le\; M_{h}. \tag{$\ast\ast$}$$

**Step 4: Apply the Squeeze Theorem.** Since $f$ is continuous on $I$,
the Extreme Value Theorem guarantees that $f$ attains its maximum and
minimum on $[x, x+h]$. Thus there exists $c_{h} \in [x, x+h]$ with
$M_{h} = f(c_{h})$, and similarly $d_{h} \in [x, x+h]$ with
$m_{h} = f(d_{h})$.

As $h \to 0^{+}$, the point $c_{h}$ is squeezed between $x$ and $x+h$,
so $c_{h} \to x$. Since $f$ is continuous, $f(c_{h}) \to f(x)$,
i.e. $M_{h} \to f(x)$. By the same argument, $m_{h} \to f(x)$.

By the Squeeze Theorem applied to $(\ast\ast)$,
$$\lim_{h \to 0^{+}} \frac{1}{h}\int_{x}^{x+h} f(t)\,dt= f(x).$$

**Step 5: The case $h < 0$.** The argument for $h \to 0^{-}$ is entirely
analogous (one reverses the interval and accounts for the sign).
Combining both one-sided limits, we obtain $(\ast)$, and therefore
$F'(x) = f(x)$. ◻
:::

## FTC Part Two: Statement {#sec:8.5}

*The first part of the Fundamental Theorem tells us what we can say
about any function defined as an integral: it is an antiderivative. The
second part tells us how to quickly compute a definite integral: through
antiderivatives.*

::: theorem
[]{#thm:8-2 label="thm:8-2"} Let $a < b$ be real numbers and let $f$ be
continuous on $[a,b]$. If $G$ is **any** antiderivative of $f$ on
$[a,b]$, then $$\int_{a}^{b} f(x)\,dx= G(b) - G(a).$$
:::

::: remark
This theorem does not tell us *how* to find an antiderivative --- for
some functions that is easy, for others it is hard. But **if** we can
find one, it lets us evaluate the definite integral very quickly,
certainly much faster than computing it from the formal definition in
terms of upper and lower sums.
:::

<figure id="fig:net-change-signed-area" data-latex-placement="ht">

<figcaption>Net change as signed area under a rate
function.</figcaption>
</figure>

::: definition
[]{#def:8-4 label="def:8-4"} We write
$$\left. G(x) \right\rvert_{x=a}^{x=b} \quad \text{or simply} \quad \left. G(x) \right\rvert_{a}^{b}$$
to mean $G(b) - G(a)$.
:::

::: example
[]{#ex:8-8 label="ex:8-8"} Compute
$\displaystyle\int_{1}^{2} x^{2}\,dx$.

**Solution.** We need an antiderivative of $x^{2}$. By inspection,
$G(x) = \dfrac{x^{3}}{3}$ works, since $G'(x) = x^{2}$. By
[\[thm:8-2\]](#thm:8-2){reference-type="ref+label" reference="thm:8-2"},
$$\int_{1}^{2} x^{2}\,dx= \left.\frac{x^{3}}{3}\right\rvert_{1}^{2} = \frac{2^{3}}{3} - \frac{1^{3}}{3} = \frac{8}{3} - \frac{1}{3} = \frac{7}{3}.$$
This is certainly much faster than computing the integral from the
definition or from Riemann sums.
:::

::: remark
Here are four integrals whose antiderivatives can be found by guess and
check. Evaluate each using
[\[thm:8-2\]](#thm:8-2){reference-type="ref+label" reference="thm:8-2"}:

1.  $\displaystyle\int_{0}^{1} 3x^{2}\,dx$,

2.  $\displaystyle\int_{0}^{\pi} \sin x\,dx$,

3.  $\displaystyle\int_{1}^{e} \dfrac{1}{x}\,dx$,

4.  $\displaystyle\int_{0}^{1} e^{x}\,dx$.
:::

## FTC Part Two: Proof {#sec:8.6}

*The proof of the second part uses the first part, and is considerably
shorter.*

::: proof
*Proof.* Define $$F(x) = \int_{a}^{x} f(t)\,dt.$$ We wish to show that
$F(b) = G(b) - G(a)$.

**Step 1: $F$ and $G$ are both antiderivatives.** Since $f$ is
continuous, [\[thm:8-1\]](#thm:8-1){reference-type="ref+label"
reference="thm:8-1"} (FTC Part One) gives $F'(x) = f(x)$. By hypothesis,
$G'(x) = f(x)$. Therefore $F$ and $G$ are two functions with the same
derivative on $[a,b]$.

**Step 2: $F$ and $G$ differ by a constant.** By the consequence of the
Mean Value Theorem (if two functions have the same derivative on an
interval, they differ by a constant), there exists a constant $C$ such
that $$F(x) = G(x) + C \quad \text{for all } x \in [a,b].$$

**Step 3: Determine $C$.** Evaluate at $x = a$:
$$F(a) = \int_{a}^{a} f(t)\,dt= 0,$$ so $0 = G(a) + C$, which gives
$C = -G(a)$.

**Step 4: Conclude.** For every $x \in [a,b]$, $F(x) = G(x) - G(a)$.
Setting $x = b$, $$F(b) = G(b) - G(a).$$ But
$F(b) = \displaystyle\int_{a}^{b} f(t)\,dt$, which is the definite
integral we wished to evaluate. Therefore
$$\int_{a}^{b} f(x)\,dx= G(b) - G(a). \qedhere$$ ◻
:::

## Summary and Comparison {#sec:8.7}

*Through this chapter and the preceding one, we have introduced various
notions related to integrals. They use similar notation but mean
different things, and sometimes we may confuse them. This section
compares them side by side.*

We have learned three concepts:

1.  The **definite integral** $\displaystyle\int_{a}^{b} f(x)\,dx$ --- a
    **number**.

2.  The **indefinite integral** $\displaystyle\int f(x)\,dx$ --- a
    **collection of functions** (the set of all antiderivatives).

3.  A **function defined by an integral**,
    $F(x) = \displaystyle\int_{a}^{x} f(t)\,dt$ --- a **single
    function**.

<figure id="fig:ftc-commutative-diagram" data-latex-placement="ht">

<figcaption>How FTC links accumulation and rates of change.</figcaption>
</figure>

### The definite integral {#the-definite-integral .unnumbered}

The definite integral $\displaystyle\int_{a}^{b} f(x)\,dx$ has both a
formal definition and a geometric interpretation.

The *formal definition* is the one we have already studied: compute the
upper integral (the infimum of all upper sums) and the lower integral
(the supremum of all lower sums); if these two quantities agree, their
common value is called the integral.

The *geometric interpretation* is simpler: if $f \ge 0$, the definite
integral equals the area under the graph of $f$ above the $x$-axis, from
$x = a$ to $x = b$.

In practice, we want to **avoid** computing integrals from the formal
definition. The [\[thm:8-2\]](#thm:8-2){reference-type="ref+label"
reference="thm:8-2"} (FTC Part Two) saves us: find any antiderivative
$G$ of $f$, and then $$\int_{a}^{b} f(x)\,dx= G(b) - G(a).$$

::: example
[]{#ex:8-9 label="ex:8-9"}
$\displaystyle\int_{1}^{2} x^{2}\,dx= \left.\frac{x^{3}}{3}\right\rvert_{1}^{2} = \frac{8}{3} - \frac{1}{3} = \frac{7}{3}$.
:::

### The indefinite integral {#the-indefinite-integral .unnumbered}

The indefinite integral $\displaystyle\int f(x)\,dx$ is the collection
of all antiderivatives of $f$. How do we compute it? By a consequence of
the Mean Value Theorem: find one antiderivative $G$, and then
$$\int f(x)\,dx= G(x) + C,$$ where $C$ is an arbitrary constant (on an
interval).

::: example
[]{#ex:8-10 label="ex:8-10"}
$\displaystyle\int x^{2}\,dx= \frac{x^{3}}{3} + C$.
:::

### A function defined by an integral {#a-function-defined-by-an-integral .unnumbered}

Given an integrable function $f$ on an interval $I$ and a point
$a \in I$, the expression $$F(x) = \int_{a}^{x} f(t)\,dt$$ defines a new
function. By [\[thm:8-1\]](#thm:8-1){reference-type="ref+label"
reference="thm:8-1"} (FTC Part One), if $f$ is continuous, then $F$ is
an antiderivative of $f$: $$F'(x) = f(x).$$ This gives us a way to
**construct** an antiderivative, even when no simpler closed-form
expression exists.

::: example
[]{#ex:8-11 label="ex:8-11"} Define
$F(x) = \displaystyle\int_{3}^{x} e^{-t^{2}}\,dt$. Then
$F'(x) = e^{-x^{2}}$ and $F(3) = 0$. These two properties completely
determine $F$, and there is no simpler way to write it.
:::

### When does the choice of variable matter? {#when-does-the-choice-of-variable-matter .unnumbered}

- **Definite integral:** The result is a number. The integration
  variable is a dummy variable and can be called anything:
  $$\int_{a}^{b} f(x)\,dx= \int_{a}^{b} f(t)\,dt.$$

- **Indefinite integral:** The result is a collection of functions *of
  the named variable*. If we change all $x$'s to $t$'s, we get a
  collection of functions of $t$, which is the same family of
  antiderivatives expressed in a different variable:
  $$\int f(x)\,dx\quad\text{and}\quad \int f(t)\,dt\quad \text{(same antiderivatives, different variable names)}.$$

- **Function defined by an integral:** The integration variable is again
  a dummy variable and may be called anything **except** $x$ (or $a$),
  since those already have designated roles. Never write
  $\displaystyle\int_{a}^{x} f(x)\,dx$; it is ambiguous.

# Integration Methods

## The Substitution Rule {#sec:9.1}

*The Substitution Rule is a method to compute antiderivatives. It is
just an easy-to-use algorithm to make things a bit simpler and a bit
more systematic than guess-and-check. Before presenting the general
rule, let us investigate where the Substitution Rule comes from and why
it works.*

### Motivation by example {#motivation-by-example .unnumbered}

We begin with a pair of simple antiderivatives.

::: example
[]{#ex:9-1 label="ex:9-1"}

1.  $\displaystyle\int x^{4}\,dx= \frac{1}{5}x^{5} + C$. This is
    immediate: the derivative of $\frac{1}{5}x^{5}$ is $x^{4}$.

2.  What about $\displaystyle\int (\ln x)^{4}\,dx$? One might guess
    $\frac{1}{5}(\ln x)^{5}$, but check:
    $$\frac{d}{dx}\!\left[\frac{1}{5}(\ln x)^{5}\right] = \frac{1}{5}\cdot 5(\ln x)^{4}\cdot \frac{1}{x} = \frac{(\ln x)^{4}}{x}.$$
    The chain rule introduces an extra factor of $\frac{1}{x}$. So
    $\frac{1}{5}(\ln x)^{5}$ is **not** an antiderivative of
    $(\ln x)^{4}$, but it *is* an antiderivative of
    $\frac{(\ln x)^{4}}{x}$.
:::

*This observation generalises. If we know that an antiderivative of $f$
is $F$, then what is an antiderivative of $f(g(x))$? We do not know in
general, but an antiderivative of $f(g(x))\cdot g'(x)$ is $F(g(x))$. The
chain rule is the reason.*

### The theorem {#the-theorem .unnumbered}

::: theorem
[]{#thm:9-1 label="thm:9-1"} Let $F$ and $g$ be differentiable functions
such that $F' = f$. Then $$\int f(g(x))\cdot g'(x)\,dx= F(g(x)) + C.$$
:::

::: proof
*Proof.* By the chain rule,
$$\frac{d}{dx}\bigl[F(g(x))\bigr] = F'(g(x))\cdot g'(x) = f(g(x))\cdot g'(x).$$

Therefore $F(g(x))$ is an antiderivative of $f(g(x))\cdot g'(x)$. ◻
:::

::: remark
Despite its traditional name, the Substitution Rule should really be
called the *backwards chain rule*: we take the chain rule, which is a
rule about derivatives, and reverse it to get a rule about
antiderivatives.
:::

### The substitution notation {#the-substitution-notation .unnumbered}

*In practice, we try to use
[\[thm:9-1\]](#thm:9-1){reference-type="ref+label" reference="thm:9-1"}
in an efficient and algorithmic way that simplifies computations. The
key idea is to introduce new notation.*

Suppose we want to compute $\displaystyle\int f(g(x))\cdot g'(x)\,dx$.
We set $$u = g(x), \qquad du = g'(x)\,dx.$$ Then the integral becomes
$\displaystyle\int f(u)\,du$, which may be easier to evaluate. After
finding an antiderivative $F(u) + C$, we **undo the substitution** by
replacing $u$ with $g(x)$.

::: remark
The expression $du = g'(x)\,dx$ is, for now, **just notation**. There is
a way to give precise meaning to the differential using so-called
*differential forms*, but that is beyond the scope of this course. The
justification for the notation is that it produces the correct result.
:::

::: example
[]{#ex:9-2 label="ex:9-2"} Compute
$\displaystyle\int \frac{(\ln x)^{4}}{x}\,dx$.

**Solution.** The integrand is written in terms of $\ln x$, and the
derivative $\frac{1}{x}$ already appears. Set $u = \ln x$, so
$du = \frac{1}{x}\,dx$. Then
$$\int \frac{(\ln x)^{4}}{x}\,dx= \int u^{4}\,du= \frac{1}{5}u^{5} + C = \frac{1}{5}(\ln x)^{5} + C.$$
:::

*In general, every time the integrand is written in terms of a function
$g(x)$ and the derivative $g'(x)$ already appears in the integrand, the
substitution $u = g(x)$ is a good idea. After substituting, we hope to
find an easier integral that we can complete.*

## Substitution Examples {#sec:9.2}

*We now work through several computational examples of the Substitution
Rule, in roughly increasing order of difficulty.*

::: remark
Before reading each solution, pause and attempt the computation
yourself.
:::

::: example
[]{#ex:9-3 label="ex:9-3"} Compute
$\displaystyle\int x^{2}\sin(x^{3}+7)\,dx$.

**Solution.** The argument of $\sin$ is $x^{3}+7$, and its derivative
$3x^{2}$ is essentially present in the integrand (up to a constant). Set
$u = x^{3}+7$, so $du = 3x^{2}\,dx$. Then
$$\int x^{2}\sin(x^{3}+7)\,dx= \frac{1}{3}\int \sin(u)\,du= -\frac{1}{3}\cos(u) + C = -\frac{1}{3}\cos(x^{3}+7) + C.$$
:::

::: example
[]{#ex:9-4 label="ex:9-4"} Compute $\displaystyle\int \tan(x)\,dx$.

**Solution.** Write $\tan x = \dfrac{\sin x}{\cos x}$. The numerator
$\sin x$ is the derivative of $\cos x$ (up to a sign). Set $u = \cos x$,
so $du = -\sin x\,dx$. Then
$$\int \tan(x)\,dx= \int \frac{\sin x}{\cos x}\,dx= -\int \frac{du}{u} = -\ln\left\lvert u \right\rvert + C = -\ln\left\lvert \cos x \right\rvert + C.$$
:::

::: example
[]{#ex:9-5 label="ex:9-5"} Compute
$\displaystyle\int x^{3}\sqrt{x^{2}+1}\,dx$.

**Solution.** The square root makes this difficult. Try $u = x^{2}+1$,
so $du = 2x\,dx$. Separate $x^{3} = x^{2}\cdot x$, and note that
$x^{2} = u - 1$. Then
$$\int x^{3}\sqrt{x^{2}+1}\,dx= \frac{1}{2}\int (u-1)\sqrt{u}\,du= \frac{1}{2}\int \bigl(u^{3/2} - u^{1/2}\bigr)\,du.$$
Integrating term by term:
$$\frac{1}{2}\!\left(\frac{u^{5/2}}{5/2} - \frac{u^{3/2}}{3/2}\right) + C = \frac{1}{5}(x^{2}+1)^{5/2} - \frac{1}{3}(x^{2}+1)^{3/2} + C.$$
:::

::: remark
Among these examples, the last one best illustrates the full power of
the Substitution Rule. The first two could arguably be done by
guess-and-check, but in the third example the substitution transforms a
complex integrand into a simple polynomial --- something that would be
very difficult to guess directly.
:::

## Substitution for Definite Integrals {#sec:9.3}

*We have used the Substitution Rule for indefinite integrals. When
computing a definite integral, there are two approaches: we can first
find an antiderivative (substituting, integrating, undoing the
substitution), or we can apply the substitution directly to the definite
integral --- including the endpoints. The second method is slightly
faster because we never need to undo the substitution.*

::: example
[]{#ex:9-6 label="ex:9-6"} Compute
$\displaystyle\int_{1}^{2} x\,(x^{2}+1)^{100}\,dx$.

**Solution.** Set $u = x^{2}+1$, so $du = 2x\,dx$. We also change the
endpoints: $$x = 1 \implies u = 2, \qquad x = 2 \implies u = 5.$$ Then
$$\int_{1}^{2} x\,(x^{2}+1)^{100}\,dx= \frac{1}{2}\int_{2}^{5} u^{100}\,du= \frac{1}{2}\cdot\frac{u^{101}}{101}\bigg|_{2}^{5} = \frac{5^{101} - 2^{101}}{202}.$$
:::

::: remark
When performing a substitution in a definite integral, you must change
**everything**: the integrand, the differential, **and** the endpoints.
The values $1$ and $2$ are values of $x$; after substitution, the
endpoints must be the corresponding values of $u$.
:::

::: theorem
[]{#thm:9-2 label="thm:9-2"} Let $a, b \in \mathbb{R}$ with $a < b$. Let
$g$ be a function that is differentiable on $[a,b]$ with $g'$ continuous
on $[a,b]$, and let $f$ be continuous on the range of $g$ restricted to
$[a,b]$. Then
$$\int_{a}^{b} f(g(x))\cdot g'(x)\,dx= \int_{g(a)}^{g(b)} f(u)\,du.$$
:::

::: proof
*Proof.* Let $F$ be an antiderivative of $f$. By
[\[thm:9-1\]](#thm:9-1){reference-type="ref+label" reference="thm:9-1"},
$F(g(x))$ is an antiderivative of $f(g(x))\cdot g'(x)$. By the
Fundamental Theorem of Calculus,
$$\int_{a}^{b} f(g(x))\cdot g'(x)\,dx= F(g(b)) - F(g(a)) = \int_{g(a)}^{g(b)} f(u)\,du.$$ ◻
:::

<figure id="fig:substitution-interval-map" data-latex-placement="ht">

<figcaption>Substitution as an interval mapping.</figcaption>
</figure>

## Integration by Parts {#sec:9.4}

*Integration by parts is a method to help compute antiderivatives. It is
an easy-to-use algorithm to make things a bit simpler and a bit more
systematic than pure guess-and-check. Before presenting examples, let us
explain where the formula comes from and why it works.*

### Motivation by example {#motivation-by-example-1 .unnumbered}

::: example
[]{#ex:9-7 label="ex:9-7"} Compute $\displaystyle\int x\,e^{x}\,dx$ by
guess-and-check.

**Solution.** We are looking for a function whose derivative is
$x\,e^{x}$. A first guess: try $x\,e^{x}$ itself. By the product rule:
$$\frac{d}{dx}\!\left[x\,e^{x}\right] = 1\cdot e^{x} + x\,e^{x} = e^{x} + x\,e^{x}.$$
The desired function $x\,e^{x}$ appears, but with an extra $e^{x}$. If
we can find a second function whose derivative is exactly $e^{x}$, we
subtract and obtain:
$$\frac{d}{dx}\!\left[x\,e^{x} - e^{x}\right] = (e^{x} + x\,e^{x}) - e^{x} = x\,e^{x}.$$
Therefore $\displaystyle\int x\,e^{x}\,dx= x\,e^{x} - e^{x} + C$.
:::

*The process we just used --- applying the product rule, identifying an
extra term, and subtracting a correction --- is precisely the idea
behind integration by parts. The formula below does the same thing in a
more systematic way.*

### The formula {#the-formula .unnumbered}

::: theorem
[]{#thm:9-3 label="thm:9-3"} Let $f$ and $g$ be differentiable
functions. Then
$$\int f(x)\,g'(x)\,dx= f(x)\,g(x) - \int f'(x)\,g(x)\,dx.$$
:::

::: proof
*Proof.* The product rule gives
$$\frac{d}{dx}\bigl[f(x)\,g(x)\bigr] = f'(x)\,g(x) + f(x)\,g'(x).$$

Taking antiderivatives of both sides and rearranging:
$$\int f(x)\,g'(x)\,dx= f(x)\,g(x) - \int f'(x)\,g(x)\,dx. \qedhere$$ ◻
:::

::: remark
Despite its traditional name, integration by parts should really be
called the *backwards product rule*: we take the product rule (a
differentiation rule) and reverse it to obtain a rule about
antiderivatives.
:::

<figure id="fig:by-parts-rectangle" data-latex-placement="ht">

<figcaption>A geometric intuition behind the product rule and
integration by parts.</figcaption>
</figure>

### The $u$ -- $v$ notation {#the-u-v-notation .unnumbered}

Setting $u = f(x)$, $dv = g'(x)\,dx$, so that $du = f'(x)\,dx$ and
$v = g(x)$, the formula becomes $$\int u\,dv= u\,v - \int v\,du.$$

::: remark
As with the substitution notation, the expressions $du = f'(x)\,dx$ and
$dv = g'(x)\,dx$ are **just notation** in this course. The formula
$\int u\,dv= u\,v - \int v\,du$ is compact, easy to remember, and easy
to use.
:::

::: example
[]{#ex:9-8 label="ex:9-8"} Compute $\displaystyle\int x\,e^{x}\,dx$
using integration by parts.

**Solution.** We write the integral as $\int u\,dv$ and choose $u = x$,
$dv = e^{x}\,dx$. Then $du = dx$, $v = e^{x}$. Applying the formula:
$$\int x\,e^{x}\,dx= x\,e^{x} - \int e^{x}\,dx= x\,e^{x} - e^{x} + C.$$
:::

*This is the same result as before, but obtained more quickly and
systematically. When choosing $u$ and $dv$, the goal is to make the
transformed integral $\int v\,du$ easier than the original. The function
whose derivative is simpler should be $u$; the function whose
antiderivative is manageable should be $dv$.*

## Integration by Parts Examples {#sec:9.5}

*We now work through several examples of integration by parts, in
roughly increasing order of difficulty.*

::: remark
Before reading each solution, pause and attempt the computation
yourself.
:::

::: example
[]{#ex:9-9 label="ex:9-9"} Compute $\displaystyle\int x\cos(x)\,dx$.

**Solution.** For $\cos x$, both the derivative and the antiderivative
are essentially the same (up to sign), so it does not matter. For $x$,
however, the derivative ($1$) is simpler than the antiderivative
($\frac{1}{2}x^{2}$). So choose $u = x$, $dv = \cos(x)\,dx$. Then
$du = dx$, $v = \sin x$.
$$\int x\cos(x)\,dx= x\sin x - \int \sin(x)\,dx= x\sin x + \cos x + C.$$
:::

::: example
[]{#ex:9-10 label="ex:9-10"} Compute
$\displaystyle\int x^{2}\,e^{-x}\,dx$.

**Solution.** The derivative of $x^{2}$ is $2x$ (simpler), so take
$u = x^{2}$, $dv = e^{-x}\,dx$. Then $du = 2x\,dx$, $v = -e^{-x}$.
$$\int x^{2}\,e^{-x}\,dx= -x^{2}\,e^{-x} + \int 2x\,e^{-x}\,dx.$$ The
new integral is simpler, but not yet finished. Apply integration by
parts a second time: $u = 2x$, $dv = e^{-x}\,dx$, $du = 2\,dx$,
$v = -e^{-x}$. $$\begin{align*}
  \int x^{2}\,e^{-x}\,dx&= -x^{2}\,e^{-x} + \left[-2x\,e^{-x} + \int 2\,e^{-x}\,dx\right] \\
  &= -x^{2}\,e^{-x} - 2x\,e^{-x} - 2\,e^{-x} + C.
\end{align*}$$
:::

::: remark
Each application of integration by parts reduced the power of $x$ by one
while keeping the exponential. When the integrand is
$x^{n}\,e^{\alpha x}$, repeated integration by parts (applied $n$ times)
will reduce the problem to an integral with no polynomial factor.
:::

::: example
[]{#ex:9-11 label="ex:9-11"} Compute $\displaystyle\int \arctan(x)\,dx$.

**Solution.** This does not look like a product, but we can write it as
$1 \cdot \arctan(x)$. The derivative of $\arctan(x)$ is
$\dfrac{1}{1+x^{2}}$, which is simpler --- so our priority is to
*differentiate away* the $\arctan$. Choose $u = \arctan(x)$, $dv = dx$.
Then $du = \dfrac{1}{1+x^{2}}\,dx$, $v = x$.
$$\int \arctan(x)\,dx= x\arctan(x) - \int \frac{x}{1+x^{2}}\,dx.$$ The
$\arctan$ is gone. For the remaining integral, note that the numerator
$x$ is (up to a constant) the derivative of the denominator $1 + x^{2}$.
Set $t = 1 + x^{2}$, $dt = 2x\,dx$:
$$\int \frac{x}{1+x^{2}}\,dx= \frac{1}{2}\int \frac{dt}{t} = \frac{1}{2}\ln\left\lvert t \right\rvert + C = \frac{1}{2}\ln(1+x^{2}) + C.$$
Therefore
$$\int \arctan(x)\,dx= x\arctan(x) - \frac{1}{2}\ln(1+x^{2}) + C.$$
:::

::: remark
The absolute value is unnecessary in $\ln(1+x^{2})$ because
$1+x^{2} > 0$ for all $x$.
:::

## Cyclic Integration by Parts {#sec:9.6}

*This section presents a somewhat peculiar use of integration by parts,
in which the method appears to fail but actually succeeds through an
algebraic trick.*

::: remark
Before reading the solution below, try to compute
$\displaystyle\int e^{x}\sin(x)\,dx$ by integration by parts. Decide
whether it helps or not, and only then continue reading.
:::

::: example
[]{#ex:9-12 label="ex:9-12"} Compute
$\displaystyle\int e^{x}\sin(x)\,dx$.

**Solution.** Both $e^{x}$ and $\sin x$ are essentially unchanged by
differentiation --- $e^{x}$ stays the same, and $\sin x$ becomes
$\pm\cos x$. So *whatever we choose*, the transformed integral is not
any easier. Let us try anyway.

**First application.** Take $u = e^{x}$, $dv = \sin(x)\,dx$. Then
$du = e^{x}\,dx$, $v = -\cos x$.
$$\int e^{x}\sin(x)\,dx= -e^{x}\cos x + \int e^{x}\cos(x)\,dx.$$ As
expected, the new integral is no simpler. Nevertheless, apply
integration by parts a second time, keeping the same convention ($u$ =
exponential, $dv$ = trig): $u = e^{x}$, $dv = \cos(x)\,dx$,
$du = e^{x}\,dx$, $v = \sin x$.
$$\int e^{x}\sin(x)\,dx= -e^{x}\cos x + e^{x}\sin x - \int e^{x}\sin(x)\,dx.$$

**The trick.** The original integral has reappeared on the right! Let
$I = \displaystyle\int e^{x}\sin(x)\,dx$. Then
$$I = -e^{x}\cos x + e^{x}\sin x - I.$$ Solving for $I$:
$$2I = e^{x}(\sin x - \cos x), \qquad I = \frac{1}{2}\,e^{x}(\sin x - \cos x) + C.$$
:::

::: remark
When using integration by parts twice in this cyclic fashion, you must
keep the same convention for which factor is $u$ and which is $dv$ in
both applications. If you swap them the second time, you will undo the
first integration by parts and obtain the useless tautology
$\displaystyle\int e^{x}\sin(x)\,dx= \int e^{x}\sin(x)\,dx$.
:::

::: remark
The integration constant $C$ deserves a comment. The symbol $I$
represents a *family* of antiderivatives (a function plus an arbitrary
constant). Both sides of the equation $I = (\text{something}) - I$ carry
an arbitrary additive constant, but those constants need not agree. When
we solve for $I$ and write the final answer, we include $+C$ to reflect
this.
:::

## Trigonometric Integrals: Odd Powers {#sec:9.7}

*We now consider methods for integrating products of trigonometric
functions. Rather than presenting a collection of formulas to memorise,
we will develop the methods from scratch so that they can be re-derived
on the spot whenever needed.*

*The goal is to compute integrals of the form*
$$\int \sin^{n}x\,\cos^{m}x\,dx,$$ *where $n$ and $m$ are non-negative
integers. The strategy depends on the parity of the exponents. In this
section we handle the case when at least one exponent is odd.*

::: example
[]{#ex:9-13 label="ex:9-13"} Compute
$\displaystyle\int \sin^{5}x\,\cos^{2}x\,dx$.

**Solution.** There are two substitutions one might try: $u = \sin x$ or
$u = \cos x$.

**Attempt 1:** $u = \sin x$, $du = \cos x\,dx$. Separate one $\cos x$
for the differential. The remaining $\cos x$ must be converted to sines:
$$\cos x = \pm\sqrt{1 - \sin^{2}x} = \pm\sqrt{1 - u^{2}}.$$ This
introduces a square root --- the integral becomes *harder*, not easier.

**Attempt 2:** $u = \cos x$, $du = -\sin x\,dx$. Separate one $\sin x$
for the differential; the remaining
$\sin^{4}x = (\sin^{2}x)^{2} = (1-\cos^{2}x)^{2}$ converts cleanly:
$$\int \sin^{5}x\,\cos^{2}x\,dx= -\int (1-u^{2})^{2}\,u^{2}\,du.$$ No
square roots. The integrand is a polynomial in $u$, which we can expand
and integrate term by term.
:::

*The lesson is clear. When substituting $u = \cos x$, we need one
$\sin x$ for the differential; the remaining $\sin^{n-1}x$ must be an
even power so that we can use $\sin^{2}x = 1 - \cos^{2}x$ without square
roots. That requires $n$ to be odd. Similarly, $u = \sin x$ works when
$m$ is odd.*

::: proposition
[]{#thm:9-4 label="thm:9-4"} Consider
$\displaystyle\int \sin^{n}x\,\cos^{m}x\,dx$.

- If $n$ is odd, use $u = \cos x$. Separate one $\sin x$ for $du$;
  convert the remaining (even) powers of $\sin$ using
  $\sin^{2}x = 1 - \cos^{2}x$.

- If $m$ is odd, use $u = \sin x$. Separate one $\cos x$ for $du$;
  convert the remaining (even) powers of $\cos$ using
  $\cos^{2}x = 1 - \sin^{2}x$.

In either case the integral reduces to a polynomial in $u$.
:::

::: remark
If **both** $n$ and $m$ are even, neither substitution avoids square
roots, and a different method is needed. That is the topic of
[9.8](#sec:9.8){reference-type="ref+label" reference="sec:9.8"}.
:::

*These same ideas extend to products of powers of secant and tangent.
Since $\sec^{2}x = 1 + \tan^{2}x$ and the derivatives
$\frac{d}{dx}[\tan x] = \sec^{2}x$ and
$\frac{d}{dx}[\sec x] = \sec x\tan x$ involve the same functions, one
may try either $u = \tan x$ or $u = \sec x$.*

::: remark
Consider the three integrals
$\displaystyle\int \sec^{4}x\,\tan^{3}x\,dx$,
$\displaystyle\int \sec^{3}x\,\tan^{4}x\,dx$, and
$\displaystyle\int \sec^{2}x\,\tan^{5}x\,dx$. Using the identity
$\sec^{2}x = 1 + \tan^{2}x$ and the derivatives above, determine which
substitution ($u = \sec x$ or $u = \tan x$) is helpful for each
integral.
:::

## Trigonometric Integrals: Even Powers {#sec:9.8}

*When both exponents in $\displaystyle\int \sin^{n}x\,\cos^{m}x\,dx$ are
even, the substitutions from [9.7](#sec:9.7){reference-type="ref+label"
reference="sec:9.7"} do not help. We need a different approach.*

::: remark
*Is this an important problem?* Historically, these integrals appeared
often in science and technology. Today we have computer algebra systems,
and nobody integrates by hand for practical purposes. However, there is
still value: we should look at these calculations as **exercises in
problem solving** --- how to break a complex problem into cases and put
together various algorithms. That is where their value comes from,
rather than from the specific integrals themselves.
:::

### Method 1: Half-angle identities {#method-1-half-angle-identities .unnumbered}

The key identities are:
$$\sin^{2}x = \frac{1 - \cos 2x}{2}, \qquad \cos^{2}x = \frac{1 + \cos 2x}{2}.$$
These replace squares of $\sin$ and $\cos$ with expressions involving
$\cos 2x$, which is easy to integrate.

::: example
[]{#ex:9-14 label="ex:9-14"} Compute $\displaystyle\int \sin^{2}x\,dx$.

**Solution.** Using the half-angle identity:
$$\int \sin^{2}x\,dx= \frac{1}{2}\int dx - \frac{1}{2}\int \cos(2x)\,dx= \frac{x}{2} - \frac{\sin 2x}{4} + C.$$
:::

*The same method works for higher even powers. For example,
$\sin^{4}x\,\cos^{2}x = (\sin^{2}x)^{2}\,\cos^{2}x$ can be rewritten
using the half-angle formulas; after expanding, each resulting term will
either be easy to integrate directly, have an odd exponent (handled by
[9.7](#sec:9.7){reference-type="ref+label" reference="sec:9.7"}), or
have a lower even exponent (to which the half-angle formulas are applied
again).*

::: remark
Compute $\displaystyle\int \sin^{4}x\,dx$ using this method.
:::

### Method 2: Integration by parts {#method-2-integration-by-parts .unnumbered}

::: example
[]{#ex:9-15 label="ex:9-15"} Compute $\displaystyle\int \sin^{2}x\,dx$
using integration by parts.

**Solution.** Write $\sin^{2}x = \sin x \cdot \sin x$. Choose
$u = \sin x$, $dv = \sin x\,dx$. Then $du = \cos x\,dx$, $v = -\cos x$.
$$\int \sin^{2}x\,dx= -\sin x\cos x + \int \cos^{2}x\,dx.$$ Now use
$\sin^{2}x + \cos^{2}x = 1$, so
$\displaystyle\int \cos^{2}x\,dx= \int dx - \int \sin^{2}x\,dx= x - \int \sin^{2}x\,dx$.
Substituting:
$$\int \sin^{2}x\,dx= -\sin x\cos x + x - \int \sin^{2}x\,dx.$$ Solving:
$$2\int \sin^{2}x\,dx= x - \sin x\cos x, \qquad \int \sin^{2}x\,dx= \frac{x - \sin x\cos x}{2} + C.$$
:::

::: remark
Both methods give the same answer (verify using
$\sin 2x = 2\sin x\cos x$). The integration-by-parts method can in
principle be used for any even-power product, although it can easily get
messy.
:::

## Integration of Secant {#sec:9.9}

*The integral of secant is a historically important problem. In the
early years of calculus in the 17th century, computing $\int \sec x\,dx$
was needed in cartography, and mathematicians struggled for a while to
find a solution.*

### Method 1: The textbook trick {#method-1-the-textbook-trick .unnumbered}

::: example
[]{#ex:9-16 label="ex:9-16"} Compute $\displaystyle\int \sec x\,dx$ by
multiplying and dividing by $\sec x + \tan x$.

**Solution.**
$$\int \sec x\,dx= \int \frac{\sec x(\sec x + \tan x)}{\sec x + \tan x}\,dx= \int \frac{\sec^{2}x + \sec x\tan x}{\sec x + \tan x}\,dx.$$
Set $u = \sec x + \tan x$, $du = (\sec x\tan x + \sec^{2}x)\,dx$. The
numerator is exactly $du$:
$$\int \sec x\,dx= \int \frac{du}{u} = \ln\left\lvert u \right\rvert + C = \ln\left\lvert \sec x + \tan x \right\rvert + C.$$
:::

::: remark
This method is fast and simple, but it raises an uncomfortable question:
how on earth would one think to multiply and divide by
$\sec x + \tan x$? This seems like too great a leap, and there is no
satisfying explanation for why one would try it, other than hindsight.
:::

### Method 2: A more natural approach {#method-2-a-more-natural-approach .unnumbered}

*The following method is longer, but each step is natural and could be
discovered by any student with enough integration practice.*

Write $\sec x = \dfrac{1}{\cos x}$. Thinking of this as $\cos^{-1}x$
(i.e. $\sin^{0}x\,\cos^{-1}x$), the exponent of cosine is odd (namely
$-1$), so by the strategy of [9.7](#sec:9.7){reference-type="ref+label"
reference="sec:9.7"}, the substitution $u = \sin x$ should help.

Multiply numerator and denominator by $\cos x$:
$$\int \sec x\,dx= \int \frac{\cos x}{\cos^{2}x}\,dx= \int \frac{\cos x}{1 - \sin^{2}x}\,dx.$$
Set $u = \sin x$, $du = \cos x\,dx$:
$$\int \sec x\,dx= \int \frac{du}{1 - u^{2}}.$$ This is a rational
function --- a quotient of polynomials. It can be integrated using
partial fraction decomposition (see
[9.10](#sec:9.10){reference-type="ref+label" reference="sec:9.10"}).

::: remark
This second method is longer, but every step is natural: rewrite in
terms of sine and cosine, apply the standard substitution strategy, and
reduce to a rational function. Once one learns partial fractions, the
problem can be completed.
:::

## Partial Fractions: Distinct Factors {#sec:9.10}

*A rational function is a quotient of polynomials. The key idea for
integrating all rational functions is that there are a few simple
rational functions whose antiderivatives we already know, and we try to
rewrite every other rational function in terms of those simpler pieces.*

::: example
[]{#ex:9-17 label="ex:9-17"} Compute
$\displaystyle\int \frac{x+3}{(x-1)(x+1)}\,dx$.

**Solution.** The denominator makes this difficult to integrate
directly. However, $\dfrac{1}{x-1}$ and $\dfrac{1}{x+1}$ are each easy
to integrate. We seek constants $A$ and $B$ such that
$$\frac{x+3}{(x-1)(x+1)} = \frac{A}{x-1} + \frac{B}{x+1}.$$ Reducing the
right-hand side to a common denominator:
$$\frac{A(x+1) + B(x-1)}{(x-1)(x+1)} = \frac{(A+B)x + (A-B)}{(x-1)(x+1)}.$$
Matching coefficients: $A + B = 1$ and $A - B = 3$. Solving gives
$A = 2$, $B = -1$.

*Alternatively*, from the identity $x + 3 = A(x+1) + B(x-1)$, substitute
$x = 1$ to get $4 = 2A$, so $A = 2$; substitute $x = -1$ to get
$2 = -2B$, so $B = -1$.

Therefore
$$\int \frac{x+3}{(x-1)(x+1)}\,dx= \int \frac{2}{x-1}\,dx- \int \frac{1}{x+1}\,dx= 2\ln\left\lvert x-1 \right\rvert - \ln\left\lvert x+1 \right\rvert + C.$$
This can be written as $\ln\!\left|\dfrac{(x-1)^{2}}{x+1}\right| + C$.
:::

### The general strategy {#the-general-strategy .unnumbered}

*The same method works whenever the denominator factors into distinct
linear factors. Here is the general procedure.*

Given a rational function $\dfrac{P(x)}{Q(x)}$:

1.  **Long division.** If $\deg P \geq \deg Q$, perform polynomial long
    division to write $\dfrac{P(x)}{Q(x)} = S(x) + \dfrac{R(x)}{Q(x)}$,
    where $\deg R < \deg Q$. The polynomial $S(x)$ is easy to integrate;
    focus on the remainder.

2.  **Factor the denominator.**

3.  **Partial fraction decomposition.** If
    $Q(x) = (x - r_{1})(x - r_{2})\cdots(x - r_{k})$ with distinct
    roots, write
    $$\frac{R(x)}{Q(x)} = \frac{A_{1}}{x - r_{1}} + \frac{A_{2}}{x - r_{2}} + \cdots + \frac{A_{k}}{x - r_{k}}.$$
    Determine the constants $A_{i}$ by reducing to a common denominator
    and matching coefficients (or by evaluating at the roots).

4.  **Integrate** each term:
    $\displaystyle\int \frac{A_{i}}{x - r_{i}}\,dx= A_{i}\ln\left\lvert x - r_{i} \right\rvert + C$.

::: remark
The formal proof that this decomposition always works (with the correct
number of constants) requires linear algebra --- it amounts to a change
of basis in a finite-dimensional vector space.
:::

<figure id="fig:partial-fractions-decomposition"
data-latex-placement="ht">

<figcaption>A rational function and its partial fraction pieces
(qualitative shape).</figcaption>
</figure>

## Partial Fractions: Repeated Factors {#sec:9.11}

*When the denominator has a repeated linear factor, the decomposition
from [9.10](#sec:9.10){reference-type="ref+label" reference="sec:9.10"}
must be modified. We need additional terms to account for the
multiplicity.*

::: example
[]{#ex:9-18 label="ex:9-18"} Compute
$\displaystyle\int \frac{x^{4}+1}{x^{3}+2x^{2}+x}\,dx$.

**Solution.**

**Step 1: Long division.** Since
$\deg(x^{4}+1) = 4 > 3 = \deg(x^{3}+2x^{2}+x)$, we perform polynomial
long division. The result is
$$\frac{x^{4}+1}{x^{3}+2x^{2}+x} = (x - 2) + \frac{3x^{2}+2x+1}{x^{3}+2x^{2}+x}.$$
The polynomial $x - 2$ is easy to integrate.

**Step 2: Factor the denominator.** $x^{3}+2x^{2}+x = x(x+1)^{2}$.

**Step 3: Partial fractions.** We seek constants $A$, $B$, $C$ such that
$$\frac{3x^{2}+2x+1}{x(x+1)^{2}} = \frac{A}{x} + \frac{B}{x+1} + \frac{C}{(x+1)^{2}}.$$
:::

::: remark
A common mistake is to try only $\dfrac{A}{x} + \dfrac{B}{x+1}$. This
has only two free constants, but the numerator on the left has three
coefficients (degree $\leq 2$), so the system will generally be
inconsistent. The term $\dfrac{C}{(x+1)^{2}}$ is needed to provide
enough degrees of freedom.
:::

*Continuing the example:* reducing to a common denominator and matching
coefficients gives $A = 1$, $B = 2$, $C = -2$. Therefore:
$$\begin{align*}
  \int \frac{x^{4}+1}{x^{3}+2x^{2}+x}\,dx&= \int (x-2)\,dx+ \int \frac{1}{x}\,dx+ \int \frac{2}{x+1}\,dx+ \int \frac{-2}{(x+1)^{2}}\,dx\\
  &= \frac{x^{2}}{2} - 2x + \ln\left\lvert x \right\rvert + 2\ln\left\lvert x+1 \right\rvert + \frac{2}{x+1} + C.
\end{align*}$$

::: remark
The antiderivative of $\dfrac{1}{(x+1)^{2}}$ is $\dfrac{-1}{x+1}$,
because
$\dfrac{d}{dx}\!\left[\dfrac{-1}{x+1}\right] = \dfrac{1}{(x+1)^{2}}$.
This is just the power rule in disguise: $(x+1)^{-2}$ integrates to
$\dfrac{(x+1)^{-1}}{-1}$.
:::

## Partial Fractions: Irreducible Quadratics {#sec:9.12}

*When the denominator contains an irreducible quadratic factor (one that
does not factor over $\mathbb{R}$), the partial fraction approach
requires different building blocks.*

::: example
[]{#ex:9-19 label="ex:9-19"} Compute
$\displaystyle\int \frac{3x+7}{x^{2}+4}\,dx$.

**Solution.** Since $\deg(3x+7) = 1 < 2 = \deg(x^{2}+4)$, no long
division is needed. The denominator $x^{2}+4$ is an irreducible
quadratic --- it has no real roots.

Split the integrand into two pieces:
$$\int \frac{3x+7}{x^{2}+4}\,dx= 3\int \frac{x}{x^{2}+4}\,dx+ 7\int \frac{1}{x^{2}+4}\,dx.$$
Each of these is a basic building block that we can integrate directly.

**First integral.** The numerator $x$ is (up to a constant) the
derivative of the denominator $x^{2}+4$. Set $u = x^{2}+4$,
$du = 2x\,dx$:
$$\int \frac{x}{x^{2}+4}\,dx= \frac{1}{2}\int \frac{du}{u} = \frac{1}{2}\ln(x^{2}+4) + C.$$
(The absolute value is unnecessary since $x^{2} + 4 > 0$ for all $x$.)

**Second integral.** This is related to $\arctan$. Factor $4$ from the
denominator:
$$\int \frac{1}{x^{2}+4}\,dx= \int \frac{1}{4\!\left(\frac{x^{2}}{4}+1\right)}\,dx= \frac{1}{4}\int \frac{1}{\left(\frac{x}{2}\right)^{2}+1}\,dx.$$
Set $u = \frac{x}{2}$, $du = \frac{1}{2}\,dx$:
$$\frac{1}{4}\int \frac{2\,du}{u^{2}+1} = \frac{1}{2}\arctan(u) + C = \frac{1}{2}\arctan\!\left(\frac{x}{2}\right) + C.$$

**Combining:**
$$\int \frac{3x+7}{x^{2}+4}\,dx= \frac{3}{2}\ln(x^{2}+4) + \frac{7}{2}\arctan\!\left(\frac{x}{2}\right) + C.$$
:::

::: remark
When the denominator is an irreducible quadratic $x^{2} + bx + c$, the
two basic building blocks for integration are:

1.  $\dfrac{x + \text{const}}{x^{2}+bx+c}$, where the numerator is the
    derivative of the denominator (handled by a substitution, yielding a
    logarithm);

2.  $\dfrac{1}{(x-h)^{2}+k^{2}}$ (after completing the square), which
    yields an arctangent.

Any rational function with an irreducible quadratic denominator can be
split into a combination of these two types.
:::

# Volumes

## Volumes by Slicing {#sec:10.1}

*We defined integrals in order to compute areas, but there are many
other applications of integrals. In this section we revisit the
definition of the Riemann integral, reinterpret the notation with a
different geometrical flavour, and use the same idea to set up volumes
as integrals.*

### Reinterpreting the integral {#reinterpreting-the-integral .unnumbered}

Recall the idea behind the Riemann integral. Given a region bounded by
the graph of a function $f$, the $x$-axis, and the vertical lines
$x = a$ and $x = b$, we break $[a,b]$ into smaller pieces using a
partition. This cuts the region into thin vertical slices. Each slice is
approximated by a rectangle of width $\Delta x$ and height $f(x)$, so
its area is approximately $f(x)\cdot\Delta x$. Summing over all slices
gives an approximation to the total area, and taking the limit as
$\Delta x \to 0$ yields the definite integral.

*What follows is not a fully rigorous argument, but it provides powerful
geometric intuition and helps us reuse the same ideas for many
applications of the integral beyond areas.*

Since the integral is a limit of sums, we abuse notation and think of it
as an actual sum of infinitely many, infinitesimally small pieces.
Specifically, we write $\,dx$ and think of it as a $\Delta x$ that is
**infinitesimally small**. The integral sign then represents the "sum"
over infinitely many such pieces.

Consider the same region as before. Instead of finitely many slices,
imagine breaking it into infinitely many slices, each of infinitesimal
width $\,dx$. Focus on a single slice. Its width is $\,dx$, and since
the slice is infinitesimally thin, its area is also infinitesimal; call
it $dA$.

::: remark
When we approximate such a slice by a rectangle, the error is on the
order of $(\,dx)^{2}$: it is infinitesimally small *squared*. Compared
with the slice itself, this error is negligible, and we may ignore it in
the limit.
:::

Therefore the area of the slice is $$dA = f(x)\,dx,$$ and the total area
is the "sum" of all such infinitesimal pieces:
$$A = \int_{a}^{b} f(x)\,dx.$$

### From areas to volumes {#from-areas-to-volumes .unnumbered}

*The advantage of thinking of integrals this way is that it helps with
geometric intuition, and it helps us reuse the same ideas for many other
applications --- for example, computing volumes.*

Suppose we have a solid (picture a carrot) whose volume we wish to
compute. If we approximate it crudely by a single cylinder, the result
is poor. But just as we sliced a region into thin rectangles for areas,
we can **slice the solid** into thin pieces. Each slice is approximately
a disc, and we know how to compute the volume of a disc. Taking the
limit as the thickness tends to zero, the approximation becomes exact.

::: definition
[]{#def:10-1 label="def:10-1"} Let a solid be generated by rotating the
region between the graph of a function $y = f(x)$ and the $x$-axis, from
$x = a$ to $x = b$, around the $x$-axis. Cut the solid into
infinitesimally thin slices perpendicular to the $x$-axis. Each slice is
a disc of radius $R = \left\lvert f(x) \right\rvert$ and thickness
$\,dx$. Its infinitesimal volume is
$$dV = \pi R^{2}\,dx= \pi\bigl[f(x)\bigr]^{2}\,dx,$$ and the total
volume is $$V = \int_{a}^{b} \pi\bigl[f(x)\bigr]^{2}\,dx.$$
:::

<figure id="fig:disk-method-slice" data-latex-placement="ht">

<figcaption>Disk method intuition: a slice rotates into a
disk.</figcaption>
</figure>

::: remark
Just as with areas, the key step is identifying the infinitesimal piece
(a thin disc), writing its volume in terms of the variable of
integration, and then summing (integrating) over all such pieces.
:::

### A concrete example {#a-concrete-example .unnumbered}

::: example
[]{#ex:10-1 label="ex:10-1"} Let $R$ be the region in the first quadrant
between the graph of $y = x^{2}$ and the $x$-axis, from $x = 0$ to
$x = 1$. Rotate $R$ around the $x$-axis. Compute the volume of the
resulting solid.
:::

::: remark
Before reading the solution, draw a picture and try to understand what
the solid looks like. It resembles a cone that has been bent slightly.
:::

**Solution.** Slice the solid into infinitesimally thin pieces
perpendicular to the $x$-axis. A single slice is obtained by taking a
thin vertical strip of width $\,dx$ from the region $R$ and rotating it
around the $x$-axis. This produces a disc.

The disc has thickness $\,dx$ and radius equal to the height of the
strip, which is $y = x^{2}$. Therefore the infinitesimal volume is
$$dV = \pi\bigl(x^{2}\bigr)^{2}\,dx= \pi x^{4}\,dx.$$ Integrating from
$x = 0$ to $x = 1$:
$$V = \int_{0}^{1} \pi x^{4}\,dx= \pi\cdot\frac{x^{5}}{5}\bigg|_{0}^{1} = \frac{\pi}{5}.$$

::: remark
The strategy is always the same: slice the solid into infinitesimally
thin pieces, write the volume of each piece, and integrate. The
calculations may be more involved for other solids, but the underlying
idea is identical --- slice the carrot infinitesimally thin.
:::

## Cylindrical Shells {#sec:10.2}

*In the previous section, we computed volumes by slicing a solid
perpendicular to the axis of revolution, producing discs (or washers).
In this section, we work with a different example that requires a
different approach. The key idea is still slicing the solid into
infinitesimally thin pieces; we simply slice in a different direction.*

### When the disc method fails {#when-the-disc-method-fails .unnumbered}

::: example
[]{#ex:10-2 label="ex:10-2"} Let $R$ be the region in the first quadrant
between the graph of $y = 2x^{4} - x^{5}$ and the $x$-axis. Rotate $R$
around the $y$-axis. Compute the volume of the resulting solid.
:::

::: remark
Before reading on, draw a picture and try to visualise the solid. It
looks like a small volcano --- a mountain with a hole in the centre. The
curve $y = 2x^{4} - x^{5}$ forms the profile, and rotating it around the
$y$-axis produces the volcano shape.
:::

*Let us first attempt the approach from
[10.1](#sec:10.1){reference-type="ref+label" reference="sec:10.1"}:
slice perpendicular to the axis of revolution (the $y$-axis). This means
slicing horizontally.*

A thin horizontal strip of height $dy$ in the region $R$ corresponds,
after rotation, to a *washer*: a disc with a hole. If the inner radius
is $r$ and the outer radius is $R$, the infinitesimal volume would be
$$dV = \pi\bigl(R^{2} - r^{2}\bigr)\,dy.$$ To finish the setup, we would
integrate with respect to $y$ from $0$ to the maximum value of the
function, and we would need to express $R$ and $r$ in terms of $y$. That
means solving $$y = 2x^{4} - x^{5}$$ for $x$ in terms of $y$.

::: remark
This equation cannot be solved for $x$ by elementary methods. The plan
was a good idea and worth trying, but ultimately we cannot complete the
problem this way. We need a different approach.
:::

### The cylindrical shell method {#the-cylindrical-shell-method .unnumbered}

*Instead of slicing horizontally (perpendicular to the $y$-axis), we
slice the region **vertically** (parallel to the $y$-axis) and integrate
with respect to $x$.*

Take a thin vertical strip of width $\,dx$ in the region $R$. When this
strip is rotated around the $y$-axis, it sweeps out a *cylindrical
shell*: a thin hollow cylinder.

::: definition
[]{#def:10-2 label="def:10-2"} When a thin vertical strip at position
$x$, of height $y = f(x)$ and width $\,dx$, is rotated about the
$y$-axis, it produces a cylindrical shell of

- **radius** $\left\lvert x \right\rvert$ (the distance from the strip
  to the axis),

- **height** $y = f(x)$,

- **thickness** $\,dx$.

Because the thickness is infinitesimally small, we may "unroll" the
shell into a thin rectangular brick of dimensions
$2\pi x \times f(x) \times \,dx$. The infinitesimal volume is therefore
$$dV = 2\pi x\cdot f(x)\,dx,$$ and the total volume is
$$V = \int_{a}^{b} 2\pi x\cdot f(x)\,dx.$$
:::

<figure id="fig:cylindrical-shells" data-latex-placement="ht">

<figcaption>Shell method intuition: a strip rotates into a
shell.</figcaption>
</figure>

::: remark
Strictly speaking, unrolling the shell into a brick is an approximation.
But because the thickness $\,dx$ is infinitesimally small, the error
from flattening the curvature is negligible --- it is of order
$(\,dx)^{2}$. If the thickness were not infinitesimal, the error could
be significant.
:::

### Completing the example {#completing-the-example .unnumbered}

We return to [\[ex:10-2\]](#ex:10-2){reference-type="ref+label"
reference="ex:10-2"}. Slice the region $R$ vertically. A thin strip at
position $x$ has width $\,dx$ and height $y = 2x^{4} - x^{5}$. Rotating
this strip around the $y$-axis produces a cylindrical shell of radius
$x$, height $2x^{4} - x^{5}$, and thickness $\,dx$. Its infinitesimal
volume is $$dV = 2\pi x\bigl(2x^{4} - x^{5}\bigr)\,dx.$$ Since
$y = 2x^{4} - x^{5} = x^{4}(2 - x)$, the function is zero at $x = 0$ and
$x = 2$, so we integrate from $0$ to $2$:
$$V = \int_{0}^{2} 2\pi x\bigl(2x^{4} - x^{5}\bigr)\,dx= 2\pi\int_{0}^{2}\bigl(2x^{5} - x^{6}\bigr)\,dx.$$
This integral can now be evaluated using antiderivatives.

### Comparing the two methods {#comparing-the-two-methods .unnumbered}

*Both methods are fundamentally the same idea: cut the solid into
infinitesimally small pieces and integrate. We simply happen to cut in
different directions.*

::: definition
[]{#def:10-3 label="def:10-3"}

- The *washer method* (or disc method): we cut the region
  **perpendicular** to the axis of revolution. Each piece is a disc or
  washer.

- The *cylindrical shell method*: we cut the region **parallel** to the
  axis of revolution. Each piece is a cylindrical shell.
:::

<figure id="fig:washer-method-slice" data-latex-placement="ht">

<figcaption>Washer method intuition: outer minus inner
disk.</figcaption>
</figure>

::: remark
The names are less important than the underlying principle. In any given
problem, one method may lead to easier integrals than the other. When
one approach produces an equation that cannot be solved, try slicing in
the other direction.
:::

# Sequences

## Sequences and Notation {#sec:11.1}

*Before diving into the theory of sequences, we need a precise
definition and a tour of the various notational conventions that appear
throughout the subject. A sequence is simply a special type of function,
but by tradition we use different notation for it.*

::: definition
[]{#def:11-1 label="def:11-1"} A *sequence* is a function whose domain
is the set of all integers greater than or equal to some fixed integer
$n_{0}$. That is, the domain has the form
$$\{n \in \mathbb{Z}: n \ge n_{0}\}$$ for some fixed
$n_{0}\in\mathbb{Z}$.
:::

::: remark
The most common choices are $n_{0}=0$ and $n_{0}=1$, so the domain is
$\mathbb{N}$ or $\{1,2,3,\dots\}$. However, some sequences are naturally
defined only for $n\ge 2$ or even $n\ge 7$. For instance, the sequence
$\frac{1}{\ln n}$ is only defined for $n\ge 2$, because $\ln 1 = 0$.
:::

### Conventions distinguishing sequences from functions {#conventions-distinguishing-sequences-from-functions .unnumbered}

*Ultimately, sequences are functions. Nevertheless, we adopt several
conventions to distinguish between a function whose domain is an
interval (or a union of intervals) and a function whose domain consists
only of natural numbers.*

- **Variable name.** For a "function" (domain an interval) we typically
  use $x$ as the variable; for a sequence we use $n$. There is no deep
  reason for this, but the convention signals that $n$ takes only
  integer values.

- **Value notation.** If $f$ is a function, we write $f(x)$. If $a$ is a
  sequence, we write $a_{n}$ (a subscript) rather than $a(n)$.

- **Listing terms.** Because the domain consists of consecutive
  integers, the values of a sequence can be listed in order:
  $$a_{0},\; a_{1},\; a_{2},\; a_{3},\; \dots$$

::: remark
Writing the first few terms of a sequence in curly braces, such as
$\{1,2,4,8,16,\dots\}$, is common but potentially misleading: a sequence
is **not** a set. The set is the *range* of the sequence; the sequence
itself also specifies the *order* of its terms.
:::

### Ways to describe a sequence {#ways-to-describe-a-sequence .unnumbered}

There are four common ways to define a sequence.

1.  **By an explicit formula.** For example,
    $a_{n} = \dfrac{2^{n}\cdot n!}{n+1}$. The factorial makes clear that
    $n$ must be a natural number.

2.  **By listing the first few terms.** For example,
    $1,\;2,\;4,\;8,\;16,\;\dots$

3.  **By a verbal description.** For example, "let $p_{n}$ be the
    $n$^th^ prime number." This is perfectly valid when no nice
    closed-form formula exists.

4.  **By a recurrence relation.** For example, the *Fibonacci sequence*
    $\{F_{n}\}$ is defined by
    $$F_{1}=1,\quad F_{2}=1,\quad F_{n}=F_{n-1}+F_{n-2}\;\text{for }n\ge 3.$$

::: remark
The first few terms of a sequence **never fully determine** the
sequence. For instance, the terms $1,2,4,8,16,\dots$ could arise from
$a_{n}=2^{n}$, but they could equally arise from
$a_{n} = 2^{n} + (n-0)(n-1)(n-2)(n-3)(n-4)$ or from many other formulas.
When there is any ambiguity, always give an explicit formula or
recurrence.
:::

### Notation for sequences {#notation-for-sequences .unnumbered}

The most complete notation for a sequence is
$$\{a_{n}\}_{n=0}^{\infty}.$$ Common abbreviations include
$\{a_{n}\}_{n\ge 0}$, $\{a_{n}\}_{n}$, $\{a_{n}\}$, or simply $(a_{n})$.
Any of these is acceptable when unambiguous.

::: remark
When there are multiple variables, be precise. For example, the sequence
$\bigl\{\frac{n}{k}\bigr\}_{k=2}^{\infty}$ has variable $k$ (not $n$),
starting at $k=2$. Here $n$ is a constant. Omitting the index
information would create genuine ambiguity.
:::

## Limits of Sequences {#sec:11.2}

*We now define the central concept of this chapter: what it means for a
sequence to have a limit. If you are already familiar with the
$\varepsilon$-$\delta$ definition of the limit of a function, the
definition below will look very similar --- we simply replace the domain
of real numbers with the domain of natural numbers.*

### Motivation {#motivation .unnumbered}

::: example
[]{#ex:11-1 label="ex:11-1"} Consider the sequence
$\left\{\dfrac{n}{n+1}\right\}_{n=0}^{\infty}$. The first few terms are
$$0,\;\frac{1}{2},\;\frac{2}{3},\;\frac{3}{4},\;\frac{4}{5},\;\dots$$
Plotting these on the real line, we see that as $n$ increases the terms
crowd ever closer to $1$. We say that the limit of the sequence is $1$.
:::

*To make this precise, we think geometrically. Draw a small open
interval centred at the candidate limit $L$. Some initial terms of the
sequence may lie outside this interval, but after a certain point every
remaining term lies inside. If this is true for **every** open interval
centred at $L$, no matter how small, then $L$ is the limit.*

::: definition
[]{#def:11-2 label="def:11-2"} Let $\{a_{n}\}$ be a sequence and let
$L\in\mathbb{R}$. We say that the *limit* of $\{a_{n}\}$ is $L$, and
write $$\lim_{n\to\infty} a_{n} = L,$$ when the following holds:
$$\forall\,\varepsilon>0,\;\exists\,n_{0}\in\mathbb{N},\;\forall\,n\in\mathbb{N},\quad
  n\ge n_{0}\;\Longrightarrow\;\left\lvert a_{n}-L \right\rvert<\varepsilon.$$
Equivalently, $n\ge n_{0}$ implies
$L-\varepsilon< a_{n} < L+\varepsilon$.
:::

<figure id="fig:sequence-epsilon-neighborhood"
data-latex-placement="ht">

<figcaption>Convergence of a sequence in an <span
class="math inline"><em>ε</em></span>-neighborhood.</figcaption>
</figure>

*In one sentence: a sequence $\{a_{n}\}$ has limit $L$ when every open
interval centred at $L$ contains a **tail** of the sequence --- that is,
all terms from some index onward.*

::: remark
This one-sentence summary encodes all three quantifiers of the formal
definition but is easier to remember and gives a clear geometric
picture. It also highlights a fundamental principle: **to determine
whether a sequence has a limit, only the tails of the sequence matter**.
Changing the first $3$, the first $12$, or the first $60$ terms can
never affect whether the sequence converges.
:::

### Notation and terminology {#notation-and-terminology .unnumbered}

When $\lim_{n\to\infty}a_{n}=L$, we also write $a_{n}\to L$ and say that
the sequence *converges* to $L$.

::: definition
[]{#def:11-3 label="def:11-3"} A sequence is *convergent* if it has a
limit (which must be a real number). Otherwise, the sequence is
*divergent*.
:::

A divergent sequence may diverge to $\infty$ (e.g. $\{n^{2}\}$), to
$-\infty$ (e.g. $\{-n\}$), or it may oscillate without tending to any
value (e.g. $\{(-1)^{n}\}$, whose terms alternate between $1$ and $-1$).

::: remark
Write a precise formal definition of "$\lim_{n\to\infty}a_{n}=\infty$",
modelled on [\[def:11-2\]](#def:11-2){reference-type="ref+label"
reference="def:11-2"}.
:::

## Tools for Computing Limits {#sec:11.3}

*We do not want to appeal to the $\varepsilon$-definition every time we
compute a limit. In this section we survey the main tools available,
emphasising what carries over from limits of functions and what does
not.*

### What works the same {#what-works-the-same .unnumbered}

::: theorem
[]{#thm:11-1 label="thm:11-1"} If $\{a_{n}\}$ and $\{b_{n}\}$ are
convergent sequences with $\lim_{n\to\infty}a_{n}=A$ and
$\lim_{n\to\infty}b_{n}=B$, then

1.  $\lim_{n\to\infty}(a_{n}\pm b_{n})=A\pm B$,

2.  $\lim_{n\to\infty}(a_{n}\cdot b_{n})=A\cdot B$,

3.  $\lim_{n\to\infty}\dfrac{a_{n}}{b_{n}}=\dfrac{A}{B}$, provided
    $B\neq 0$.

The proofs are identical to the corresponding proofs for limits of
functions.
:::

::: theorem
[]{#thm:11-2 label="thm:11-2"} If $a_{n}\le b_{n}\le c_{n}$ for all $n$
(or at least for all sufficiently large $n$), and
$$\lim_{n\to\infty}a_{n}=\lim_{n\to\infty}c_{n}=L,$$ then
$\lim_{n\to\infty}b_{n}=L$. Same theorem, same proof as for functions.
:::

### L'Hôpital's Rule: a caveat {#lhôpitals-rule-a-caveat .unnumbered}

*L'Hôpital's Rule does **not** directly extend to sequences, because we
cannot take the derivative of a sequence. (What is the derivative of
$n!$?) However, there is a useful workaround.*

::: theorem
[]{#thm:11-3 label="thm:11-3"} Let $f$ be a function defined on
$[c,\infty)$ for some integer $c$, and let $a_{n}=f(n)$ for every
integer $n\ge c$.

1.  If $\lim_{x\to\infty}f(x)=L\in\mathbb{R}$, then
    $\lim_{n\to\infty}a_{n}=L$.

2.  If $\lim_{x\to\infty}f(x)=\infty$, then
    $\lim_{n\to\infty}a_{n}=\infty$.
:::

::: remark
If $\lim_{x\to\infty}f(x)$ does not exist (for instance because $f$
oscillates), we **cannot** conclude anything about the sequence. The
sequence may or may not converge. For example, the function
$f(x)=\sin(\pi x)$ has no limit at $\infty$, but the sequence
$a_{n}=\sin(\pi n)=0$ is convergent.
:::

Therefore, when a sequence $\{a_{n}\}$ "comes from" a function $f$
(i.e. $a_{n}=f(n)$), we may apply L'Hôpital's Rule to $f$ and use
[\[thm:11-3\]](#thm:11-3){reference-type="ref+label"
reference="thm:11-3"} to transfer the result to the sequence ---
provided the limit of $f$ exists.

### Composition with a continuous function {#composition-with-a-continuous-function .unnumbered}

::: theorem
[]{#thm:11-4 label="thm:11-4"} Let $\{a_{n}\}$ be a sequence with
$\lim_{n\to\infty}a_{n}=L$, and let $f$ be a function that is continuous
at $L$. Then $$\lim_{n\to\infty}f(a_{n})=f(L).$$
:::

::: remark
Write a proof of [\[thm:11-4\]](#thm:11-4){reference-type="ref+label"
reference="thm:11-4"}. It is a great exercise because you must use
**both** the definition of limit of a sequence and the definition of
continuity.
:::

::: example
[]{#ex:11-2 label="ex:11-2"} We compute $\lim_{n\to\infty}e^{1/n!}$.
Since $\lim_{n\to\infty}\frac{1}{n!}=0$ and the exponential function is
continuous at $0$, [\[thm:11-4\]](#thm:11-4){reference-type="ref+label"
reference="thm:11-4"} gives $$\lim_{n\to\infty}e^{1/n!}=e^{0}=1.$$
:::

*In summary, every tool you know for computing limits of functions as
the variable approaches $\infty$ carries over to sequences. The only
exception is L'Hôpital's Rule, which requires extending the sequence to
a function on the positive reals first.*

## Monotonicity and Boundedness {#sec:11.4}

*In this section we introduce two structural properties of sequences ---
monotonicity and boundedness --- and then state three theorems that
describe how these properties interact with convergence.*

### Monotonic sequences {#monotonic-sequences .unnumbered}

::: definition
[]{#def:11-4 label="def:11-4"} A sequence $\{a_{n}\}$ is

- *increasing* if $a_{n}<a_{n+1}$ for every $n$,

- *decreasing* if $a_{n}>a_{n+1}$ for every $n$,

- *non-decreasing* if $a_{n}\le a_{n+1}$ for every $n$,

- *non-increasing* if $a_{n}\ge a_{n+1}$ for every $n$.

A sequence is *monotonic* if it satisfies any one of these four
conditions.
:::

::: remark
For a sequence, "$a_{n}<a_{n+1}$ for every $n$" is equivalent to the
more familiar condition "$n<m \Rightarrow a_{n}<a_{m}$." Both
formulations are useful; the first is often simpler to check.
:::

::: example
[]{#ex:11-3 label="ex:11-3"} The sequence $\{n^{2}\}$ is increasing. The
sequence $\left\{\frac{1}{n+1}\right\}$ is decreasing. The sequence
$1,1,2,2,3,3,4,4,\dots$ is non-decreasing but not increasing.
:::

::: definition
[]{#def:11-5 label="def:11-5"} A sequence $\{a_{n}\}$ is *eventually
decreasing* if there exists an index $n_{0}$ such that $a_{n}>a_{n+1}$
for every $n\ge n_{0}$. The terms *eventually increasing*, *eventually
non-decreasing*, and *eventually monotonic* are defined similarly.
:::

::: example
[]{#ex:11-4 label="ex:11-4"} Consider the sequence
$\{n^{3}e^{-n}\}_{n=0}^{\infty}$. Define $f(x)=x^{3}e^{-x}$. Then
$$f'(x)=e^{-x}(3x^{2}-x^{3})=x^{2}e^{-x}(3-x).$$ Since $f'(x)<0$ for all
$x>3$, the function $f$ is decreasing on $[3,\infty)$. Therefore the
sequence $\{n^{3}e^{-n}\}$ is decreasing for $n\ge 3$; that is, it is
*eventually* decreasing.
:::

### Bounded sequences {#bounded-sequences .unnumbered}

::: definition
[]{#def:11-6 label="def:11-6"} A sequence $\{a_{n}\}$ is

- *bounded below* if there exists $A\in\mathbb{R}$ with $A\le a_{n}$ for
  every $n$,

- *bounded above* if there exists $B\in\mathbb{R}$ with $a_{n}\le B$ for
  every $n$,

- *bounded* if it is both bounded below and bounded above.
:::

::: remark
It is not worthwhile to define "eventually bounded." Can you see why? If
a sequence is eventually bounded, it is already bounded: the finitely
many initial terms that were excluded are themselves a finite set of
real numbers, so they cannot make the sequence unbounded.
:::

::: remark
Construct eight sequences, one for each combination of
bounded/unbounded, monotonic/not monotonic, and convergent/divergent.
Some combinations may be impossible --- discover which ones.
:::

### Three fundamental theorems {#three-fundamental-theorems .unnumbered}

*The following three results describe the precise relationship between
convergence, monotonicity, and boundedness. Their proofs will occupy the
next two sections.*

::: theorem
[]{#thm:11-5 label="thm:11-5"} If a sequence is convergent, then it is
bounded.
:::

::: theorem
[]{#thm:11-6 label="thm:11-6"} If a sequence is eventually monotonic and
bounded, then it is convergent.

Equivalently:

1.  If a sequence is eventually non-decreasing and bounded above, then
    it is convergent.

2.  If a sequence is eventually non-increasing and bounded below, then
    it is convergent.
:::

<figure id="fig:monotone-bounded-convergence" data-latex-placement="ht">

<figcaption>A monotone increasing sequence bounded above
converges.</figcaption>
</figure>

::: remark
The word "eventually" is crucial and perfectly natural: since
convergence depends only on the tail of a sequence, any hypothesis about
convergence should likewise depend only on the tail. Whether the first
$15$ terms are out of order is irrelevant.
:::

::: theorem
[]{#thm:11-7 label="thm:11-7"} If a sequence is eventually increasing
and not bounded above, then it diverges to $\infty$.
:::

*[\[thm:11-6,thm:11-7\]](#thm:11-6,thm:11-7){reference-type="ref+label"
reference="thm:11-6,thm:11-7"} together tell us that the behaviour of an
increasing sequence is very restricted: it is either convergent (if
bounded above) or divergent to $\infty$ (if not bounded above). No other
outcome is possible. This will be especially useful when we study
series.*

## Boundedness of Convergent Sequences {#sec:11.5}

*We now prove [\[thm:11-5\]](#thm:11-5){reference-type="ref+label"
reference="thm:11-5"}: every convergent sequence is bounded. The key
idea is simple --- all but finitely many terms are close to the limit,
and a finite collection of numbers is always bounded.*

::: proof
*Proof.* Let $\{a_{n}\}$ be a convergent sequence and let
$L=\lim_{n\to\infty}a_{n}$.

Choose $\varepsilon=1$ in
[\[def:11-2\]](#def:11-2){reference-type="ref+label"
reference="def:11-2"}. Then there exists $n_{0}\in\mathbb{N}$ such that
for every $n\ge n_{0}$, $$L-1<a_{n}<L+1.$$

Define $$\begin{align*}
  A &= \min\{L-1,\; a_{0},\; a_{1},\;\dots,\; a_{n_{0}-1}\},\\
  B &= \max\{L+1,\; a_{0},\; a_{1},\;\dots,\; a_{n_{0}-1}\}.
\end{align*}$$

Fix an arbitrary $n\in\mathbb{N}$. There are two cases.

- If $n\ge n_{0}$, then $A\le L-1<a_{n}<L+1\le B$.

- If $n<n_{0}$, then $a_{n}$ appears in the lists defining $A$ and $B$,
  so $A\le a_{n}\le B$ by construction.

In either case, $A\le a_{n}\le B$. Therefore the sequence is bounded. ◻
:::

::: remark
The choice $\varepsilon=1$ is arbitrary; any positive number would work.
We choose $1$ for simplicity. The essential point is that once
$\varepsilon$ is fixed, all terms from index $n_{0}$ onward are trapped
in the interval $(L-\varepsilon,\,L+\varepsilon)$. Only the finitely
many terms $a_{0},\dots,a_{n_{0}-1}$ remain, and a finite set of real
numbers always has a minimum and a maximum.
:::

## The Monotone Convergence Theorem {#sec:11.6}

*We now prove [\[thm:11-6\]](#thm:11-6){reference-type="ref+label"
reference="thm:11-6"} in the case of a non-decreasing sequence that is
bounded above. The proof for a non-increasing, bounded-below sequence is
entirely analogous. The key ingredient is the least-upper-bound axiom
for $\mathbb{R}$.*

### Proof strategy {#proof-strategy .unnumbered}

*Since we want to prove convergence, the very first step must be to
identify the limit. The limit is not given to us; we must construct it
from the hypotheses. For an increasing, bounded-above sequence, the
natural candidate is the supremum of its range.*

::: proof
*Proof.* Let $\{a_{n}\}$ be a non-decreasing sequence that is bounded
above.

Let $A=\{a_{n}:n\in\mathbb{N}\}$ be the range of the sequence. The set
$A$ is non-empty (it contains $a_{0}$) and bounded above (by
hypothesis). By the least-upper-bound axiom, $A$ has a supremum. Set
$$L=\sup A.$$ We claim that $\lim_{n\to\infty}a_{n}=L$.

Let $\varepsilon>0$. Since $L$ is the supremum and $L-\varepsilon<L$,
the number $L-\varepsilon$ is **not** an upper bound of $A$. Therefore
there exists $n_{0}\in\mathbb{N}$ such that $$L-\varepsilon<a_{n_{0}}.$$

Fix an arbitrary $n\ge n_{0}$. Because the sequence is non-decreasing
and $n\ge n_{0}$, $$a_{n_{0}}\le a_{n}.$$ Because every term of the
sequence is at most $L$ (by definition of supremum), $$a_{n}\le L.$$
Combining these with the inequality $L-\varepsilon<a_{n_{0}}$:
$$L-\varepsilon<a_{n_{0}}\le a_{n}\le L<L+\varepsilon.$$ Therefore
$\left\lvert a_{n}-L \right\rvert<\varepsilon$, which completes the
proof that $\lim_{n\to\infty}a_{n}=L$. ◻
:::

::: remark
Observe how each hypothesis was used: "bounded above" guarantees the
existence of $\sup A$; "increasing" ensures that once a single term
exceeds $L-\varepsilon$, every subsequent term does as well. Without
monotonicity, finding one term in $(L-\varepsilon,L+\varepsilon)$ would
say nothing about the terms that follow.
:::

::: remark
Write a rigorous proof of
[\[thm:11-7\]](#thm:11-7){reference-type="ref+label"
reference="thm:11-7"}: if $\{a_{n}\}$ is eventually increasing and not
bounded above, then $\lim_{n\to\infty}a_{n}=\infty$. The ideas are
similar to the proof above.
:::

## The Growth Hierarchy {#sec:11.7}

*We close the chapter with what is sometimes called the "Big Theorem"
--- a hierarchy among the most common families of positive sequences. It
tells us, at a glance, which terms dominate in a sum or quotient,
letting us compute many limits almost instantly.*

### Motivation: rational sequences {#motivation-rational-sequences .unnumbered}

::: example
[]{#ex:11-5 label="ex:11-5"} Compute
$\displaystyle\lim_{n\to\infty}\frac{n^{3}+2n+1}{5n^{3}+3n^{2}}$.

When the numerator and denominator are both polynomials, only the
highest-degree terms matter. The quick answer is
$\frac{n^{3}}{5n^{3}}=\frac{1}{5}$.

To justify this rigorously, factor $n^{3}$ from numerator and
denominator: $$\frac{n^{3}+2n+1}{5n^{3}+3n^{2}}
  =\frac{n^{3}\!\left(1+\frac{2}{n^{2}}+\frac{1}{n^{3}}\right)}
        {n^{3}\!\left(5+\frac{3}{n}\right)}
  =\frac{1+\frac{2}{n^{2}}+\frac{1}{n^{3}}}{5+\frac{3}{n}}.$$ As
$n\to\infty$, each correction term $\frac{2}{n^{2}}$, $\frac{1}{n^{3}}$,
$\frac{3}{n}$ tends to $0$, so by the limit laws the full limit is
$\frac{1}{5}$.
:::

*The reason the lower-order terms vanish is that, for instance,
$\lim_{n\to\infty}\frac{n}{n^{3}}=0$: the term $n$ grows **much more
slowly** than $n^{3}$. Can we extend this idea beyond polynomials?*

### The "much smaller" relation {#the-much-smaller-relation .unnumbered}

::: definition
[]{#def:11-7 label="def:11-7"} Let $\{a_{n}\}$ and $\{b_{n}\}$ be
sequences with $b_{n}>0$ for all $n$. We write $$a_{n}\ll b_{n}$$ and
say "$a_{n}$ is *much smaller* than $b_{n}$" to mean
$$\lim_{n\to\infty}\frac{a_{n}}{b_{n}}=0.$$ Equivalently, we say
"$b_{n}$ is *much larger* than $a_{n}$."
:::

### Statement of the Big Theorem {#statement-of-the-big-theorem .unnumbered}

::: theorem
[]{#thm:11-8 label="thm:11-8"} For any exponent $p>0$ and any base
$c>1$, $$\ln n \;\ll\; n^{p} \;\ll\; c^{n} \;\ll\; n! \;\ll\; n^{n}.$$
In words: logarithms are much smaller than any positive power, which is
much smaller than any exponential (with base $>1$), which is much
smaller than factorials, which are much smaller than power-exponentials.
:::

<figure id="fig:growth-hierarchy" data-latex-placement="ht">

<figcaption>Discrete comparison of common growth rates.</figcaption>
</figure>

### Using the theorem {#using-the-theorem .unnumbered}

::: example
[]{#ex:11-6 label="ex:11-6"} Compute
$\displaystyle\lim_{n\to\infty}\frac{e^{n}+2n^{100}}{\ln n+5e^{n}}$.

By [\[thm:11-8\]](#thm:11-8){reference-type="ref+label"
reference="thm:11-8"}, $n^{100}\ll e^{n}$ and $\ln n\ll e^{n}$.
Therefore $e^{n}$ is the dominant term in both numerator and
denominator. Factor $e^{n}$: $$\frac{e^{n}+2n^{100}}{\ln n+5e^{n}}
  =\frac{1+2\,\frac{n^{100}}{e^{n}}}{\frac{\ln n}{e^{n}}+5}.$$ As
$n\to\infty$, $\frac{n^{100}}{e^{n}}\to 0$ and
$\frac{\ln n}{e^{n}}\to 0$, so the limit is $\dfrac{1}{5}$.
:::

## Proof of the Growth Hierarchy {#sec:11.8}

*[\[thm:11-8\]](#thm:11-8){reference-type="ref+label"
reference="thm:11-8"} comprises four separate claims. The first two
(logarithms vs. powers, and powers vs. exponentials) can be proved using
L'Hôpital's Rule, because the sequences involved extend to functions on
$[1,\infty)$. The last two involve $n!$, which is defined only for
natural numbers, and require different techniques.*

::: remark
Before reading on, try to prove that $\ln n\ll n^{p}$ and
$n^{p}\ll c^{n}$ using L'Hôpital's Rule and
[\[thm:11-3\]](#thm:11-3){reference-type="ref+label"
reference="thm:11-3"}.
:::

### Claim 1: $\ln n \ll n^{p}$ for every $p>0$ {#claim-1-ln-n-ll-np-for-every-p0 .unnumbered}

Fix $p>0$ and define $f(x)=\frac{\ln x}{x^{p}}$ for $x\ge 1$. Applying
L'Hôpital's Rule ($\infty/\infty$ form):
$$\lim_{x\to\infty}\frac{\ln x}{x^{p}}
  =\lim_{x\to\infty}\frac{1/x}{p\,x^{p-1}}
  =\lim_{x\to\infty}\frac{1}{p\,x^{p}}=0.$$ By
[\[thm:11-3\]](#thm:11-3){reference-type="ref+label"
reference="thm:11-3"}, $\lim_{n\to\infty}\frac{\ln n}{n^{p}}=0$.

### Claim 2: $n^{p}\ll c^{n}$ for every $p>0$ and $c>1$ {#claim-2-npll-cn-for-every-p0-and-c1 .unnumbered}

Fix $p>0$ and $c>1$. Define $f(x)=\frac{x^{p}}{c^{x}}$ for $x\ge 1$.
Since both numerator and denominator tend to $\infty$, we apply
L'Hôpital's Rule repeatedly. After $k=\lceil p\rceil$ applications, the
numerator has degree at most $0$ in $x$ (it is a constant when $p$ is an
integer, or tends to $0$ when $p$ is not an integer) while the
denominator still tends to $\infty$, so the limit is $0$. By
[\[thm:11-3\]](#thm:11-3){reference-type="ref+label"
reference="thm:11-3"}, $\lim_{n\to\infty}\frac{n^{p}}{c^{n}}=0$.

### Claim 3: $c^{n}\ll n!$ for every $c>1$ {#claim-3-cnll-n-for-every-c1 .unnumbered}

::: proof
*Proof.* Fix $c>1$ and define $p_{n}=\dfrac{c^{n}}{n!}$ for $n\ge 0$.

Observe that
$$p_{n+1}=\frac{c^{n+1}}{(n+1)!}=\frac{c}{n+1}\cdot\frac{c^{n}}{n!}=\frac{c}{n+1}\,p_{n}.$$

For $n\ge c$ (i.e. $n+1>c$), we have $\frac{c}{n+1}<1$, so
$p_{n+1}<p_{n}$. Hence the sequence is eventually decreasing.

Since $p_{n}>0$ for all $n$, the sequence is bounded below by $0$. By
the Monotone Convergence Theorem
([\[thm:11-6\]](#thm:11-6){reference-type="ref+label"
reference="thm:11-6"}), the sequence converges. Let
$L=\lim_{n\to\infty}p_{n}$.

Taking limits on both sides of the recurrence
$p_{n+1}=\frac{c}{n+1}\,p_{n}$:
$$L = \lim_{n\to\infty}\frac{c}{n+1}\cdot\lim_{n\to\infty}p_{n}= 0\cdot L=0.$$
Therefore $\lim_{n\to\infty}\frac{c^{n}}{n!}=0$, as required. ◻
:::

::: remark
Every step of the proof above was necessary. The final calculation
(showing $L=0$ from the recurrence) is valid **only because we already
know the sequence converges**. Without first establishing convergence
via the Monotone Convergence Theorem, the same algebra would merely show
that the limit, *if it exists*, must be $0$ --- it would not rule out
divergence.
:::

### Claim 4: $n!\ll n^{n}$ {#claim-4-nll-nn .unnumbered}

::: proof
*Proof.* Write
$$\frac{n!}{n^{n}}=\frac{1\cdot 2\cdot 3\cdots n}{n\cdot n\cdot n\cdots n}
  =\frac{1}{n}\cdot\frac{2}{n}\cdot\frac{3}{n}\cdots\frac{n}{n}.$$

Separate the first factor:
$$\frac{n!}{n^{n}}=\frac{1}{n}\cdot\prod_{k=2}^{n}\frac{k}{n}.$$ Each
factor $\frac{k}{n}\le 1$ for $k\le n$, so the entire product satisfies
$$0<\frac{n!}{n^{n}}\le\frac{1}{n}.$$

Since $\lim_{n\to\infty}0=0$ and $\lim_{n\to\infty}\frac{1}{n}=0$, the
Squeeze Theorem ([\[thm:11-2\]](#thm:11-2){reference-type="ref+label"
reference="thm:11-2"}) gives
$$\lim_{n\to\infty}\frac{n!}{n^{n}}=0. \qedhere$$ ◻
:::

# Improper Integrals

## Unbounded Domains {#sec:12.1}

*Before we can try to compute an integral from $a$ to $\infty$, we need
to decide what it even means to integrate a function all the way to
infinity. We motivate the definition with a concrete example and then
state the general definition.*

### Motivating example {#motivating-example .unnumbered}

::: example
[]{#ex:12-1 label="ex:12-1"} Compute
$\displaystyle\int_{0}^{\infty}\frac{1}{1+x^{2}}\,dx$.

Geometrically, this represents the area between the $x$-axis and the
graph of $\frac{1}{1+x^{2}}$ starting at $x=0$ and extending to
infinity. We cannot compute this directly --- we only know how to
integrate a function between two real numbers $a$ and $b$.

However, for any real number $b>0$ we *can* compute
$\int_{0}^{b}\frac{1}{1+x^{2}}\,dx$, and then let $b$ grow without
bound: $$\int_{0}^{\infty}\frac{1}{1+x^{2}}\,dx
  \;=\; \lim_{b\to\infty}\int_{0}^{b}\frac{1}{1+x^{2}}\,dx.$$ An
antiderivative of $\frac{1}{1+x^{2}}$ is $\arctan x$, so
$$\begin{align*}
  \lim_{b\to\infty}\int_{0}^{b}\frac{1}{1+x^{2}}\,dx
  &= \lim_{b\to\infty}\Bigl[\arctan x\Bigr]_{0}^{b} \\
  &= \lim_{b\to\infty}\bigl(\arctan b - \arctan 0\bigr) \\
  &= \frac{\pi}{2} - 0 \;=\; \frac{\pi}{2}.
\end{align*}$$ The area under this curve, extending all the way to
infinity, is $\dfrac{\pi}{2}$.
:::

### The general definition {#the-general-definition .unnumbered}

::: definition
[]{#def:12-1 label="def:12-1"} Let $a\in\mathbb{R}$ and let $f$ be
continuous on $[a,\infty)$. We define
$$\int_{a}^{\infty}f(x)\,dx\;=\; \lim_{b\to\infty}\int_{a}^{b}f(x)\,dx,$$
provided the limit exists.

- Since $f$ is continuous on $[a,b]$, the integral
  $\int_{a}^{b}f(x)\,dx$ exists for every $b>a$.

- If the limit exists (is a finite number), we say the improper integral
  is *convergent*.

- If the limit does not exist, we say the improper integral is
  *divergent*.
:::

::: remark
Divergence can occur in different ways: the limit may be $+\infty$,
$-\infty$, or fail to exist for other reasons (e.g. oscillation).
:::

::: remark
Try to compute each of the following before watching the solutions in
the next few sections: $$\int_{0}^{\infty}\frac{x}{x^{2}+1}\,dx, \qquad
  \int_{0}^{\infty}\sin x\,dx, \qquad
  \int_{1}^{\infty}\frac{1}{x^{p}}\,dx, \qquad
  \int_{0}^{1}\ln x\,dx.$$ The last integral is improper in a different
way --- try to figure out what is different and how to define it.
:::

## A Divergent Integral {#sec:12.2}

*This second example looks deceptively similar to the first, yet the
outcome is completely different.*

::: example
[]{#ex:12-2 label="ex:12-2"} Determine whether
$\displaystyle\int_{0}^{\infty}\frac{x}{x^{2}+1}\,dx$ converges or
diverges.

By [\[def:12-1\]](#def:12-1){reference-type="ref+label"
reference="def:12-1"}, $$\int_{0}^{\infty}\frac{x}{x^{2}+1}\,dx
  \;=\; \lim_{b\to\infty}\int_{0}^{b}\frac{x}{x^{2}+1}\,dx.$$ To find an
antiderivative, note that
$\frac{x}{x^{2}+1} = \frac{1}{2}\cdot\frac{2x}{x^{2}+1}$, and $2x$ is
the derivative of $x^{2}+1$. Hence $$\int_{0}^{b}\frac{x}{x^{2}+1}\,dx
  \;=\; \frac{1}{2}\Bigl[\ln(x^{2}+1)\Bigr]_{0}^{b}
  \;=\; \frac{1}{2}\ln(b^{2}+1) - \frac{1}{2}\ln 1
  \;=\; \frac{1}{2}\ln(b^{2}+1).$$ As $b\to\infty$, $b^{2}+1\to\infty$,
and therefore $\ln(b^{2}+1)\to\infty$. The limit does not exist, so
$$\int_{0}^{\infty}\frac{x}{x^{2}+1}\,dx\quad\text{is \textbf{divergent}.}$$
:::

::: remark
The integrands $\frac{1}{x^{2}+1}$ and $\frac{x}{x^{2}+1}$ look very
similar, yet the first gives a convergent integral equal to
$\frac{\pi}{2}$ while the second diverges. Whether the area under a
curve extending to infinity is finite or infinite depends delicately on
how fast the function decays.
:::

## Oscillating Divergence {#sec:12.3}

*Not every divergent integral diverges to $\pm\infty$. Divergence can
also result from oscillation.*

::: example
[]{#ex:12-3 label="ex:12-3"} Determine whether
$\displaystyle\int_{0}^{\infty}\sin x\,dx$ converges or diverges.

By [\[def:12-1\]](#def:12-1){reference-type="ref+label"
reference="def:12-1"}, $$\int_{0}^{\infty}\sin x\,dx
  \;=\; \lim_{b\to\infty}\int_{0}^{b}\sin x\,dx
  \;=\; \lim_{b\to\infty}\Bigl[-\cos x\Bigr]_{0}^{b}
  \;=\; \lim_{b\to\infty}\bigl(1 - \cos b\bigr).$$ As $b\to\infty$,
$\cos b$ oscillates between $-1$ and $1$ without settling down, so
$1-\cos b$ oscillates between $0$ and $2$. The limit does not exist, and
the integral is **divergent**.
:::

::: remark
It is tempting to argue by symmetry that the positive and negative
regions of $\sin x$ cancel, giving $0$. This reasoning is flawed. Each
positive arch from $[2k\pi,(2k+1)\pi]$ has area $2$, and each negative
arch contributes $-2$ to the integral. As $b$ grows, the partial
integrals oscillate between $0$ and $2$ rather than settling to any
single value. The integral is not $0$ --- it is simply **not a number**.
:::

## The $p$-Integral {#sec:12.4}

*The family of integrals $\int_{1}^{\infty}\frac{1}{x^{p}}\,dx$ is
arguably the most important family of improper integrals. Its
convergence behaviour is simple to state and appears repeatedly when we
study comparison tests and, later, series.*

::: theorem
[]{#thm:12-1 label="thm:12-1"} For every $p\in\mathbb{R}$,
$$\int_{1}^{\infty}\frac{1}{x^{p}}\,dx
  \quad\text{is}\quad
  \begin{cases}
    \text{convergent} & \text{if } p>1, \\[4pt]
    \text{divergent } (+\infty) & \text{if } p\le 1.
  \end{cases}$$ When $p>1$, the value of the integral is
$\dfrac{1}{p-1}$.
:::

::: proof
*Proof.* By [\[def:12-1\]](#def:12-1){reference-type="ref+label"
reference="def:12-1"}, $$\int_{1}^{\infty}\frac{1}{x^{p}}\,dx
  \;=\; \lim_{b\to\infty}\int_{1}^{b}x^{-p}\,dx.$$

**Case 1: $p\neq 1$.** An antiderivative of $x^{-p}$ is
$\dfrac{x^{-p+1}}{-p+1}$, so $$\int_{1}^{b}x^{-p}\,dx
  \;=\; \frac{b^{1-p}}{1-p} - \frac{1}{1-p}.$$

- If $p<1$, then $1-p>0$, so $b^{1-p}\to\infty$ as $b\to\infty$, and the
  limit is $+\infty$.

- If $p>1$, then $1-p<0$, so $b^{1-p}\to 0$ as $b\to\infty$, giving
  $$\lim_{b\to\infty}\left(\frac{b^{1-p}}{1-p}-\frac{1}{1-p}\right)
      \;=\; 0 - \frac{1}{1-p}
      \;=\; \frac{1}{p-1}.$$

**Case 2: $p=1$.** An antiderivative of $\frac{1}{x}$ is $\ln x$, so
$$\int_{1}^{b}\frac{1}{x}\,dx\;=\; \ln b - \ln 1 \;=\; \ln b \;\to\; +\infty
  \quad\text{as }b\to\infty.$$ Combining the cases: the integral
converges if and only if $p>1$. ◻
:::

::: remark
This result is worth memorising. Once we introduce comparison tests, the
$p$-integral becomes the standard family against which we compare other
integrals. It plays exactly the same role for series later.
:::

<figure id="fig:p-integral-comparison" data-latex-placement="ht">

<figcaption>The <span class="math inline"><em>p</em></span>-integral
threshold at <span
class="math inline"><em>p</em> = 1</span>.</figcaption>
</figure>

## Unbounded Integrands {#sec:12.5}

*So far, every improper integral has been improper because the domain
extended to $\pm\infty$. There is a second, equally important type: the
integrand may be unbounded on the interval of integration, typically due
to a vertical asymptote at one of the endpoints.*

### Motivating example {#motivating-example-1 .unnumbered}

::: example
[]{#ex:12-4 label="ex:12-4"} Compute
$\displaystyle\int_{0}^{1}\ln x\,dx$.

The function $\ln x$ is unbounded near $x=0$ (it has a vertical
asymptote there), so the integral is improper. We cannot integrate a
function that is unbounded on its domain in the usual Riemann sense.

For any $c$ with $0<c<1$, the function $\ln x$ is continuous on $[c,1]$,
so $\int_{c}^{1}\ln x\,dx$ exists. We define $$\int_{0}^{1}\ln x\,dx
  \;=\; \lim_{c\to 0^{+}}\int_{c}^{1}\ln x\,dx.$$ By integration by
parts, an antiderivative of $\ln x$ is $x\ln x - x$. Therefore
$$\begin{align*}
  \int_{c}^{1}\ln x\,dx
  &= \Bigl[x\ln x - x\Bigr]_{c}^{1} \\
  &= (1\cdot\ln 1 - 1) - (c\ln c - c) \\
  &= -1 - c\ln c + c.
\end{align*}$$ We need to evaluate $\lim_{c\to 0^{+}}c\ln c$. This is an
indeterminate form of type $0\cdot(-\infty)$. Rewriting as a quotient
and applying L'Hôpital's rule: $$\lim_{c\to 0^{+}}c\ln c
  \;=\; \lim_{c\to 0^{+}}\frac{\ln c}{1/c}
  \;=\; \lim_{c\to 0^{+}}\frac{1/c}{-1/c^{2}}
  \;=\; \lim_{c\to 0^{+}}(-c)
  \;=\; 0.$$ Therefore $$\int_{0}^{1}\ln x\,dx
  \;=\; \lim_{c\to 0^{+}}(-1 - c\ln c + c)
  \;=\; -1 - 0 + 0
  \;=\; -1.$$ The negative sign is expected: the graph of $\ln x$ lies
below the $x$-axis on $(0,1)$.
:::

### The general definition {#the-general-definition-1 .unnumbered}

::: definition
[]{#def:12-2 label="def:12-2"} Let $a<b$ be real numbers and let $f$ be
continuous on $(a,b]$. We define
$$\int_{a}^{b}f(x)\,dx\;=\; \lim_{c\to a^{+}}\int_{c}^{b}f(x)\,dx,$$
provided the limit exists. Since $f$ is continuous on $[c,b]$ for every
$c\in(a,b)$, the integral $\int_{c}^{b}f(x)\,dx$ always makes sense. As
before, we say the improper integral is *convergent* when the limit
exists and *divergent* otherwise.
:::

::: remark
There is, of course, a symmetric definition when the integrand is
unbounded at the *right* endpoint: if $f$ is continuous on $[a,b)$, then
$$\int_{a}^{b}f(x)\,dx\;=\; \lim_{c\to b^{-}}\int_{a}^{c}f(x)\,dx.$$
:::

<figure id="fig:unbounded-integrand-integrable"
data-latex-placement="ht">

<figcaption>An improper integral converging despite an endpoint
blow-up.</figcaption>
</figure>

## Doubly Improper Integrals {#sec:12.6}

*Some integrals are improper in more than one way --- for instance, both
endpoints may be problematic, or there may be a singularity in the
interior. Such integrals require extra care to avoid fallacious
cancellations.*

### A cautionary example {#a-cautionary-example .unnumbered}

::: example
[]{#ex:12-5 label="ex:12-5"} Consider
$\displaystyle\int_{-\infty}^{\infty}x\,dx$.

One might argue that $f(x)=x$ is odd, so the positive and negative
regions cancel by symmetry, giving $0$. This reasoning is **wrong**.
:::

*To see why, suppose we try to evaluate the integral by centring the
domain at $0$:* $$\lim_{R\to\infty}\int_{-R}^{R}x\,dx
  \;=\; \lim_{R\to\infty}\left[\frac{x^{2}}{2}\right]_{-R}^{R}
  \;=\; \lim_{R\to\infty}\left(\frac{R^{2}}{2}-\frac{R^{2}}{2}\right)
  \;=\; 0.$$ But if we instead centre at $1$, integrating from $1-R$ to
$1+R$, a similar computation gives $\infty$. The two choices of
"symmetric" limits yield different answers.

*Moreover, the substitution $u=x-1$ transforms
$\int_{-\infty}^{\infty} x\,dx$ into
$\int_{-\infty}^{\infty}(u+1)\,du= \int_{-\infty}^{\infty}u\,du+ \int_{-\infty}^{\infty}1\,du$.
If $I = \int_{-\infty}^{\infty}x\,dx$ were a number, we would conclude
$I = I + \infty$, a contradiction.*

::: remark
If we ever try to cancel $+\infty$ with $-\infty$, fundamental
properties such as linearity and substitution break down. The only safe
course is to declare such integrals divergent.
:::

### The correct strategy {#the-correct-strategy .unnumbered}

::: definition
[]{#def:12-3 label="def:12-3"} Suppose an integral
$\int_{a}^{b}f(x)\,dx$ is improper at more than one point (e.g. at both
endpoints, or at an interior point). The procedure is:

1.  **Split** the domain into finitely many subintervals so that each
    piece is improper at **exactly one** endpoint.

2.  **Evaluate** each piece independently as a separate limit.

3.  The original integral is *convergent* if and only if **every** piece
    is convergent. If even one piece diverges, the whole integral is
    *divergent*.

The final value, when convergent, does not depend on how the domain is
split.
:::

::: example
[]{#ex:12-6 label="ex:12-6"} For
$\displaystyle\int_{-\infty}^{\infty}x\,dx$, split at $0$:
$$\int_{-\infty}^{\infty}x\,dx
  \;=\; \int_{-\infty}^{0}x\,dx+ \int_{0}^{\infty}x\,dx
  \;=\; \lim_{a\to-\infty}\int_{a}^{0}x\,dx+ \lim_{b\to\infty}\int_{0}^{b}x\,dx.$$
The first limit equals $-\infty$ and the second equals $+\infty$. Since
both pieces must converge independently and neither does, the integral
is **divergent**.
:::

::: example
[]{#ex:12-7 label="ex:12-7"} The integral
$\displaystyle\int_{0}^{\infty}\frac{1}{\sqrt{x}\,(1+x^{2})}\,dx$ is
improper at $x=0$ (vertical asymptote) and at $x=\infty$. Split at
$x=1$: $$\int_{0}^{\infty}\frac{1}{\sqrt{x}\,(1+x^{2})}\,dx
  \;=\;
  \underbrace{\int_{0}^{1}\frac{1}{\sqrt{x}\,(1+x^{2})}\,dx}_{\text{improper at }0}
  \;+\;
  \underbrace{\int_{1}^{\infty}\frac{1}{\sqrt{x}\,(1+x^{2})}\,dx}_{\text{improper at }\infty}.$$
Each piece is improper at one endpoint only and can be studied with the
definitions in
[\[sec:12.1,sec:12.5\]](#sec:12.1,sec:12.5){reference-type="ref+label"
reference="sec:12.1,sec:12.5"}. The original integral converges if and
only if both pieces converge.
:::

::: example
[]{#ex:12-8 label="ex:12-8"} The integral
$\displaystyle\int_{-1}^{1}\frac{1}{x^{2}}\,dx$ is improper at $x=0$
(vertical asymptote inside the domain). Split at $0$:
$$\int_{-1}^{1}\frac{1}{x^{2}}\,dx
  \;=\; \int_{-1}^{0}\frac{1}{x^{2}}\,dx+ \int_{0}^{1}\frac{1}{x^{2}}\,dx.$$
Each piece diverges (both equal $+\infty$), so the original integral is
**divergent**.
:::

::: remark
A common error is to fail to notice that the integrand is undefined or
unbounded at an interior point and to blindly apply the Fundamental
Theorem of Calculus across the singularity. Always check for vertical
asymptotes inside the interval of integration before computing.
:::

## The Basic Comparison Test {#sec:12.7}

*In many cases, computing the exact value of an improper integral is
difficult or impossible. Often, all we need to know is whether the
integral converges or diverges. For non-negative functions, comparison
provides a powerful tool.*

### Positive functions: only two outcomes {#positive-functions-only-two-outcomes .unnumbered}

::: proposition
[]{#thm:12-2 label="thm:12-2"} Let $f$ be continuous and non-negative on
$[a,\infty)$. Then $\int_{a}^{\infty}f(x)\,dx$ is either convergent (a
finite number) or divergent to $+\infty$. No other behaviour is
possible.
:::

::: proof
*Proof.* Define $F(b)=\int_{a}^{b}f(x)\,dx$. By the Fundamental Theorem
of Calculus, $F'(b)=f(b)\ge 0$, so $F$ is non-decreasing. A
non-decreasing function has a limit at infinity that is either finite
(by the Monotone Convergence Theorem, applied to the sequence $F(n)$ and
extended to all $b$ via monotonicity) or $+\infty$ (when $F$ is
unbounded above). These are the only two possibilities. ◻
:::

::: remark
Because there are only two outcomes for non-negative functions, we adopt
a convenient shorthand: $$\int_{a}^{\infty}f(x)\,dx< \infty
  \quad\text{means ``convergent'',}
  \qquad
  \int_{a}^{\infty}f(x)\,dx= \infty
  \quad\text{means ``divergent''.}$$ This notation is **only valid for
non-negative integrands**. For functions that change sign, "not
$\infty$" does not guarantee convergence (the integral could oscillate).
:::

### The theorem {#the-theorem-1 .unnumbered}

::: theorem
[]{#thm:12-3 label="thm:12-3"} Let $a\in\mathbb{R}$ and let $f,g$ be
continuous on $[a,\infty)$ with $0\le f(x)\le g(x)$ for all $x\ge a$.
Then:

1.  If $\displaystyle\int_{a}^{\infty}g(x)\,dx$ converges, then
    $\displaystyle\int_{a}^{\infty}f(x)\,dx$ converges.

2.  If $\displaystyle\int_{a}^{\infty}f(x)\,dx$ diverges, then
    $\displaystyle\int_{a}^{\infty}g(x)\,dx$ diverges.
:::

::: remark
Equivalently, using the shorthand for non-negative integrands:

- If the integral of the **bigger** function is $<\infty$, then the
  integral of the **smaller** function is also $<\infty$.

- If the integral of the **smaller** function is $=\infty$, then the
  integral of the **bigger** function is also $=\infty$.

The remaining two combinations (bigger diverges, or smaller converges)
give **no information**.
:::

<figure id="fig:comparison-test-area" data-latex-placement="ht">

<figcaption>Area comparison intuition for improper
integrals.</figcaption>
</figure>

## Basic Comparison Test Examples {#sec:12.8}

*We now illustrate the Basic Comparison Test by comparing new integrals
against the $p$-integral family from
[\[thm:12-1\]](#thm:12-1){reference-type="ref+label"
reference="thm:12-1"}.*

::: example
[]{#ex:12-9 label="ex:12-9"} Determine whether
$\displaystyle\int_{1}^{\infty}\frac{\sin^{2}x}{x^{2}}\,dx$ converges or
diverges.

For all $x\ge 1$,
$$0 \;\le\; \frac{\sin^{2}x}{x^{2}} \;\le\; \frac{1}{x^{2}}.$$ We know
$\int_{1}^{\infty}\frac{1}{x^{2}}\,dx$ converges because $p=2>1$
([\[thm:12-1\]](#thm:12-1){reference-type="ref+label"
reference="thm:12-1"}). By the Basic Comparison Test
([\[thm:12-3\]](#thm:12-3){reference-type="ref+label"
reference="thm:12-3"}),
$\displaystyle\int_{1}^{\infty}\frac{\sin^{2}x}{x^{2}}\,dx$ is
**convergent**.
:::

::: example
[]{#ex:12-10 label="ex:12-10"} Determine whether
$\displaystyle\int_{1}^{\infty}\frac{\sin^{2}x}{x}\,dx$ converges or
diverges.

We can bound $0\le\frac{\sin^{2}x}{x}\le\frac{1}{x}$, and
$\int_{1}^{\infty}\frac{1}{x}\,dx$ diverges ($p=1$). But the Basic
Comparison Test says: if the *bigger* function's integral diverges, we
learn **nothing** about the smaller.

As it turns out, this integral *is* divergent, but the Basic Comparison
Test alone does not establish this with the bound above.
:::

::: remark
[\[ex:12-10\]](#ex:12-10){reference-type="ref+label"
reference="ex:12-10"} illustrates an important lesson: the Basic
Comparison Test is inconclusive when the *bigger* function's integral
diverges. In such cases, one must try a different bound or a different
method entirely.
:::

::: example
[]{#ex:12-11 label="ex:12-11"} Determine whether
$\displaystyle\int_{1}^{\infty}\frac{\ln x}{x^{2}}\,dx$ converges or
diverges.

We would like to bound $\ln x$ by a power of $x$. From the "Big Theorem"
on the growth of logarithms,
$$\lim_{x\to\infty}\frac{\ln x}{x^{1/2}} = 0,$$ which means that for all
sufficiently large $x$, $\ln x < x^{1/2}$.

A first attempt to compare $\ln x$ with $x$ gives:
$$\frac{\ln x}{x^{2}} < \frac{x}{x^{2}} = \frac{1}{x},$$ but
$\int_{1}^{\infty}\frac{1}{x}\,dx= \infty$, so this comparison is
**inconclusive**.

Instead, use the tighter bound $\ln x < x^{1/2}$:
$$0 \;\le\; \frac{\ln x}{x^{2}} \;<\; \frac{x^{1/2}}{x^{2}} \;=\; \frac{1}{x^{3/2}}$$
for all sufficiently large $x$. Since
$\int_{1}^{\infty}\frac{1}{x^{3/2}}\,dx$ converges ($p=\frac{3}{2}>1$),
the Basic Comparison Test gives that
$\displaystyle\int_{1}^{\infty}\frac{\ln x}{x^{2}}\,dx$ is
**convergent**.
:::

::: remark
The comparison need only hold for all sufficiently large $x$ (say
$x\ge M$ for some $M$). The integral from $1$ to $M$ is a finite number
and does not affect convergence or divergence. This principle applies to
both the Basic and Limit-Comparison Tests.
:::

## The Limit-Comparison Test {#sec:12.9}

*The Limit-Comparison Test provides a more flexible method of
comparison. Rather than requiring a pointwise inequality $f(x)\le g(x)$,
we only need the two functions to be *asymptotically proportional*:
their ratio must tend to a positive constant.*

::: theorem
[]{#thm:12-4 label="thm:12-4"} Let $a\in\mathbb{R}$ and let $f,g$ be
positive and continuous on $[a,\infty)$. Suppose
$$\lim_{x\to\infty}\frac{f(x)}{g(x)} = L,$$ where $0<L<\infty$ (a
positive, finite number). Then
$$\int_{a}^{\infty}f(x)\,dx\;\text{ converges}
  \quad\Longleftrightarrow\quad
  \int_{a}^{\infty}g(x)\,dx\;\text{ converges.}$$ That is, the two
integrals are either both convergent or both divergent.
:::

### How to use the test {#how-to-use-the-test .unnumbered}

*The strategy is: given a complicated integrand $f$, identify the
"dominant" behaviour of $f(x)$ for large $x$ and let $g$ be that simpler
function. Then verify that $\lim_{x\to\infty}f(x)/g(x)$ is a positive
finite number.*

::: example
[]{#ex:12-12 label="ex:12-12"} Determine whether
$\displaystyle\int_{1}^{\infty}\frac{x^{2}+3x}{\sqrt{x^{5}+1}}\,dx$
converges or diverges.

Let $f(x)=\dfrac{x^{2}+3x}{\sqrt{x^{5}+1}}$. For large $x$, the dominant
terms are $x^{2}$ in the numerator and $\sqrt{x^{5}}=x^{5/2}$ in the
denominator. So we expect
$f(x)\approx \frac{x^{2}}{x^{5/2}}=\frac{1}{x^{1/2}}$. Set
$g(x)=\dfrac{1}{x^{1/2}}$.

Compute the limit: $$\lim_{x\to\infty}\frac{f(x)}{g(x)}
  = \lim_{x\to\infty}\frac{x^{2}+3x}{\sqrt{x^{5}+1}}\cdot x^{1/2}
  = \lim_{x\to\infty}\frac{x^{5/2}+3x^{3/2}}{\sqrt{x^{5}+1}}
  = 1.$$ Since $L=1>0$, the Limit-Comparison Test applies. We know
$\int_{1}^{\infty}\frac{1}{x^{1/2}}\,dx$ diverges
($p=\frac{1}{2}\le 1$). Therefore
$\displaystyle\int_{1}^{\infty}\frac{x^{2}+3x}{\sqrt{x^{5}+1}}\,dx$ is
**divergent**.
:::

::: example
[]{#ex:12-13 label="ex:12-13"} Determine whether
$\displaystyle\int_{1}^{\infty}\sin\!\left(\frac{1}{x^{2}}\right)\,dx$
converges or diverges.

For $x\ge 1$, the argument $\frac{1}{x^{2}}\in(0,1]$, so
$\sin\!\left(\frac{1}{x^{2}}\right)>0$. As $x\to\infty$,
$\frac{1}{x^{2}}\to 0$, and we recall $\lim_{t\to 0}\frac{\sin t}{t}=1$.
Set $f(x)=\sin\!\left(\frac{1}{x^{2}}\right)$ and
$g(x)=\frac{1}{x^{2}}$. Then $$\lim_{x\to\infty}\frac{f(x)}{g(x)}
  = \lim_{x\to\infty}\frac{\sin(1/x^{2})}{1/x^{2}}
  = 1.$$ Since $L=1>0$ and $\int_{1}^{\infty}\frac{1}{x^{2}}\,dx$
converges ($p=2>1$), the Limit-Comparison Test gives that
$\displaystyle\int_{1}^{\infty}\sin\!\left(\frac{1}{x^{2}}\right)\,dx$
is **convergent**.
:::

::: remark
What can we conclude if $L=0$ in the Limit-Comparison Test? What if
$L=\infty$? In each case, only *half* of the conclusion survives. Try to
determine which half by examining the proof in the next section.
:::

## Proof of the Limit-Comparison Test {#sec:12.10}

*The proof reduces the Limit-Comparison Test to the Basic Comparison
Test by extracting a two-sided inequality from the definition of a
limit.*

### Rough work {#rough-work .unnumbered}

*The hypothesis $\lim_{x\to\infty}\frac{f(x)}{g(x)}=L$ means that for
large $x$, $f(x)\approx L\cdot g(x)$. If $f$ is approximately a positive
constant times $g$, it is plausible that their integrals converge or
diverge together. To make this rigorous, we use the formal definition of
a limit to sandwich $f$ between two constant multiples of $g$.*

::: proof
*Proof.* Since $f$ and $g$ are positive and continuous on $[a,\infty)$,
[\[thm:12-2\]](#thm:12-2){reference-type="ref+label"
reference="thm:12-2"} implies each of $\int_{a}^{\infty}f(x)\,dx$ and
$\int_{a}^{\infty}g(x)\,dx$ is either convergent or $+\infty$. We show
these two integrals have the same status.

Take $\varepsilon=\dfrac{L}{2}>0$. By the definition of the limit, there
exists $M\ge a$ such that for all $x\ge M$,
$$\left\lvert\frac{f(x)}{g(x)}-L\right\rvert < \frac{L}{2}.$$

Equivalently, for all $x\ge M$,
$$\frac{L}{2}\,g(x) \;\le\; f(x) \;\le\; \frac{3L}{2}\,g(x).$$ Both
$\frac{L}{2}$ and $\frac{3L}{2}$ are positive constants.

*The inequality only holds for $x\ge M$, but this is sufficient: for any
continuous function $h$,*
$$\int_{a}^{\infty}h(x)\,dx= \underbrace{\int_{a}^{M}h(x)\,dx}_{\text{finite number}} + \int_{M}^{\infty}h(x)\,dx,$$
*so the integral from $a$ to $\infty$ converges if and only if the
integral from $M$ to $\infty$ converges.*

**Step 1.** Assume $\int_{M}^{\infty}g(x)\,dx$ converges. Then
$\int_{M}^{\infty}\frac{3L}{2}\,g(x)\,dx$ converges (a constant multiple
of a convergent integral). Since $f(x)\le\frac{3L}{2}\,g(x)$ for
$x\ge M$, the Basic Comparison Test
([\[thm:12-3\]](#thm:12-3){reference-type="ref+label"
reference="thm:12-3"}) gives $\int_{M}^{\infty}f(x)\,dx<\infty$.

**Step 2.** Assume $\int_{M}^{\infty}f(x)\,dx$ converges. Since
$\frac{L}{2}\,g(x)\le f(x)$ for $x\ge M$, the Basic Comparison Test
gives $\int_{M}^{\infty}\frac{L}{2}\,g(x)\,dx<\infty$, and hence
$\int_{M}^{\infty}g(x)\,dx<\infty$.

Since convergence from $M$ to $\infty$ is equivalent to convergence from
$a$ to $\infty$, we conclude:
$$\int_{a}^{\infty}f(x)\,dx\text{ converges}
  \quad\Longleftrightarrow\quad
  \int_{a}^{\infty}g(x)\,dx\text{ converges.} \qedhere$$ ◻
:::

::: remark
Examining the proof reveals two extended versions of the theorem:

- If $L=0$: only the inequality $f(x)\le\frac{3L}{2}\,g(x)$ survives in
  a useful form (with $L$ replaced by a small $\varepsilon$). We can
  conclude: if $\int_{a}^{\infty}g(x)\,dx$ converges, then
  $\int_{a}^{\infty}f(x)\,dx$ converges. But the converse need not hold.

- If $L=\infty$: by symmetry (swap $f$ and $g$, the reciprocal limit is
  $0$), we can conclude: if $\int_{a}^{\infty}g(x)\,dx$ diverges, then
  $\int_{a}^{\infty}f(x)\,dx$ diverges. But the converse need not hold.
:::

# Series

## Naive Infinite Sums {#sec:13.1}

*A series is an infinite sum. In this section we are intentionally
careless: we assume infinite sums are well-defined, behave well, and can
be manipulated exactly like finite sums. The contradictions that arise
will motivate the need for a rigorous definition.*

### A careless computation {#a-careless-computation .unnumbered}

::: example
[]{#ex:13-1 label="ex:13-1"} Fix a real number $x$ and set
$$S \;=\; \sum_{n=0}^{\infty} x^{n} \;=\; 1 + x + x^{2} + x^{3} + \cdots$$
Multiplying both sides by $x$ gives
$$xS \;=\; x + x^{2} + x^{3} + \cdots$$ Subtracting the second line from
the first, all terms cancel except the leading $1$:
$$S - xS = 1 \quad\Longrightarrow\quad S = \frac{1}{1-x}, \qquad x\neq 1.$$
This appears to give a value for every $x\neq 1$. But substituting $x=2$
yields $$1 + 2 + 4 + 8 + 16 + \cdots \;=\; \frac{1}{1-2} \;=\; -1,$$
which is absurd: a sum of positive terms cannot be negative.
:::

::: example
[]{#ex:13-2 label="ex:13-2"} Set
$T = \sum_{n=0}^{\infty}(-1)^{n} = 1 - 1 + 1 - 1 + \cdots$. Grouping in
pairs starting from the left gives
$$(1-1) + (1-1) + \cdots \;=\; 0+0+\cdots \;=\; 0.$$ But grouping
differently gives
$$1 + (-1+1) + (-1+1) + \cdots \;=\; 1 + 0 + 0 + \cdots \;=\; 1.$$ We
have "proved" $0 = 1$, which is obviously false.
:::

::: remark
Both contradictions arise from the same source: assuming every infinite
sum represents a number, and that it can be manipulated like a finite
sum. Properties such as associativity and commutativity are valid for
finite sums but **may fail** for infinite sums.
:::

### The road ahead {#the-road-ahead .unnumbered}

*To work with infinite sums without contradictions we need three
things:*

1.  A **definition** of what an infinite sum means.

2.  A way to distinguish *convergent* series (those that represent a
    number) from *divergent* ones (those that do not).

3.  **Theorems** that identify which properties of finite sums carry
    over to infinite sums, and which do not.

## Definition of Series {#sec:13.2}

*In everyday English, "series" and "sequence" are nearly synonymous; in
mathematics they are fundamentally different. A sequence is an infinite
list; a series is an infinite sum. We now make the latter idea precise.*

### Motivating example {#motivating-example-2 .unnumbered}

::: example
[]{#ex:13-3 label="ex:13-3"} Consider the sum
$$\sum_{n=1}^{\infty}\frac{1}{2^{n}} \;=\; \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \cdots$$
Imagine a unit square. Shade half of it (area $\frac{1}{2}$), then a
quarter ($\frac{1}{4}$), then an eighth, and so on. No matter how many
pieces we add, we remain inside the square, yet the un-shaded region
shrinks to nothing. It seems the sum should equal $1$.

Algebraically, define partial sums: $$S_{1} = \frac{1}{2}, \qquad
  S_{2} = \frac{1}{2}+\frac{1}{4} = \frac{3}{4}, \qquad
  S_{3} = \frac{1}{2}+\frac{1}{4}+\frac{1}{8} = \frac{7}{8}.$$ In
general, $S_{k} = \sum_{n=1}^{k}\frac{1}{2^{n}} = 1 - \frac{1}{2^{k}}$,
so
$$\sum_{n=1}^{\infty}\frac{1}{2^{n}} \;=\; \lim_{k\to\infty} S_{k} \;=\; \lim_{k\to\infty}\!\Bigl(1-\frac{1}{2^{k}}\Bigr) = 1.$$
The key idea: we never truly add infinitely many terms at once. Instead,
we add the first $k$ terms and take $k\to\infty$.
:::

### The general definition {#the-general-definition-2 .unnumbered}

::: definition
[]{#def:13-1 label="def:13-1"} Let $(a_{n})$ be a sequence. The *$k$-th
partial sum* of the series $\sum_{n=1}^{\infty}a_{n}$ is
$$S_{k} \;=\; \sum_{n=1}^{k} a_{n} \;=\; a_{1}+a_{2}+\cdots+a_{k}.$$ We
define $$\sum_{n=1}^{\infty}a_{n} \;=\; \lim_{k\to\infty} S_{k},$$
provided the limit exists.

- If the limit exists (is a finite number), the series is *convergent*.

- If the limit does not exist, the series is *divergent*.

Divergence may occur because the limit is $+\infty$, $-\infty$, or
because the sequence of partial sums oscillates.
:::

::: remark
The definition parallels that of improper integrals. An improper
integral $\int_{a}^{\infty}f(x)\,dx$ is defined as
$\lim_{b\to\infty}\int_{a}^{b}f(x)\,dx$: a limit of proper integrals.
Similarly, a series (infinite sum) is a limit of finite sums. In both
cases, the limit may or may not exist.
:::

<figure id="fig:partial-sums-converge" data-latex-placement="ht">

<figcaption>A convergent series’ partial sums approach a
limit.</figcaption>
</figure>

## A Telescoping Series {#sec:13.3}

*We compute a series directly from the definition, illustrating both the
guess-and-induct approach and the more elegant partial-fraction
technique.*

::: remark
Compute $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{2}+n}$ directly
from the definition before reading on.
:::

::: example
[]{#ex:13-4 label="ex:13-4"} Compute
$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{2}+n}$.

**Step 1: Compute partial sums.**
$$S_{1} = \frac{1}{1^{2}+1} = \frac{1}{2}, \qquad
  S_{2} = \frac{1}{2}+\frac{1}{6} = \frac{2}{3}, \qquad
  S_{3} = \frac{2}{3}+\frac{1}{12} = \frac{3}{4}.$$ The pattern
$S_{k} = \dfrac{k}{k+1}$ can be verified by induction.

**Alternative --- partial fractions (no guessing).** Factor
$n^{2}+n = n(n+1)$ and decompose:
$$\frac{1}{n(n+1)} \;=\; \frac{1}{n} - \frac{1}{n+1}.$$ Therefore
$$\begin{align*}
  S_{k} &= \sum_{n=1}^{k}\!\Bigl(\frac{1}{n}-\frac{1}{n+1}\Bigr) \\
  &= \Bigl(1-\frac{1}{2}\Bigr)+\Bigl(\frac{1}{2}-\frac{1}{3}\Bigr)+\cdots+\Bigl(\frac{1}{k}-\frac{1}{k+1}\Bigr) \\
  &= 1 - \frac{1}{k+1} \;=\; \frac{k}{k+1}.
\end{align*}$$

This is a *telescoping* sum. No induction is needed; the derivation
itself constitutes a proof.

**Step 2: Take the limit.** $$\sum_{n=1}^{\infty}\frac{1}{n^{2}+n}
  \;=\; \lim_{k\to\infty}\frac{k}{k+1} \;=\; 1.$$ The series is
convergent and its sum is $1$.
:::

## Two Divergent Series {#sec:13.4}

*We verify that our definition correctly identifies two series that
ought to be divergent. Each diverges for a different reason, providing a
useful sanity check on the definition.*

::: example
[]{#ex:13-5 label="ex:13-5"} Show that
$\displaystyle\sum_{n=1}^{\infty}1$ is divergent.

The $k$-th partial sum is $S_{k}=k$. Therefore
$$\sum_{n=1}^{\infty}1 \;=\; \lim_{k\to\infty} k \;=\; \infty.$$ The
series is divergent (to $\infty$), exactly as expected.
:::

::: example
[]{#ex:13-6 label="ex:13-6"} Show that
$\displaystyle\sum_{n=0}^{\infty}(-1)^{n}$ is divergent.

The first few partial sums are
$$S_{0}=1,\quad S_{1}=0,\quad S_{2}=1,\quad S_{3}=0,\quad\ldots$$ In
general, $S_{k}=1$ if $k$ is even and $S_{k}=0$ if $k$ is odd. The
sequence $1,0,1,0,\ldots$ has no limit --- it oscillates. Therefore the
series is divergent.
:::

::: remark
The series $\sum(-1)^{n}$ is not divergent because the partial sums tend
to $\pm\infty$; it is divergent because they fail to settle down to any
single value. Divergence can take many forms.
:::

## Geometric Series {#sec:13.5}

*The geometric series is one of the most important families of series.
We compute it carefully from the definition, obtaining both the domain
of convergence and the formula for the sum.*

::: remark
Fix $x\in\mathbb{R}$. Use the definition of series to determine for
which values of $x$ the series $\sum_{n=0}^{\infty}x^{n}$ converges, and
find its sum when it does.
:::

::: theorem
[]{#thm:13-1 label="thm:13-1"} For any $x\in\mathbb{R}$,
$$\sum_{n=0}^{\infty}x^{n} \;=\;
  \begin{cases}
    \dfrac{1}{1-x} & \text{if } \left\lvert x \right\rvert<1, \\[6pt]
    \text{divergent} & \text{if } \left\lvert x \right\rvert\ge 1.
  \end{cases}$$
:::

::: proof
*Proof.* **Case $x=1$.** The series becomes $\sum 1 = \infty$, which is
divergent.

**Case $x\neq 1$.** The $k$-th partial sum is
$S_{k}=1+x+x^{2}+\cdots+x^{k}$. Multiplying by $x$:
$$xS_{k} = x+x^{2}+\cdots+x^{k+1}.$$ Subtracting gives
$S_{k}-xS_{k}=1-x^{k+1}$, so $$S_{k} = \frac{1-x^{k+1}}{1-x}.$$

Taking the limit,
$$\sum_{n=0}^{\infty}x^{n} = \lim_{k\to\infty}\frac{1-x^{k+1}}{1-x} = \frac{1-\lim_{k\to\infty}x^{k+1}}{1-x}.$$

- If $\left\lvert x \right\rvert<1$, then $x^{k+1}\to 0$, so the sum
  equals $\dfrac{1}{1-x}$.

- If $x>1$, then $x^{k+1}\to\infty$, so the limit does not exist.

- If $x\le -1$, then $x^{k+1}$ oscillates (e.g. $-1,1,-1,\ldots$ when
  $x=-1$), so the limit does not exist.

In every case with $\left\lvert x \right\rvert\ge 1$ the series is
divergent. ◻
:::

::: remark
The formula $\sum x^{n}=\frac{1}{1-x}$ is only valid when
$\left\lvert x \right\rvert<1$. Using it outside this range --- as we
did carelessly in [13.1](#sec:13.1){reference-type="ref+label"
reference="sec:13.1"} --- leads to contradictions.
:::

<figure id="fig:geometric-series-area" data-latex-placement="ht">

<figcaption>Geometric series visualized by filling a unit
square.</figcaption>
</figure>

## Linearity of Series {#sec:13.6}

*Not every property of finite sums extends to infinite sums. For
instance, finite sums are commutative, but infinite sums are not (see
[13.17](#sec:13.17){reference-type="ref+label" reference="sec:13.17"}).
We single out two properties that **do** carry over: addition and scalar
multiplication.*

### A cautionary observation {#a-cautionary-observation .unnumbered}

*Consider the alternating harmonic series
$1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots = \ln 2$. If we rearrange
the same terms (two positives, then one negative, repeating), the new
sum is $\frac{3}{2}\ln 2$, not $\ln 2$. Rearranging the terms of a
convergent series can change its value! This shows that we must
carefully *prove* any property we wish to use for infinite sums.*

### The linearity theorems {#the-linearity-theorems .unnumbered}

::: theorem
[]{#thm:13-2 label="thm:13-2"} If $\sum a_{n}$ and $\sum b_{n}$ are both
convergent, then $\sum(a_{n}+b_{n})$ is also convergent and
$$\sum_{n=1}^{\infty}(a_{n}+b_{n}) \;=\; \sum_{n=1}^{\infty}a_{n} \;+\; \sum_{n=1}^{\infty}b_{n}.$$
:::

::: proof
*Proof.* Write $S_{k}=\sum_{n=1}^{k}a_{n}$, $T_{k}=\sum_{n=1}^{k}b_{n}$,
and $R_{k}=\sum_{n=1}^{k}(a_{n}+b_{n})$. For finite sums we have
$R_{k}=S_{k}+T_{k}$. By hypothesis, $\lim_{k\to\infty}S_{k}$ and
$\lim_{k\to\infty}T_{k}$ both exist. By the limit laws,
$$\lim_{k\to\infty}R_{k} = \lim_{k\to\infty}S_{k}+\lim_{k\to\infty}T_{k},$$
so $\sum(a_{n}+b_{n})$ converges and equals the sum of the two series. ◻
:::

::: theorem
[]{#thm:13-3 label="thm:13-3"} If $\sum a_{n}$ is convergent and
$c\in\mathbb{R}$, then $\sum c\,a_{n}$ is convergent and
$$\sum_{n=1}^{\infty}c\,a_{n} \;=\; c\sum_{n=1}^{\infty}a_{n}.$$
:::

::: proof
*Proof.* The proof follows the same template: write $S_{k}$ for the
partial sums of $\sum a_{n}$, observe that the $k$-th partial sum of
$\sum c\,a_{n}$ equals $c\,S_{k}$ (a property of finite sums), and apply
the limit laws. ◻
:::

::: remark
Both theorems require the hypothesis that the original series are
convergent. Without this, the limit laws cannot be applied. This
*template* recurs in almost every proof about series: (1) express the
infinite sum as a limit of finite sums, (2) use a known property of
finite sums, (3) pass to the limit.
:::

## Tails of Series {#sec:13.7}

*When studying convergence, the beginning of a series is irrelevant ---
only its tail matters. This simple but powerful observation makes many
theorems more widely applicable.*

::: theorem
[]{#thm:13-4 label="thm:13-4"} Let $(a_{n})$ be a sequence. The series
$\sum_{n=0}^{\infty}a_{n}$ is convergent if and only if
$\sum_{n=1}^{\infty}a_{n}$ is convergent. Moreover, if both converge,
$$\sum_{n=0}^{\infty}a_{n} \;=\; a_{0} + \sum_{n=1}^{\infty}a_{n}.$$
More generally, for any integers $m_{1}$ and $m_{2}$, the series
$\sum_{n=m_{1}}^{\infty}a_{n}$ converges if and only if
$\sum_{n=m_{2}}^{\infty}a_{n}$ converges.
:::

::: proof
*Proof.* Express each series as a limit of partial sums, use the
corresponding property for finite sums, and pass to the limit. ◻
:::

::: remark
Because of [\[thm:13-4\]](#thm:13-4){reference-type="ref+label"
reference="thm:13-4"}, we may write "$\sum a_{n}$ is convergent" without
specifying the starting index. The starting index affects the *value* of
the sum but not whether the series converges.
:::

*This observation has a useful consequence for applying convergence
theorems. A typical theorem has the form:*
$$\text{If for all } n\in\mathbb{N},\;\text{[some property]},\quad\text{then } \sum a_{n} \text{ converges.}$$
*By the tail principle, the same conclusion holds if \[some property\]
is true only for all sufficiently large $n$ --- that is, for all
$n\ge n_{0}$ for some $n_{0}\in\mathbb{N}$. In other words, a
convergence theorem that requires a condition for all $n$ automatically
yields a stronger version requiring the condition only **eventually**.
Whenever we prove a theorem of the first form, we get the second form
for free.*

::: definition
[]{#def:13-2 label="def:13-2"} For the purpose of convergence, only what
happens for large values of $n$ matters. Given a series
$\sum_{n=1}^{\infty}a_{n}$ and a positive integer $n_{0}$, the *tail* of
the series starting at $n_{0}$ is the series
$\sum_{n=n_{0}}^{\infty}a_{n}$. The original series and any of its tails
either both converge or both diverge.
:::

## The Divergence Test {#sec:13.8}

*Before deploying heavy machinery, there is one quick check worth
performing on every new series: does the general term tend to zero? If
not, the series cannot converge.*

::: theorem
[]{#thm:13-5 label="thm:13-5"} If
$\displaystyle\sum_{n=1}^{\infty}a_{n}$ is convergent, then
$\displaystyle\lim_{n\to\infty}a_{n}=0$.
:::

::: proof
*Proof.* Suppose $\sum a_{n}$ converges; denote the $k$-th partial sum
by $S_{k}$ and its limit by $S$. Write $$a_{n} = S_{n} - S_{n-1}.$$
Since $\lim_{n\to\infty}S_{n}=S$ and $\lim_{n\to\infty}S_{n-1}=S$, the
limit laws give $$\lim_{n\to\infty}a_{n} = S - S = 0. \qedhere$$ ◻
:::

<figure id="fig:divergence-test" data-latex-placement="ht">

<figcaption>A necessary condition for convergence: <span
class="math inline"><em>a</em><sub><em>n</em></sub> → 0</span>.</figcaption>
</figure>

::: remark
The **converse is false**. Having $\lim a_{n}=0$ does **not** guarantee
that $\sum a_{n}$ converges. For example,
$\lim_{n\to\infty}\frac{1}{n}=0$ but $\sum\frac{1}{n}$ diverges (the
harmonic series), while $\lim_{n\to\infty}\frac{1}{n^{2}}=0$ and
$\sum\frac{1}{n^{2}}$ converges. We will establish these facts in later
sections.
:::

*In practice we use the Divergence Test in its contrapositive form:*

::: corollary
[]{#cor:13-1 label="cor:13-1"} If $\lim_{n\to\infty}a_{n}\neq 0$
(including the case where the limit does not exist), then $\sum a_{n}$
is **divergent**.
:::

::: example
[]{#ex:13-7 label="ex:13-7"} The series
$\displaystyle\sum_{n=0}^{\infty}\frac{\arctan n}{1+e^{-n}}$ is
divergent, because
$$\lim_{n\to\infty}\frac{\arctan n}{1+e^{-n}} = \frac{\pi/2}{1+0} = \frac{\pi}{2}\neq 0.$$
:::

::: remark
The Divergence Test is a quick first step. It can never prove
convergence, but it can sometimes prove divergence immediately, allowing
us to move on without further analysis.
:::

## Positive Series {#sec:13.9}

*Proving convergence for a general series can be hard. Positive series
are substantially simpler: their only two behaviours are convergence and
divergence to $\infty$. This dichotomy is what makes comparison
arguments possible.*

::: definition
[]{#def:13-3 label="def:13-3"} A series $\sum a_{n}$ is called
*positive* if $a_{n}>0$ for all $n$, *negative* if $a_{n}<0$ for
all $n$, and *non-negative* if $a_{n}\ge 0$ for all $n$.
:::

::: theorem
[]{#thm:13-6 label="thm:13-6"} A positive series is either convergent or
divergent to $\infty$. In particular, it cannot diverge by oscillation.
:::

::: proof
*Proof.* If $\sum a_{n}$ is positive, then each $a_{n}>0$, so
$$S_{k+1} = S_{k}+a_{k+1} > S_{k}.$$ The sequence $(S_{k})$ is therefore
increasing. By the Monotone Convergence Theorem, an increasing sequence
either converges (if it is bounded above) or diverges to $\infty$ (if it
is unbounded). ◻
:::

::: remark
The same conclusion holds for non-negative series (replace "increasing"
with "non-decreasing") and for *eventually* non-negative series, by the
tail principle ([13.7](#sec:13.7){reference-type="ref+label"
reference="sec:13.7"}).
:::

### Notation for positive series {#notation-for-positive-series .unnumbered}

*Because a positive series can only converge or equal $\infty$, we adopt
a convenient shorthand.*

We write $\sum a_{n} < \infty$ to mean the positive series is
convergent, and $\sum a_{n} = \infty$ to mean it is divergent.

::: remark
This notation is reserved for positive (or non-negative) series
**only**. An arbitrary series that is not $\infty$ may still be
divergent by oscillation.
:::

*To prove that a positive series converges, it suffices to show it is
**not** $\infty$ --- equivalently, that the partial sums are bounded
above. This is less work than proving a limit exists directly. The
Integral Test, the Basic Comparison Test, and the Limit Comparison Test
all exploit this fact.*

## The Integral Test {#sec:13.10}

*Series and improper integrals are defined in the same way --- as limits
of their "finite" counterparts. It is natural to ask whether there is a
direct relationship between them. The Integral Test provides one,
letting us leverage antiderivatives to study convergence of series.*

### Deriving the test {#deriving-the-test .unnumbered}

*Let $f$ be continuous, positive, and decreasing on $[1,\infty)$. We
compare the integral $\int_{1}^{N}f(x)\,dx$ with finite sums by bounding
the area under the curve using rectangles.*

- **Upper bound.** On each interval $[n,n+1]$, the maximum of $f$ (since
  $f$ is decreasing) occurs at the left endpoint. Rectangles of height
  $f(n)$ and width $1$ give
  $$\int_{1}^{N}f(x)\,dx\;\le\; \sum_{n=1}^{N-1}f(n).$$

- **Lower bound.** Rectangles of height $f(n+1)$ and width $1$ give
  $$\int_{1}^{N}f(x)\,dx\;\ge\; \sum_{n=2}^{N}f(n).$$

Combining and letting $N\to\infty$:
$$\sum_{n=2}^{\infty}f(n) \;\le\; \int_{1}^{\infty}f(x)\,dx\;\le\; \sum_{n=1}^{\infty}f(n).$$
Since $f$ is positive, each quantity is either a finite number or
$\infty$. The two series differ only by the single term $f(1)$, so they
converge or diverge together. Sandwiching the integral between them
forces the integral to share their behaviour.

::: theorem
[]{#thm:13-7 label="thm:13-7"} Let $a\in\mathbb{R}$ and let $f$ be
continuous, positive, and decreasing on $[a,\infty)$. Then
$$\int_{a}^{\infty}f(x)\,dx\quad\text{converges} \qquad\Longleftrightarrow\qquad \sum_{n=\lceil a\rceil}^{\infty}f(n) \quad\text{converges.}$$
:::

::: remark
We write $\int_{a}^{\infty}f(x)\,dx\;\sim\; \sum f(n)$ to indicate the
integral and series are either both convergent or both divergent. This
does **not** mean they are equal; when both converge, their values are
generally different.
:::

## Integral Test Applications {#sec:13.11}

*We apply the Integral Test to two important examples. The first
identifies an entire family of convergent (and divergent) series; the
second handles a series that is not covered by the $p$-series family.*

::: example
[]{#ex:13-8 label="ex:13-8"} For $p>0$, determine when
$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{p}}$ converges.

The function $f(x)=\frac{1}{x^{p}}$ is continuous, positive, and
decreasing on $[1,\infty)$. By the Integral Test,
$$\sum_{n=1}^{\infty}\frac{1}{n^{p}} \;\sim\; \int_{1}^{\infty}\frac{1}{x^{p}}\,dx.$$
From the theory of improper integrals,
$\int_{1}^{\infty}\frac{1}{x^{p}}\,dx$ converges if and only if $p>1$.
:::

::: theorem
[]{#thm:13-8 label="thm:13-8"} The series
$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{p}}$ converges if and only
if $p>1$.
:::

::: remark
For $p\le 0$ the terms $\frac{1}{n^{p}}$ do not tend to zero, so the
series diverges by the Divergence Test
([\[thm:13-5\]](#thm:13-5){reference-type="ref+label"
reference="thm:13-5"}). For $p>0$ the convergence behaviour follows from
the Integral Test and the $p$-integral
([\[thm:12-1\]](#thm:12-1){reference-type="ref+label"
reference="thm:12-1"}).
:::

::: remark
In particular, the *harmonic series* $\sum\frac{1}{n}$ (the case $p=1$)
is divergent, while $\sum\frac{1}{n^{2}}$ is convergent. These are the
two benchmark series that the Divergence Test could not distinguish
([13.8](#sec:13.8){reference-type="ref+label" reference="sec:13.8"}).
:::

::: example
[]{#ex:13-9 label="ex:13-9"} Show that
$\displaystyle\sum_{n=2}^{\infty}\frac{1}{n\ln n}$ diverges.

The starting index is $n=2$ because $\ln 1=0$. Set
$f(x)=\frac{1}{x\ln x}$, which is continuous, positive, and decreasing
on $[2,\infty)$. By the Integral Test,
$$\sum_{n=2}^{\infty}\frac{1}{n\ln n} \;\sim\; \int_{2}^{\infty}\frac{1}{x\ln x}\,dx.$$
An antiderivative of $\frac{1}{x\ln x}$ is $\ln(\ln x)$ (check:
$\frac{d}{dx}\ln(\ln x)=\frac{1}{\ln x}\cdot\frac{1}{x}$). Therefore
$$\int_{2}^{b}\frac{1}{x\ln x}\,dx= \ln(\ln b)-\ln(\ln 2) \;\xrightarrow{b\to\infty}\; \infty.$$
The integral diverges, so by the Integral Test the series diverges as
well.
:::

## Comparison Tests {#sec:13.12}

*The comparison tests for series are identical in spirit and in proof to
the comparison tests for improper integrals. For brevity we state the
results without reproving them, but the proofs transfer verbatim from
the integral setting.*

*Both tests rest on the dichotomy for positive series
([\[thm:13-6\]](#thm:13-6){reference-type="ref+label"
reference="thm:13-6"}): a positive series is either convergent or
$\infty$. To prove convergence, it suffices to show the partial sums are
bounded above.*

::: theorem
[]{#thm:13-9 label="thm:13-9"} Suppose $0 \le a_{n} \le b_{n}$ for all
$n$ (or for all sufficiently large $n$). Then:

1.  If $\sum b_{n}$ converges, then $\sum a_{n}$ converges.

2.  If $\sum a_{n}$ diverges, then $\sum b_{n}$ diverges.
:::

::: theorem
[]{#thm:13-10 label="thm:13-10"} Let $\sum a_{n}$ and $\sum b_{n}$ be
positive series. If
$$\lim_{n\to\infty}\frac{a_{n}}{b_{n}} = L, \qquad 0<L<\infty,$$ then
$\sum a_{n}$ and $\sum b_{n}$ either both converge or both diverge.
:::

::: remark
The proof of each theorem follows the same pattern as for improper
integrals: replace every integral with a series, and every proper
integral with a partial sum. The details are otherwise unchanged.
:::

## Alternating Series Test {#sec:13.13}

*We now move beyond positive series. A large and well-behaved family
consists of alternating series --- those whose terms switch sign at
every step. Under mild hypotheses, they must converge, and there is a
clean geometric picture explaining why.*

::: definition
[]{#def:13-4 label="def:13-4"} A series $\sum a_{n}$ is *alternating* if
$a_{n}\cdot a_{n+1}<0$ for every $n$ --- that is, consecutive terms have
opposite signs.
:::

*A typical alternating series has the form $\sum(-1)^{n}b_{n}$ or
$\sum(-1)^{n+1}b_{n}$ with $b_{n}>0$.*

::: theorem
[]{#thm:13-11 label="thm:13-11"} Suppose the series
$\sum_{n=1}^{\infty}(-1)^{n+1}b_{n}$ satisfies:

1.  $b_{n}>0$ for all $n$ [(]{.upright}the series alternates in
    sign[)]{.upright},

2.  $(b_{n})$ is decreasing,

3.  $\lim_{n\to\infty}b_{n}=0$.

Then the series is convergent.
:::

::: proof
*Proof.* Write $S_{k}=\sum_{n=1}^{k}(-1)^{n+1}b_{n}$. The terms are
$b_{1},-b_{2},b_{3},-b_{4},\ldots$

**Step 1: Ordering of partial sums.** Since $b_{n}$ is decreasing and
positive, $$\begin{align*}
  S_{2k+2} &= S_{2k} + (b_{2k+1}-b_{2k+2}) \ge S_{2k}, \\
  S_{2k+1} &= S_{2k-1} - (b_{2k}-b_{2k+1}) \le S_{2k-1}.
\end{align*}$$ Also $S_{2k+1}=S_{2k}+b_{2k+1}>S_{2k}$. Therefore
$$S_{2}\le S_{4}\le S_{6} \le \cdots \le S_{5} \le S_{3} \le S_{1}.$$

**Step 2: Even and odd subsequences converge.** The sequence $(S_{2k})$
is increasing and bounded above (by $S_{1}$), so by the Monotone
Convergence Theorem it converges to some limit $A$. Similarly,
$(S_{2k+1})$ is decreasing and bounded below (by $S_{2}$), so it
converges to some limit $B$.

**Step 3: The two limits agree.** Since $S_{2k+1}=S_{2k}+b_{2k+1}$,
taking limits gives $B = A + 0 = A$ (using hypothesis (iii)).

**Step 4: Full sequence converges.** The even and odd subsequences both
converge to the same limit $A$. By a standard lemma (if the even-indexed
and odd-indexed subsequences of a sequence both converge to the same
limit, then the full sequence converges to that limit),
$\lim_{k\to\infty}S_{k}=A$. ◻
:::

::: example
[]{#ex:13-10 label="ex:13-10"} The alternating harmonic series
$\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n} = 1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots$
converges by the Alternating Series Test, since $b_{n}=\frac{1}{n}$ is
positive, decreasing, and has limit $0$.
:::

::: example
[]{#ex:13-11 label="ex:13-11"} The series
$\displaystyle\sum_{n=2}^{\infty}\frac{(-1)^{n}}{\ln n}$ converges by
the Alternating Series Test, since $b_{n}=\frac{1}{\ln n}$ is positive,
decreasing, and has limit $0$.
:::

## Alternating Series Estimation {#sec:13.14}

*Alternating series that satisfy the hypotheses of the Alternating
Series Test are not only easy to test for convergence --- they are also
easy to estimate. The error made by truncating the series is bounded by
the first omitted term.*

::: theorem
[]{#thm:13-12 label="thm:13-12"} Under the same three hypotheses as
[\[thm:13-11\]](#thm:13-11){reference-type="ref+label"
reference="thm:13-11"}, let $S=\sum_{n=1}^{\infty}(-1)^{n+1}b_{n}$ and
$S_{k}=\sum_{n=1}^{k}(-1)^{n+1}b_{n}$. Then
$$\left\lvert S - S_{k} \right\rvert \;\le\; b_{k+1}.$$ In words: the
error made by approximating the infinite sum with its $k$-th partial sum
is at most the absolute value of the first omitted term.
:::

::: proof
*Proof.* From the proof of
[\[thm:13-11\]](#thm:13-11){reference-type="ref+label"
reference="thm:13-11"}, the value $S$ lies between every consecutive
pair of partial sums. In particular, $S$ is between $S_{k}$ and
$S_{k+1}$, so
$\left\lvert S-S_{k} \right\rvert\le\left\lvert S_{k+1}-S_{k} \right\rvert=b_{k+1}$. ◻
:::

<figure id="fig:alternating-series-estimation"
data-latex-placement="ht">

<figcaption>Alternating series estimation: the remainder is bounded by
the next term.</figcaption>
</figure>

::: example
[]{#ex:13-12 label="ex:13-12"} Estimate
$\displaystyle S=\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{4}}$ with error
less than $0.001$.

(Note: this series uses $(-1)^{n}$ rather than $(-1)^{n+1}$. Since
$(-1)^{n}=-(-1)^{n+1}$, the series equals
$-\sum\frac{(-1)^{n+1}}{n^{4}}$, which is simply the negative of an
alternating series in standard form. The Alternating Series Test and its
estimation theorem still apply.)

The series satisfies the hypotheses of the Alternating Series Test
($b_{n}=\frac{1}{n^{4}}$ is positive, decreasing, and tends to $0$), so
the estimation theorem applies. Truncating at the $k$-th term gives
error at most $\frac{1}{(k+1)^{4}}$. We need
$$\frac{1}{(k+1)^{4}} < 0.001 \quad\Longleftrightarrow\quad (k+1)^{4}>1000.$$
The smallest integer $k$ satisfying this is $k=5$ (since
$6^{4}=1296>1000$). Therefore
$$S \;\approx\; S_{5} = \sum_{n=1}^{5}\frac{(-1)^{n}}{n^{4}} = -1+\frac{1}{16}-\frac{1}{81}+\frac{1}{256}-\frac{1}{625} \approx -0.94754.$$
The exact value (computable by advanced methods) begins
$-0.94703\ldots$, confirming that the error is indeed less than $0.001$.
:::

::: remark
For other types of convergent series, bounding the truncation error is
generally much harder. The simplicity of the alternating-series error
bound is one of the reasons alternating series are so pleasant to work
with.
:::

## Absolute and Conditional Convergence {#sec:13.15}

*When a series is neither positive nor alternating, we have few direct
tools. A natural strategy is to take absolute values, reducing the
problem to a positive series. This motivates the distinction between
absolute and conditional convergence.*

### Motivation {#motivation-1 .unnumbered}

::: example
[]{#ex:13-13 label="ex:13-13"} Is
$\displaystyle\sum_{n=1}^{\infty}\frac{\sin n}{n^{2}}$ convergent?

This series is not positive (since $\sin n$ changes sign irregularly)
and not alternating. However, taking absolute values gives a positive
series:
$$\sum_{n=1}^{\infty}\frac{\left\lvert \sin n \right\rvert}{n^{2}} \;\le\; \sum_{n=1}^{\infty}\frac{1}{n^{2}},$$
and $\sum\frac{1}{n^{2}}$ converges ($p$-series with $p=2$). By the
Basic Comparison Test,
$\sum\frac{\left\lvert \sin n \right\rvert}{n^{2}}$ converges. Can we
then conclude the original series converges?
:::

### The Absolute Convergence Test {#the-absolute-convergence-test .unnumbered}

::: theorem
[]{#thm:13-13 label="thm:13-13"} If
$\displaystyle\sum_{n=1}^{\infty}\left\lvert a_{n} \right\rvert$
converges, then $\displaystyle\sum_{n=1}^{\infty}a_{n}$ converges.
:::

*Returning to [\[ex:13-13\]](#ex:13-13){reference-type="ref+label"
reference="ex:13-13"}: since
$\sum\frac{\left\lvert \sin n \right\rvert}{n^{2}}$ converges, the
Absolute Convergence Test tells us that $\sum\frac{\sin n}{n^{2}}$
converges as well.*

::: remark
The converse is false. A series may converge while the series of
absolute values diverges (see the definitions below).
:::

### Absolute versus conditional convergence {#absolute-versus-conditional-convergence .unnumbered}

::: definition
[]{#def:13-5 label="def:13-5"} A convergent series $\sum a_{n}$ is
called:

- *absolutely convergent* if $\sum\left\lvert a_{n} \right\rvert$ also
  converges,

- *conditionally convergent* if $\sum\left\lvert a_{n} \right\rvert$
  diverges.
:::

::: example
[]{#ex:13-14 label="ex:13-14"} The alternating harmonic series
$\sum\frac{(-1)^{n+1}}{n}$ is **conditionally convergent**: the series
itself converges (Alternating Series Test), but $\sum\frac{1}{n}$
diverges ($p$-series with $p=1$).
:::

::: example
[]{#ex:13-15 label="ex:13-15"} The series $\sum\frac{(-1)^{n+1}}{n^{2}}$
is **absolutely convergent**: the series itself converges (Alternating
Series Test), and $\sum\frac{1}{n^{2}}$ also converges ($p$-series with
$p=2$).
:::

::: remark
Absolutely convergent series are the "nice" type. They behave much like
finite sums and enjoy all the properties we would expect (including
commutativity of terms). Conditionally convergent series are
**treacherous**: they converge, but rearranging their terms can change
the sum, or even make the series diverge. See
[13.17](#sec:13.17){reference-type="ref+label" reference="sec:13.17"}.
:::

## Proof of Absolute Convergence {#sec:13.16}

*We prove the Absolute Convergence Test
([\[thm:13-13\]](#thm:13-13){reference-type="ref+label"
reference="thm:13-13"}) by separating a series into its positive and
negative parts and using comparison.*

### Positive and negative parts {#positive-and-negative-parts .unnumbered}

*Given a series $\sum a_{n}$, define its *positive part*
$a_{n}^{+}=\max(a_{n},0)$ and its *negative part*
$a_{n}^{-}=\min(a_{n},0)$. Write $\mathrm{P.T.}=\sum a_{n}^{+}$ for the
sum of the positive parts and $\mathrm{N.T.}=\sum a_{n}^{-}$ for the sum
of the negative parts. For finite sums,
$\sum a_{n}=\mathrm{P.T.}+\mathrm{N.T.}$ is obvious. For infinite sums,
this splitting is valid **only when both $\mathrm{P.T.}$ and
$\mathrm{N.T.}$ converge**.*

::: lemma
[]{#lem:13-1 label="lem:13-1"} If $\sum\mathrm{P.T.}$ and
$\sum\mathrm{N.T.}$ both converge, then $\sum a_{n}$ converges and
$\sum a_{n}=\sum\mathrm{P.T.}+\sum\mathrm{N.T.}$
:::

::: proof
*Proof.* Write the $k$-th partial sum as $S_{k}=P_{k}+N_{k}$, where
$P_{k}$ and $N_{k}$ are the partial sums of the positive and negative
parts respectively. This identity holds for finite sums. Since both
$\lim P_{k}$ and $\lim N_{k}$ exist by hypothesis, the limit law gives
$\lim S_{k}=\lim P_{k}+\lim N_{k}$. ◻
:::

::: remark
When $\sum\mathrm{P.T.}=\infty$ and $\sum\mathrm{N.T.}=-\infty$, the
splitting tells us nothing: the original series may still converge or
diverge, depending on the order of the terms. This is exactly what
happens for conditionally convergent series --- see
[13.17](#sec:13.17){reference-type="ref+label" reference="sec:13.17"}.
:::

### Proof of the Absolute Convergence Test {#proof-of-the-absolute-convergence-test .unnumbered}

::: proof
*Proof of [\[thm:13-13\]](#thm:13-13){reference-type="ref+label"
reference="thm:13-13"}.* Assume $\sum\left\lvert a_{n} \right\rvert$
converges.

The positive terms satisfy
$\left\lvert a_{n}^{+} \right\rvert\le\left\lvert a_{n} \right\rvert$,
where $a_{n}^{+}=a_{n}$ if $a_{n}>0$ and $0$ otherwise. By the Basic
Comparison Test, $\sum a_{n}^{+}$ converges.

Similarly,
$\left\lvert a_{n}^{-} \right\rvert\le\left\lvert a_{n} \right\rvert$,
where $a_{n}^{-}=a_{n}$ if $a_{n}<0$ and $0$ otherwise. The series
$\sum\left\lvert a_{n}^{-} \right\rvert$ converges by comparison, so
$\sum a_{n}^{-}$ converges as well (it differs only by a sign).

Both the positive and negative parts converge. By
[\[lem:13-1\]](#lem:13-1){reference-type="ref+label"
reference="lem:13-1"}, $\sum a_{n}=\sum a_{n}^{+}+\sum a_{n}^{-}$
converges. ◻
:::

## Rearrangements of Series {#sec:13.17}

*This is perhaps one of the most surprising results about infinite sums:
rearranging the terms of a convergent series can change its value. We
explore when this happens and why.*

::: example
[]{#ex:13-16 label="ex:13-16"} The alternating harmonic series
$1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots$ converges to $\ln 2$.
Rearranging the same terms --- two positives, then one negative,
repeating --- produces a different convergent series with sum
$\frac{3}{2}\ln 2$. Same terms, different order, different answer.
:::

::: theorem
[]{#thm:13-14 label="thm:13-14"} If $\sum a_{n}$ is **absolutely
convergent**, then every rearrangement of its terms converges to the
same sum.
:::

::: theorem
[]{#thm:13-15 label="thm:13-15"} If $\sum a_{n}$ is **conditionally
convergent**, then for every $L\in\mathbb{R}$ there exists a
rearrangement of the series that converges to $L$. There also exist
rearrangements that diverge to $+\infty$, to $-\infty$, or by
oscillation.
:::

*Three properties of a conditionally convergent series $\sum a_{n}$
explain why this is possible:*

1.  $\lim_{n\to\infty}a_{n}=0$ (true for any convergent series, by the
    necessary condition for convergence,
    [\[thm:13-5\]](#thm:13-5){reference-type="ref+label"
    reference="thm:13-5"}).

2.  The positive terms alone sum to $+\infty$.

3.  The negative terms alone sum to $-\infty$.

::: proof
*Proof sketch of [\[thm:13-15\]](#thm:13-15){reference-type="ref+label"
reference="thm:13-15"}.* Suppose we wish to rearrange the terms so the
sum equals a target value $L$.

1.  Add positive terms (in their original order) until a partial sum
    first exceeds $L$. This is possible because the positive terms sum
    to $\infty$.

2.  Add negative terms until a partial sum first drops below $L$. This
    is possible because the negative terms sum to $-\infty$.

3.  Repeat, alternating between positive and negative terms.

Each time the partial sum overshoots or undershoots $L$, it does so by
at most the term just added. Since $\lim a_{n}=0$, these overshoots
shrink to zero, so the partial sums converge to $L$. ◻
:::

::: remark
This theorem is shocking: the "value" of a conditionally convergent
series depends on the *order* we add its terms. In summary:

- **Absolutely convergent** series are the "good" type --- they behave
  like finite sums.

- **Conditionally convergent** series are treacherous --- they converge,
  but one must not rearrange their terms.
:::

## The Ratio Test {#sec:13.18}

*The Ratio Test determines convergence by examining how fast the terms
of a series shrink. It is especially effective for series involving
factorials and exponentials.*

::: theorem
[]{#thm:13-16 label="thm:13-16"} Let $\sum a_{n}$ be a series with
$a_{n}\neq 0$ for all $n$. Suppose
$$L \;=\; \lim_{n\to\infty}\frac{\left\lvert a_{n+1} \right\rvert}{\left\lvert a_{n} \right\rvert}$$
exists (or equals $\infty$). Then:

1.  If $L<1$, the series is **absolutely convergent**.

2.  If $L>1$ [(]{.upright}including $L=\infty$[)]{.upright}, the series
    is **divergent**.

3.  If $L=1$, the test is **inconclusive**.
:::

### Idea of the proof {#idea-of-the-proof .unnumbered}

***Case $L>1$.** For large $n$,
$\left\lvert a_{n+1} \right\rvert>\left\lvert a_{n} \right\rvert$, so
the terms grow in absolute value and cannot tend to $0$. By the
Divergence Test ([\[thm:13-5\]](#thm:13-5){reference-type="ref+label"
reference="thm:13-5"}), the series diverges.*

***Case $L<1$.** For large $n$,
$\left\lvert a_{n+1} \right\rvert\approx L\cdot\left\lvert a_{n} \right\rvert$,
meaning each term is roughly a fixed fraction $L$ of the previous one.
This mirrors the behaviour of a geometric series $\sum L^{n}$, which
converges because $\left\lvert L \right\rvert<1$. A (rigorous)
comparison with such a geometric series shows
$\sum\left\lvert a_{n} \right\rvert$ converges, so the series is
absolutely convergent.*

::: remark
Try to fill in the formal $\varepsilon$-details of the proof for the
case $L<1$: choose $r$ with $L<r<1$, show
$\left\lvert a_{n+1} \right\rvert\le r\left\lvert a_{n} \right\rvert$
for all large $n$, and compare $\sum\left\lvert a_{n} \right\rvert$ with
a convergent geometric series.
:::

## Ratio Test Examples {#sec:13.19}

*We illustrate the Ratio Test with two examples that highlight its
strengths and its limitations.*

::: example
[]{#ex:13-17 label="ex:13-17"} Determine whether
$\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^{n}\,e^{2n}}{n!\,(n+3)}$
converges.

Set $a_{n}=\frac{(-1)^{n}\,e^{2n}}{n!\,(n+3)}$. Compute $$\begin{align*}
  \frac{\left\lvert a_{n+1} \right\rvert}{\left\lvert a_{n} \right\rvert}
  &= \frac{e^{2(n+1)}}{(n+1)!\,(n+4)}\cdot\frac{n!\,(n+3)}{e^{2n}} \\
  &= \frac{e^{2}}{n+1}\cdot\frac{n+3}{n+4}.
\end{align*}$$ Therefore
$$L = \lim_{n\to\infty}\frac{e^{2}}{n+1}\cdot\frac{n+3}{n+4} = 0.$$
Since $L=0<1$, the Ratio Test tells us the series is **absolutely
convergent**.
:::

::: remark
The Ratio Test is particularly effective when $a_{n}$ involves
factorials and exponentials, because the ratio
$\left\lvert a_{n+1}/a_{n} \right\rvert$ simplifies these terms cleanly.
:::

::: example
[]{#ex:13-18 label="ex:13-18"} Attempt to use the Ratio Test on
$\displaystyle\sum_{n=1}^{\infty}\frac{n+1}{n^{2}+2}$.

Set $a_{n}=\frac{n+1}{n^{2}+2}$. Then
$$\frac{a_{n+1}}{a_{n}} = \frac{(n+2)(n^{2}+2)}{((n+1)^{2}+2)(n+1)}.$$
Both numerator and denominator are degree-$3$ polynomials with leading
coefficient $1$, so $$L = \lim_{n\to\infty}\frac{a_{n+1}}{a_{n}} = 1.$$
The Ratio Test is **inconclusive**.
:::

*For this series the Limit Comparison Test
([\[thm:13-10\]](#thm:13-10){reference-type="ref+label"
reference="thm:13-10"}) is the right tool. Comparing with
$\sum\frac{1}{n}$:*
$$\lim_{n\to\infty}\frac{(n+1)/(n^{2}+2)}{1/n} = \lim_{n\to\infty}\frac{n(n+1)}{n^{2}+2} = 1,$$
so the series diverges (since the harmonic series diverges).

::: remark
In general, whenever $a_{n}$ is a rational function of $n$ (a quotient
of polynomials), the Ratio Test gives $L=1$ and is inconclusive. The
Limit Comparison Test with an appropriate $p$-series is the better
choice. These two tests complement each other: the Ratio Test handles
factorials and exponentials; the Limit Comparison Test handles rational
functions.
:::

# Power Series and Taylor Series

## A Motivating Example {#sec:14.1}

*We begin with a concrete example of a power series before defining the
general notion. This example illustrates the phenomena that arise every
time: a radius of convergence, an interval of convergence, and different
behaviour at the endpoints.*

::: example
[]{#ex:14-1 label="ex:14-1"} Define a function $g$ by
$$g(x) \;=\; \sum_{n=1}^{\infty}\frac{x^{n}}{n\cdot 3^{n}}.$$ The domain
of $g$ is the set of real numbers $x$ for which this series converges,
since convergent means the series adds up to a number.
:::

*Without any calculation, we can already anticipate the shape of the
answer. When $x$ is large the terms $x^{n}$ are large, and we expect
divergence. When $x$ is small, close to zero, the terms are small, and
we expect convergence.*

::: remark
Find the exact domain of $g$. This is an exercise in convergence tests;
begin with the ratio test.
:::

### Applying the ratio test {#applying-the-ratio-test .unnumbered}

Set $a_{n}=\dfrac{x^{n}}{n\cdot 3^{n}}$. Then
$$\frac{\left\lvert a_{n+1} \right\rvert}{\left\lvert a_{n} \right\rvert}
  \;=\; \frac{\left\lvert x \right\rvert^{n+1}}{(n+1)\cdot 3^{n+1}}
        \cdot \frac{n\cdot 3^{n}}{\left\lvert x \right\rvert^{n}}
  \;=\; \frac{\left\lvert x \right\rvert}{3}\cdot\frac{n}{n+1}.$$ Taking
the limit as $n\to\infty$, the factor $\frac{n}{n+1}\to 1$, so
$$\lim_{n\to\infty}\frac{\left\lvert a_{n+1} \right\rvert}{\left\lvert a_{n} \right\rvert}
  \;=\; \frac{\left\lvert x \right\rvert}{3}.$$

- If $\left\lvert x \right\rvert<3$, this limit is less than $1$, and
  the ratio test gives **absolute convergence**.

- If $\left\lvert x \right\rvert>3$, this limit is greater than $1$, and
  the ratio test gives **divergence**.

- If $\left\lvert x \right\rvert=3$, the ratio test is inconclusive; we
  check the endpoints individually.

### Checking the endpoints {#checking-the-endpoints .unnumbered}

At $x=3$: $$\sum_{n=1}^{\infty}\frac{3^{n}}{n\cdot 3^{n}}
  \;=\; \sum_{n=1}^{\infty}\frac{1}{n},$$ the harmonic series, which is
**divergent**.

At $x=-3$: $$\sum_{n=1}^{\infty}\frac{(-3)^{n}}{n\cdot 3^{n}}
  \;=\; \sum_{n=1}^{\infty}\frac{(-1)^{n}}{n},$$ which is
**conditionally convergent** by the alternating series test.

### Conclusion {#conclusion .unnumbered}

The domain of $g$ is the interval $[-3,3)$. We call this interval the
*interval of convergence*, and the number $3$ (half the length of the
interval) the *radius of convergence*. In the next section we will see
that this picture---an interval centred at some point, absolute
convergence in the interior, divergence in the exterior, and
case-by-case behaviour at the endpoints---appears for every power
series.

<figure id="fig:motivating-example-interval" data-latex-placement="ht">

<figcaption>A typical power-series convergence picture: absolute inside,
case-by-case at endpoints.</figcaption>
</figure>

## Definition of Power Series {#sec:14.2}

*Polynomials are nice. Taking derivatives, computing integrals,
evaluating limits---everything is easy with polynomials. The idea behind
power series is to enlarge the family of "nice, easy functions" from
finite polynomials to infinite polynomials. An infinite polynomial is a
series of powers, and that is why it is called a *power series*.*

::: definition
[]{#def:14-1 label="def:14-1"} Let $a\in\mathbb{R}$ and let
$c_{0},c_{1},c_{2},\ldots$ be real numbers. A *power series centred at
$a$* is an expression of the form $$\sum_{n=0}^{\infty}c_{n}(x-a)^{n}
  \;=\; c_{0}+c_{1}(x-a)+c_{2}(x-a)^{2}+\cdots$$ The numbers $c_{n}$ are
called the *coefficients*. When the power series is convergent, it
defines a function of $x$.
:::

::: remark
If the notation is intimidating, think first of the case $a=0$. Then the
power series is simply $c_{0}+c_{1}x+c_{2}x^{2}+\cdots$, which looks
exactly like a polynomial of infinite degree.
:::

*The domain of a function defined by a power series is the set of real
numbers $x$ for which the series converges. One value is always in the
domain: $x=a$, because every term except $c_{0}$ vanishes. In the best
case the domain is all of $\mathbb{R}$; in the worst case it is just the
single point $\{a\}$. In general, some values of $x$ will be in the
domain and some will not.*

### The main theorem {#the-main-theorem .unnumbered}

*The following theorem, stated in three parts, describes the structure
of convergence for every power series and explains why power series are
so powerful.*

::: theorem
[]{#thm:14-1 label="thm:14-1"} Let $\sum_{n=0}^{\infty}c_{n}(x-a)^{n}$
be a power series centred at $a$.

1.  **Interval of convergence.** The domain (the set of values of $x$
    for which the series converges) is always an interval centred
    at $a$. It could be a single point, a bounded interval (open,
    closed, or half-open), or all of $\mathbb{R}$.

2.  **Nature of convergence.** In the *interior* of this interval, the
    series is **absolutely convergent**. In the *exterior*, it is
    **divergent**. At the endpoints, if any, anything may happen: the
    series may converge absolutely, converge conditionally, or diverge,
    independently at each endpoint.

3.  **Polynomial-like behaviour.** In the interior of the interval of
    convergence, a power series can be **treated like a polynomial**.
    That is, power series may be added, multiplied, composed,
    differentiated, and integrated **term by term**, in the same way as
    finite polynomials. In particular, differentiation and integration
    do not change the radius of convergence. For sums and products of
    two power series, the resulting series converges at least on the
    intersection of the two intervals of convergence. Composition
    $f\circ g$ is valid when $g(x)$ lies inside the interval of
    convergence of $f$.
:::

::: definition
[]{#def:14-2 label="def:14-2"} The domain described in part (i) of
[\[thm:14-1\]](#thm:14-1){reference-type="ref+label"
reference="thm:14-1"} is called the *interval of convergence*. Its
radius (half its length) is called the *radius of convergence*, denoted
$R$. We allow $R=0$ (when the domain is $\{a\}$) and $R=\infty$ (when
the domain is $\mathbb{R}$).
:::

*That the domain is always an interval centred at $a$ is intuitively
natural: the farther $x$ is from $a$, the larger
$\left\lvert x-a \right\rvert$ is, and the more likely the series is to
diverge. The closer $x$ is to $a$, the more likely it is to converge.*

<figure id="fig:radius-of-convergence" data-latex-placement="ht">

<figcaption>Radius of convergence for a power series centered at <span
class="math inline"><em>a</em></span>.</figcaption>
</figure>

### Derivatives and antiderivatives {#derivatives-and-antiderivatives .unnumbered}

Part (iii) of [\[thm:14-1\]](#thm:14-1){reference-type="ref+label"
reference="thm:14-1"} has an especially useful consequence for
derivatives and antiderivatives. If
$$f(x) \;=\; \sum_{n=0}^{\infty}c_{n}\,x^{n},$$ then inside the interval
of convergence, $$f'(x) \;=\; \sum_{n=1}^{\infty}n\,c_{n}\,x^{n-1}
  \qquad\text{and}\qquad
  \int_{0}^{x}f(t)\,dt\;=\; \sum_{n=0}^{\infty}\frac{c_{n}}{n+1}\,x^{n+1}.$$
These are obtained by differentiating or integrating term by term,
exactly as one would do for a finite polynomial.

::: remark
The proof of [\[thm:14-1\]](#thm:14-1){reference-type="ref+label"
reference="thm:14-1"} is technical. The key ingredient is that in the
interior of the interval of convergence, the series enjoys *absolute
uniform convergence* on every compact subset. We will not develop that
theory here; instead we focus on stating the theorem and learning to use
it.
:::

### The road ahead {#the-road-ahead-1 .unnumbered}

*Our ultimate goal is twofold. First, try to rewrite as many functions
as possible as power series, using *Taylor series*. Second, once we have
done that, exploit the polynomial-like behaviour of power series to make
calculations---limits, integrals, estimates, differential
equations---**much** easier. This programme will occupy us for the
remainder of this chapter, and it is well worth the effort.*

## Taylor Polynomials {#sec:14.3}

*Our goal is to approximate functions with polynomials. Polynomials are
simple, and they make everything easy. Given a function $f$ and a point
$a$ in its domain, we want to find a polynomial $P$ such that $P(x)$ is
close to $f(x)$ when $x$ is near $a$.*

### The tangent line as a first approximation {#the-tangent-line-as-a-first-approximation .unnumbered}

*We already know one example of such an approximation: the tangent line.
Of all lines through the point $(a,f(a))$, the tangent line is the one
whose graph stays closest to the graph of the function near $a$. But
what, precisely, does "closest" mean? And how can we construct even
better polynomial approximations?*

### The remainder {#the-remainder .unnumbered}

Define the *remainder* (or *error*) as the difference between the
function and the polynomial: $$R(x) \;=\; f(x)-P(x).$$ We want this
error to be small near $a$. Saying $R(a)=0$ is too weak: many lines pass
through $(a,f(a))$, and most are poor approximations. Saying
$\lim_{x\to a}R(x)=0$ is still not enough, because every line through
$(a,f(a))$ satisfies this.

*What makes the tangent line special is that its remainder approaches
zero **fast**. The remainder for every other line also tends to zero,
but the tangent line's remainder does so faster than any other line's.
This is the key idea: we need the error to approach zero *fast*.*

### A scale for "fast" {#a-scale-for-fast .unnumbered}

*To measure how fast a function approaches zero, we need a scale. A
natural one is provided by powers of $(x-a)$.*

For simplicity, consider first the case $a=0$. As $x\to 0$, every
positive power $x^{n}$ approaches $0$, but the larger the exponent $n$,
the faster the approach. This gives us our yardstick: we compare the
remainder with powers of $x$.

::: definition
[]{#def:14-3 label="def:14-3"} Let $f$ and $g$ be continuous at $a$, and
let $n\in\mathbb{N}$. We say that $g$ is an *approximation for $f$ near
$a$ of order $n$* when
$$\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^{n}} \;=\; 0.$$ Note that for
$n\ge 1$, this condition forces $f(a)=g(a)$ (otherwise the limit would
not be finite).
:::

*The limit is an indeterminate form $\frac{0}{0}$: the numerator
$f(x)-g(x)$ tends to $0$ (because both are continuous at $a$ and
approximate each other there), and the denominator $(x-a)^{n}$ tends to
$0$. For this indeterminate form to resolve to $0$, the numerator must
approach $0$ faster than the denominator. That is precisely the content
of the definition.*

::: definition
[]{#def:14-4 label="def:14-4"} Let $a\in\mathbb{R}$, let $f$ be
continuous at and near $a$, and let $n\in\mathbb{N}$. The *$n$-th Taylor
polynomial for $f$ at $a$* is a polynomial $P_{n}$ of degree at most $n$
that is an approximation for $f$ near $a$ of order $n$. That is,
$$\lim_{x\to a}\frac{f(x)-P_{n}(x)}{(x-a)^{n}} \;=\; 0.$$
:::

::: remark
The requirement that $\deg P_{n}\le n$ deserves a comment. One can
always find polynomials of higher degree with the same approximation
property, but polynomials of lower degree are simpler, so we prefer
them. Later we will show that, provided $f$ has enough derivatives, such
a polynomial always exists and is unique.
:::

::: remark
Check that the first Taylor polynomial $P_{1}$ is the tangent line to
$f$ at $a$.
:::

*This definition explains where Taylor polynomials come from and why
they are useful. However, it is not directly helpful for computations.
Based on it alone, we have no recipe for actually *constructing*
$P_{n}$. The next section remedies this.*

## Taylor Polynomials via Derivatives {#sec:14.4}

*We now translate the definition of Taylor polynomials into a second,
equivalent form that is more concrete and better suited for
computations.*

### Smoothness notation {#smoothness-notation .unnumbered}

::: definition
[]{#def:14-5 label="def:14-5"} A function is called $C^{0}$ when it is
continuous. It is $C^{1}$ when its first derivative exists and is
continuous, $C^{2}$ when the first two derivatives exist and are
continuous, and in general $C^{n}$ when all derivatives up to and
including order $n$ exist and are continuous. A function is $C^{\infty}$
when **all** of its derivatives exist and are continuous.
:::

::: remark
We will encounter many results that require different numbers of
derivatives. The $C^{n}$ notation makes statements shorter.
:::

### From the limit condition to matching derivatives {#from-the-limit-condition-to-matching-derivatives .unnumbered}

*Recall the original definition: $g$ is an approximation for $f$ near
$a$ of order $n$ when*
$$L \;=\; \lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^{n}} \;=\; 0.$$ *We now
investigate, under the assumption that $f$ and $g$ are $C^{n}$, what
conditions on the derivatives of $f$ and $g$ are equivalent to $L=0$.*

Suppose first that $f(a)\neq g(a)$. Then the numerator has a nonzero
limit while the denominator tends to $0$, so $L$ does not exist as a
finite number. Hence we need $f(a)=g(a)$.

With $f(a)=g(a)$ we have the indeterminate form $\frac{0}{0}$. Apply
L'Hôpital's Rule:
$$L \;=\; \lim_{x\to a}\frac{f'(x)-g'(x)}{n(x-a)^{n-1}}.$$ The same
argument now forces $f'(a)=g'(a)$, and we apply L'Hôpital's Rule again.
Repeating this process $n$ times, we arrive at
$$L \;=\; \lim_{x\to a}\frac{f^{(n)}(x)-g^{(n)}(x)}{n!}
  \;=\; \frac{f^{(n)}(a)-g^{(n)}(a)}{n!},$$ where the last step uses the
continuity of the $n$-th derivatives.

::: theorem
[]{#thm:14-2 label="thm:14-2"} Let $f$ and $g$ be $C^{n}$ functions at a
point $a$. Then the following are equivalent:

1.  $\displaystyle\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^{n}}=0$. (The
    function $g$ approximates $f$ near $a$ of order $n$.)

2.  $f^{(k)}(a) = g^{(k)}(a)$ for every $k=0,1,2,\ldots,n$.
:::

*In words: $g$ is a good approximation for $f$ near $a$ if and only if
$f$ and $g$ have the same first few derivatives at $a$. How good the
approximation is depends on how many derivatives agree.*

### Second definition of Taylor polynomial {#second-definition-of-taylor-polynomial .unnumbered}

We can now rewrite the definition of Taylor polynomial using
condition (ii) of [\[thm:14-2\]](#thm:14-2){reference-type="ref+label"
reference="thm:14-2"}.

::: definition
[]{#def:14-6 label="def:14-6"} Let $a\in\mathbb{R}$, $n\in\mathbb{N}$,
and let $f$ be a $C^{n}$ function at $a$. The *$n$-th Taylor polynomial
for $f$ at $a$* is the polynomial $P_{n}$ of degree at most $n$
satisfying
$$P_{n}^{(k)}(a) = f^{(k)}(a) \qquad\text{for each } k=0,1,\ldots,n.$$
:::

::: remark
This is not a completely new idea. The first Taylor polynomial is a
polynomial of degree at most $1$ whose value at $a$ is $f(a)$ and whose
derivative at $a$ is $f'(a)$. That is exactly the tangent line.
:::

*This definition is more useful for computations than the first: we are
simply specifying the value of the polynomial and its first $n$
derivatives at $a$. But we should always keep the first definition
([\[def:14-4\]](#def:14-4){reference-type="ref+label"
reference="def:14-4"}) in mind---it tells us *why* Taylor polynomials
are good approximations. In the next section, we take this one step
further, providing an explicit formula for the coefficients.*

## The Explicit Formula and Taylor Series {#sec:14.5}

*We have defined Taylor polynomials in two equivalent ways: first via
the approximation property
([\[def:14-4\]](#def:14-4){reference-type="ref+label"
reference="def:14-4"}), then via matching derivatives
([\[def:14-6\]](#def:14-6){reference-type="ref+label"
reference="def:14-6"}). Both are useful for understanding, but neither
gives us a quick recipe for computing the coefficients. Our goal now is
to simplify the definition even further and obtain an explicit formula.*

### The case $a=0$ {#the-case-a0 .unnumbered}

A polynomial of degree at most $n$ can be written as
$$P_{n}(x) \;=\; c_{0}+c_{1}\,x+c_{2}\,x^{2}+\cdots+c_{n}\,x^{n}.$$ We
impose the matching conditions from
[\[def:14-6\]](#def:14-6){reference-type="ref+label"
reference="def:14-6"}: $P_{n}^{(k)}(0)=f^{(k)}(0)$ for $k=0,1,\ldots,n$.

::: remark
Differentiate $P_{n}$ repeatedly and evaluate at $0$. Each condition
determines exactly one coefficient. Try to find the formula before
reading on.
:::

Differentiating $k$ times and setting $x=0$ kills every term except the
one of degree $k$: $$P_{n}^{(k)}(0) \;=\; k!\,c_{k}.$$ The matching
condition $P_{n}^{(k)}(0)=f^{(k)}(0)$ therefore forces
$$c_{k} \;=\; \frac{f^{(k)}(0)}{k!}.$$

### The general case {#the-general-case .unnumbered}

For an arbitrary centre $a$, write the polynomial in powers of $(x-a)$
instead of powers of $x$:
$$P_{n}(x) \;=\; c_{0}+c_{1}(x-a)+c_{2}(x-a)^{2}+\cdots+c_{n}(x-a)^{n}.$$
*This is still a generic polynomial of degree at most $n$; we have
simply changed basis from powers of $x$ to powers of $(x-a)$. The
advantage is that the $k$-th derivative evaluated at $a$ depends only on
the coefficient $c_{k}$.*

::: remark
Impose the conditions $P_{n}^{(k)}(a)=f^{(k)}(a)$ for $k=0,1,\ldots,n$
and find the coefficients. Take as much time as you need.
:::

The same calculation gives $P_{n}^{(k)}(a)=k!\,c_{k}$, and the matching
condition yields $$c_{k} \;=\; \frac{f^{(k)}(a)}{k!}.$$

### Third definition of Taylor polynomial {#third-definition-of-taylor-polynomial .unnumbered}

::: definition
[]{#def:14-7 label="def:14-7"} Let $f$ be a $C^{n}$ function at $a$. The
$n$-th Taylor polynomial for $f$ at $a$ is
$$P_{n}(x) \;=\; \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}\,(x-a)^{k}.$$
:::

*Some textbooks take this formula as the starting point. We chose to
begin with the more abstract approximation definition
([\[def:14-4\]](#def:14-4){reference-type="ref+label"
reference="def:14-4"}) and slowly derive the formula from it, because
the abstract version explains *why* Taylor polynomials are good
approximations. It is best to understand all three equivalent
viewpoints.*

::: remark
By construction the polynomial has degree at most $n$: the terms up to
degree $n$ suffice to match the first $n$ derivatives. Higher-degree
terms could be added without affecting those derivatives, but they are
unnecessary. Since the formula pins down every coefficient, the $n$-th
Taylor polynomial of a given function at a given point is **unique**.
This was not obvious from the earlier definitions, where it seemed
possible that two different polynomials might satisfy the same
conditions.
:::

### Graphical intuition {#graphical-intuition .unnumbered}

*Consider a function and its Taylor polynomials at $a=0$. The first
Taylor polynomial is the tangent line---a reasonable approximation very
close to $0$. The second Taylor polynomial is better, and the third
better still. The sixth Taylor polynomial produces a fantastic
approximation, not just near $0$, but on a surprisingly large interval
around it. The higher the order, the better the approximation.*

<figure id="fig:taylor-approx-exp" data-latex-placement="ht">

<figcaption>Taylor polynomial approximations to <span
class="math inline"><em>e</em><sup><em>x</em></sup></span> near <span
class="math inline">0</span>.</figcaption>
</figure>

### The Taylor series {#the-taylor-series .unnumbered}

*This raises a natural question: what happens if we use a "polynomial of
infinite degree"? Such an object is not a polynomial---it is a power
series---but if every finite truncation is a good approximation, perhaps
the infinite version is an **exact** representation of the function.*

::: definition
[]{#def:14-8 label="def:14-8"} Let $f$ be a $C^{\infty}$ function at
$a$. The *Taylor series for $f$ at $a$* is the power series
$$\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}\,(x-a)^{k}.$$ This is the
same formula as in [\[def:14-7\]](#def:14-7){reference-type="ref+label"
reference="def:14-7"}, but with the sum extended to all degrees. All the
derivatives of the power series at $a$ agree with the corresponding
derivatives of $f$.
:::

*Like any power series, the Taylor series makes sense only where it
converges. In the ideal case it converges to $f(x)$ on some interval
around $a$.*

::: remark
A function that equals its Taylor series on an interval around $a$ is
called *analytic*. Not every $C^{\infty}$ function is analytic: there
exist $C^{\infty}$ functions whose Taylor series converges but does
**not** equal the function. However, most of the common functions we
encounter are analytic. Whether a given function equals its Taylor
series is a deeper question, addressed in
[14.7](#sec:14.7){reference-type="ref+label" reference="sec:14.7"}.
:::

## Computing Maclaurin Series {#sec:14.6}

*In the previous sections we derived the explicit formula for Taylor
polynomials and the Taylor series. In this section we illustrate them
with examples.*

::: definition
[]{#def:14-9 label="def:14-9"} When the Taylor series is centred at
$a=0$, it is called a *Maclaurin series*. That is, the Maclaurin series
for $f$ is $$\sum_{k=0}^{\infty}\frac{f^{(k)}(0)}{k!}\,x^{k}.$$
:::

*We say that a function is *analytic* when it is equal to its Taylor
series (see [14.7](#sec:14.7){reference-type="ref+label"
reference="sec:14.7"} for the precise definition). For analytic
functions, the Taylor series is not merely an approximation---it **is**
the function. Spoiler: most common functions, including exponentials and
trigonometric functions, are analytic. It will take some work to prove
this. For now, we focus on *finding* the Maclaurin series, without yet
proving equality.*

::: example
[]{#ex:14-2 label="ex:14-2"} Define $f(x)=e^{x}$. Since the derivative
of $e^{x}$ is itself, every derivative equals $e^{x}$, and so
$$f^{(k)}(0) = e^{0} = 1 \qquad\text{for all } k\ge 0.$$ The Maclaurin
series is therefore $$e^{x} \;=\; \sum_{k=0}^{\infty}\frac{x^{k}}{k!}
  \;=\; 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \cdots$$ This
equality holds for **all** $x\in\mathbb{R}$. (The proof of analyticity
is given in [14.8](#sec:14.8){reference-type="ref+label"
reference="sec:14.8"}.)
:::

::: remark
If we want the Taylor series for $e^{x}$ centred at a point $c\neq 0$,
one convenient method is to substitute $u=x-c$. Then
$e^{x}=e^{c+u}=e^{c}\cdot e^{u}$, and we can use the Maclaurin series
for $e^{u}$:
$$e^{x} \;=\; e^{c}\sum_{k=0}^{\infty}\frac{(x-c)^{k}}{k!}.$$ This
substitution trick works for many functions, and it is the reason we
most often work with Maclaurin series.
:::

::: example
[]{#ex:14-3 label="ex:14-3"} The derivatives of $\sin x$ repeat in a
cycle of length four:
$$\sin x,\;\cos x,\;-\sin x,\;-\cos x,\;\sin x,\;\ldots$$ Evaluating at
$x=0$ gives the pattern $0,\,1,\,0,\,-1,\,0,\,1,\,0,\,-1,\,\ldots$ . All
even-order derivatives vanish, and the odd-order derivatives alternate
between $1$ and $-1$. Therefore
$$\sin x \;=\; \sum_{m=0}^{\infty}\frac{(-1)^{m}}{(2m+1)!}\,x^{2m+1}
  \;=\; x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \cdots$$
This holds for all $x\in\mathbb{R}$.
:::

::: remark
Repeat the calculation for $\cos x$. You should obtain
$$\cos x \;=\; \sum_{m=0}^{\infty}\frac{(-1)^{m}}{(2m)!}\,x^{2m}
  \;=\; 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - \frac{x^{6}}{6!} + \cdots$$
valid for all $x\in\mathbb{R}$.
:::

### The four fundamental Maclaurin series {#the-four-fundamental-maclaurin-series .unnumbered}

To summarise, we now have four Maclaurin series that will serve as
building blocks: $$\begin{align*}
  e^{x}           &= \sum_{k=0}^{\infty}\frac{x^{k}}{k!},            & \left\lvert x \right\rvert&<\infty, \\[4pt]
  \sin x          &= \sum_{m=0}^{\infty}\frac{(-1)^{m}}{(2m+1)!}\,x^{2m+1}, & \left\lvert x \right\rvert&<\infty, \\[4pt]
  \cos x          &= \sum_{m=0}^{\infty}\frac{(-1)^{m}}{(2m)!}\,x^{2m},     & \left\lvert x \right\rvert&<\infty, \\[4pt]
  \frac{1}{1-x}   &= \sum_{n=0}^{\infty}x^{n},                        & \left\lvert x \right\rvert&<1.
\end{align*}$$ *We will use all kinds of manipulations to derive
Maclaurin series for new functions from these four.*

## Analytic Functions and Remainders {#sec:14.7}

*Fair warning: this section is packed with theorems, some quite
technical. They will make the rest of this chapter considerably easier,
so they are worth the effort.*

### Precise definition of analytic {#precise-definition-of-analytic .unnumbered}

*So far we have been casually saying that a function is analytic when it
equals its Taylor series. But we need to specify *which* Taylor series,
and on which domain.*

::: definition
[]{#def:14-10 label="def:14-10"} Let $f$ be a $C^{\infty}$ function on
an open interval $I$, and let $a\in I$. Denote by $S_{a}$ the Taylor
series of $f$ centred at $a$. We say $f$ is *analytic at $a$* when
$f(x)=S_{a}(x)$ for all $x$ in some open interval centred at $a$. We say
$f$ is *analytic* (without specifying a point) when it is analytic at
every point of its domain.
:::

### Properties of analytic functions {#properties-of-analytic-functions .unnumbered}

::: theorem
[]{#thm:14-3 label="thm:14-3"} The following hold:

1.  Polynomials are analytic.

2.  Sums, products, quotients (where the denominator is nonzero), and
    compositions of analytic functions are analytic.

3.  Derivatives and antiderivatives of analytic functions are analytic.

Moreover, all operations listed in [(ii)]{.upright} and
[(iii)]{.upright} can be performed on the corresponding Taylor series
term by term, exactly as one would do with polynomials. The Taylor
series of a function at a point is unique.
:::

::: remark
Because of [\[thm:14-3\]](#thm:14-3){reference-type="ref+label"
reference="thm:14-3"}, our strategy is very efficient. We only need to
prove that the exponential and the sine function are analytic. All other
elementary functions can then be obtained from these two, from
polynomials, and from the operations listed above.
:::

### Remainders and analyticity {#remainders-and-analyticity .unnumbered}

*Let us make a plan for proving a function is analytic.*

Let $f$ be $C^{\infty}$ on an open interval, and fix $a$ in that
interval. We can always write $$f(x) \;=\; P_{n}(x) + R_{n}(x),$$ where
$P_{n}$ is the $n$-th Taylor polynomial and $R_{n}=f-P_{n}$ is the
$n$-th remainder. The Taylor series is
$$S_{a}(x) \;=\; \lim_{n\to\infty}P_{n}(x),$$ since the Taylor
polynomials are the partial sums of the Taylor series. Therefore
$$f(x)=S_{a}(x) \quad\Longleftrightarrow\quad \lim_{n\to\infty}R_{n}(x)=0.$$

::: remark
There are **two different limits** involving $R_{n}$ that must not be
confused.

- From the *definition* of Taylor polynomials, we know that for a fixed
  $n$, the remainder $R_{n}(x)\to 0$ as $x\to a$ (and it does so fast).

- To prove a function is *analytic*, we need the remainder
  $R_{n}(x)\to 0$ as $n\to\infty$, for a fixed value of $x$.

These are different limits, and the first does not imply the second.
:::

### Lagrange's Remainder Theorem {#lagranges-remainder-theorem .unnumbered}

*To show $R_{n}\to 0$ as $n\to\infty$, we need a concrete formula for
$R_{n}$. This is provided by the remainder theorems---a family of
results that give explicit expressions for the remainder. There are
several versions (Lagrange, Cauchy, integral form); all are proved using
the Mean Value Theorem and are interchangeable for our purposes.*

::: theorem
[]{#thm:14-4 label="thm:14-4"} Let $I$ be an open interval, $a\in I$,
$n\in\mathbb{N}$, and let $f$ be $C^{n+1}$ on $I$. Write
$$f(x) = P_{n}(x) + R_{n}(x),$$ where $P_{n}$ is the $n$-th Taylor
polynomial for $f$ at $a$. Then for every $x\in I$, there exists a
number $\xi$ between $a$ and $x$ such that
$$R_{n}(x) \;=\; \frac{f^{(n+1)}(\xi)}{(n+1)!}\,(x-a)^{n+1}.$$
:::

::: remark
This is reminiscent of the Mean Value Theorem: under certain hypotheses,
there exists some intermediate point $\xi$ satisfying an equation. The
exact value of $\xi$ is unknown, but the formula is powerful
nonetheless, because it lets us **bound** $R_{n}$.
:::

*Lagrange's Remainder Theorem has two main applications. First, we can
use it to prove that a function is analytic, by showing $R_{n}\to 0$ as
$n\to\infty$ (see [14.8](#sec:14.8){reference-type="ref+label"
reference="sec:14.8"}). Second, we can use it to **estimate** the value
of a complicated function with a Taylor polynomial and bound the error
(see [14.11](#sec:14.11){reference-type="ref+label"
reference="sec:14.11"}).*

<figure id="fig:taylor-remainder-band" data-latex-placement="ht">

<figcaption>A qualitative "error band" around a Taylor
approximation.</figcaption>
</figure>

## Analyticity of the Exponential {#sec:14.8}

*We now prove that the exponential function equals its Maclaurin series.
This is a model example of how to use Lagrange's Remainder Theorem to
establish analyticity.*

::: theorem
[]{#thm:14-5 label="thm:14-5"} For every $x\in\mathbb{R}$,
$$e^{x} \;=\; \sum_{k=0}^{\infty}\frac{x^{k}}{k!}.$$
:::

::: proof
*Proof.* Fix $x\in\mathbb{R}$. Write $f(t)=e^{t}$. Since every
derivative of $f$ equals $e^{t}$, the $n$-th Taylor polynomial at $a=0$
is $$P_{n}(x) \;=\; \sum_{k=0}^{n}\frac{x^{k}}{k!},$$ and
$f(x)=P_{n}(x)+R_{n}(x)$. We must show $R_{n}(x)\to 0$ as $n\to\infty$.

By [\[thm:14-4\]](#thm:14-4){reference-type="ref+label"
reference="thm:14-4"}, there exists $\xi$ between $0$ and $x$ with
$$R_{n}(x) \;=\; \frac{e^{\xi}}{(n+1)!}\,x^{n+1}.$$

**Case $x>0$.** Since $0<\xi<x$, the exponential is increasing, so
$e^{\xi}\le e^{x}$. Therefore
$$\left\lvert R_{n}(x) \right\rvert \;\le\; e^{x}\cdot\frac{\left\lvert x \right\rvert^{n+1}}{(n+1)!}.$$

Since $\dfrac{\left\lvert x \right\rvert^{n+1}}{(n+1)!}\to 0$ as
$n\to\infty$ (factorial growth dominates any fixed power), the Squeeze
Theorem gives $R_{n}(x)\to 0$.

**Case $x<0$.** Since $x<\xi<0$, we have $e^{\xi}\le e^{0}=1$. The same
argument applies with the bound
$\left\lvert R_{n}(x) \right\rvert\le\dfrac{\left\lvert x \right\rvert^{n+1}}{(n+1)!}\to 0$.

**Case $x=0$.** Trivially $R_{n}(0)=0$ for all $n$. ◻
:::

::: remark
Use a very similar argument to prove that $\sin x$ is analytic:
$$\sin x \;=\; \sum_{m=0}^{\infty}\frac{(-1)^{m}}{(2m+1)!}\,x^{2m+1}
  \qquad\text{for all } x\in\mathbb{R}.$$ The key observation is that
every derivative of $\sin$ is bounded in absolute value by $1$, so
$\left\lvert f^{(n+1)}(\xi) \right\rvert\le 1$ and
$\left\lvert R_{n}(x) \right\rvert\le\dfrac{\left\lvert x \right\rvert^{n+1}}{(n+1)!}\to 0$.
:::

## Constructing New Power Series {#sec:14.9}

*We always have the slow method: compute all the derivatives, plug into
the Taylor series formula, then prove analyticity with the Remainder
Theorem. But there is a better way. We already have four functions
written as power series (exponential, sine, cosine, geometric). Using
the fact that power series can be manipulated like polynomials
([\[thm:14-1\]](#thm:14-1){reference-type="ref+label"
reference="thm:14-1"}), we can derive power series for new functions
quickly.*

::: remark
Before reading the solutions below, try to write each of the following
functions as a power series centred at $0$: $e^{-x}$,
$x^{3}\sin(x^{2})$, $\dfrac{1}{x}$ centred at $3$.
:::

::: example
[]{#ex:14-6 label="ex:14-6"} Start from the known expansion
$e^{x}=\sum_{k=0}^{\infty}\frac{x^{k}}{k!}$, valid for all $x$. Replace
$x$ by $-x$: $$e^{-x}
  \;=\; \sum_{k=0}^{\infty}\frac{(-x)^{k}}{k!}
  \;=\; \sum_{k=0}^{\infty}\frac{(-1)^{k}}{k!}\,x^{k}
  \;=\; 1 - x + \frac{x^{2}}{2!} - \frac{x^{3}}{3!} + \cdots$$ Valid for
all $x\in\mathbb{R}$.
:::

::: example
[]{#ex:14-7 label="ex:14-7"} Begin with
$\sin x = \sum_{m=0}^{\infty}\frac{(-1)^{m}}{(2m+1)!}\,x^{2m+1}$, valid
for all $x$. Replace $x$ by $x^{2}$: $$\sin(x^{2})
  \;=\; \sum_{m=0}^{\infty}\frac{(-1)^{m}}{(2m+1)!}\,x^{4m+2}.$$
Multiply term by term by $x^{3}$: $$x^{3}\sin(x^{2})
  \;=\; \sum_{m=0}^{\infty}\frac{(-1)^{m}}{(2m+1)!}\,x^{4m+5}
  \;=\; x^{5} - \frac{x^{9}}{3!} + \frac{x^{13}}{5!} - \cdots$$ Valid
for all $x\in\mathbb{R}$.
:::

::: example
[]{#ex:14-8 label="ex:14-8"} Since the centre is $a=3$, set $u=x-3$ so
that powers of $u$ appear naturally. Then $x=u+3$, and
$$\frac{1}{x} = \frac{1}{u+3}
  = \frac{1}{3}\cdot\frac{1}{1+u/3}
  = \frac{1}{3}\cdot\frac{1}{1-(-u/3)}.$$ Apply the geometric series
with variable $-u/3$: $$\frac{1}{x}
  = \frac{1}{3}\sum_{n=0}^{\infty}\!\Bigl(-\frac{u}{3}\Bigr)^{\!n}
  = \sum_{n=0}^{\infty}\frac{(-1)^{n}}{3^{n+1}}\,(x-3)^{n}.$$ This is
valid when $\left\lvert -u/3 \right\rvert<1$,
i.e. $\left\lvert x-3 \right\rvert<3$, i.e. $x\in(0,6)$.
:::

## The Logarithm Series {#sec:14.10}

*The domain of $\ln x$ is only the positive reals. In particular, $\ln$
is not even defined at $0$, so we cannot write a Maclaurin series for
$\ln x$ directly. Instead, we shift the function and consider
$\ln(1+x)$, whose domain includes $0$.*

### Strategy {#strategy .unnumbered}

*The function $\ln(1+x)$ does not closely resemble any of our four
fundamental series, but its derivative does. Since*
$$\frac{d}{dx}\ln(1+x) = \frac{1}{1+x},$$ *and the right-hand side is
closely related to the geometric series, we will write the derivative as
a power series and then integrate to recover $\ln(1+x)$.*

::: example
[]{#ex:14-9 label="ex:14-9"} We have $$\frac{1}{1+x} = \frac{1}{1-(-x)}
  = \sum_{n=0}^{\infty}(-x)^{n}
  = \sum_{n=0}^{\infty}(-1)^{n}\,x^{n},
  \qquad \left\lvert x \right\rvert<1.$$ Integrate term by term (valid
inside the interval of convergence): $$\ln(1+x)
  = \int_{0}^{x}\frac{1}{1+t}\,dt
  = \sum_{n=0}^{\infty}\frac{(-1)^{n}}{n+1}\,x^{n+1}
  = \sum_{m=1}^{\infty}\frac{(-1)^{m+1}}{m}\,x^{m},$$ where the second
form uses the substitution $m=n+1$. Writing out the first few terms:
$$\ln(1+x) \;=\; x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \frac{x^{4}}{4} + \cdots, \qquad \left\lvert x \right\rvert<1.$$
:::

::: remark
When we differentiate or integrate a power series term by term, the
**radius** of convergence does not change. The geometric series has
radius $1$, so the series for $\ln(1+x)$ also has radius $1$. The
behaviour at the endpoints, however, may change; in fact the series for
$\ln(1+x)$ converges at $x=1$ (it gives $\ln 2$ as the alternating
harmonic series) but not at $x=-1$.
:::

<figure id="fig:log-series" data-latex-placement="ht">

<figcaption>Approximating <span
class="math inline">ln (1 + <em>x</em>)</span> by truncating its power
series.</figcaption>
</figure>

::: remark
Use a very similar derivation to write $\arctan x$ as a Maclaurin
series. Start with the fact that
$\dfrac{d}{dx}\arctan x = \dfrac{1}{1+x^{2}}$.
:::

## Estimation via Taylor Polynomials {#sec:14.11}

*One of the primary uses of Taylor series is to estimate complicated
functions. Taylor polynomials were designed precisely for this purpose:
they are good approximations. In this section we illustrate the method
with a concrete example.*

::: example
[]{#ex:14-10 label="ex:14-10"} We wish to estimate $\sqrt{e}=e^{1/2}$
with an error smaller than $0.001$.

Since $e^{x}$ equals its Maclaurin series, we have $$e^{1/2}
  = \sum_{k=0}^{\infty}\frac{(1/2)^{k}}{k!}
  = P_{n}({\textstyle\frac{1}{2}}) + R_{n}({\textstyle\frac{1}{2}}),$$
where $P_{n}$ is the $n$-th Taylor polynomial and $R_{n}$ is the
remainder. We need to choose $n$ large enough that
$\left\lvert R_{n}(1/2) \right\rvert<0.001$.

**Bounding the remainder.** By
[\[thm:14-4\]](#thm:14-4){reference-type="ref+label"
reference="thm:14-4"}, there exists $\xi\in(0,\frac{1}{2})$ with
$$R_{n}({\textstyle\frac{1}{2}})
  = \frac{e^{\xi}}{(n+1)!}\Bigl(\frac{1}{2}\Bigr)^{\!n+1}.$$ Since
$e^{\xi}\le e^{1/2}<2$ (because $e<3$, so $\sqrt{e}<\sqrt{3}<2$), we
obtain $$\left\lvert R_{n}({\textstyle\frac{1}{2}}) \right\rvert
  < \frac{2}{2^{n+1}\,(n+1)!}
  = \frac{1}{2^{n}\,(n+1)!}.$$ We need $2^{n}(n+1)!>1000$. Checking:
$2^{4}\cdot 5!=16\cdot 120=1920>1000$. So $n=4$ suffices.

**Computing the estimate.** $$P_{4}({\textstyle\frac{1}{2}})
  = 1 + \frac{1}{2} + \frac{(1/2)^{2}}{2!} + \frac{(1/2)^{3}}{3!} + \frac{(1/2)^{4}}{4!}
  = \frac{211}{128}
  \approx 1.64844.$$ The exact value begins
$\sqrt{e}\approx 1.64872\ldots$ , confirming that our estimate is
correct to three decimal places.
:::

::: remark
This is precisely the process a calculator or computer uses to evaluate
$e^{x}$: replace the function with its Taylor polynomial, compute the
polynomial (a finite sum), and bound the error using the Remainder
Theorem.
:::

## Integration via Power Series {#sec:14.12}

*Power series are, in a sense, polynomials, and nothing is easier to
integrate than a polynomial. In this section we illustrate how Taylor
series can compute integrals that are impossible or impractical by other
means.*

::: example
[]{#ex:14-11 label="ex:14-11"} Compute
$\displaystyle\int_{0}^{3}e^{-x^{2}}\,dx$.

It can be shown (using differential Galois theory) that $e^{-x^{2}}$ has
no antiderivative expressible in terms of elementary functions. Power
series offer a way around this obstacle.

Start with $e^{x}=\sum_{k=0}^{\infty}\frac{x^{k}}{k!}$ and replace $x$
by $-x^{2}$: $$e^{-x^{2}}
  = \sum_{k=0}^{\infty}\frac{(-1)^{k}}{k!}\,x^{2k}.$$ Integrate term by
term: $$\int_{0}^{3}e^{-x^{2}}\,dx
  = \sum_{k=0}^{\infty}\frac{(-1)^{k}}{k!}\cdot\frac{3^{2k+1}}{2k+1}
  = \sum_{k=0}^{\infty}\frac{(-1)^{k}\cdot 3^{2k+1}}{k!\,(2k+1)}.$$ This
is a convergent series (the factorial in the denominator ensures that
the terms eventually decrease rapidly), and truncating it to a partial
sum yields an estimate to any desired accuracy.
:::

::: example
[]{#ex:14-12 label="ex:14-12"} Find
$\displaystyle\int\frac{1}{1-x^{8}}\,dx$.

One could factor $1-x^{8}$ and decompose into partial fractions, but the
result is extremely complicated. Instead, use the geometric series with
variable $x^{8}$:
$$\frac{1}{1-x^{8}} = \sum_{n=0}^{\infty}x^{8n}, \qquad \left\lvert x \right\rvert<1.$$
Integrate term by term: $$\int\frac{1}{1-x^{8}}\,dx
  = \sum_{n=0}^{\infty}\frac{x^{8n+1}}{8n+1} + C, \qquad \left\lvert x \right\rvert<1.$$
This expression is far shorter, far cleaner, and far more useful than
the partial-fractions answer.
:::

::: remark
The moral: using power series to compute integrals is often
preferable---sometimes because no elementary antiderivative exists, and
sometimes because the elementary antiderivative, while it exists in
principle, is too complicated to be useful.
:::

## Limits via Power Series {#sec:14.13}

*Power series provide an extremely efficient method for computing limits
of indeterminate forms. The strategy is simple: expand numerator and
denominator as power series, and keep only the first nonzero term.*

### The key observation {#the-key-observation .unnumbered}

Consider $\displaystyle\lim_{x\to 0}\frac{2x^{3}+7x^{5}}{5x^{3}-x^{4}}$.
Factor $x^{3}$ from both to get $\dfrac{2+7x^{2}}{5-x}\to\dfrac{2}{5}$.
The only terms that matter are those with the **smallest exponent**. The
same idea applies when the numerator and denominator are power series
instead of polynomials.

::: example
[]{#ex:14-13 label="ex:14-13"} Compute
$\displaystyle\lim_{x\to 0}\frac{\sin x - x}{x^{3}}$.

Replace $\sin x$ by its Maclaurin series: $$\sin x - x
  = \Bigl(x - \frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\cdots\Bigr) - x
  = -\frac{x^{3}}{6} + \frac{x^{5}}{120} - \cdots$$ The first nonzero
term is $-\frac{x^{3}}{6}$. Therefore
$$\lim_{x\to 0}\frac{\sin x - x}{x^{3}}
  = \lim_{x\to 0}\frac{-\frac{x^{3}}{6}+\text{h.o.t.}}{x^{3}}
  = -\frac{1}{6}.$$
:::

::: example
[]{#ex:14-14 label="ex:14-14"} Compute
$\displaystyle\lim_{x\to 0}\frac{3x^{2}-e^{x^{2}}+\cos 2x}{x\sin x - \ln(1+x^{2})}$.

This is an indeterminate form of type $\frac{0}{0}$. Using L'Hôpital's
Rule would require four differentiations of a messy expression. Power
series are much faster.

**Numerator.** Expand each piece: $$\begin{align*}
  3x^{2} &= 3x^{2}, \\
  e^{x^{2}} &= 1 + x^{2} + \frac{x^{4}}{2!} + \cdots, \\
  \cos 2x &= 1 - \frac{(2x)^{2}}{2!} + \frac{(2x)^{4}}{4!} - \cdots
  = 1 - 2x^{2} + \frac{2}{3}\,x^{4} - \cdots
\end{align*}$$ Combine: $$3x^{2} - e^{x^{2}} + \cos 2x
  = (-1+1) + (3-1-2)x^{2} + \Bigl(-\frac{1}{2}+\frac{2}{3}\Bigr)x^{4}+\cdots
  = \frac{1}{6}\,x^{4} + \text{h.o.t.}$$ The constant and $x^{2}$ terms
cancel; the first nonzero term is $\frac{1}{6}x^{4}$.

**Denominator.** Expand each piece: $$\begin{align*}
  x\sin x &= x\Bigl(x - \frac{x^{3}}{3!}+\cdots\Bigr) = x^{2} - \frac{x^{4}}{6}+\cdots, \\
  \ln(1+x^{2}) &= x^{2} - \frac{x^{4}}{2} + \cdots
\end{align*}$$ Combine: $$x\sin x - \ln(1+x^{2})
  = (1-1)x^{2} + \Bigl(-\frac{1}{6}+\frac{1}{2}\Bigr)x^{4}+\cdots
  = \frac{1}{3}\,x^{4} + \text{h.o.t.}$$

**Conclusion.**
$$\lim_{x\to 0}\frac{3x^{2}-e^{x^{2}}+\cos 2x}{x\sin x - \ln(1+x^{2})}
  = \frac{1/6}{1/3}
  = \frac{1}{2}.$$
:::

::: remark
Here is a secret: experienced analysts and calculus instructors **rarely
use L'Hôpital's Rule**. They almost always use this power-series method,
because it is faster and less error-prone.
:::

## Exact Summation of Series {#sec:14.14}

*There are very few series whose exact value can be computed directly
from the definition---mostly just geometric and a few telescoping
series. Taylor series change this dramatically: with a little
creativity, we can compute the exact value of many more.*

::: example
[]{#ex:14-15 label="ex:14-15"} Compute
$\displaystyle\sum_{n=1}^{\infty}\frac{n}{2^{n}}$.

**Step 1: Interpret as a power series.**
$$\sum_{n=1}^{\infty}\frac{n}{2^{n}}
  = \sum_{n=1}^{\infty}n\,x^{n}\bigg|_{x=1/2}.$$

**Step 2: Relate to a known series.** We know
$\sum_{n=0}^{\infty}x^{n}=\dfrac{1}{1-x}$ for
$\left\lvert x \right\rvert<1$. Differentiating term by term:
$$\sum_{n=1}^{\infty}n\,x^{n-1} = \frac{1}{(1-x)^{2}}.$$ Multiply both
sides by $x$: $$\sum_{n=1}^{\infty}n\,x^{n} = \frac{x}{(1-x)^{2}}.$$

**Step 3: Evaluate.** Setting $x=\frac{1}{2}$:
$$\sum_{n=1}^{\infty}\frac{n}{2^{n}}
  = \frac{1/2}{(1/2)^{2}}
  = \frac{1/2}{1/4}
  = 2.$$
:::

::: example
[]{#ex:14-16 label="ex:14-16"} Compute
$\displaystyle\sum_{n=0}^{\infty}\frac{2^{n}}{(n+2)\cdot n!}$.

**Step 1: Interpret as a power series.**
$$\sum_{n=0}^{\infty}\frac{2^{n}}{(n+2)\cdot n!}
  = \sum_{n=0}^{\infty}\frac{x^{n}}{(n+2)\cdot n!}\bigg|_{x=2}.$$

**Step 2: Relate to a known series.** We know
$\sum_{n=0}^{\infty}\dfrac{x^{n}}{n!}=e^{x}$, so
$\sum_{n=0}^{\infty}\dfrac{x^{n+1}}{n!}=x\,e^{x}$. To introduce the
factor $(n+2)$ in the denominator, integrate: since
$\displaystyle\int x^{n+1}\,dx= \frac{x^{n+2}}{n+2}$,
$$\sum_{n=0}^{\infty}\frac{x^{n+2}}{(n+2)\cdot n!}
  = \int_{0}^{x}t\,e^{t}\,dt.$$ Integration by parts gives
$$\int_{0}^{x}t\,e^{t}\,dt= (x-1)e^{x}+1.$$

**Step 3: Extract the desired sum.** Dividing by $x^{2}$:
$$\sum_{n=0}^{\infty}\frac{x^{n}}{(n+2)\cdot n!}
  = \frac{(x-1)e^{x}+1}{x^{2}}.$$

**Step 4: Evaluate at $x=2$.**
$$\sum_{n=0}^{\infty}\frac{2^{n}}{(n+2)\cdot n!}
  = \frac{(2-1)e^{2}+1}{4}
  = \frac{e^{2}+1}{4}.$$
:::

## Application to Kinetic Energy {#sec:14.15}

*One of the major uses of Taylor series in the sciences is to
approximate complicated physical equations with simpler polynomials. In
this section we illustrate this with a fundamental example from physics:
kinetic energy.*

### Two formulas for kinetic energy {#two-formulas-for-kinetic-energy .unnumbered}

The kinetic energy of a particle---the energy it possesses because of
its motion---has a different formula in classical and relativistic
physics.

**Classical formula.**
$$T_{\text{classical}} \;=\; \frac{1}{2}\,m_{0}\,v^{2},$$ where $m_{0}$
is the rest mass and $v$ is the velocity.

**Relativistic formula.** Einstein's famous equation $E=mc^{2}$ gives
the total energy. The kinetic energy is the total energy minus the rest
energy $m_{0}c^{2}$:
$$T_{\text{rel}} \;=\; m_{0}c^{2}\!\left(\frac{1}{\sqrt{1-(v/c)^{2}}}-1\right),$$
where $c$ is the speed of light and the relativistic mass is
$m = m_{0}/\!\sqrt{1-(v/c)^{2}}$.

*These two expressions look very different, yet they describe the same
physical quantity. The classical formula should be obtainable from the
relativistic one as an approximation when velocities are small compared
to $c$. This is precisely what Taylor polynomials are designed for.*

### Taylor expansion {#taylor-expansion .unnumbered}

::: example
[]{#ex:14-17 label="ex:14-17"} Set $u=(v/c)^{2}$ and consider the
function $f(u)=(1-u)^{-1/2}$. When $v\ll c$, the variable $u$ is small
and close to $0$, so we expand around $u=0$.

**First-order approximation.**
$$f(0)=1, \qquad f'(u)=\tfrac{1}{2}(1-u)^{-3/2}, \qquad f'(0)=\tfrac{1}{2}.$$
So $f(u) \approx 1+\frac{1}{2}u$. Substituting back:
$$T_{\text{rel}} \;\approx\; m_{0}c^{2}\!\left(1+\frac{1}{2}\cdot\frac{v^{2}}{c^{2}}-1\right)
  = \frac{1}{2}\,m_{0}\,v^{2}
  = T_{\text{classical}}.$$ The classical formula is exactly the first
nonzero Taylor polynomial of the relativistic formula.

**Second-order approximation.**
$$f''(u) = \tfrac{3}{4}(1-u)^{-5/2}, \qquad f''(0) = \tfrac{3}{4}.$$ The
second Taylor polynomial is
$f(u)\approx 1+\frac{1}{2}u+\frac{3}{8}u^{2}$. This gives the first
*relativistic correction* to the classical kinetic energy:
$$T_{\text{rel}} \;\approx\; \frac{1}{2}\,m_{0}\,v^{2} + \frac{3}{8}\,m_{0}\,\frac{v^{4}}{c^{2}}.$$
Higher-order Taylor polynomials yield further correction terms, each one
improving the approximation for moderate velocities, until eventually
one may as well use the full relativistic expression.
:::

::: remark
This is a recurring pattern throughout physics. One derives an exact
equation using fundamental principles, but that equation is too
complicated for practical use. Replacing certain functions by their
Taylor polynomials yields simpler, approximate equations valid in
appropriate regimes (here, small $v/c$). The classical formula for
kinetic energy is not an accident---it is the inevitable low-velocity
consequence of the deeper relativistic formula.
:::

# Precalculus Reference

*This appendix collects the precalculus facts and identities used
throughout the course. Results are stated without proof. Familiarity
with this material is assumed from the first chapter onward.*

## Trigonometric Identities {#sec:A.1}

Trigonometric identities pervade every part of calculus. When you
differentiate $\sin x$ or $\cos x$, when you integrate powers of
trigonometric functions, and when you simplify expressions after a
trigonometric substitution, you rely on the identities collected here.
Knowing them cold---not just recognising them, but being able to
reproduce them quickly---will save you enormous time throughout the
course.

Many of the identities below are consequences of just one fact: the
Pythagorean identity $\sin^2\theta + \cos^2\theta = 1$. We organise them
into groups so that you can see the logical relationships.

::: proposition
[]{#prop:A-1 label="prop:A-1"} $$\begin{align*}
  \sin^2\theta + \cos^2\theta &= 1 \\
  1 + \tan^2\theta            &= \sec^2\theta \\
  1 + \cot^2\theta            &= \csc^2\theta
\end{align*}$$
:::

::: proposition
[]{#prop:A-2 label="prop:A-2"} $$\begin{align*}
  \csc\theta &= \dfrac{1}{\sin\theta} \\
  \sec\theta &= \dfrac{1}{\cos\theta} \\
  \cot\theta &= \dfrac{1}{\tan\theta} \\
  \tan\theta &= \dfrac{\sin\theta}{\cos\theta} \\
  \cot\theta &= \dfrac{\cos\theta}{\sin\theta}
\end{align*}$$
:::

::: proposition
[]{#prop:A-3 label="prop:A-3"} $$\begin{align*}
  \sin(\alpha \pm \beta) &= \sin\alpha\cos\beta \pm \cos\alpha\sin\beta \\
  \cos(\alpha \pm \beta) &= \cos\alpha\cos\beta \mp \sin\alpha\sin\beta \\
  \tan(\alpha \pm \beta) &= \dfrac{\tan\alpha \pm \tan\beta}
                                  {1 \mp \tan\alpha\tan\beta}
\end{align*}$$
:::

::: proposition
[]{#prop:A-4 label="prop:A-4"} $$\begin{align*}
  \sin(2\theta) &= 2\sin\theta\cos\theta \\
  \cos(2\theta) &= \cos^2\theta - \sin^2\theta \\
                &= 2\cos^2\theta - 1 \\
                &= 1 - 2\sin^2\theta \\
  \tan(2\theta) &= \dfrac{2\tan\theta}{1 - \tan^2\theta}
\end{align*}$$
:::

::: proposition
[]{#prop:A-5 label="prop:A-5"} $$\begin{align*}
  \sin^2\theta &= \dfrac{1 - \cos(2\theta)}{2} \\
  \cos^2\theta &= \dfrac{1 + \cos(2\theta)}{2} \\
  \tan^2\theta &= \dfrac{1 - \cos(2\theta)}{1 + \cos(2\theta)}
\end{align*}$$
:::

::: proposition
[]{#prop:A-6 label="prop:A-6"} $$\begin{align*}
  \sin\alpha\cos\beta &= \tfrac{1}{2}[\sin(\alpha+\beta)+\sin(\alpha-\beta)] \\
  \cos\alpha\sin\beta &= \tfrac{1}{2}[\sin(\alpha+\beta)-\sin(\alpha-\beta)] \\
  \cos\alpha\cos\beta &= \tfrac{1}{2}[\cos(\alpha-\beta)+\cos(\alpha+\beta)] \\
  \sin\alpha\sin\beta &= \tfrac{1}{2}[\cos(\alpha-\beta)-\cos(\alpha+\beta)]
\end{align*}$$
:::

::: proposition
[]{#prop:A-7 label="prop:A-7"} $$\begin{align*}
  \sin\alpha + \sin\beta
    &= 2\sin\!\left(\dfrac{\alpha+\beta}{2}\right)
        \cos\!\left(\dfrac{\alpha-\beta}{2}\right) \\
  \sin\alpha - \sin\beta
    &= 2\cos\!\left(\dfrac{\alpha+\beta}{2}\right)
        \sin\!\left(\dfrac{\alpha-\beta}{2}\right) \\
  \cos\alpha + \cos\beta
    &= 2\cos\!\left(\dfrac{\alpha+\beta}{2}\right)
        \cos\!\left(\dfrac{\alpha-\beta}{2}\right) \\
  \cos\alpha - \cos\beta
    &= -2\sin\!\left(\dfrac{\alpha+\beta}{2}\right)
         \sin\!\left(\dfrac{\alpha-\beta}{2}\right)
\end{align*}$$
:::

   $\theta$   $\sin\theta$   $\cos\theta$    $\tan\theta$     $\csc\theta$     $\sec\theta$     $\cot\theta$
  ---------- -------------- -------------- ---------------- ---------------- ---------------- ----------------
     $0$          $0$            $1$             $0$         $\text{undef}$        $1$         $\text{undef}$
   $\pi/6$       $1/2$       $\sqrt{3}/2$    $1/\sqrt{3}$         $2$          $2/\sqrt{3}$      $\sqrt{3}$
   $\pi/4$    $\sqrt{2}/2$   $\sqrt{2}/2$        $1$           $\sqrt{2}$       $\sqrt{2}$          $1$
   $\pi/3$    $\sqrt{3}/2$      $1/2$         $\sqrt{3}$      $2/\sqrt{3}$         $2$          $1/\sqrt{3}$
   $\pi/2$        $1$            $0$        $\text{undef}$        $1$         $\text{undef}$        $0$
    $\pi$         $0$            $-1$            $0$         $\text{undef}$        $-1$        $\text{undef}$
   $3\pi/2$       $-1$           $0$        $\text{undef}$        $-1$        $\text{undef}$        $0$
    $2\pi$        $0$            $1$             $0$         $\text{undef}$        $1$         $\text{undef}$

  : Values of Trigonometric Functions at Standard Angles

::: remark
All angles in the table above are measured in radians. The notation
$\text{undef}$ indicates that the function is undefined at that angle
because its denominator is zero; geometrically, the function has a
vertical asymptote there.
:::

## Exponential and Logarithmic Laws {#sec:A.2}

The exponential function $e^x$ and the natural logarithm $\ln x$ are
everywhere in calculus: they appear in differentiation rules,
integration formulas, growth and decay models, and the definitions of
many other functions. The algebraic laws listed here are the foundation
on which all of that rests.

In particular, the change-of-base formula lets us reduce any exponential
$a^x$ to $e^{x \ln a}$, which is essential when differentiating or
integrating exponentials with arbitrary bases in Chapters 3 and 4.

::: proposition
[]{#prop:A-8 label="prop:A-8"} For $a > 0$ and all
$x, y \in \mathbb{R}$: $$\begin{align*}
  a^x \cdot a^y    &= a^{x+y} \\
  \dfrac{a^x}{a^y} &= a^{x-y} \\
  (a^x)^y          &= a^{xy} \\
  (ab)^x           &= a^x b^x \\
  a^0              &= 1 \\
  a^{-x}           &= \dfrac{1}{a^x}
\end{align*}$$
:::

::: remark
The law $(a^x)^y = a^{xy}$ is used constantly when simplifying
expressions before differentiating---for instance, rewriting
$\sqrt[3]{x^2}$ as $x^{2/3}$ so that the power rule applies directly.
:::

::: proposition
[]{#prop:A-9 label="prop:A-9"} For $a > 0$, $a \neq 1$, and $x, y > 0$:
$$\begin{align*}
  \log_a(xy)  &= \log_a x + \log_a y \\
  \log_a(x/y) &= \log_a x - \log_a y \\
  \log_a(x^r) &= r\log_a x \\
  \log_a x    &= \dfrac{\ln x}{\ln a}
                 \quad \text{(change of base)} \\
  \ln(e^x)    &= x \quad \text{for all } x \in \mathbb{R}\\
  e^{\ln x}   &= x \quad \text{for all } x > 0
\end{align*}$$
:::

::: remark
The change-of-base formula $\log_a x = \dfrac{\ln x}{\ln a}$ is the key
to differentiating $a^x$ for $a \neq e$: we write $a^x = e^{x \ln a}$
and apply the chain rule. It also converts any logarithmic integral into
one involving $\ln$.
:::

## Algebraic Techniques {#sec:A.3}

The algebraic manipulations below appear throughout the course:
completing the square is essential for certain integrals and limit
calculations, factoring identities simplify rational expressions, and
the binomial theorem underpins Taylor expansions and series analysis.

::: proposition
[]{#prop:A-10 label="prop:A-10"}
$$x^2 + bx = \left(x + \dfrac{b}{2}\right)^2 - \dfrac{b^2}{4}$$
:::

::: example
[]{#ex:A-1 label="ex:A-1"} Write $x^2 + 6x + 5$ in completed square
form.

We isolate the quadratic and linear terms and apply the formula:
$$\begin{align*}
  x^2 + 6x + 5
    &= (x^2 + 6x) + 5 \\
    &= \left(x^2 + 6x + 9\right) - 9 + 5 \\
    &= (x + 3)^2 - 4
\end{align*}$$ Hence $x^2 + 6x + 5 = (x+3)^2 - 4$, so the minimum value
of the expression is $-4$, attained at $x = -3$.
:::

::: proposition
[]{#prop:A-11 label="prop:A-11"} $$\begin{align*}
  a^2 - b^2 &= (a-b)(a+b) \\
  a^3 - b^3 &= (a-b)(a^2+ab+b^2) \\
  a^3 + b^3 &= (a+b)(a^2-ab+b^2)
\end{align*}$$
:::

::: proposition
[]{#prop:A-12 label="prop:A-12"} For $n \in \mathbb{N}$ and
$a, b \in \mathbb{R}$:
$$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$ The first three
cases explicitly: $$\begin{align*}
  (a+b)^2 &= a^2 + 2ab + b^2 \\
  (a+b)^3 &= a^3 + 3a^2 b + 3ab^2 + b^3
\end{align*}$$
:::

::: remark
When integrating a rational function $p(x)/q(x)$ where
$\deg p \geq \deg q$, perform polynomial long division first to write
the integrand as a polynomial plus a proper rational function.

For example, divide $x^3 + 2x$ by $x^2 + 1$: $$\begin{align*}
  x^3 + 2x &= (x^2 + 1) \cdot x + (2x - x) \\
            &= (x^2 + 1) \cdot x + x
\end{align*}$$

We verify this step by step. We seek $q(x)$ and $r(x)$ with
$\deg r < \deg(x^2 + 1) = 2$ such that
$x^3 + 2x = (x^2+1)\,q(x) + r(x)$.

First, divide the leading term: $x^3 \div x^2 = x$.

Multiply and subtract: $$\begin{align*}
  x^3 + 2x - x \cdot (x^2 + 1)
    &= x^3 + 2x - x^3 - x \\
    &= x
\end{align*}$$

Since $\deg(x) = 1 < 2 = \deg(x^2+1)$, we stop. Therefore:
$$\dfrac{x^3 + 2x}{x^2 + 1} = x + \dfrac{x}{x^2 + 1}$$
:::

## Inverse Functions {#sec:A.4}

Inverse functions are central to Chapter 4, where we study inverse
trigonometric functions ($\arcsin$, $\arccos$, $\arctan$) and where we
treat the natural logarithm as the inverse of the exponential. The
derivative rule for inverse functions, stated below, appears in
Chapter 3 and is used repeatedly whenever we differentiate an inverse
function.

Understanding when a function *has* an inverse---and the role of
restricting the domain to guarantee invertibility---is essential before
any of those later results make sense.

::: definition
[]{#def:A-1 label="def:A-1"} Let $f \colon A \to B$ be a function. A
function $g \colon B \to A$ is called the *inverse* of $f$ if
$$g(f(x)) = x \quad \text{for all } x \in A
  \qquad \text{and} \qquad
  f(g(y)) = y \quad \text{for all } y \in B.$$ When such a $g$ exists,
$f$ is called *invertible*, and we write $g = f^{-1}$.
:::

::: remark
A function $f$ is invertible if and only if it is *bijective*: injective
(one-to-one) and surjective (onto). Geometrically, $f$ passes the
horizontal line test.
:::

::: proposition
[]{#prop:A-13 label="prop:A-13"} Let $f$ be differentiable and
invertible on an interval, with $f'(x) \neq 0$. Then $f^{-1}$ is
differentiable and
$$\bigl(f^{-1}\bigr)'(y) = \dfrac{1}{f'\!\left(f^{-1}(y)\right)}.$$
:::

::: remark
The proof of [\[prop:A-13\]](#prop:A-13){reference-type="ref+label"
reference="prop:A-13"} uses the chain rule and appears in
[4.4](#sec:4.4){reference-type="ref+label" reference="sec:4.4"}.
:::
