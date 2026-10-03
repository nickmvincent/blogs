---
title: "N-gram search as posterior updating for data attribution"
content_id: "garden/draft/posterior"
date: "2026-05-27"
slug: "posterior"
summary: "A short argument that model outputs and training-data priors can improve rough approximations of data attribution."
original_url: "https://dataleverageshortposts.leaflet.pub/3mni4cwhlhvx3"
captured_from: "https://nickmvincent.github.io/short-focus-posts/posterior.html"
source_revision: "cbe747fa1c1f30dd85d9cf552f4db279c7be2d7d"
source_sha256: "a01d5ec5ce9812f88e8ca58373183e4400caf76e9d0577a5b2cd50ebf9a3b006"
status: "draft"
visibility: "public"
---

I originally wrote a version of this [on Twitter](https://x.com/nickmvincent/status/2058242437949333584) in response to a large discussion about using n-gram search to find specific passages in Internet training data that may "explain" certain AI outputs.

---

Many of the proposed responses to AI impacts that touch on data attribution and/or the flow of economic winnings *require* us to assume some kind of quantitative distribution of credit.

Typically, the "credit" construct in these discussions is some kind of data counterfactual, either a leave-one-out variant or some Shapley-like aggregate over many combinations of training data. When we are discussing how to give credit or reward, we typically end up leaning on some notion of "causal impact" of data.

However, I think almost everyone -- even those who aren't thinking about the formal training data attribution task at all -- has some implicit understanding that getting anywhere close to an exact distribution of credit scores for the training data of large models with large training sets is extremely hard. So, at the moment, everyone ends up using simplifying assumptions, and these assumptions are generally not made explicit.

Furthermore, the definition of credit and causal impact that a given approach leans on is itself often left implicit. We would almost always benefit from making it explicit: we should say which specific counterfactual scenarios we are considering when we try to assign any kind of "causal" credit. We also must be explicit about how much we want to connect causal impact and moral desert. One can argue that a document could have been used heavily in training, and even memorized, without that implying that that particular document "deserves" a large share of economic surplus; so making our counterfactual of interest explicit is very important.

Responses that try to handwave away the whole issue (often arguing that the whole endeavor of trying to credit training data is pointless) basically take the stance that we should just assume all data credit values to be zero and give all the value to the operators of AI systems. One way we might justify this more formally is to note that the leave-one-out scores for granular units of data in very large models are all very, very small. (However, the scores for larger coalitions of data may not be small at all!) Responses in the general space of UBI/AI dividends/data dividends basically take the stance that we should use a kind of uniform approximation -- just give each person or each unit of training data a value of 1/n.

There are a number of other responses that also have their own assumptions about implicit value distributions (collective licensing schemes imply some kind of pooling approximation, some approaches emphasize retrieval-level influence over training-level, etc.). Will avoid spelling these out here for the sake of space.

One question that follows -- how good are these approximations, and how well do they work for driving a specific social outcome (e.g., incentivizing paid knowledge work, incentivizing volunteer peer production)?

And a second question, which connects directly to the debate about using n-gram search as a proxy for attribution, is this: if we do not have access to actual training data or information from the actual training process (e.g., logs of gradient updates), but we do have information about the output of a model (for instance, the fact that a model produced a sequence that has only appeared in one niche blog) combined with industry-wide assumptions about the model (for instance, an assumption that every frontier model is assumed to have seen some variant of Common Crawl during pretraining), can we use that information in any way to get a better approximation than "assume all data values are zero" or "assume all data values are 1/n"?

I think it will be valuable to more formally connect things like n-gram search approaches to membership inference and sequence-level training data attribution.

One conceptual approach here is to think of the high-level process as trying to improve a posterior (I hope to write something longer on this front; if you've seen anything along these lines, please let me know).

But in the meantime, unless somebody offers a better set of data values (for instance, if an AI operator offers access to direct data attribution scores for their model), I think it likely is the case that using some information about model outputs **will** give us a "directionally better" approximation than all-zero or 1/n.

(More formally, I think the error of our approximate data value distribution will on average go down!)

And again, without full data access or direct access to data attribution, what we should do pragmatically right now is to aggregate across any information we can get (whether that's n-gram search and membership inference or tacit community knowledge like "everybody uses Common Crawl" or "everybody used to use book torrents") to try to do better than a 1/n approximation or an all-zero approximation.
