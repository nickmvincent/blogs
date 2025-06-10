---
title: "Is Zuckerberg Right To Say That Your"
subtitle: "Examining the Meta CEO's claim that the "individual work of most creators isn’t valuable enough for it to matter" in the context of AI training."
date: 2024-09-28
original_url: "https://dataleverage.substack.com/p/is-zuckerberg-right-to-say-that-your"
---

> **Original Substack post:** [https://dataleverage.substack.com/p/is-zuckerberg-right-to-say-that-your](https://dataleverage.substack.com/p/is-zuckerberg-right-to-say-that-your)

![herd of horse traveling on grass hill during day](https://images.unsplash.com/photo-1505494978186-6cde6324454b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHw5fHxoZXJkfGVufDB8fHx8MTcyNzU1MTAxNXww&ixlib=rb-4.0.3&q=80&w=1080 "herd of horse traveling on grass hill during day")

The Verge recently published an [interview](https://www.theverge.com/2024/9/25/24254042/mark-zuckerberg-creators-value-ai-meta) with Meta CEO Mark Zuckerberg. This article leads with a potentially provocative claim: both individual creators (e.g., a blogger or YouTuber) and publishers (e.g., a news outlet) “tend to overestimate the value of their specific content”. Zuckerberg goes on to say that if individuals or organizations opt out from training, Meta might choose to simply ignore their data with minimal loss of AI performance. This stance echoes how Meta has treated news organizations making demands of Meta in Canada and Australia (i.e., just [implementing a news ban](https://www.cbc.ca/news/business/meta-block-news-1.7174031)).

Is this claim true?

Thanks for reading Data Leverage! Subscribe for free to receive new posts and support my work.

First of all, there’s a falsifiable technical claim here about the average leave-one-out influence of any individual or group on important benchmark scores. In other words, we could try to answer the implied question here — “What is the exact impact of *your* content or *your publisher’s content* on an AI model” — by setting up experiments to answer questions such as, “If we train a model without your content, what questions does the new AI system get wrong, what facts does it forget, and what new errors does it make?”

Of course retraining an entire model just to check the value of one individual’s content might seem excessive, but that’s where the still growing field of *[training data influence estimation](https://arxiv.org/abs/2212.04612)* and *[data attribution](https://arxiv.org/abs/2303.14186)* comes in. Major players like Anthropic are working on enhancing these [techniques](https://www.anthropic.com/research/influence-functions); this line of work may very well carry over to data bargaining.

So, if we interpret the claim that the"individual work of most creators isn’t valuable enough for it to matter" as, “the average influence — whether an estimated “leave-one-out score” or related definition of influence — of a given individual or small organization is nearly zero for the benchmarks of interest to Meta”, I think that claim is true, and it’s important to face it head on. We do need to be realistic about this fact; if you were to get a paycheck *tomorrow* based on your contributions to AI, it would likely be quite small. Furthermore, the exact methods used to estimate your individual contributions might feel fickle, and implemented poorly, could even increase [economic inequality](http://www.nickmvincent.com/static/eaamo_data_dividends.pdf) (if most people get 50 cents and a few people get a windfall).

However, hidden in Zuckerberg’s claim is an assumption about the organizing power of data creators. If individuals or publishers are able to band together and coordinate about access to their creative works, the game is changed. It’s uncontroversial to note that when it comes to wages for labour, in many fields one’s wages are not purely determined by individual merit, but rather are directly related to access to collective bargaining. The same thing is true for emerging “AI content deals”.

So perhaps a more explicit version of the above quote might be: "the individual work of most creators isn’t valuable enough for it to matter, if we assume these creators are never able to coordinate for the purposes of bargaining". Consider the extreme in which everybody demands a stop to training; in this world, the production of AI models would essentially grind to a halt (I should clarify my stance: I don’t think this would be a good thing, and I think Meta and others’ AI models have societal benefits; but we should recognize this potential leverage).

So, it’s true that many people may be overestimating the value of their individual work in a world in which they need to bargain on their own, but they may actually be underestimating their bargaining power with sufficient coordination.

Maybe Mark’s implicit “there’s no way you could organize well enough to threaten our current model” is true; after all, don’t we have many reasons to be broadly pessimistic about how humans address social dilemmas? While I think there’s a lot of hard work to be done to make collective bargaining around data viable and mainstream, I also think it is viable. A key factor to consider is in many ways, online collective action can be easier than offline equivalents; I could potentially just “click join” to become part of a data [intermediary](https://hbr.org/2018/09/a-blueprint-for-a-better-digital-society) and then the actual questions of data [escrow](https://raulcastrofernandez.com/papers/data_station_paper-11.pdf) and sharing can be handled by computing systems.

So, I think Zuckerberg’s point here does stem from some cold hard facts about how leave-one-out scores and other influence values are distributed among observations for models trained on very large datasets. But, there’s a very strong serious chance that an attitude that dismisses the possibility of effective bargaining by content creators could backfire, contingent on some combination of regulatory, grassroots, and within-industry support for entities that engage in data bargaining.

Zuckerberg also states that when it comes to fair use and licensing, “I think that all these things are basically going to need to get relitigated and rediscussed in the AI era.” I absolutely agree on this front; we’re going to need to consider new models that fall somewhere in between a complete free-for-all and a complete retreat into walled fortresses of information.

There’s no doubt that like other companies producing AI models, Meta is providing a lot of value for the world (in particular, sharing the Llama model weights is definitely facilitating academic and public interest research on LLMs) while simultaneously creating the potential for severe economic impacts and major disruptions to the digital ecology of online platforms where creation and curation happen. In the long run, setting up societal frameworks for this kind of bargaining will, I think, be net beneficial, even if it causes some friction in the short term.

*Edits:*

* *Sep 28. fixed several typos (line work → line of work, in many field → in many fields)*

Thanks for reading Data Leverage! Subscribe for free to receive new posts and support my work.
