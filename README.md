# APS2023Exam

Kattis Exam submission for the course: Algorithmic Problem Solving | 2023 | ITU

**Group**: D

**Authors**: Andreas Kongstad, Chrisanna Kate Cornish, and Christian Emil Stender

**Supervisor**: Jakob Uttenthal Israelsen

**Overleaf Report: <https://www.overleaf.com/project/643e70e477af1249dd8f164e>**

# Superhero Cats

The Superhero Cats are a team of feline crusaders dedicated to saving people from perilous situations! They have a limited amount of time and Catcoin to devote to critical life-saving missions. They need to prioritise their efforts to maximise the number of people they can save. Each mission can only be completed once by the team and some missions will have to fall by the wayside. Choose their missions carefully, time is precious and there are lives needing saving!

### Input

The input begins with three integers $M$, $T$ and $N$, separated by a space.
\begin{itemize}
    \item {$M: (0 < M < 250)$ The maximum amount of Catcoin available.}
    \item {$T: (0 < T < 125)$ The amount of time they have until nap time.}
    \item {$N: (0 < N < 100)$ The total amount of available missions.}
\end{itemize}

Then follows $N$ lines of the form: $m$ $t$ $r$ each describing a single mission where:
\begin{itemize}
    \item {$m: (0 < m \le M)$ The Catcoin cost}
    \item {$t: (0 < t \le T)$ The time consumption in minutes}
    \item {$r: (0 < r < 100)$ The number of people available for rescue}
\end{itemize}

All missions can only be completed once(!) and missions are always successful - they are super heroes after all.

### Output

Output a single line containing the amount of people that can be rescued without exceeding $M$ or $T$.

# Solutions to existing problems

## Moving Pianos

**Link: <https://open.kattis.com/problems/piano>**

## Buzzwords

**Link: <https://open.kattis.com/problems/buzzwords>**

## Breaking Bad

**Link: <https://open.kattis.com/problems/breakingbad>**
