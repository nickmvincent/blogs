# Ideas

A post in which I list a number of ideas. The goal is to experiment in moving more of my notes towards public, and to create some accountability in tracking which ideas I've prioritized at various points in time.

For each I record a one-sentence summary of the idea, a set of bullet points with further information, and then links to any longer posts or papers I've written that directly or indirectly touch on the idea.

## AI "Outputs" and "Actions" and Human stamps of approval

Every AI output (e.g., a sequence of tokens from an LLM) or "action" maps to some set of *human stamps of approval*

- We might rephrase this as a conjecture: for a given example of a "successful AI output" (a snippet of code that solves a software engineer's problem, a reworded email that's more polite, a funny poem that makes your friends laugh), we could, given enough time and resources, produce a list of "top ten people whose stamps of approval made this possible". With even more time and resources, we might produce a list of n people that were *needed* for the output -- if those people never gave their stamp of approval, the output couldn't exist.
  - Technical bounds on how accurately or efficiently we could produce such lists will depend on the model and a number of environmental conditions, but we quickly prove this to be possible for small models.
- This conjecture is extremely important. It suggests, first of all, that "synthetic" data in the LLM context could also be called "processed" or "laundered" data, as the human stamps of approval still exist but the synthesizing process obfuscates our ability to reproduce them. Say we produce synthetic data by prompting an LLM, then get very similar outputs from our "synthetically-trained LLM". We can still trace these outputs back to individual people contributing code, etc., but it's just harder now.

Posts:
- Not explicitly, though it appears implicitly in almost all my data labor and data leverage-related work.


## Importance of Maps and Looms Metaphor

I believe it is very useful to think of modern AI systems as a kind of ultra dimensional map/loom combination.

Posts:
- On the maps point: https://dataleverage.substack.com/p/ai-technologies-are-system-maps-and-you-are-a-cartographer
- On the looms point: TBA


## Model Naming That Emphasizes Human Contributions

If we are going to include parameter sizes in model names, I think it would also be a good idea to include estimates of the number of human contributors, perhaps separated into pre-training and post-training?

Posts:
- https://x.com/nickmvincent/status/1829215803985801605


## Concerns with Framing of "Synthetic Data"-focused work

Core idea: "Synthetic data is not a particularly useful concept in the realm of generative AI pre-training data, if we characterize units of data using a unique set of contributor ids, which is probably a good idea in many contexts, albeit rarely practiced.

Posts:
- #todo

## Letting People Put Weights on Their Contributions to Unlock More Intelligent Models

Let me look at my old data contributions and say, this is good, this is bad


- This exists to a degree because the practing of "weighing stuff" is inherent in institutional and community publishing practices (conference papers, upvoted posts, etc.) but tons of nuance missed
- Few options to do this with explicit feedback data
  - Kind of happens by default, if I use thumbs up/down fedback on 1/20 of my LLM "chats" I'm weighting them. In the same sense that 0/1 interaction data can beat 1-5 star data at scale, maybe this is fine, but we're probably missing out on richness.

## Data Scaling Laws are Leverage Estimates

...


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

Frequent retrain, never opt out...
Frequent retrain, can easily opt out...


## On AI Agents

Tweet: 


## All Models Are Wrong, Some Are Useful, There's Always a Model in "Prod"

all models are wrong, some are useful, but there's always a model running in prod. There's some "model" being "run" right now and every day we don't change it has some moral cost as well.

Tweet:

## Eval leverage

When models threaten the labor leverage of a group (e.g., academics who perform lit reviews become less valuable), there is some ability to "hold out" by refusing to evaluate the model. This gives a buffer before it can be deployed.

## The Moral Weight of Actuation

When you hook your model to a machine or API, there's moral weight in that choice and you take on responsibility.


Tweet: 

## Eventually all ML will become human subjects research?



## Measuring if something is really a public good (how clubby is it)?

...

## Under what conditions do corporate incentives permit FAccT work?

...

Important for students taking e.g. HCAI or Fairness class and want to practices in industry


## LLM-based "search" can be more reproducible then old school?


## More examples land value-style tax for "knowledge spaces" and "information spaces"?

Harberger tax on intellectual property

Not a new idea, e.g. radical markets

- Things in knowledge space that are static could be governed like land
- Things that are less static can be governed like digital goods
- No need to embed a poison pill in anything — either it expires or it doesn’t 
Core challenge remains 

LVT: https://en.wikipedia.org/wiki/Land_value_tax
Harberger tax, aka COST: https://en.wikipedia.org/wiki/Harberger_Tax (Common Ownership Self-assessed Tax)

## Unaddressed valuation question: how to allocate $ between people who contributed to train vs test?

If true random sample, it's equal

But if it's not a true random sample...


## Need to incentivize an append-focused lens on citation practice.

Citation lists as static artifacts don’t make (much) sense. 
If we agree more citations are better (e.g., we should have unlimited space for citations) why can't people vote to add citations or just "this is relevant" afterwords. including follow up work! People who add citations to some existing work and get social approval should some credit anyway!
Downsides: if there's no pressure along the lines of the "this is going to be archival", authors will be sloppier. I think it's worth it, though.


## Doing too much and causal inference

Doing a bunch of things at once is data poisoning against causal inference tasks