---
title: "Microblog One Book Is Worth 006 Benchmark"
subtitle: "Commenting on recent coverage of, and discussion about, Meta's arguments about training data value quantification. "
date: 2025-04-21
original_url: "https://dataleverage.substack.com/p/microblog-one-book-is-worth-006-benchmark"
---

> **Original Substack post:** [https://dataleverage.substack.com/p/microblog-one-book-is-worth-006-benchmark](https://dataleverage.substack.com/p/microblog-one-book-is-worth-006-benchmark)

This will be a “contextualized microblog”. I saw several posts in quick succession that I thought could be worth commenting on as a group.

First, a set of relevant links that discuss training data value in the context of lawsuits, compensation and consent:

* A previous (Sep 2024) [newsletter](https://dataleverage.substack.com/p/is-zuckerberg-right-to-say-that-your) in which I discuss the intersection of collective bargaining and data valuation: “Is Zuckerberg right to say that your specific creative work has no value to AI?”

  + This newsletter is mainly a reaction to this [article](https://www.theverge.com/2024/9/25/24254042/mark-zuckerberg-creators-value-ai-meta) from The Verge
* A much more recent (April 2025) [tweet](https://x.com/AndrewCurran_/status/1914045840265789540) with much discussion from Andrew Curran, which comments on a screenshot of a quote from this Vanity Fair [article](https://www.vanityfair.com/news/story/meta-ai-lawsuit) on AI lawsuits, and in particular Meta.

  + The quote: ‘But their defense also hinges on the argument that the individual books themselves are, essentially, worthless—one expert witness for Meta describes that the influence of a single book in LLM pretraining “adjusted its performance by less than 0.06% on industry standard benchmarks, a meaningless change no different from noise.”’
* A response [tweet](https://x.com/giffmana/status/1914245144422776906) from Lucas Beyer criticizing the discourse around this number/topic (discussing practical constraints that should be considered in interpreting a number like this, especially variance between experiments)
* See also: this recent [coverage](https://www.businessinsider.com/meta-ai-llama-models-training-data-ablation-2025-4) from Barr and Dixit at Business Insider of Meta’s data ablation experiments

I think Beyer’s points are critical to account for in data value discussions. Robust data valuation remains expensive and there’s so much more context needed to throw around numbers like this (as he notes: model scale, training duration, exact benchmark details, and so on).

## The Short Argument

What I want to add (echoing the September post) is this: in any data valuation experiment, another factor that must be accounted for is whether and how data points will be *grouped*. In pure “leave-one-out” experiments, there are no groups; it’s every data point for itself. There are technicalarguments for grouping data points: we might want to compute data value along natural groupings that emerge from the data (e.g., demographic groups), compute Shapley values with account for various “coalitions” that might exist, or compute data values in a way that gives more weight to either smaller or larger groups.[1](#footnote-1)

Different approaches can be empirically tested for effectiveness on various tasks like data selection or mislabel detection. However, in the context of training data and consent/compensation/law (topics that are typically the forte of economics, philosophy, human-computer interaction, etc.), there is no purely technical approach that can determine the appropriate group size to test**.** Rather, for practical purposes (e.g. for a market or for a lawsuit) the appropriate group size is dependent on coordination and collective bargaining capabilities of the training data creators.

The 0.06% number (again, with all its many caveats) is really only relevant if we accept an implicit assumption that all authors would be acting as individual agents in some hypothetical data market. Another extreme (also unrealistic) would be to assume perfect cooperation between all data creators in the world, and then to attribute 100% of model performance to that single coalition. In my opinion: the approach that would most benefit these discussions would be a middle ground. We should be calculating and openly discussing data values at the level of economic sectors, groups of firms, individual firms, and perhaps specific interest groups, but probably not at the level of individual people or books.

[1](#footnote-anchor-1)

To briefly list just a few papers:

* Koh, P. W. W., Ang, K. S., Teo, H., & Liang, P. S. (2019). On the accuracy of influence functions for measuring group effects. *Advances in neural information processing systems*, *32*. [[link](https://proceedings.neurips.cc/paper/2019/hash/a78482ce76496fcf49085f2190e675b4-Abstract.html)]
* Ghorbani, A., & Zou, J. (2019, May). Data shapley: Equitable valuation of data for machine learning. In *International conference on machine learning* (pp. 2242-2251). PMLR. [[link](https://proceedings.mlr.press/v97/ghorbani19c.html)]
* Jia, R., Dao, D., Wang, B., Hubis, F. A., Hynes, N., Gürel, N. M., ... & Spanos, C. J. (2019, April). Towards efficient data valuation based on the shapley value. In *The 22nd International Conference on Artificial Intelligence and Statistics* (pp. 1167-1176). PMLR. [[link](https://proceedings.mlr.press/v89/jia19a.html)]
* Kwon, Y., & Zou, J. (2021). Beta shapley: a unified and noise-reduced data valuation framework for machine learning. *arXiv preprint arXiv:2110.14049*. [[link](https://arxiv.org/abs/2110.14049)]
