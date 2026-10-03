---
title: "Two natural allies of a \"Data Transparency\" agenda: capabilities forecasters and social simulators"
subtitle: "Making an \"if you like X, you might want to support Y\" argument for data-focused policy"
date: "2026-03-09"
original_url: "https://dataleverage.substack.com/p/two-natural-allies-of-a-data-transparency"
content_id: "substack/post/190292186"
authors: ["Nick Vincent"]
published_at: "2026-03-09T18:51:17.885Z"
source_updated_at: "2026-03-09T18:55:05.275Z"
archived_at: "2026-09-25T20:33:42+00:00"
source_body_sha256: "d25a847a8b4e2595a3dd3ed5041203027e8cd82a9a7983f3f9bf966ef0fb548a"
---

![white and blue floral textile]

Extremely *clear* water. Photo by [Hans] on [Unsplash]

If you’ve read this blog — or the title of this blog — you might not be surprised that I am a fan of data-centric research and data-centric policy advocacy. Many of my posts and research outputs include extended arguments for why we should support policy and research that leads to more documentation of data, more efforts to appraise the value of data, and better rules for transactions involving data. Often, I motivate these arguments through the frame of mitigating negative impacts from AI progress or just by making the case that we should generally be making AI systems more human-centered by giving people agency.

In the past few weeks, two separate (but in my view, related!) areas of discourse I’ve been following with interest are:

1.  capabilities forecasting (e.g. discussion of “[Task-Completion Time Horizons of Frontier AI Models]” from METR).

2.  social simulation (especially responses to the announcement of [Simile.ai], a venture extending previously influential [research] on LLM social simulation)

In this post, I want to make a brief argument that anyone interested in one or both of the above two agendas is a very natural ally of “Clear Data Rules” advocacy. I’ll focus in particular on a pretty high-level “wave a magic wand and get more data transparency” conceptualization of clear data rules, and hopefully get into nuanced interactions in the comments, future posts, or more formal follow-up work.

------------------------------------------------------------------------

First, it is notable that much of the capabilities discourse has been very focused on predicting progress over time. The x-axis in the main METR plot that’s been the subject of discourse (noting that there are a lot of plots and robustness checks in the actual paper) is time. Thus, the questions being discussed in this debate tend to center understanding how rates of progress in the AI field will change (or not) and what this means for the urgency of institutional and societal response.

However, for any single data point in “Figure 1 METR plot”, we could in theory characterize each model by its training data (and more specifically, pre-training data, various post-training datasets with different goals, internal evaluation datasets that may have guided design decisions, etc.). At a high-level, we’d expect information about training data to be highly predictive of performance on a given benchmark. For instance, including a large number of expert Python programmers in post-training should greatly improve success at a Python coding task suite.

There’s plenty of nuance to be further investigated regarding interactions between pre- and post-training, transfer of knowledge across related domains, etc. But even a simplified understanding is useful to reason about how more training data transparency might impact scaling models and forecasting more generally.

Consider just this high-level claim: if we had significant dataset documentation for each model, we could likely greatly improve our models of domain-specific AI progress. If we wave our magic policy wand and get rich datasheets for every frontier model, capabilities measurement would benefit massively overnight. Thus, parties who mainly want better capabilities forecasting and scaling models might want to advocate for data transparency and clear data rules *even if they don’t care about any of the other stuff I normally talk about*.

------------------------------------------------------------------------

Second, let’s turn to the topic of AI social simulation. The goal of simile.ai is to build a model that “predicts human behavior in any situation, and a product that deploys it at scale”. More generally, we might understand AI social simulations as attempting to use the fact that real human records are used to train AI models, thus these model weights retain real insights about human behavior and the world, and thus the models themselves might contribute to epistemically useful simulations if the simulations are engineered and calibrated correctly.

There’s much to debate here. Some scholars have quite harshly [criticized] this endeavor (and I think they make many good points) and others have argued in [favor].

Without wading into the broader normative discussion here or touching on any specific empirical questions (more to come on that front!), I’d posit this: social simulation might be promising in some contexts but almost all useful contexts will require the use of fully documented frontier models, with a particular focus on the representation of different groups of people in training (and ideally, some attempt at group-level training data attribution). I have a longer version of this argument in a deck I presented at the University of Washington’s [CSSS] recently, which you can glance at [here].

Basically, if we want to make strong claims about an LLM/AI social simulation and the application of results to a given group of people, we probably want to know about how different groups of people contributed to any upstream AI models!

So, anyone interested in LLM social simulation may also want to advocate for data transparency purely to make LLM social simulation more useful.

------------------------------------------------------------------------

  [white and blue floral textile]: ../media/two-natural-allies-of-a-data-transparency/973fab1baad747d6dfdc.jpg "white and blue floral textile"
  [Hans]: https://unsplash.com/@hansphoto
  [Unsplash]: https://unsplash.com
  [Task-Completion Time Horizons of Frontier AI Models]: https://metr.org/time-horizons/
  [Simile.ai]: https://www.simile.ai/
  [research]: https://arxiv.org/abs/2304.03442
  [criticized]: https://arxiv.org/abs/2401.08572
  [favor]: https://icml.cc/virtual/2025/poster/40125
  [CSSS]: https://csss.uw.edu/
  [here]: https://github.com/nickmvincent/public-talks/tree/main/2025-10_csss_gabm
