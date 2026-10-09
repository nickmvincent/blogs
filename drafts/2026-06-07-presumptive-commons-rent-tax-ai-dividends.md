---
title: "An AI Dividends Plan that Combines Capabilities Assessment and Data Attribution: Without Taxing Compute or Requiring State Ownership"
content_id: "garden/post/presumptive-commons-rent-tax-ai-dividends"
date: "2026-06-07"
slug: "presumptive-commons-rent-tax-ai-dividends"
summary: "Data dividends based on capability measurement, data provenance, and AI auditing."
original_url: "https://dataleverage.leaflet.pub/3mnqonrblbhwi"
captured_from: "https://nickmvincent.github.io/long-posts/presumptive-commons-rent-tax-ai-dividends.html"
source_revision: "cbe747fa1c1f30dd85d9cf552f4db279c7be2d7d"
source_sha256: "bac0dfad116a84518978367f14b8ff71b29a3b0e0e525f4031758016913b1b1a"
captured_at: "2026-09-25"
status: "draft"
visibility: "public"
updated_at: "2026-10-08"
---

*I wrote the first draft of this after the Sanders op-ed, and updated it in August 2026 after the discussion had time to settle, and then again in September and October 2026. I hope to continue revising it and/or extend this into a more serious proposal -- I welcome feedback!*

## Background

