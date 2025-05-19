# Ideas

A file in which I attempt to organize and link together common ideas that appear in my work (spanning academic papers to blog posts). One goal of maintaining this file is to experiment in moving more of my notes into semi-public spaces, and to create some accountability in tracking which ideas I've prioritized at various points in time.

For each "idea object", I aim to record a one-sentence summary of the idea, a set of bullet points with further information, and then links to any longer posts or papers I've written that directly or indirectly touch on the idea. After enough gardening, this file might be useful for a kind of "graph view" into my writing.

The current version has a bit of CV / resume vibe (i.e. excessively focused on my own outputs). In the future, I hope to link this with efforts to curate much larger lists of other people's work and plug this into a much, much bigger graph.

## Public AI institutions can act as data appraisers

A public body that trains and deploys AI systems can also provide a public service by sharing estimates of data value that allow data markets to operate much more efficiently.

Posts:
- Newsletter: https://dataleverage.substack.com/p/public-ai-data-appraisal-and-data

## AI "Outputs" and "Actions" Stem from Human "Stamps of Approval"

Every AI output (e.g., a sequence of tokens from an LLM) or "action" maps to some set of *human stamps of approval*

- We might rephrase this as a conjecture: for a given example of a "successful AI output" (a snippet of code that solves a software engineer's problem, a reworded email that's more polite, a funny poem that makes your friends laugh), we could, given enough time and resources, produce a list of "top ten people whose stamps of approval made this possible". With even more time and resources, we might produce a list of n people that were *needed* for the output -- if those people never gave their stamp of approval, the output would have hit some threshold of difference
  - Technical bounds on how accurately or efficiently we could produce such lists will depend on the model and a number of environmental conditions, but we can quickly prove this to be possible for small models.
  - As models get bigger we need to be looser in our estimation, but doing this should conceptually still be possible, and we should be able to do better than random.
- This conjecture is extremely important. It suggests, first of all, that "synthetic" data in the LLM context could also be called "processed" or "laundered" data, as the human stamps of approval still exist but the synthesizing process obfuscates our ability to reproduce them. Say we produce synthetic data by prompting an LLM, then get very similar outputs from our "synthetically-trained LLM". We can still trace these outputs back to individual people contributing code, etc., but it's just harder now.

Posts:
- Tweet: https://x.com/nickmvincent/status/1879589740640719241
  - 1/2: "Problem w/ "synthetic data" term is that (I posit) there's *always* some human action you can trace a "synthetic document" to. Problem w/ "AI agents" term is that there's *always* some humans who did the actuation and kick-off who hold moral agency. Obfuscating either is bad." 2/2: "Of course using the terms with caveats totally makes sense. But I think there's increasing body of public discussions (including news coverage, blogs, micro-blogs, sometimes papers) that currently serves to obfuscate the underlying human labour and human responsibility."
- Newsletter: TODO


## Hypermaploom: Importance of Maps and Looms Metaphor

I believe it is very useful to think of modern AI systems as a kind of ultra dimensional map/loom combination.

Posts:
- On the maps point: https://dataleverage.substack.com/p/ai-technologies-are-system-maps-and-you-are-a-cartographer
- On the looms point: TODO!


## HCNames: Model Naming That Emphasizes Human Contributions

If we are going to include parameter sizes in model names, I think it would also be a good idea to include estimates of the number of human contributors, perhaps separated into pre-training and post-training?

Posts:
- Tweet: https://x.com/nickmvincent/status/1829215803985801605
- Microblog: https://github.com/nickmvincent/blogs/blob/main/microblogs/2025-05-17_three_terms.md


## EvalName: We should also name evaluation sets in a way that emphasized human contributions

corollary to HCNames: we should also name eval sets in a way that includes an estimate of the number of human contributors.

## Eval leverage

When models threaten the labor leverage of a group (e.g., academics who perform lit reviews become less valuable), there is some ability to "hold out" by refusing to evaluate the model. This gives a buffer before it can be deployed.

- Newsletter: https://dataleverage.substack.com/p/evaluation-data-leverage-advances

## Unaddressed valuation question: how to allocate $ between people who contributed to train vs test?

We should write down a principled to way think about allocating $ or credit between people who contribute to a train set or a test set.

- If they don't choose (and they probably shouldn't so the holdout set is clean -- if people know they're being evaluated, they might act differently), it should be equal?

## Concerns with Framing of "Synthetic Data"-focused work

Core idea: "Synthetic data is not a particularly useful concept in the realm of generative AI pre-training data, if we characterize units of data using a unique set of contributor ids, which is probably a good idea in many contexts, albeit rarely practiced.

Posts:
- https://x.com/nickmvincent/status/1879589740640719241
  - recorded above.
- https://x.com/nickmvincent/status/1726965303236813133
  - 1/ "Producing "synthetic" data -- records that look like human records but are model outputs and not the output of a form or sensor -- is definitely useful for privacy guarantees, and for achieving certain LLM performance outcomes, it seems. But!" 2/ "The way I've seen the term synthetic data used (in online LLM discussions, not in e.g. privacy research) implies "breaking free" of the human dependence. Not true! Any given synthetic record -- if we have the documentation capabilities -- can be traced to human activities..." 3/ "There's always some sensor or some form, and some degree of human knowledge, preference, and agency upstream. (Synthetic records from a contained game-environment are kind of, but not totally, an exception)." 4/ I think this is important because a shift towards talking and thinking about "synthetic" data may once again hide and de-prioritize the underlying human activity (and IMO, emphasizing this activity can be mutually beneficial for society + AI builders) 5/ I suppose my TLDR here is: Model-generated "synthetic records" seem great for certain privacy and capability outcomes, but we must keep in mind they are laundered copies of "original records" that capture human knowledge and preferences
- https://x.com/nickmvincent/status/1726961643266163047
  (quote tweet) "This seems very cool, but at some point I really want to make a longer case for my view on conflating "synthetic" data in LLM context as "AI-generated" -- every single piece is still traceable back to some individual people and their individual activities!"
- https://x.com/nickmvincent/status/1817211542091551150 quote tweet
- https://x.com/nickmvincent/status/1726965304843206740 quote tweet


## Letting People Put Weights on Their Contributions to Unlock More Intelligent Models

Let me look at my old data contributions and say, "this is good", or "this is bad".

- This exists to a degree because the practing of "weighing stuff" is inherent in institutional and community publishing practices (conference papers, upvoted posts, etc.) but tons of nuance missed
- Few options to do this with explicit feedback data
  - Kind of happens by default, if I use thumbs up/down fedback on 1/20 of my LLM "chats" I'm weighting them. In the same sense that 0/1 interaction data can beat 1-5 star data at scale, maybe this is fine, but we're probably missing out on richness.

## Data Scaling Laws are Leverage Estimates

When we conduct basic data scaling experiments, even without any explicit "collective action simulations", we get insight into the potential leverage of groups of size X.


## Lots of value in writing out the extremes of data flow

It would be useful to really write out some of the likely consequences of very "extreme data flow scenarios", such as "What if we never retrain any models, and nobody can ever opt out of data inclusion", or "what if we frequently retrain models, and everyone can easily change their opt out preferences every day".

- We might consider an Opt in opt out cost curve and a Retraining frequency curve
- We also need to consider a preference distribution (how much people value opt in and opt out)

NEVER retrain, never opt out
- perfect for historians
- compounding inequalities

Never retrain, can opt out
- people "disappear" from the timeline
- weird blips

Extend this!


## On AI Agents and Moral Agency

For now, every AI process still has a human who invoked it or kicked off the job, and they probably have some moral agency.

- Corollary: The Moral Weight of Actuation. When you hook your model to a machine or API, there's moral weight in that choice and you take on responsibility.


## All Models Are Wrong, Some Are Useful, There's Always a Model in "Prod"

All models are wrong, some are useful, but there's always a model running in prod. There's some "model" being "run" right now and every day we don't change it has some moral cost as well.

Tweet:



## Eventually all ML will become human subjects research?

...

## Measuring if something is really a public good (how clubby is it)?

...

## Under what conditions do corporate incentives permit FAccT work?

...

Important for students taking e.g. HCAI or Fairness class and want to practices in industry


## LLM-assisted "search" could be more reproducible than "real" search?

...

## More examples land value-style tax for "knowledge spaces" and "information spaces"?

Harberger tax on intellectual property

Not a new idea, e.g. radical markets

- Things in knowledge space that are static could be governed like land
- Things that are less static can be governed like digital goods
- No need to embed a poison pill in anything — either it expires or it doesn’t 
Core challenge remains 

LVT: https://en.wikipedia.org/wiki/Land_value_tax
Harberger tax, aka COST: https://en.wikipedia.org/wiki/Harberger_Tax (Common Ownership Self-assessed Tax)


## Need to incentivize an append-focused lens on citation practice.

Citation lists as static artifacts don’t make (much) sense. 
If we agree more citations are better (e.g., we should have unlimited space for citations) why can't people vote to add citations or just "this is relevant" afterwords. including follow up work! People who add citations to some existing work and get social approval should some credit anyway!
Downsides: if there's no pressure along the lines of the "this is going to be archival", authors will be sloppier. I think it's worth it, though.


## Doing too much as data poisoning against causal inferrers

Doing a bunch of things at once is data poisoning against causal inference tasks