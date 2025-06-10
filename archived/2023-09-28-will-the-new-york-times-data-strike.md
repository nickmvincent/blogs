---
title: "Will The New York Times Data Strike"
subtitle: "How can we start thinking about how opt-out decisions by content-producing organizations will affect LLMs?"
date: 2023-09-28
original_url: "https://dataleverage.substack.com/p/will-the-new-york-times-data-strike"
---

> **Original Substack post:** [https://dataleverage.substack.com/p/will-the-new-york-times-data-strike](https://dataleverage.substack.com/p/will-the-new-york-times-data-strike)

![moon photo](https://images.unsplash.com/photo-1447433516455-abac93050eab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80 "moon photo")

*Image from NASA, hosted on [unsplash](https://unsplash.com/photos/lEBDlbXLEgs).*

In a previous post, I discussed how the decision by the New York Times to opt out of large language model (LLM) training might be a sign that we’re entering the era of the data strike, and a new paradigm for content creation and sharing.

Since that article was posted, we have indeed seen a large number of organizations [follow suit](https://palewi.re/docs/news-homepages/openai-gptbot-robotstxt.html). As of September 28th, there’s at least 490 news organizations who have asked GPTBot to stay away.

Then, we saw another development: the announcement of [browsing-enabled ChatGPT](https://www.reuters.com/technology/openai-says-chatgpt-can-now-browse-internet-2023-09-27/), which may seriously change the incentives around how organizations want their content platforms to connect with LLM technologies. This will likely warrant its own post, as the sudden potential to see traffic from ChatGPT is likely to reshape the decision landscape, in ways that may hearken back to early discussions about search engines and content.

With these developments top of mind, an important question is likely top of mind for the NYT and other opting-out news organizations: when will a data strike be impactful?

We might also consider the very broad version of this question: for a variety of different groups we might imagine conducting a data strike (e.g. “just the New York Times”, “a coalition of all major newspapers”, “everyone in the United States”), how does potential impact (what we’ve called “[data leverage power](https://dl.acm.org/doi/pdf/10.1145/3449177)”) vary?

Across these groups, we’d expect to see a distribution of different data leverage power values: everyone in the US banding together to opt out would have quite a large impact on ChatGPT (and co.), and if I begin a one-person data strike by myself, it will have basically no impact. Other groups fall somewhere in between.

What the NYT probably cares about is this: “*Is our content sufficiently impactful that the loss of our data will meet some threshold of performance loss such that OpenAI or others want to negotiate with us?*” In other words, “*Do we have enough leverage?*”

While answering this question requires a great deal of effort (and is a topic of ongoing research), I think we can actually draw some insight from earlier [research](https://dl.acm.org/doi/10.1145/3308558.3313742) we conducted on data strikes in the context of recommender systems. There, we saw different subgroups of movie fans (e.g. “film noir fans”, “comedy fans”) were quite varied in terms of their ability to “punch above their weight”. In some cases, it seems niche groups could have outsized impact. In the extreme, a group of film noir fans could band together to make a recommender system “unlearn” the existence of film noir as a genre.

One key takeaway from that research is that our ability to evaluate the impacts of data strikes is highly dependent on the extent to which a given data strike might change the test sets that AI developers use. In other words, there’s an issue of circularity: evaluating LLM performance (and AI performance in general) requires a stable “test set”: opt out decisions will invariably change this test set and thus fundamentally impact our very definition of “AI capabilities”.

One very interesting possibility is that a particularly large data strike might prevent an AI developer from even *testing* their model in a certain context (because, e.g. they have no journalistic content to create a journalism focused benchmark).

Transferring this insight from the movie recommendation domain to the news domain, this suggests that content like news may have two distinct sources of value: the easy to measure impact of making a technology aware of an event (i.e., value as a knowledge base) and the hard measure impact on broad LLM capabilities (i.e., value from teaching ChatGPT to write like a journalist). If my outlet is the only outlet that covered a news story and I withhold my content, LLMs won’t know about that event (though in time, other outlets will presumably cover the event as well).

LLMs use much, much, much bigger training datasets than academic movie recommender experiments. But, I’d conjecture that there’s a shared concept that unites data strikes against a small movie recommender and a data strikes against a large language model: a group’s ability to effectively data strike relates to how much of the full dataset’s “similar content” the group itself covers. The intuition here is this: if the NYT goes on strike, but the LA Times and Washington Post don’t, ChatGPT’s general capabilities of “write in a journalistic style” might not see much of a dip (though the disappearance “exclusive coverage” from the NYT might make a big splash).

A key idea here is that for any given set of content we might produce as individuals or part of a group, there’s probably some other set of content out there that can serve as a substitute. We must acknowledge this fact as we think about data-related negotiations in this new era of content.

Put simply, some documents are “closer” (in some sense) to each other than to other documents; the New York Times articles are all close to each other, probably pretty close to LA Times articles, and probably decently far from something like a long legal paper or a Twitter thread.

It probably matters that when attempting a data strike aimed at knocking out a specific capability (“write in the style of journalists”), organizers are able to get a good portion of people who contribute content “close” to that capability involved (though some very recent data-focused interpretability [work](https://www.anthropic.com/index/influence-functions) discussed below complicates this picture a bit). To use jargon for just a sentence, it’ll probably be possible to conceptualize data strike effectiveness in terms of how different groups achieve “coverage” of regions of latent space.

A very exciting direction of technical research will involve figuring out the best definition of closeness that is able to predict the specific impacts of different bargaining outcome and collective action campaigns on LLM capabilities.

Additionally, finding *thresholds* for similarity at which this idea holds is an important area of future research: would a data strike by Python coders be threatened if people who code in other programming languages don’t join in? It seems possible! Similarly, are there organizations or platforms with a lot of journalistic-esque content that could threaten the leverage of the NYT data strike?

In short, if all major news organizations were to engage in a joint data strike, I think we can be quite confident in predicting that “post-strike” LLMs would exhibit qualitative and quantitative differences in output. But if it’s just the New York Times alone, it’s harder to say.

## Measuring a Data Strike’s Impact

After a successful data strike (via legal action, or just via an opt-out form), the NYT or the regulators might want to see if it was really successful. They might try some tests along the lines of recent [research](https://arxiv.org/abs/2305.00118) that’s looked into propensity to complete copyrighted materials (see also evaluation efforts like recent work from [Liu et al](https://arxiv.org/abs/2308.05374), covered by [Business Insider](https://www.businessinsider.com/openais-latest-chatgpt-version-hides-training-on-copyrighted-material-2023-8)).

However, as noted above, if ChatGPT still has access to tons of articles from very similar publications, it might be the case that auditors don’t see much evidence that ChatGPT’s capabilities qualitatively changed.

What’s more, a model that has access to New York Times content but has been specially tuned to not output this content verbatim might look the “most innocent of all” in one of these audits. There are open technical questions here that probably involve combining work on memorization, machine unlearning and [concept erasure](https://arxiv.org/abs/2306.03819).

Overall, from the perspective of an external auditor working with a black box LLM, it will probably be hard to tell if a given organization’s content was truly “wiped" from training data, and thus also challenging to tell how much impact a data strike had on an LLM. This is a critical concern for organizers of collective action. In the EU, there are ongoing discussions about [data transparency](https://techcrunch.com/2023/05/11/eu-ai-act-mep-committee-votes/?guccounter=1) laws that could seriously change the landscape here, likely shifting power towards data creators

Of course, if a major LLM operator actually has to completely retrain a model with no NYT content (which would have some serious logistical concerns, discussed below), they’ll know the exact impact. We might also ask whether AI operators themselves are able to preemptively estimate the impact? There are actually two very recent lines of work that suggest answering this question is indeed becoming more viable.

One approach might be to keep the LLM architecture the same, but use a data valuation procedure to estimate "how big of a change would we see if this training data were added or removed?" In fact, Anthropic has published research presenting one method to do [exactly that.](https://www.anthropic.com/index/influence-functions)

It could make sense to actually partially train a fresh model without a certain subset of data and compare performance directly – this is generally what influence functions and other data valuation techniques aim to approximate. The main argument against doing this is that it would be very expensive. A pragmatic compromise that attempts to make things a bit easier for AI operators might be setting standards about regular intervals at which retraining happens (perhaps there’s a speculative fiction piece to be written about the many implications of “Retraining Day” as a new global holiday).

Another approach for estimating data value might be using the “[SILO](https://arxiv.org/abs/2308.04430)” architecture proposed in recent research: create a pretraining set with only truly public domain data and put potentially licensed and licensable content in a siloed off “data store”.

This allowed the researchers who proposed this architecture to directly test questions like “say we give the model access to six of the Harry Potter books and ask it to generate the 7th; how does performance compare when it has access to no Harry Potter books?” This architecture is also able to directly attribute outputs to certain sentences in the training data (e.g., quoting a passage from a Harry Potter book directly).

## Connections with Reddit’s Data Strike and the Moderation Strike at Stack Exchange

The NYT is not alone in starting a data strike aimed specifically at gaining leverage over LLM operators. Reddit recently announced a similar [initiative](https://arstechnica.com/information-technology/2023/04/reddit-will-start-charging-ai-models-learning-from-its-extremely-human-archives/) (see this previous [post](https://dataleverage.substack.com/p/reddit-stackoverflow-and-europe-all)).

Both of these organizations are profit-driven private firms. But their content may have, at times, seemed like a commons. Some NYT content is free to Internet users, and search engines, social media sites, and chatbots generally benefit from access to NYT content (because end-users ultimately want to consume this content). Similarly, Reddit data has effectively acted as a commons for the purposes of [AI research](https://en.wikipedia.org/wiki/GPT-2) and other [computational social science](https://ojs.aaai.org/index.php/ICWSM/article/view/7347).

Neither of these platforms ever operated a true commons, and were always reliant on ad revenue to keep the servers running. But now it seems the flashes of commons-esque access patterns may be disappearing. We might characterize this as an [enclosure](https://en.wikipedia.org/wiki/Enclosure) of the pseudo-commons. This is further complicated by the fact that the free ChatGPT (and Claude, Bard, etc.) also have a pseudo-commons character. If the NYT and Reddit are successful in harming LLM capabilities to gain leverage, we may see short term “welfare drops” (to the extent one believes LLMs do provide users utility).

It’s interesting to contrast this with a platform like Stack Overflow. It seems like the platform that was more explicitly framed as a commons has weathered things better so far: recent battles between volunteer moderators and leadership have at least led to some degree of [collective bargaining](https://meta.stackexchange.com/questions/391847/moderation-strike-results-of-negotiations?cb=1) and iteration on AI-related policies. The data, which has always been shared via Creative Commons (with some [serious](https://meta.stackexchange.com/questions/333089/stack-exchange-and-stack-overflow-have-moved-to-cc-by-sa-4-0) [contention](https://meta.stackexchange.com/questions/344491/an-update-on-creative-commons-licensing.) around slight changes to licensing), remains open for now.

On a platform like the NYT or Reddit, there’s some major variance in how much each reader contributes to firm revenue. Lots of content on the Internet pre-generative AI falls into an ambiguous space where in practice, only some fraction of content consumers directly pay or provide high value as an ad consumer. It seems that the generative AI wave may ultimately lead to some reduction of this ambiguity, which might in turn lead to less overall readership/consumption (but more consumption that happens as part of an explicit economic transaction).

## Conclusion

Ultimately, I am a big believer that supporting group-level data agency will push the AI ecosystem away from harmful uses and towards broadly shared benefits. In more words: in the very long run, one of the most important things we can do to slowly steer AI operators into building a multiplicity of AI systems that, together, embody a plurality of human values (as opposed to embodying the values of a few powerful people) held across the world is to make it easier for people to control how their data contributions flow to AI systems. Importantly, I also think data-related actions, especially opt-out actions should be undertaken primarily at the group level and not the individual level.

Thus, from a somewhat long-view, academic-hat perspective I think the fact that organizations like the NYT and Reddit are “flexing their data leverage muscles” is very important in principle, regardless of the actual outcomes in the next 3-6 months (and even if it this the case that LLMs continue to promote consumer welfare). I think that at some point, it’s very important that some organization tests out the legal and technical landscape here, even if in the long run the vast majority of data-based collective bargaining relies mainly on the *threat* of collective action. Data strikes in the wild will help us understand the role of public opinion, how people perceive their role as simultaneous users and creators of AI (see e.g. writing on [heteromation](https://firstmonday.org/ojs/index.php/fm/article/view/5331/4090), [prosumers](https://en.wikipedia.org/wiki/Prosumer), [data dignity](https://www.radicalxchange.org/concepts/data-dignity/)).

From a practical perspective, I do think the NYT’s strike efficacy ([data leverage power](https://dl.acm.org/doi/pdf/10.1145/3449177)) could be inhibited by a lack of coalition building with other news organizations (or even groups like academic professional organizations). This may limit their leverage, and could make other organizations more hesitant to try data strikes of their own. The fact that other organizations are following suit with robots.txt is important to note.

I am deeply excited about progress in data valuation and attribution. I do think the fundamental challenges with external auditing may not be getting enough attention, but am hoping that perhaps sharing valuation and attribution as part of the collective bargaining process could be viable in the long run. For instance, perhaps AI operators can be incentivized to share influence estimates that capture the likely impact of an NYT-strike or an all-news-orgs-strike as part of a bargaining process. Here, some kind of public body for AI might play a key role as a mediator of new kinds of generative AI-era bargaining agreements.

Finally, I do worry that a paradigm in which models are constantly being destroyed and retrained on the basis of constant ongoing legal battles will lead to a net negative effect on consumer welfare and stymy potential gains in scientific progress that accompany generative AI. There does seem to be a serious risk that public discussions on these topics become even more polarized and miss out on the nuances in present benefits and harms. But, I think finding a balance of opting out and in, of contribution of strikes, of creation and destruction is totally viable and will be to the net benefit of humanity.

[Subscribe now](https://dataleverage.substack.com/subscribe?)