In June 2026, US Senator Bernie Sanders put forth a proposal for a new kind of ["AI dividend"][sanders-ai-dividend]. One thing that stood out to me, having worked on a big [data dividends report][data-dividend-report] in 2020 (published in 2021), was how the Sanders proposal was quite similar in spirit to early data dividends discourse. See also [Castro Fernandez and Weyl](https://hbr.org/2026/06/how-ai-companies-can-pay-fair-rates-for-the-content-they-need).

And in September 2026, the new DeepMind Institute published this [Economic policy for AGI](https://institute.deepmind.com/essays/economic-policy-for-agi/) essay, once again bringing attention to these ideas.

As I've worked on data dividends, I've also been working on a number of highly related topics -- sometimes in tension with data dividends -- including data-related collective action (both [data leverage](https://arxiv.org/abs/2012.09995) and [algorithmic collective action](https://arxiv.org/abs/2505.00195)), [data valuation for markets](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b0b74d6b049d34084da136418ef42334-Abstract-Position_Paper_Track.html), and "[public AI](https://publicai.network/)".

While a "one-time" data dividend might complement "from-here-on-out" data markets, recurring data dividends tied to data licensing could introduce the data dividend operator as a market participant competing as a kind of public option data vendor, depending on how data access and payments are structured. Not necessarily a bad thing, but certainly disruptive.

And while a world in which most data labor is remunerated via dividends would be very compatible with a commons-focused, public goods approach to AI, it's also very possible that data markets reduce incentives to contribute data openly (you could be getting paid for it!).

In our 2021 report, we focused on trying to find various proxies for the concept of "data dependence" in order to rank different companies in terms of how much data they use (e.g. by counting their users, auditing the volume of data within their organizational databases, etc.). 

However, a key insight I think we should apply to today's data dividend discussions: rather than trying to measure data dependence directly, we could instead lean on a rebuttable policy assumption that more capable AI systems draw more heavily on the data commons (broadly construed) that humanity has built. I think we can create a tax that aims to create incentives that support (1) use of data commons with reciprocity alongside (2) responsible use of attested data from private markets to (3) increase our collective certainty about how data drives powerful AI capabilities.

## The Proposal

Tensions abound. In this post, I want to lay out a relatively concrete proposal for a "data dividend" that I believe has the potential to navigate the tension between backward-looking redistribution or dividend-style policy options and forward-looking data markets. I think this proposal has the potential to dodge common critiques that come up in discussions of AI-specific economic interventions. 

Specifically: I propose that we design and implement a presumptive commons-rent tax (PCRT) on *operating profits attributable to frontier AI systems* which can be credited away (possibly to zero) by providing independent evaluators with data attribution receipts arguing that specific frontier capabilities derive from either private market data or commons data which was used with some kind of reciprocity. Note there will be some complexity around taxing normal returns on [investment][nber-ai-taxes].

There are of course serious technical and institutional roadblocks that must be addressed to make this realistic. Three major barriers to implementing this today are (1) building up capacity for AI auditing and evaluation, (2) enabling audits/evals with a data attribution lens -- which will require serious technical progress in data attribution, and (3) more generally addressing challenges around international cooperation when it comes to tax and corporate regulation. Conveniently, however, [auditing and evaluation][frontier-ai-auditing] are becoming a major policy focus, and it seems like AI safety as a concept may have the potential to enable international cooperation.

The two complementary motivations for this approach would be (1) *a presumption that model capabilities are dependent on data commons* (combined with the argument that extraction of rent from commons and threats to their sustainability can justify taxation or other governance interventions to ensure reciprocity) and (2) the fact that we might want to independently disincentivize *unexplained capabilities*.

Put another way, this is trying to tie together two distinct ideas. First, rent extraction that undermines a commons is a reason to consider governance or a tax on rents. This need not mean [centralized management](https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/lecture/). Second, I think unexplained capabilities are concerning from both an AI safety perspective and a "health of post-AI markets for information" perspective. If designed well, I think policy can combine relatively simple ways of funding data commons and enforcing safety regulations in a "best of both worlds" fashion.

Finally, this proposal allows for policymakers to dynamically steer the primary goal towards revenue generation or industry behavior change. By tweaking the parameters that determine how burden is imposed and how easily credits can be earned, the overall proposal can lean more towards revenue generation or more towards just incentivizing privatized data flow. Thus, we have an easy answer to a possible FAQ of "why not just have standard corporate taxation to address these issues?" That is: this tax would complement more general approaches to corporate taxation and there's a world in which most parties effectively credit away most of this tax and just pay standard corporate tax.

We could call this data dividends funded via a tax on presumed commons usage that can be rebutted with data attribution receipts.

## How the credits will work

This could involve a relatively simple "tax credit" system: the more evidence that AI companies can provide showing how specific capabilities map to data, the lower the tax goes. A model with an entirely private, fully "paid for" data supply chain, and evidence linking that data to its capabilities, would pay zero commons-rent tax. A model with some commons dependence (e.g. Internet-scale pretraining) might pay a small tax (or could earn credits via engagement with other reciprocity programs like [Wikimedia Enterprise][wikimedia-enterprise]).

Tax proceeds would be split between funding new public goods, making additional reciprocity and sustainability payments to data commons themselves (e.g. funding new projects to help the Internet react to new forms of agentic commerce and activity, spam and scams, etc.; paying to help maintain core Internet infrastructure; supporting peer-production projects, etc.), and making payments to individuals (if viable).

Who would judge the legitimacy of tax credit claims from AI companies? The emerging ecosystem of international AI auditing organizations could work together to verify these claims and lower their tax burden.

The designers of the tax would need to determine a base rate and the specific mapping function that determines how additional evidence (something like "percent of capabilities explained" or "percent of data accounted for") converts to tax credits. These design choices would determine whether the tax ultimately incentivizes large-scale behavior change from AI companies (e.g. radically overhauling data pipelines or improving data transparency) or simply encourages them to pay the tax. Optimistically, if something like this were implemented, we would either end up in a world where companies profiting from highly capable data-dependent systems pay a large amount of aggregate funds into various shared funds (perhaps even internationally governed) or a world where the vast majority of upstream data flows through healthy data markets where data creators have the collective leverage necessary to get paid through a mixture of upfront and royalty payments.

Of course, there are a lot of details to be worked out!


## Brief history of data dividends research in 2021

In the 2021 report, we analyzed a variety of possible fundraising and disbursement mechanisms for a “data dividend” (which [Governor Newsom of California had proposed in 2019](https://www.gov.ca.gov/2019/02/12/state-of-the-state-address/)). While we were not aiming to pick a single answer, our "likely good first step" suggestion was a data dependence tax to fund public goods. To make "data dependence" operational, we suggested using user count as a proxy: firms with lots of users are probably getting lots of value from aggregated data.

Some other notable works on data dividends around that time include:

- [Bax's computational treatment](https://arxiv.org/pdf/1905.01805) of individual and grouped data dividends using Shapley and Owen values
- [Wadhwa's Data Catalyst review](https://datacatalyst.org/wp-content/uploads/2020/06/Economic-Impact-and-Feasibility-of-Data-Dividends-1.pdf) of the economic impact and feasibility of data dividends
- I contributed to this [2019 preprint](https://arxiv.org/abs/1912.00757) on data dividend design choices and this later [2023 EAAMO poster paper](https://www.nickmvincent.com/static/eaamo_data_dividends.pdf) on the challenges of “meritocratic” data valuation for dividends

Another key idea from the report was that, in the context of retroactive dividends (as opposed to forward-looking markets), it is probably best to avoid “fine-grained valuation” (e.g., trying to write personalized checks for individuals). In the context of data markets, it could still make sense in some cases to price both individual data points and collective bundles.

In short: for a dividend, we should tax dependence on collective data and disburse it coarsely while we figure out better valuation and interpretability methods. I think the reasoning from that report holds up pretty well in light of AI progress. I also think it’s notable that the motivation described in the Sanders proposal matches the arguments in our original report pretty closely.

However, I also think we should be sensitive to [concerns][nber-ai-taxes] from economists about the impacts of compute taxes, automation taxes, capital taxes, etc. After the Sanders op-ed went out, the idea quickly drew a cross-ideological mix of interest, skepticism, and pushback (see e.g. [AP][ap-ai-public-ownership], [WaPo][washpost-sanders-ai-stake], [Reason][reason-sanders-ai-wealth], [Cato][cato-trump-sanders-swf], [Fortune][fortune-sacks-ai-equity] for a mix of perspectives).

One general concern that cuts across some of the critiques: depending on design, an AI dividend tax could have negative effects on growth, investment, diffusion, etc. If we can avoid it, we might want to avoid explicitly targeting “AI,” “compute,” or “automation.”

## The use of commons and pseudo-commons and private data

Something that’s complicated about frontier AI systems is that they depend on many different categories of data. Some of the data used to train modern systems are digital commons like Wikipedia that have [clear licenses](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use) and are meant to be used (with attribution and other license conditions). Some data is literally in the public domain.

A large portion of the data used for pretraining (e.g. [Common Crawl](https://www.commoncrawl.org/terms-of-use)) occupies a gray area. Much of it is copyrighted and there are not clear established terms regarding acceptable forms of AI training. The [U.S. Copyright Office's report on generative AI training][copyright-office-ai-training] describes the still evolving fair use and licensing landscape. Similarly, the OSS code used for training is being treated as a de facto commons, while the application of attribution and copyleft clauses to generative AI remains contested/debated.

Finally, there's a huge swath of data that is definitely not a commons in any legal sense -- e.g. click data, trace data, and posts on private social media platforms. These data were produced under terms of service that tend to favor the platforms, but we can nonetheless think of them as collectively forming a very broad pool. Your Facebook posts and Google search history are not part of a literal commons. As we rethink data governance for the post-AI age, however, we might want to treat such data as subject to commons governance. The general idea of this proposal works even if you reject this particular point.

## Capability as a proxy for data dependence (and presumed commons dependence)

One possible way to approximate extraction from the commons is to take a "rebuttable presumption of data-dependence" approach to the existence of powerful AI. Modern AI systems rely on data across training and evaluation and reinforcement learning and synthetic data still have upstream human-data dependencies. There are some counterexamples where data dependence may not be proof of commons dependence (e.g. [AlphaZero](https://arxiv.org/abs/1712.01815) self-play using only game rules -- though game rules are arguably super high leverage human records...).

Instead of using user count or something else as a primary proxy for data dependence, we can just use capability itself. We would basically be working from a default assumption that if an AI system is very capable and monetized, a meaningful chunk of that value came from commons data. I think this assumption is currently very justified and will remain so in the near term.

There are several possible ways we could try to coarsely estimate the fraction of value attributable to data versus the value attributable to compute, non-data technical progress, interface progress, and other factors. We would need to pick a provisional number and calibrate it against evidence. 50% might be a starting placeholder. For a related proposal, see [Castro Fernandez and Weyl](https://hbr.org/2026/06/how-ai-companies-can-pay-fair-rates-for-the-content-they-need). The [Sanders proposal][sanders-ai-dividend] also uses 50%, but for a one-time tax paid in company stock, rather than an estimate of the share of value attributable to data. The more capable a system is, the more burden a company should face in explaining how it got so good.

Thus, we could iterate on various data dividends proposals to design what we might call a “presumptive tax on commons rent from frontier AI”. When a firm makes money from a powerful AI system, we presume some share of the rent came from commons and commons-ish data. AI operators can lower their presumptive commons-rent tax by either showing that capabilities came from data that was acquired under non-commons conditions (e.g., licensed data purchased via a healthy data market) or by showing that capabilities came directly from specific commons data sources (and showing some evidence of reciprocity).

As a toy example, suppose a highly capable AI system earns $10B in annual rents and the presumptive commons-rent share is set at 50%. If an AI operator can substantiate that half of its capability-relevant data came from licensed and/or reciprocated data sources, the firm's tax base might fall from $5B to $2.5B.

## How evidence of data use would lower the tax burden

We would need a clean accounting scheme here, with a possible unit being **explained data**. Explained data would estimate the share of a model’s effective, capability-relevant data contribution that the company can actually account for. To count as tax-reducing explained data, a data source would need to be documented, have provenance and proof of fair acquisition (e.g., because it was licensed, bought under contract, or similar), and plausibly relevant to the capabilities being taxed. Under this proposal, the tax rate would depend on the capability level achieved by a model, so more capable models would require more explained data. This might be informed by many areas of research, e.g. [scaling laws][kaplan-scaling-laws], [compute-optimal training](https://arxiv.org/abs/2203.15556), [training data attribution][training-data-attribution], and so on.

Preparing such evidence would look something like this:

- first, a company profiting from AI systems prepares data documentation, building on work such as ["Datasheets for Datasets"](https://arxiv.org/abs/1803.09010), for each commercial system it releases for consumers or enterprise customers (this could be done at the model-family level to avoid imposing an undue burden on AI companies)
- second, each entry in the datasheet would be labeled with an acquisition/governance status (licensed, internally generated, public-domain, governed by a data union/trust, etc.)
- third, provenance evidence would be collected to support the acquisition/governance classifications
- fourth, usage evidence shows how much each data component was actually used (this could include details about mixture fractions, sampling rates, repetition, deduplication, training stage, post-training role, eval role, and upstream sources for synthetic or RL data). Ultimately, this evidence would be reviewed by AI auditing organizations, so it would not have to be completely standardized; the framework could allow flexibility for different model types
- fifth, just as datasheet entries would be linked to provenance evidence, usage entries would be linked to ablations to show how those data components actually mattered for the relevant capabilities. This research will be expensive, but we'll need to do it anyway if we want to deploy AI in high-risk contexts.

For a first implementation, we might just use "evidence tiers" as determined by the adjudicating organizations responsible for capability measurement.

To summarize: model capability comes from a production process involving compute, model size, data quantity, data quality, interface and tool access, etc. Capability measurement would be used to set a default presumed tax rate. Companies could present data details to reduce their tax base, and an auditor (or a network of auditing organizations) would convert the evidence into "accepted explained-data points" to determine a final rate.

This could create a good set of incentives:

- if companies want lower taxes, they should build datasheets and [provenance systems][data-provenance-initiative] from the start
- if they want larger reductions, they need to run and share data-centric scientific experiments
- if they rely heavily on commons data, they can still do that, but they should pay something back or give something back
- this additional commons-rent tax is fully avoidable!

As of October 2026, parts of this proposal overlap with existing data transparency rules: the [EU AI Act's public training-content summary](https://digital-strategy.ec.europa.eu/en/library/explanatory-notice-and-template-public-summary-training-content-general-purpose-ai-models), the voluntary [EU General-Purpose AI Code of Practice][eu-ai-code], and [California AB 2013][california-ab-2013], which set a January 1, 2026 deadline for training data disclosures by covered developers. Attribution and auditing work would be an additional ask that would build on the information required by these laws.

## Targeting "unexplained capabilities"

But wait a second -- if the whole concern around taxing compute or automation is that "we shouldn't tax stuff that we want more of," isn't this potentially even worse than those other taxes, if we interpret this proposal as a tax on intelligence itself or capability itself?

Critically, the PCRT should not be designed as a tax on intelligence or capability, but rather a tax on unexplained or mysterious capability. If an AI operator trains on 100% licensed/accounted-for data and can show that this data actually drove the relevant capabilities, its commons tax would be near zero.

If you train on Wikipedia, Common Crawl, public code, user traces, etc., you would end up paying some reasonable tax back to the commons (and the tax might also be reduced if you show evidence of, e.g., contributing to something like [Wikimedia Enterprise][wikimedia-enterprise], or making in-kind contributions of data, model weights, gold-standard code, etc.). Ideally, during any kind of transition period, there would be a way to transfer existing reciprocity programs into tax credits as well. And perhaps reciprocity programs could just be integrated into the program in the long term.

## Auditing and enforcement

How would this be enforced? This is where the recent momentum around auditing and safety comes in. Capability measurement -- and assessment of the ablations and whether AI operators are able to provide plausible accounts of, at a high level, how data choices drive capabilities -- could be handled by an ecosystem of independent auditing institutions, along the lines of the [frontier AI auditing ecosystem][frontier-ai-auditing].

The ecosystem of auditing orgs would become part of the infrastructure for data governance: measuring capabilities, reviewing provenance, looking at ablations, etc. This would also get companies to contribute to advancing and sharing science about where model capabilities come from, in turn helping the auditing organizations.

Critically, by looping in auditing and safety organizations, this proposal could also take advantage of the fact that AI safety is one area with a plausible path to international cooperation. The [International Network for Advanced AI Measurement, Evaluation and Science](https://www.aisi.gov.uk/blog/international-ai-network-consensus-and-open-questions), established in 2024 as the International Network of AI Safety Institutes, offers a precedent for technical cooperation (though not for joint tax collection). I think cooperation around AI safety might offer one of the few plausible paths toward a global wealth fund rather than various national funds and sovereign-focused economic interventions.

A single global wealth fund is morally attractive because our data commons is transnational. However, a more realistic path might be to go federated: we could imagine national or regional AI commons funds collecting revenue, while treaty or club arrangements allocate some share to global public goods and commons institutions.

Of course, we likely would not want independent AI auditors to be burdened with global taxation responsibility (nor would they likely want a bunch of extra work). Public tax authorities would still set the rules while auditors (ideally with support to hire the staff needed to do all this) could review evidence.

Compared to compute and automation taxes, I believe this kind of approach would avoid some of the concerns raised by economists and instead target a specific harm: companies turning collective human activity and public knowledge into private rents without a proportionate return.

In the current world, this would mean that AI companies would pay a bunch of taxes, which then might fuel, e.g., a national wealth fund, or ideally a global wealth fund. But it also creates a path to lower the burden: license data, work with data unions/trusts, document provenance, run ablations, or give value back to the commons.

[sanders-ai-dividend]: https://www.sanders.senate.gov/op-eds/the-public-should-own-half-of-the-big-a-i-companies/
[data-dividend-report]: https://www.nickmvincent.com/static/Data-Dividend_final.pdf
[attestation]: https://dataleverage.substack.com/p/attestation-across-the-ai-supply
[evaluation-crisis]: https://dataleverage.substack.com/p/the-ai-evaluation-crisis-is-an-opportunity
[clear-data-rules]: https://dataleverage.substack.com/p/almost-everybody-including-both-data
[eu-ai-code]: https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
[frontier-ai-auditing]: https://www.averi.org/ourwork/frontier-ai-auditing
[nber-ai-taxes]: https://www.nber.org/papers/w34873
[ap-ai-public-ownership]: https://apnews.com/article/sam-altman-ai-bernie-sanders-trump-public-ownership-772224f9cd138eb79d3ef3336858a5d5
[washpost-sanders-ai-stake]: https://www.washingtonpost.com/opinions/2026/06/03/bernie-sanders-wants-government-stake-ai-companies/
[reason-sanders-ai-wealth]: https://reason.com/2026/06/02/bernie-sanders-ai-wealth-fund-bill-shows-that-he-doesnt-understand-ai-or-wealth/
[cato-trump-sanders-swf]: https://www.cato.org/blog/trump-opened-door-sanderss-sovereign-wealth-fund
[fortune-sacks-ai-equity]: https://fortune.com/2026/06/06/former-ai-czar-david-sacks-bernie-sanders-bill-government-equity-stupidity-tax-nationalization-trump-public-stakes/
[wikimedia-enterprise]: https://wikimediafoundation.org/news/2021/10/25/wikimedia-foundation-launches-wikimedia-enterprise-the-new-opt-in-product-for-companies-and-organizations-to-easily-reuse-content-from-wikipedia-and-wikimedia-projects/
[data-provenance-initiative]: https://www.nature.com/articles/s42256-024-00878-8
[kaplan-scaling-laws]: https://arxiv.org/abs/2001.08361
[training-data-attribution]: https://arxiv.org/abs/2308.03296
[california-ab-2013]: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013
[copyright-office-ai-training]: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf
