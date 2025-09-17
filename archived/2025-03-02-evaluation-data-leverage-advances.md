---
title: Evaluation Data Leverage Advances
subtitle: Research agents and increasingly general reasoning models open the door for immense "evaluation data leverage".
date: 2025-03-02
original_url: https://dataleverage.substack.com/p/evaluation-data-leverage-advances
---
''
> **Original Substack post:** [https://dataleverage.substack.com/p/evaluation-data-leverage-advances](https://dataleverage.substack.com/p/evaluation-data-leverage-advances)

This post has two related goals:

* Motivate the idea of “Evaluation Data Leverage”: knowledge workers will be able to bargain with AI operators for access to their data-generating activities that are specifically needed to evaluate new AI models and products.
* Highlight the challenge that more “general” AI products require evaluation practices that will be very laborious for workers and have a large overall price tag. This could very well create major optics issues for the AI and tech industry if these organizations become widely regarded as agents of precarity.

![](https://substack-post-media.s3.amazonaws.com/public/images/a362c169-14a8-4ef6-9fa7-cf448b081d18\_855x899.png "")

*An ad for evaluation labour from 1894 ([Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Hartford_Steam_Boiler_Inspection_and_Insurance_Co._ad.png)).*

Time marches on, and tech companies continue to ship products that use large-scale models to do some combination of augmenting and/or automating knowledge work. Increasingly, across various firms, two trends emerging are the use of “reasoning” and the implementation of “deep research agents”.

Together, these developments mean that AI products continue to produce larger and potentially more complex artifacts. For instance, a good deal of ink has been spilled over the value of Deep Research. Will (AI) research agents replace (human) research assistants? Are you getting equivalent value to eight hours of human knowledge work in 10 minutes? Are your outputs full of hard-to-catch hallucinations? Will these agents lead to a slew of epistemically toxic artifacts strewn across the web (and in the case of Google’s Deep Research, which makes you read the output in Google Docs, your personal Drive).

This short Tyler Cowen blog [post](https://marginalrevolution.com/marginalrevolution/2025/02/deep-research.html) nicely captures both the positive view (in the content) and the negative view (in the comments and responses). As another example, consider this commentary piece in [Science](https://www.science.org/content/blog-post/evaluation-deep-research-performance) from Derek Lowe.

Well, to know that for sure whether we can get 8 hours of human knowledge work in 10 minutes, we’d probably want to do a very thorough comparison.

Here is OpenAI’s Deep Research [release](https://openai.com/index/introducing-deep-research/). Three benchmarks are mentioned: HLE, GAIA, and “internal evaluation of expert-level tasks”. We get three examples, which are claimed to have saved 4, 5, and 2 hours. Presumably these used some binary pass/fail rating scheme (we see a “Pass Rate” mentioned): the experts “approved” the answers. It’s unclear if the experts estimated the time needed, or if they actually worked until they reached some quality threshold (determined by other experts?) and then paused their stopwatch. We’ll get more info down the line: “We will share our safety insights and safeguards for deep research in a system card when we widen access to Plus users.”

Why harp on this? Evaluating “deep research” across past and future areas of human inquiry will take immense manual labour.

## What could a very thorough evaluation process look like?

Well, we’d probably want to start by getting a group of white-collar workers to agree to sign on to produce points of comparison. Ideally (in terms of richness of data — especially if we want to compare the process used, the intermediate states of the output artifacts, etc.), they’d agree to be monitored — perhaps via a webcam and/or screen capture. Getting very fine-grained data would involve surveillance technology similar to that used to monitor students taking remote exams during COVID. Generally, this kind of software can [be](https://www.nbcnews.com/think/opinion/remote-testing-monitored-ai-failing-students-forced-undergo-it-ncna1246769) [distressing](https://www.technologyreview.com/2020/08/07/1006132/software-algorithms-proctoring-online-tests-ai-ethics/) to use. Of course, in the context of working as a distinguished data evaluator in the service of humanity, perhaps people would be fine with it.

It seems likely this kind of surveilled-knowledge-work-data-labor has happened quite a bit already, and will happen even more, but probably in relative secrecy (i.e. of similar level of transparency to operations of an organization like Scale AI — that is to say, pretty opaque to the general public). I think the optics of this are going to be very bad, because some of this evaluation work will be ramping up in conjunction with disruptive job market impacts. That is, people will viscerally see movement towards a more precarious overall economy for most workers. The AI industry may start to hold blame in the eyes of the public for a rollback in cushiness of (some) knowledge work.

Perhaps this whole surveillance process is overkill. Could we build a pretty decent evaluation set just by asking people to send in their “human deep research report” and self-reported data about time use? In practice, many timesheet-based knowledge workers do this and it works fine. And, this is what many existing benchmarks already look like, and may be what the evals mentioned in the Deep Research release post look like as well.

However, I actually think the surveillance approach will be necessary, and here’s why: LLMs have already become embedded in knowledge work. They’re being used in crowdwork, and there’s increasing consensus that for some types of assignments they have effectively trivialized unsupervised homework.

It’s going to be very important to have relatively “pure” evals for those evals to mean anything (I personally think this feedback loop is even more concerning than “model collapse” — more on this in another post).

## One quick bout of napkin math

To illustrate the idea that evaluation labor is going to take a lot of human-hours, we might run through one quick bout of napkin math. Looking at the three examples provided by OpenAI, we might assume that one Deep Research query is “valued” at 5 hours of time (and that more complex queries take more time to compare).

Let’s value our expert billing rate at $200/hr (of course, successful coordination by AI operators could drive this down; successful coordination by data intermediaries could drive it up).

So, using English Wikipedia as a proxy (with numerous caveats) for how many “articles” make up human knowledge, let’s say we want to produce a deep research-level report for 1/10 of Wikipedia’s almost 7M articles (~700k reports, 5 hours per question, $200/hr): this will require 700M of labor costs (small beans compared to 11 trillion [needed](https://github.com/nickmvincent/data_napkin_math) to commission a brand new LLM dataset from scratch). But if we then want to double check our work (get 2 people per report), we’re paying 1.4B. If we want to robustly measure variances and inter-rater reliability, we might be looking at tens of billions — that could eat an entire fundraising round for an AI start-up!

And critically, for any domain in which the relevant experts are able to organize, **they could bargain around this evaluation contract.** Knowledge workers in a given domain could easily make it functionally impossible to measure how well AI is doing in that domain.

## Evaluation data leverage

Right now, a variety of tools exist, and there are very heterogeneous perspectives on their usefulness. You can find strong examples showing apparent utility alongside very strong examples of negative utility. There’s certainly some motivated reasoning going on here on both sides, and there’s plenty of precedent for public opinion being split on new technology.

But this situation is somewhat unique, because the explicit goal of extreme generality makes the evaluation of “AI” a very collective human task. Compare this to evaluating vacuum cleaners — a relatively small set of people can cover all the edge cases for a vacuum cleaner. But for a research agent, we ideally want to model, well, everybody who does research. And if this agent is supposed to be used by consumers, we also want to model… every consumer.

I’ve long argued for a “We all helped achieve this” framing for discussing the production of LLMs (with the caveat that of course, the distribution of credit is not literally uniform). And almost by definition, serious evaluation of general AI will require similar, if not greater, large-scale coordination.

We will still have leverage through our training data, though the magnitude of this leverage is highly contingent on pending legal decisions, regulatory action (or lack thereof), and answering technical questions about data protection technology. Organizing collective action when your estimated leverage is very volatile is a scary prospect and not useful for movement building.

This means that if I had to pick the most “stable” form of data leverage right, it would be data action specifically aimed at the evaluation side of things.

Putting things another way, if I could give advice to a billionaire interested in AI safety who was open to a “data leverage” approach, it would be to directly fund organizing efforts for existing data workers and to begin raising awareness about evaluation leverage for general knowledge workers.

## Will Evaluation Leverage Actually Happen?

I believe there is a high probability that evaluation data leverage will become significant—and in some cases, it may already be taking shape. In particular, I expect evaluation data leverage to be especially useful for, and used by, organizations that represent professionalized labour, e.g. medicine and law.

On the other hand, an area where evaluation data leverage will face serious challenges is in the general white-collar workplace. These contexts rarely have collective bargaining for employees and employees typically have no rights over the intellectual property they produce or other outputs. In large firms, I expect employers to add more draconian surveillance style that basically converts more existing knowledge work into AI eval work (in fact, some firms may have already run their own bespoke evals of Deep Research because they actually have detailed logs of employees producing similar outputs). In other words, white-collar workers will probably get a new set of tasks — moonlighting as AI evaluators.

## Fitting this into past frameworks

In the original data leverage framework [paper](https://arxiv.org/abs/2012.09995), we primarily compare and contrast different types of actions: data strikes, data poisoning, and leverage through conscious data contribution. In a follow-up [paper](https://arxiv.org/pdf/2305.13238), we taxonomized data labor, with a focus on six particular dimensions: for a given data-generating activity that produces some valuable record: (1) is the data labor legible to the creator, (2) is the creator aware of the end-use for that data, (3) does the creator collaborate with others to produce the data, (4) is the data eventually made “open”, (5) how “replaceable” (vs specialized) in the activity, and (6) is the data-generating activity part of the creator’s set of “livelihood generating activities” (i.e., are they doing this as part of their job?)

## What Makes Eval Data Eval Data?

Of course, it’s interesting to note that there’s nothing that makes eval data special other than the fact that the data is used for evaluation. In fact, the more special handling applied to the production of eval data, the less useful it is, because we typically want to know performance for our “true” distribution (or as close as we can get).

In other words, we can’t actually look at a document and say whether it’s “eval” or “training”. **This means for a data laborer, access to “evaluation-specific leverage” is about end use-awareness.**

Critically, this means eval leverage waxes and wanes. Immediately after the release of deep research agents (which are perhaps being pushed out more quickly than planned due to market race dynamics) is the full moon for eval leverage in this context.
