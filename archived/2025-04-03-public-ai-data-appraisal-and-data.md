---
title: "Public Ai Data Appraisal And Data"
subtitle: "A consortium of Public AI labs can substantially improve data pricing, which may also help to concretize debates about the ethics and legality of training practices."
date: 2025-04-03
original_url: "https://dataleverage.substack.com/p/public-ai-data-appraisal-and-data"
---

> **Original Substack post:** [https://dataleverage.substack.com/p/public-ai-data-appraisal-and-data](https://dataleverage.substack.com/p/public-ai-data-appraisal-and-data)

![File:Book of Royal Gemstones WDL2839.jpg](https://substack-post-media.s3.amazonaws.com/public/images/9683f401-86ef-444c-9933-a381fbeeb328\_500x607.jpeg "File:Book of Royal Gemstones WDL2839.jpg")

*This is, once again, an early draft and will likely be updated. I welcome comments and pushback (or support!).*

There is a growing[1](#footnote-1) movement around building “public AI” — which would mean, to quote the Public AI Network (PAINT) [website](https://publicai.network/), building public institutions, public-private partnerships, and international collaboration to enable "AI provisioned like electricity, parks, highways, libraries, or the Internet itself”. Here, I want to add an argument for public AI to the pile: building public AI will be extremely helpful in **improving the efficiency of data markets.**

The public AI concept has been explored substantively in whitepapers from [PAINT](https://bit.ly/publicAIpaper)[2](#footnote-2) [Mozilla](https://assets.mofoprod.net/network/documents/Public_AI_Mozilla.pdf)[3](#footnote-3). The general idea is to take action (again, see the whitepapers for tractable plans towards this vision) to build widely available public goods that support an ecosystem of AI products built on primarily on open data and using an entirely open software stack.

This is not about building one singular national AI institute, or stopping private organizations from pursuing AI. Instead, it’s a public goods-based ecosystem that can support private-public partnerships and a plurality of different organizations.

This is important to note, because in this post, I’ll refer generally to the notion of “public AI labs”. The idea is that a “public AI lab” that performs model training and data appraisal might be an organization like a [Canadian AI Institute](https://cifar.ca/ai/), [AI Sweden](https://www.ai.se/en), [AI Singapore](https://aisingapore.org/), the [Barcelona Supercomputing Center](https://www.bsc.es/), or the [UK AISI](https://www.aisi.gov.uk/). Perhaps some of these organizations might be connected via some consortium. So when I say “a public AI lab might do some data valuation experiments”, this concretely could refer to experiments run in a number of locations across the world.

Problem 1: While there is emerging market for training-focused data deals (e.g. buyers like [Google](https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22/) and [OpenAI](https://openai.com/index/openai-and-reddit-partnership/) are paying sellers like Reddit and news organizations for access to content, which is presumably being used for training and/or evaluation[4](#footnote-4)), there is currently not much transparency with regards to how data is currently being priced. This is likely to create a lot of uncertainty and volatile negotiations when it comes data prices. Why is Reddit’s data worth $60M to Google? Why not $60B or $60k?

To summarize Raul Castro Fernandez ([summarizing](https://en.wikipedia.org/wiki/Arrow_information_paradox) Kenneth Arrow and what’s now called the “Arrow information Paradox”) in work on [Data-Sharing Consortia](https://raulcastrofernandez.com/papers/data-sharing-consortia-escrow.pdf)[5](#footnote-5): if you’re a *buyer* looking to acquire data for AI development purposes, you can’t really guess how much value you’ll get until you see it, and you won’t know for sure until you train on it. On the other hand, for someone selling data, once the seller lets the buyers see the “product”, there’s no way to take it back. This is bad on both fronts, and means there are many cases where data transactions are mutually beneficial but don’t happen.

Problem 2: The current AI data training paradigm is plagued by a constellation of issues related to [consent](https://arxiv.org/abs/2407.14933) and [legality](https://blogs.gwu.edu/law-eti/ai-litigation-database/). It is also unclear how AI products being deployed now may affect (and potentially wither) incentives for future data creation. While there is still uncertainty as to how the training paradigm will hold up to lawsuits, regulation, and consumer demand, I think it’s now fully uncontroversial to say that this tension exists, and even die hard defenders of the current paradigm would agree there is a public relations and optics problem.

Here, I’ll discuss how public AI could substantially help with problem 1, and how this might carry over to helping problem 2 (although this will depend quite a bit on how open legal and regulatory questions are answered).

## A healthier market with public AI labs as data appraisers

The Data-Sharing Consortia solution to the “Arrow information paradox” is to have an intermediary entity hold data in escrow and use a well-designed market mechanism that manages transactions and remuneration using estimates of data value. In short, a well designed system *can* solve the problem of “Hey, I want to buy some data, and here’s how much I’m willing to pay, but I only want the data if it’s actually going to be good”.

Critically, this involves the data intermediary organizations running data value experiments, which might involve calculating “[influence](https://arxiv.org/abs/2405.13954) estimates”[6](#footnote-6), “[Shapley](https://arxiv.org/abs/2110.14049) values”, or something like the “Entitlement Stake” introduced by Castro Fernandez in the Data Consortia paper. These are all different approaches that try to give an “attribution score” to a data point or group of data points.

A key takeaway from this body of work is that at the end of the day, if we want to be really sure about data value, *somebody* needs to do some experiments in which they try out different data.

Public AI contributors can implement this vision — and amplify its impact — by acting as public-interest appraising agents. A public AI body would have incentives to train models specifically with the intent of revealing and sharing data value, which can improve the overall efficiency of the market. In other words, while the data consortium vision can work with private actors (just as a private auction house *can* allocate goods in a welfare-maximizing fashion), public AI would actively level the informational playing field. Note that these contributors could include various public benefit corporations and non-profits as well.

In fact, if “public AI” is implemented as more of a consortium than an individual lab — with an approach that emphasizes decentralization and pooling — the process of building public AI models would involve “natural experiments” for data value (because e.g. there were some experiments in Canada with dataset 1, and some experiments in Sweden with a different dataset 2, and then these datasets or models are merged in some way). In fact [research](https://arxiv.org/abs/2410.15661) from AI2, Cohere, CMU, and UW suggests that a modular “train, pool, and merge” approach can be effective for data valuation that leads to better overall models[7](#footnote-7).

Decentralized AI training naturally exposes some estimates of data value in a way that centralized training does not (though brings its own complications to the table). Critically, getting *some* estimates of data values won’t require taking much additional action beyond what organizations might already being doing in the process of training models (though doing extensive value experiments will still be rather expensive, at least with current techniques). The various contributors to a public AI consortium can go about their business of acquiring data, training models, deploying services, and so on, and just by keeping track of any data ablation experiments and data valuation estimation that are used in that process, produce value estimates that can be shared publicly to the benefit of data sellers.

There is a long history of state-based appraisal agencies. Consider, for instance, organizations like [BC Assessment](https://www.bcassessment.ca/) that assess property values (in part to facilitate the buying and selling of properties, but also to facilitate the deployment of property taxes).

In classical auction design [work](https://www.jstor.org/stable/1911865?seq=1), theoretical results suggest that expert appraisals can benefit sellers when buyers are risk averse. In practice, auction houses employ expert appraisers. Of course, in some settings, buyers and sellers might employ their own private appraisers (effectively spending some money to increase their confidence about the valuation of a good). More generally, we might expect that in the current “Buyer’s Market” for data in which many of the would-be appraisers are employed by AI operators, public-interest appraisal will benefit sellers.

Put simply, any “public AI” body with a mandate towards transparency that engaged in any data ablation experiments in the process of model training and shared said experiments could act as a third-party appraiser.

Note that this does not remove incentives to participate in data-sharing consortium, though it may complicate the mechanism design. As an example, consider a public AI body who buys the same Reddit data as Google and OpenAI, but then reveals a number of benchmark deltas that can be “attributed” to that dataset. E.g., “we bought Reddit’s data for $60M and all we got was a lousy 1% accuracy on this “social media lingo” benchmark”. Or, “we bought Reddit’s data and our conversational capabilities went through the roof!” Either outcome could affect the price that Microsoft and Anthropic might be willing to pay for that same data, but would not necessarily tell Microsoft and Anthropic the exact impact on their models’ performance.

Ultimately, individual buyers still need to consider their specific, often private, circumstances (access to other proprietary data, engineering design decisions, etc.) that may affect valuation, so a public AI body will never give a data market participant full confidence about the value they can obtain from some dataset. However, the end result will be reduced information asymmetry and reduced appraisal costs.

This would also be critical for upstream stakeholders, e.g. the actual Reddit users who created Reddit’s “data assets”, if they wanted to become involved in the decision-making around these deals. Reddit could stand to benefit from its users being knowledgeable about, and involved in data deals, as the userbase has a history of successful protest action against the [platform](https://en.wikipedia.org/wiki/2023_Reddit_API_controversy).

My expectation is that levelling the informational playing field will be a net positive for market dynamics. In fact, I would expect that because right now, AI companies can run experiments to actually calculate data value but data sellers can not, that many recent and ongoing data deals will be seen through the lens of history as favourable towards the buyers. And we should also expect that without collective bargaining (or in the extreme, cartel behaviour) by data sellers, that AI companies will walk away as winners in the current market, especially if they succeed in automating large amounts of economically valuable labour.

In short, key points for this argument are:

* Data appraisal can improve market dynamics
* Public bodies can perform data appraisal and share the appraisal results
* A decentralized consortium of public AI labs will perform some degree of “natural appraisal”, and with an explicit pooling and merging approach can do even more appraisal.
* Public appraisal is critical for upstream stakeholders (e.g., Reddit users).

## Would Data Appraisal Help with Consent and Legal Issues?

Above, we made the case that a public AI body can improve auction and market dynamics by acting as an expert appraiser. By telling us how much Reddit’s data impacted AI performance on some benchmark (which OpenAI, Google, and Reddit may all be hesitant to do), we can better understand if $60M is a “good deal”.

An additional effect of the data appraisal described above would be adding concrete evidence to be used in to ongoing debates about the morality and legality of various training practices.

Very concretely, currently if one wants to make an argument about, for instance, the empirical value of training on LibGen, to my knowledge one of the best sources is the unsealed [documents](https://storage.courtlistener.com/recap/gov.uscourts.cand.415175/gov.uscourts.cand.415175.391.14.pdf) from a lawsuit against Meta (of course, organizations like AI2, Cohere for AI, and many academic researchers continue to conduct and publish [data](https://arxiv.org/abs/2402.07827) [ablation](https://arxiv.org/abs/2402.00159)[8](#footnote-8)[9](#footnote-9) experiments). A pool of such estimates provided by public AI bodies (though perhaps not specifically looking at pirated materials) would be extremely valuable to anyone trying to assess the cost-benefit trade-offs of different regulatory regimes, and might also serve to reveal certain “high-leverage coalitions” of creators who can bargain very effectively.

Of course, it’s worth noting that one outcome of looming legal and regulatory questions could be that public AI-type organizations become the *only* organizations that can engage in internet scale pre-training. I think that most folks following these discussions think this is highly unlikely, but it’s worth stating: it could be the case that public AI systems are the *best performing AI systems, full stop*,because they are the only organizations that retain wide-ranging training privileges.

More generally, on average, if organizations are not paying for data, then the more “public interest” an organization is (a loose concept, to be sure, but operationalizable) the larger we might expect their allowable training set size to be (against, averaging across legal decision and normative preferences). Exploring this moral landscape will the subject of future writing.

Critically, given the uncertainty of the current moment and the wide range of perspectives and institutions represented in the big tent of public AI, it’s critical to note that these arguments do not rely on any one legal outcome or specific moral perspective: achieving healthier data market outcomes and concretizing legal and ethical debates can be seen as beneficial from across the spectrum of perspectives.

## Additional notes

**Exclusivity of data deals:** One important caveat to the above arguments is that publicly shared data values are most useful if data deals are primarily not exclusive. Indeed, if the predominant data licensing contract focuses on exclusivity, this will be bad for public AI. For instance, if OpenAI has an exclusive license to train on some content organization’s outputs, this could block the public AI network from using or appraising that data. However, given the challenges in data excludability and early evidence of a “live by the sword, die by the sword” to data (e.g. Deepseek distilling OpenAI’s models), it seems that exclusive deals may be threatened.

**Public AI labs as the data intermediaries in the consortium model**: If public AI organizations don’t actually hold data and train on it — if for instance, they only focus on providing compute, or supporting open source software — they won’t be able to contribute to data appraisal. So, it’s critical that public AI is involved in all components of the AI stack.

**Precedent from data use exemptions for cultural and heritage reasons:** In many cases, organizations doing cultural and heritage related work already have certain protections or exemptions when it comes to data use. This means that in some cases, attempts to appraise data value may conflict with existing frameworks for exemption. But in other cases, these exemptions may be useful as said organizations can appraise the value of the data in their area of expertise (e.g., understand the impact of a specific cultural dataset on some benchmark).

![File:Isaac Lea collection of precious stones. Miss Margaret W. Moodey in charge LCCN2016892128.jpg](https://substack-post-media.s3.amazonaws.com/public/images/5761564e-f879-422c-b212-cb2005b60b39\_960x744.jpeg "File:Isaac Lea collection of precious stones. Miss Margaret W. Moodey in charge LCCN2016892128.jpg")

[[wikimedia commons](https://commons.wikimedia.org/wiki/File:Isaac_Lea_collection_of_precious_stones._Miss_Margaret_W._Moodey_in_charge_LCCN2016892128.jpg)]

### Acknowledgments

Thanks to many folks in the Public AI Network for conversations that led to this post. Given my plans to update this post, I’m going to make sure everyone has had a chance to read the latest draft before I name any specific names here.

## Changelog

* May, 2025: fixed some typos.

[1](#footnote-anchor-1)

Caveat: I see myself as a part of this movement, so when I say it is “growing”, I am certainly not an objective observer of said growth, but I think there is a very solid case to be made (see e.g. a number of events on the Public AI Network website: https://publicai.network/)

[2](#footnote-anchor-2)

Jackson, B., Cavello, B., Devine, F., Garcia, N., Klein, S. J., Krasodomski, A., Tan, J., & Tursman, E. (2024). Public AI: Infrastructure for the Common Good. Public AI Network. <https://doi.org/10.5281/zenodo.13914560>

[3](#footnote-anchor-3)

Marda, N., Sun, J., and Surman, M. (2024). Public AI: Making AI work for everyone, by everyone. https://assets.mofoprod.net/network/documents/Public\_AI\_Mozilla.pdf

[4](#footnote-anchor-4)

See e.g. https://www.monda.ai/blog/ultimate-list-of-data-licensing-deals-for-ai and https://sr.ithaka.org/our-work/generative-ai-licensing-agreement-tracker/

[5](#footnote-anchor-5)

Castro Fernandez, R. (2023). Data-sharing markets: model, protocol, and algorithms to incentivize the formation of data-sharing consortia. Proceedings of the ACM on Management of Data, 1(2), 1-25. https://raulcastrofernandez.com/papers/data-sharing-consortia-escrow.pdf

[6](#footnote-anchor-6)

Note that there *is* active work on making influence functions work for LLMs. Though some of this work involves calculating something a bit different from a true leave-one-out-estimate. See Choe, S. K., Ahn, H., Bae, J., Zhao, K., Kang, M., Chung, Y., ... & Xing, E. (2024). What is your data worth to gpt? llm-scale data valuation with influence functions. *arXiv preprint arXiv:2405.13954*

[7](#footnote-anchor-7)

Na, C., Magnusson, I., Jha, A. H., Sherborne, T., Strubell, E., Dodge, J., & Dasigi, P. (2024, January). Scalable Data Ablation Approximations for Language Models through Modular Training and Merging. In *EMNLP*. https://arxiv.org/abs/2410.15661

[8](#footnote-anchor-8)

Soldaini, L., Kinney, R., Bhagia, A., Schwenk, D., Atkinson, D., Authur, R., ... & Lo, K. (2024). Dolma: An open corpus of three trillion tokens for language model pretraining research. *arXiv preprint arXiv:2402.00159*. https://arxiv.org/abs/2402.00159

[9](#footnote-anchor-9)

Üstün, A., Aryabumi, V., Yong, Z. X., Ko, W. Y., D'souza, D., Onilude, G., ... & Hooker, S. (2024). Aya model: An instruction finetuned open-access multilingual language model. *arXiv preprint arXiv:2402.07827*. https://arxiv.org/abs/2402.07827
