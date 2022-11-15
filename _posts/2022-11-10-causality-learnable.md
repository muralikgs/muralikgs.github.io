---
layout: post
title: Is Causality Learnable from Observations?
date: 2022-06-08 11:12:00-0400
# tags: graphical-models, causal-discovery, structure-learning. 
categories: graphical-models
---
<!---
\( ... \) is for inline math expressions in paragraph mode!
-->

<p style='text-align: justify;'> Establishing causal relations is one of the main ways by which we develop an understanding of the world around us. Some of the successful laws of science, Newton's second law for example, do precisely this. In this case, the force exerted causally influences the movement of an object, or more concisely, \( \boldsymbol{f} = m\boldsymbol{a} \). In general, this is an arduous task (<a href="https://www.jmlr.org/papers/v5/chickering04a.html">Chickering et al. (2004)</a>) and identifiability of the causal structure is not guaranteed for most cases when we only have access to observations of the system. This blog post is going to be the first in a series of posts on the identifiability of such causal relations from observations. This is written mostly to aid in my understanding of this area but the aim is to make this as self explanatory as possible.</p>

<p style='text-align: justify;'> Let us start with a description of the problem at hand. Let \(G = (V, E)\) be a graph that encodes the causal relations between the system variables, where \(V = \{x_1,\ldots, x_p\}\) and \(E \subseteq V \times V\) is the set of all edges in the graph. The <em>parent set</em> of the node \(x_i\), denoted as \(\mathrm{pa}(x_i)\) is the set of all nodes from which there exists an edge directed towards \(x_i\). Another common representation of such a system is the <em>Structural Equation Model</em> (SEM), where each parent-child relationship is represented in the form of an algebraic equation. That is, 
$$
\begin{equation}
x_i = f(\boldsymbol{x}, \varepsilon_i)
\end{equation}
$$</p>

## Identifiability
