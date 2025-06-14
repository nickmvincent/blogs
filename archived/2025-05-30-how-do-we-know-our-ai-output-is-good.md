---
title: "How Do We Know Our Ai Output Is Good"
subtitle: "Connecting evaluation and dataset documentation via the lens of "AI as ranking"."
date: 2025-05-30
original_url: "https://dataleverage.substack.com/p/how-do-we-know-our-ai-output-is-good"
---

> **Original Substack post:** [https://dataleverage.substack.com/p/how-do-we-know-our-ai-output-is-good](https://dataleverage.substack.com/p/how-do-we-know-our-ai-output-is-good)

![File:Operation of trains and station work and telegraphy (1914) (14737911176).jpg](https://substack-post-media.s3.amazonaws.com/public/images/420a8f89-e9e1-4aee-a2ba-79d2ca786cf7\_960x509.jpeg "File:Operation of trains and station work and telegraphy (1914) (14737911176).jpg")

Having argued that it’s useful to view many types of AI systems through the lens of ranking previous bundles and chunks of human-recorded information ([post 1](https://dataleverage.substack.com/p/google-and-tiktok-rank-bundles-of), [post 2](https://dataleverage.substack.com/p/each-instance-of-ai-utility-stems)), we now turn to some intersections between this framing and the evaluation of AI products.

In this post, we’ll discuss the current challenges with evaluating AI (much ink has [already](https://arxiv.org/abs/2502.06559v1) [been](https://arxiv.org/abs/2504.20879) [spilled](https://simonwillison.net/2025/Apr/30/criticism-of-the-chatbot-arena/)) and then link these challenges back to the topics of dataset documentation and data leverage.

Imagine you’ve just asked ChatGPT/Claude/Gemini/Copilot/Deepseek some questions. Perhaps they were like one of these prompts:

* Tell me about some influential advisors who played major roles in various civilizations during the ancient history period.
* What is the most effective approach to reduce ulnar wrist pain?
* What is the most famous restaurant in Chicago?

For each of these types of questions (and many more), each major commercial AI product will now give you a great-looking answer. Having hand-picked these examples and tried them out, I can also say the quality of these specific answers are decent. If we buy the arguments from previous posts, we might view these answers as “ranked chunks” of prior human records (and if we use a web search enabled AI products, we might also get some ranked bundles).

But we’re still left with quite a few questions. Are the answers all equally good? Which specific answers are good? Which model is best? (Again: these questions are not new, have been hotly discussed and debated, and presumably every major lab is fervently trying to answer these internally).

To answer these question as a user, we actually have a few options! If we want to be very principled about our epistemics, then we might want to do something like create a comprehensive and systematic test bank (our own personalized “benchmark”, like “[Humanity’s Last Exam](https://agi.safe.ai/)”) and evaluate each model. But maybe we just want to be pragmatic consumers who don’t spend a lot of time thinking about these issues (so we just go with our gut), or maybe we want to find some middle ground (do some double checks, but only here and there?).

![](https://substack-post-media.s3.amazonaws.com/public/images/256b8be7-fea3-4fbd-a493-9a44d8d98bfc\_2052x1318.png "")

First, we might check what the AI “says on the box”. Do these systems even claim to be accurate? Do they tell us about their confidence in a given answer? ChatGPT says: “ChatGPT can make mistakes. Check important info.” Gemini says “Gemini can make mistakes, so double-check it”. Claude says something similar, and links to a dedicated [help page](https://support.anthropic.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on).

So, officially speaking, any time we make an AI query, we should be double-checking it. This seems be great — if we follow the instructions to the letter, we’ll naturally calculate our own internal accuracy scores for these products. We can simply subscribe to all the AI products, keep score as instructed for a month or so, and then we’ll know what’s best.

But in practice, it’s not so simple. First of all, it seems enormously unlikely that people will actually do this (nice example: [database](https://www.polarislab.org/ai-law-tracker.html) of hallucinated references in law). Some people might even start to wonder: “If I need to double check every response, what am I paying tens or hundreds of dollars a month for?” There is some interesting “data napkin math” to be done here about how long double checks actually take, how people value their time and value AI products, and so on.

Further, it’s unclear in the current interfaces what specific steps the user is meant to take to perform a “double check”. Are we pasting the query into Google (which might give us another AI overview)? Or, are we meant to find and read a primary source that gets at the core of our informational query? Presumably, the intended interpretation is closer to this. For some fraction of all our queries to AI, we should also be reading from academics journals and newspapers (which is not totally unreasonable with current products[1](#footnote-1), and could even be enforced or more strongly promoted[2](#footnote-2)).

The process of “double checking” is also a reminder of what most AI systems are currently doing: delivering us information (to check an answer, we probably need to get more information via some other pathway).

![](https://substack-post-media.s3.amazonaws.com/public/images/d43ddadb-b814-4a86-bc86-b70554c47303\_1018x318.png "")

## Bar charts and Vibes

So, every AI tool tells us to double check things, but none of the major AI products (to my knowledge) are actually taking this very seriously in terms of enforcement or norm setting (not to say it’s an easy problem: again, I don’t think paying consumers will react well to a pop-up that says “Hey, it looks like you haven’t done any double-checking labour in past few hours. Get to work!”).

So what are people using to make their decisions in practice? Two options are (1) the bar charts (and other summaries) that labs are putting out alongside model releases to summarize performance across different domains and (2) vibes from social media, word of mouth, brand recognition, and related factors.

![](https://substack-post-media.s3.amazonaws.com/public/images/35d30cce-a3e7-4865-9256-dcdd76b004d0\_1606x1208.png "")

My guess is the latter constellation (vibes/word of mouth/brand) is currently more influential: I think right now, tweets about how “Claude is the best for coding!”, or “Gemini’s context window is so good!” are playing a larger role than benchmark bar charts or Chatbot Arena scores (which have recently come under [some](https://simonwillison.net/2025/Apr/30/criticism-of-the-chatbot-arena/) fire). Ultimately, ChatGPT remains dominant in market share, and there’s a strong argument to be made that is in large part based on early brand value creation and word of mouth, and benchmarks have thus far had very little impact on market share stats.

Again, while not perhaps a ideal, this all makes sense from a pragmatic perspective. As we discussed in the [Eval Data Leverage post](https://dataleverage.substack.com/p/evaluation-data-leverage-advances), there simply hasn’t been enough time for most users to fully assess these new models across the breadth of possible use cases, so we have to go off something like bar charts or vibes.

## Dataset details as quality signals

Of course this was going to circle back to data. In “[Selling AGI like AG1: Will Consumers Push Back Against Proprietary Blends of Herbs and of Data?](https://dataleverage.substack.com/p/selling-agi-like-ag1-will-the-market)”, I made the case that perhaps down the line, dataset information will actually become an important signal for consumers.

Concretely, I think that it might become compelling to advertise an AI product with some messaging around “we got 10,000 hours of labour from scientific experts that went into post-training and evaluation”. This would be a proxy for “model will perform well on scientific tasks”. In other words, it would aiming to communicate the same thing as a benchmark bar chart saying “Look, our model is really good at science”. But, if consumers don’t understand or trust the process by which the bar chart was constructed, details about the data might be compelling.

To be clear, ideally we’d want both: transparency in data and transparency in evals. But at the end of the day, these two things should be highly related. While of course there are situations where a model could have lots of data from domain X but do bad on a benchmark from that domain, or it could be the case that a model could do well on a benchmark without much data from the domain, *in general* we’d expect tight coupling between training choices and evaluation performance, because *that’s what statistical learning underlying these technologies is trying to achieve*.

Hence, if we conduct a dataset documentation [effort](https://arxiv.org/abs/2403.13073) aimed at estimating the prevalence of a group of people’s contribution to a training dataset, we might expect that measure (which we could call something like “estimated intellectual property dispossession” — a concept that certainly makes some normative claims but is distinct from actual legal outcomes re: IP and AI) to tell us about how likely that group is to be affected by AI-based substitution.

## Approaches for measuring this tight coupling

There are a number of technical approaches for understanding the coupling between model inputs and outputs. One specific field of research we could look to that helps concretize this is work on “membership inference attacks”. To quote [Hayes et al.](https://arxiv.org/abs/2505.18773) in recent work on the topic, an MIA is when “an adversary aims to determine whether a specific data record was part of a model’s training set”. In short, these attacks work well against small models, but computational challenges make it hard to use MIAs against larger models; the work from Hayes et al. shows it is still possible to conduct such attacks, with nuances.

Membership inference gives us one lens to quantify the connection between AI inputs and outputs. Other related frames include [training data extraction](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting), [memorization](https://openreview.net/forum?id=TatRHT_1cK), and even [differential privacy](https://www.nowpublishers.com/article/Details/TCS-042). But even relatively straightforward benchmarks that are grouped by topic or domain should point us on the right track of guessing, in general, what was in the training data.

## Tying this back to AI utility and acts of ranking

So, finally, having walked through double checks, bar charts, vibes, and the coupling between training data and model outputs, I want make an argument connecting this discussion to the idea that “[Each Instance of "AI Utility" stems from some human act(s) of information recording and ranking](https://dataleverage.substack.com/p/each-instance-of-ai-utility-stems)”.

Both search results and AI answers are useful because some human somewhere recorded information. All these tools are competing to deliver us bundles or remixed chunks of information — which is hard, we have limited attention! (And critically, this means that of course tech and AI companies are providing lots of value; the original value of an AI output can be traced to human records, but the ranking is critical too).

We might even go a step further and say that each AI output actually represents some weighted combination of every possible chunk of information that’s out there. And when we use AI models, we’re making our decision through either formal or informal feedback about whether the weighted combination of chunks of information we got met our needs (and could have met our needs even better).

A variety of implications:

* For dataset documentation: This all makes the documentation of training (including post-training!) data all the more important. If each question we pose to ChatGPT is fundamentally a request to rank all the information available to the system — in both chunks and in bundles — and deliver us some weighted combination of information that we will use to act, we probably **really** want to know about the upstream information.
* For AI Social Simulations: Authors have argued in [favour](https://arxiv.org/abs/2504.02234) of using LLMs for social simulation (and other authors have raised serious [concerns](https://dl.acm.org/doi/full/10.1145/3613904.3642703)). The ranking-data-labour framing can be further clarifying when we think about things like AI social simulations: a simulation of people using LLMs to take actions could have real epistemic value if the ranking system delivers information that’s derived from real people in relevant situations. But, there will always be many ways that a model might deliver us information that has a neutral or harmful effect on the overall utility we get out of said simulation.

  + Dataset documentation would really help here!
* For decision making more generally: The ranking framing can also be helpful for thinking about the morality of using AI in any given decision process (which has received substantial attention [over](https://www.nature.com/articles/s43586-022-00172-0.epdf?sharing_token=20oCMhzni41xvDUut2OItdRgN0jAjWel9jnR3ZoTv0OwjbZm_FCT7gsPxkyDixLb1Sapyw-rKunjdUM-MQsb2Df0fuyC5afG4elbIDnGjYVTr4j3hlrQ7YmaASLl3Q0UKi5thaNq9gvVPV-cT8IZm9wh7kXFdLAzLh60tNgS2gE%3D) [the](https://arxiv.org/abs/2005.04176) years). If a person makes the decision on their own, they incorporate various information that's stored in their brain, or that is otherwise available to them. AI models make different information available, but there are many ways that this additional information could be unjust or harmful.

  + Again, this suggests that if we use AI for decision making, a deep understanding of both the training data and summarized evals would be extremely helpful.

At the end of the day, as AI gets rolled out more widely in society, we’re collectively going to be running more computations in which we “assign weights” over all the information that humans have ever put into our records. We’re going to want to understand what’s being weighted, whether through systematic evaluation, systematic dataset documentation, or some combination of the two (and perhaps also systematic inspection of model internals!).

When we’re designing AI products, grand “public AI” proposals, or schemes for new data markets or collective bargaining apparatuses, this framing can (I believe) help us do a better job about reasoning about how and when to use AI.

[1](#footnote-anchor-1)

As more tools incorporate heavy use of search and links, I do think it’s getting more reasonable to check things. Personally, I do actually find myself actually clicking links provided by o3 and Gemini 2.5 and generally finding the experience reasonable and useful. In particular, I think using o3 in conjunction with web search and scholarly search engines is extremely useful! But I think there’s still going to be a lot of resistance to checking things often and the “logically extreme interpretation” — that people are going to double check every “important query” to the product they’re paying hundreds of dollars a month for — is a bit absurd.

[2](#footnote-anchor-2)

It could be interesting to imagine an “AI” tool which does actually expect and/or enforce that users do fact verification at some regular interval (and perhaps every user is explicitly conscripted into some kind of knowledge maintenance project). But such tools would not be marketed, or priced, the way that current offerings are.
