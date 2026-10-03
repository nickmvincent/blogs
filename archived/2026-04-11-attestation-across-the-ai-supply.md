---
title: "Attestation across the AI Supply Chain"
subtitle: "A proposal for interoperable attestation objects that connect training data, evaluation labor, and AI-generated outputs across the AI supply chain."
date: "2026-04-11"
original_url: "https://dataleverage.substack.com/p/attestation-across-the-ai-supply"
content_id: "substack/post/191601927"
authors: ["Nick Vincent"]
published_at: "2026-04-11T00:00:19.538Z"
source_updated_at: "2026-09-13T13:29:57.103Z"
archived_at: "2026-09-25T20:33:40+00:00"
source_body_sha256: "12048d1542af8ed8030795bcf8ebc3ff20db692141a11331dc384c05ba84e963"
---

![blue and white light streaks]

Photo by [Solen Feyissa] on [Unsplash]

I am feeling hopeful that momentum in the AI evaluation space can help improve data markets and data ecosystems more broadly. Here’s the bullet point summary:

-   Some AI users (public bodies, enterprise users, picky consumers) and other parties (regulators, insurers) are going to, or have already started to, demand some kind of “attestation objects” in the domain of AI evaluation.

-   These buyers want some kind of proof that a model was evaluated; evaluation organizations are already beginning to document and share their evaluations

-   An attestation that a certain evaluation procedure was performed could be similar to, and interconnected with, other kinds of attestations across the AI supply chain.

    -   One related attestation could say that a certain piece of data was used to train a model.

    -   One related attestation could say that a certain piece of information was retrieved and used at inference time.

    -   One related attestation could say that a certain information object (sequence of output tokens) really came from a certain model.

    -   One related attestation could say that a piece of AI-assisted output (e.g. downstream code) came from a certain AI output.

-   On the technical side, we should make it easy for these pieces of information to be linked to each other. They can support a “full picture” of AI supply chain provenance

    -   The technology needed here is actually relatively simple: registries for the attestation objects, techniques for verification, and appropriate privacy-preserving ways to share registries and associate people and organizations with attestation objects

-   Full supply chain provenance can be a product differentiator for AI developers that helps to combat model extraction/distillation

-   The existence of more “guilds” who act as sellers in markets for attested evaluation and training data can provide important incentives to their members (knowledge workers of all types) to maintain quality and expertise; this can align incentives so that these guilds provide a resisting force against overreliance and slop

-   What does this suggest we do?

    -   On the social side, we should try to create more demand for all these kinds of attestations; we should definitely leverage momentum and energy around evals

    -   On the policy side, we should look for opportunities to incentivize attestation and to make interoperable schemas and cross-talk easy

-   In total, I think there are at least five distinct forces that could create demand for attestations: gov’t regulation, anti-distillation, procurement requirements, AI insurers, consumer demand.

-   If any of these succeed in creating real demand, this will enable markets for attested relationships instead of markets for “raw tokens”. This would be great for society because it can bypass some “core” information economics challenges with markets for information and likely create healthier overall data flow dynamics.

------------------------------------------------------------------------

This post argues that a shared family of attestation objects could improve several markets across the AI supply chain: consumer choice among AI products, upstream markets for training and retrieval data, markets for audits and evaluations, and downstream markets for AI-assisted artifacts. Broadly, I’ll use the term “attestation object” here to refer to a verifiable record about who contributed what, in what role, to which model or output, under what validation process. We can enable this “shared family” by making progress on the design of an appropriate schema for the objects (technical/protocol work), the implementation of supporting policy and regulation, and by building relevant platforms that enable markets for attested evaluation and other data.

The ideas discussed here build on work already underway in at least three adjacent areas: the dataset documentation space (inclusive of efforts such as [datasheets], [model cards], and [data provenance]); the “[Frontier AI Auditing]” world; and the content authenticity and provenance world (e.g. [C2PA]).

Momentum around audits can foster more training data transparency and better markets for training and retrieval data. Parties interested in provenance for AI-generated outputs could help promote transparency upstream. Norms around transparent AI usage may drive further demand for transparency up the chain.

I’ll note that, in addition to momentum around auditing, we’re starting to see some evidence that consumers might care about attestations for AI products. See, for instance, the [“Introducing ChatGPT Health”] blog post, which emphasizes working with “260 physicians who have practiced in 60 countries and dozens of specialties” to obtain “feedback on model outputs over 600,000 times across 30 areas of focus”.

Data policy conversations often involve two somewhat different strategies for improving data markets. “Data protection” strategies are focused on trying to stop scraping, distillation, or reuse through a combination of law, platform rules, anti-scraping, and poisoning. An “attestation-forward” strategy tries to get AI users and/or regulators to care about verified provenance relationships upstream of AI products.

These approaches can complement each other (in the short term, effective data protection may produce more pressure to get attestations working) but also likely benefit from somewhat divergent policy approaches. Data protection efforts try to block unwanted scraping and distillation; attestation efforts that succeed in making verified provenance, evaluation, and output identity matter could make **“just scraping anyway” less valuable.**

Very concretely, an attestation-forward data strategy would involve roughly four broad types of attestation objects:

-   a **training contribution** object: “I am a medical doctor and I attest that I authored a textbook chapter and agreed to include it in the ChatGPT Health training dataset.”

-   an **evaluation record** object: “I am a medical doctor working with an AI evaluation organization and I attest that I reviewed 100 ChatGPT Health outputs and believe they represent standard of care.”

-   an **output provenance** object: “OpenAI as an organization attests that this output telling you to take more Advil came from the GPT-6.0-med1000 model.”

-   a **downstream use** object: “I am a vibe-coder making an iPhone health app and I attest that I used GPT-6.0-med1000 while building this app.”

Users buying AI products, AI developers buying data, anyone commissioning audits, and anyone consuming AI-generated outputs all face a related set of issues stemming from information asymmetry and lack of information generally. At the same time, the auditing and evaluation space has significant momentum; at present, there is an active [ecosystem][Frontier AI Auditing] of third parties such as [METR], [Apollo Research], and the [AI Security Institute] providing attested evaluations of frontier models.

For users looking to pay for AI products, there remain challenges in DIY benchmarking of models. It also remains challenging for consumers to interpret benchmarks and evaluations. Consumers are stuck mainly making decisions based on model outputs alone; there are currently few opportunities for consumers to incorporate facts about model inputs into their decision-making.

For developers looking to pay for data in AI markets, there are core market design challenges that stem from the non-rivalry and non-excludability of information alongside practical challenges with fine-grained assessment of data value. Markets for data are [fragmented], opaque, and inefficient at the moment.

Each stage of the AI supply chain could, in theory, combined linked attestations from key actors. Data creators can attest that they included their data in training sets. Auditors can attest to their participation in evaluation processes. Model outputs can include attestation objects that help people verify that a given output really came from a certain model, and in some domains that kind of output transparency may itself become required. And downstream artifacts can bundle all these attestations together via flow-down.

If the schema for attestation and provenance can be synchronized across the supply chain, we can achieve a win-win-win-win:

-   Win 1: For data creators and buyers, we might establish healthier markets for training data that emphasize attestation objects rather than raw tokens. Upstream data markets would rely less on winning the constant battle between data protectors versus data extractors (inclusive of various approaches for scraping and distillation), and would more easily accommodate arrangements that preserve research or public-interest use while still giving workers or collectives something to bargain over.

-   Win 2: For auditors, we can help increase demand for high quality audits and create standardization around benchmarking and evaluation. Better provenance for the full supply chain should also make auditing itself easier.

-   Win 3: For labs, we can make it easier to sell model outputs without being undercut by distilled models.

-   Win 4: For people consuming content, we can provide means to verify content authenticity. More generally, people can use all of this upstream information to help them assess AI-generated content of all types. This would help end-users who just want to read an AI output to answer a question and people who want to use AI outputs for other things (e.g., to sell AI-produced software).

The main downside -- the answer to “why aren’t we literally doing this today if it’s so good?” -- is that attestation will impose new costs on various actors. Training and evaluation labor may cost more under this paradigm (though hopefully, with real returns in terms of model utility, safety, etc.). And, we still need to answer a number of technical and design questions to make attestation work.

While much of my previous writing has focused on Win 1, I’m excited about all of these angles. (Of course this is the optimistic view -- see the end of this post for a more negative set of “likely objections”.)

Most of this post will be aimed at motivating attestations across the supply chain. I hope to write more in the future about realistic pathways towards achieving this vision. I’ll briefly note that there are at least five ways to create incentives for attestations and that I do think we have some viable low-hanging fruit in the policy space. On the incentives side, the main channels I see are: direct mandates for some kind of attestation in narrow high-stakes settings; pressure via procurement rules from enterprise buyers and public bodies; asks from insurers and other liability-sensitive counterparties; self-interest from labs seeking product differentiation and/or anti-scraping incentives; and direct user preference / consumer demand. There is already real progress around [auditing][Frontier AI Auditing], [public procurement guidance], and [regulatory transparency requirements].

On the policy side, some “minimal asks” include:

-   getting policymakers to “bless” a small number of interoperable formats and a credible process for deciding who counts as a verifier

-   **requiring** attestations for certain contexts

-   disincentivizing bogus provenance and evaluation claims using consumer protection

-   maintaining some data protection and licensing “backdrop” since contributors are less likely to participate in markets at all if the baseline expectation is still that their work will simply be scraped and reused anyway.

Next, I’ll describe roughly how I think buyers are choosing AI today and why the current approach is incomplete. Second, I’ll summarize the state of play for upstream markets for training data and evaluation labor. Third, I’ll describe how interoperable attestation objects can link contributions, evaluations, and outputs. Finally, I’ll try to tie the whole thing together by arguing that this kind of attestation layer can improve incentives for buyers, labs, and knowledge workers.

Or put another way, this is yet another blog making the case for data transparency and healthy market flow as a coalition-building cause that can unite auditors, content creators, AI labs, and the general public around a mutually beneficial set of incentives.

### Core assumptions behind the proposal

The claims above rest on a core set of *assumptions*:

-   Information is hard to price cleanly because it is largely non-rival and often hard to exclude (see e.g. classical work from [Arrow on the economics of information] and [Jones and Tonetti on the non-rivalry of data]).

-   Fine-grained data valuation is inherently challenging because small units of data have influences that are very small in raw magnitude and it is very expensive to acquire ground truth; value is usually more legible when data is grouped into bundles or collectives (see e.g. work on “[data dividends]“).

-   Training data and evaluation data are not totally separate substances so much as different uses of similar underlying human knowledge work (see e.g. [Deng et al. on training/evaluation overlap via benchmark contamination] for one example of the overlap in practice).

-   Output-only evaluation is useful but costly and incomplete, especially for increasingly general systems (see e.g. [Raji et al. on the limits of “general” benchmarks] and [Liang et al. on holistic evaluation and coverage gaps]).

-   Markets for upstream contributions likely need some kind of trusted approach to data flow, not just shipping of raw bits, if contributors are going to participate and capture value (see e.g. [Castro Fernandez on auditable data-sharing arrangements]).

-   Good faith open data strategies can conflict with efforts to empower workers or collectives to bargain.

-   Consumers, regulators, insurers, or other downstream decision-makers will sometimes care enough about verified provenance to influence decision-making around AI (see e.g. [Brundage et al. on frontier AI auditing][Frontier AI Auditing] and [OpenAI’s health launch as an example of product-level signaling around physician involvement and evaluation][“Introducing ChatGPT Health”]).

-   In some important domains, transparency about model outputs themselves -- not just the training process -- will increasingly be expected or required.

-   In at least some important domains, attested inputs and evaluation processes will be meaningfully predictive of downstream quality, safety, or trustworthiness.

With that overview in place, here’s the longer argument:

## I. The market problem: buyers of AI products can see outputs, but not the chain behind them

Imagine someone who is choosing from a menu of AI products. Perhaps this person is a consumer who just wants to use AI for small personal projects (”help me build personalized note-taking software”), a researcher seeking some occasional help with research tasks (”help me debug this LaTeX issue”), a hobbyist software developer seeking to find a tool to use heavily, somebody seeking a rigorously tested AI system that can offer medical advice, or a company’s CTO looking to make an enterprise contract for org-wide AI access.

Across all these contexts and scales, a person buying an AI product is (for now) mainly buying “information outputs” such as answers to questions, documents that fulfill some requested purpose, or pieces of code that can complete certain tasks. A user buys an AI subscription or AI credits, and now can enter an input (a prompt/query) and get an output. Modern frontier models can provide a dazzlingly varied set of outputs: a single tool can first give you something like a search engine results page, followed by a complex working piece of code, a working spreadsheet, and then finally a poem and an accompanying piece of visual art. Some systems are even agentic and can produce outputs that are themselves actionable (e.g., the output is a series of actions, and then the system performs some “actuation,” often using the user’s computer and/or API keys).

Generally (and we’ll get more precise about this later in the article), we choose to spend money (perhaps a lot of money!) on AI if we think those outputs will be “good” in some sense. We might think the AI is good in a statistical sense because we inspected the outputs, or because we read an evaluation study with robust evaluation of many outputs, or because we make some assumptions about how an AI was developed that make it “good.” However, users could also consider facts about how the model was built (such as information about the training data).

If you are using AI to make personalized note-taking software, facts about the training data may not be very high stakes. However, if we want to buy an AI product to ask medical questions, we might care deeply about both AI outputs and inputs to said AI. We most likely want to know that a doctor has looked at some of the model’s outputs and attested they are “good”; we might also want to know that there were some inputs from actual doctors such as content from medical textbooks and research papers used in the development of the original model. Finally, when we get a medically relevant output from an AI system -- e.g. the system we paid to access has printed out some text telling us to take a medicine or take some action -- we ideally want that output to be verifiably linked to information about the evaluation of the model, and ideally the training data as well.

## II. How AI products are chosen today: four channels of evidence

If we look at the key factors that might cause someone shopping for AI products today to pick one product over another, I think we can bucket these into four groups. Put another way, most “AI buyer choices” can be traced to evidence or beliefs from one of four channels of information:

-   the “outputs” channel. How good are the actual information outputs from an AI system?

-   the “inputs” channel. How were specific models used in an AI system trained and how was the overall system developed?

-   the “product” channel. Covers factors related to the delivery of the information outputs: pricing, uptime, latency, UX, privacy/compliance, support, lock-in, etc.

-   the “internals” channel. Facts about model machinery, the channel we’re furthest from being able to make practical use of, but potentially a very valuable channel.

The product channel matters a lot if you’re buying an AI product today. However, it’s the channel I’ll discuss the least in this post, in part because the focus here is on data-related differentiation but also because generally getting information about product factors currently works pretty well and thus enables relatively healthy market dynamics. We also won’t talk much about the internals channel, e.g. making decisions based on the results of interpretability-based studies, though I think this will be increasingly important to think about going forward. Instead, this essay focuses on the missing value of the inputs channel, and on how attestations can connect inputs to outputs.

At present, I think most AI users are choosing primarily based on beliefs about outputs plus some broad assumptions about inputs. Those beliefs about outputs may range from “my friends told me Claude Code outputs good code” to “I read the recent model cards” to “I run my own private eval set.” The corresponding assumptions about inputs are usually something like: the frontier labs probably sourced strong data, had capable people inspect and filter it, and used best-in-class training practices.

That is often reasonable. Outputs matter most for many use-cases, and if I only care about outputs, information about training is mainly useful as a proxy for output quality. Still, distinguishing these channels can improve AI literacy by more clearly separating the facts about outputs and inputs that might drive consumer behavior. That helps both consumers choose and developers differentiate.

## III. Why outputs alone may not always be enough

How do we know if the information outputs from an AI system are good? Let’s return to our first example: imagine a user who is looking to buy an AI product to help write personal note-taking software (and more generally play around with AI-coded personal software). This user probably plans to send a prompt to an AI model that looks something like this: “write me the code for software I can use for daily note-taking” (perhaps with a bit more detail regarding their personal preferences for how the software should work).

Say this user can do a “trial run” and send this prompt to three different AI providers, A, B, and C. How will this user decide which provider product to buy?

### Option 1: inspect outputs yourself

One option would be to look at the output from each model and assess the quality of that output. If the user is already an expert in this domain, perhaps they can just read the code produced by all three models and identify an obvious “best” model. Of course, if they wanted to have some statistical rigor in evaluation they’d probably want to look at more than one sample per model, though this will create some budgeting challenges and basically means the user needs to conduct their own benchmarking study. For a fuller treatment of the topic of looking at model outputs statistically, see e.g. [evalstats] from Ian Arawjo.

### Option 2: rely on published evaluations

Another option that also uses the outputs channel would be to look at the results of an already published benchmarking study, either from the model provider or from a third party. In this case, the user would basically be making the assumption that “other people tried similar inputs, and performance on those related tasks will probably proxy for performance on the task I care about.” Here the rigor of the benchmark matters: how many total variants were tried, who checked that the output worked, etc.

When AI developers themselves or third party evaluation organizations produce a benchmarking study, the results of these studies will impact the organizations’ reputation, so generally we should expect these kinds of studies to be reasonably consistent in terms of providing real signal. Benchmarking will always be noisy, but over time, there are incentives to evaluate models in ways that accurately reflect differences in capabilities. In other words, this approach should be pretty decent, and if we only ever have access to these kinds of signals for consumer decision-making, we could sustain a reasonably efficient market for AI products.

### Option 3: rely on vibes and reputation

A third option after “do your own evals” or “read the best recent evaluation report” is to simply seek out a more general vibes-based ranking for the “most intelligent” model or the “best” AI developer. I think this is what many people are doing in practice right now, though there is certainly a small population of power users who diligently run their own personal benchmarking processes each time a new model releases.

This approach is also not necessarily that ineffective. A vibes-based approach likely does integrate reputation and social proof in a way that matches other kinds of consumer decision-making and creates decent outcomes. Not everybody needs to read the auditing deep cuts or full review history for every product they buy.

What’s interesting is that using vibes to generally rank AI companies actually starts to mix information from the outputs channel and the inputs channel, because people are making some assumptions about training data and the training process itself. I think most people choosing with vibes are indeed assuming that AI developers themselves and third parties have evaluated the outputs of the model and found those outputs to be good, and perhaps that AI developers have special internal-only evaluation practices and employees that are especially skilled at AI evaluation. But this approach likely also involves assuming that the labs have used “best in class” training approaches, have sourced the best data they can get their hands on, and have a large team doing whatever they can to make models better. Critically, vibes-based decision-making is not entirely inputs-agnostic, and it’s important to acknowledge this because I think it means people will care about inputs in the long run.

### The issues with current status quo

However, this is also where we can start to envision some room for improvement in the AI consumer experience. If consumers had more specific knowledge about the inputs to an AI product, both broad facts about the training data and facts about the evaluation process, this could be useful to them. Even as underlying training techniques enable models to become more general and more broadly intelligent, it seems likely that the presence of certain types of data, data about certain topics, and data from certain experts in model inputs will proxy for output quality.

In the medical case, information about the outputs might be more important. If sketchy training data leads to outputs that top doctors give a thumbs up to, we might take that. And overemphasis on training data may create metric chasing, e.g. including social media posts from medical doctors in pre-training data to drive up the volume of tokens from MDs. But input information should still provide some signal. Either we want real medical data in the training set or we want solid evidence our AI system has figured out medicine from first principles.

More broadly, both output studies and input details are proxies for future quality. For statistical systems, that is often the best we’re going to get. The under-emphasized problem is that as models become more general, comprehensive output evaluation across all the things they can do becomes prohibitively expensive. Many people have commented on this; see, for example, the [“Evaleval”] project and its [“Every Eval Ever”] effort, Raji et al. on [“everything in the whole wide world benchmarking”], and recent online discussions in which people contrast their personal experience with a model and that model’s benchmark results.

The labor required to really, fully, comprehensively evaluate increasingly general technologies will be very costly. We’re going to need a whole lot of doctors and scientists to give feedback on a whole lot of LLM outputs to be sure we can use LLMs effectively in those contexts. But we’re also going to need a whole lot of general users, with distinct combinations of niche interests, needs, preferences, etc., to give feedback as well. All this feedback will be relevant to evaluation of current models, but also relevant to the training of new models, the design of reinforcement learning environments, etc. It’s going to take time to do all this evaluation, and will in some sense involve a kind of commandeering of the entire knowledge economy.

Simple napkin math suggests the relevant numbers get big quickly. Suppose we want rigorous evaluation coverage across 30 major medical specialties, with 1,000 representative cases per specialty, 10 independent physician reviews per case, and 30 minutes per review. That is 300,000 physician judgments, or 150,000 physician-hours, for one pass over one model version; at \$200/hour for specialist time, that is about \$30 million just in doctor-review labor. And that is before benchmark design, adjudication, compliance, or program management.

It’s worth thinking about how many hours of physician labor you want upstream of a chatbot prescribing your medicines!

Note that here I’ve focused on a running example of a consumer from the general population. I think this story is useful, but you might be thinking “I just don’t believe consumers will care that much”. You may be right -- and critically, all the above argumentation applies directly to the context of enterprise AI users, who have much more bargaining power and are very likely to care about exactly all these issues described above.

## IV. What current “upstream markets” look like: deals, marketplaces, and labor

Before an AI product is brought to market for consumers to consider, developers must also participate in two important upstream markets: acquiring training data and acquiring evaluations. Some companies may get their training and evaluation data without direct outside assistance, e.g. just scrape the training data and use in-house employees to do evals, but I expect as the industry matures both of these domains will become more market-like, with a broader set of data sellers at the training level and evaluation providers to choose from. Note here I’ll sometimes use “data” a bit loosely to cover both training inputs and evaluation labor, since both are forms of human knowledge work that developers are trying to source.

There is already an informal market for evaluators. It is not yet as legible or standardized as something like AWS Marketplace, but frontier labs already hire or contract with domain experts, benchmark designers, red teamers, and specialized third-party evaluators. Organizations like [METR][1] and [Apollo][Apollo Research] along with similar evaluation and auditing groups, are early examples of a more specialized evaluation layer emerging around frontier AI systems.

Now, let’s step away from the perspective of someone picking between AI products and instead consider a developer who wants data to build their AI product, or a seller, either an individual or an organization, looking to monetize their content.

### Three current market forms

I’ll bucket the ways we can buy training data and evaluation labor right now into three broad categories. These are ideal types rather than perfectly separate boxes, but they capture a lot of the current landscape:

-   **Big licensing deals.** These are bespoke boardroom transactions: a lab or platform negotiates directly with a publisher, forum, data broker, or other large rights-holder for access to a corpus or feed. The deal terms are highly customized and usually cover things like scope of use, refresh cadence, exclusivity, audit rights, indemnity, and payment over time. An example would be [Google reportedly paying Reddit roughly \$60M/year for access to Reddit data], with Reddit separately disclosing in its [S-1] that its January 2024 data licensing arrangements had an aggregate contract value of \$203M.

-   **Licensing via marketplace.** This is more like online shopping for large datasets. Instead of a bespoke negotiation, the seller lists a relatively standardized product with a posted description, delivery format, usage terms, and price, and the buyer can compare options much more quickly. An example would be going to AWS Marketplace to buy [12 months of “Anonymized, non-aggregated granular consumer-level data across all asset classes” from Equifax for \$175k]. Economically, the appeal here is lower transaction cost and easier comparison across sellers, though the quality and rights picture may still require substantial diligence.

-   **Pay individual people, per task or per hour, for data outputs.** This is the crowdwork or expert-labor bucket. Here the buyer is not primarily acquiring a pre-existing corpus; they are paying people to generate judgments, labels, rankings, reviews, or other evaluative outputs under a specified protocol. An example might be paying somebody [via Prolific] at [at least \$8/hr, and typically more like \$12/hr] to label web data, or paying domain experts to peer review model outputs. This category matters especially for evaluation, where the scarce input is often expert attention rather than a static archive.

One nearby fourth form, if one wanted to break the taxonomy out further, would be recurring API or feed access rather than transfer of a bulk dataset: paying for ongoing, metered access to a live corpus or stream. I think that form mostly collapses back into Categories 1 and 2 depending on how standardized the arrangement is, so I am leaving it as an adjacent case rather than promoting it to a main bucket.

See also the data deals tracker [here][fragmented] from the authors of “A Sustainable AI Economy Needs Data Deals That Work for Generators”.

### Collectives and intermediaries

Another idea that’s gained some popularity over the last decade is the notion of joining a data cooperative, collective, union, or intermediary. Generally, the idea here is that you join the coop, contribute data, and some actor in the coop transacts in a market on your behalf. In fact, there are some ways to join a data cooperative today. Organizations such as [Swash] and [Brave Rewards] monetize various online actions and tasks. The user bases of data-coop-style tools are very small compared to general Internet usage. For reference, Brave reported [101M monthly active users as of September 30, 2025], while StatCounter has recently put Brave at roughly [1% of worldwide desktop browser share]. Some of the means of monetization, e.g. watching ads, are also quite different from an aspirational vision of data markets in which data sellers are spending their time crafting valuable documents and records and then being rewarded for their contributions to shared epistemics. I do really believe that a useful North Star is trying to shoot for a world in which more overall human work looks like the good parts of journalism, scientific peer review, editing Wikipedia, and participating in Q&A, with the bad parts minimized or automated away.

While the above data cooperatives involve a technical approach to enabling cooperation, and participation remains niche, I actually think there is a lot of low-hanging fruit for applying the collectives/coops/unions idea to the three types of markets described above.

First, for the big boardroom deals, we could imagine pools of users directly weighing in on the deal conditions. For example, when it comes time for Reddit to renegotiate with Google or others, they loop users in, either voluntarily or under threat of collective action. Second, data coops can post their own quality-assessed CSV file for sale on AWS Data Marketplace right now, but they still need social and technical support to actually organize in the first place and produce a good CSV. And there is a large body of work, including ongoing efforts, that aim to support collective bargaining for data workers, see e.g. the body of work from Dr. [Saiph Savage] and [Data Workers’ Inquiry] from DAIR.

One consideration is that successful organization of data workers may actually involve a shift from crowdwork markets to collectives that sell bundled data, i.e. moving more overall information from Category 3 to Category 2, or even 1.

### Two policy levers: data protection and attestation

There is also an emerging set of actors interested in supporting various forms of what we might term “data protection for the AI age”. [Cloudflare’s public support of anti-scraping] is one example.

I think it is useful to start from a fairly grim baseline: many people assume their data will be scraped, distilled, and reused unless they actively block it through anti-scraping, anti-distillation, poisoning, preference signals, legal enforcement, or some mix of these.

In general, supporting data protection action can make it more likely that data sellers will engage with markets rather than give up because everything will be scraped anyway. In other words, some actor, public or private, needs to do some level of policing for a market to emerge. This is a bitter pill from an open-culture perspective, since open culture is foundational to modern ML, including both peer production of critical training data and open-source implementations of algorithms and tooling. Still, there is likely a middle ground in which open culture continues in many domains while others become more financialized. Any actions that move us away from the current situation are probably net good in the short term, though we should be cautious about a pendulum-swing-too-far data-cartel scenario in which nobody can use any information without paying.

Under an attestation-centered regime, data might still be readable or even openly available, but what becomes scarce is the ability to make a trusted downstream claim about provenance, licensing, evaluation, or output identity. Scraping without the attestation may no longer be enough to compete in markets where buyers, enterprise customers, insurers, or regulators care about verified inputs and verified outputs.

This is why attestation is particularly appealing for public AI strategy. It suggests a path where openness and bargaining do not always have to be direct opposites. In the strongest version, a dataset or corpus might be free for research or public-interest AI use, while commercial actors must pay if they want to rely on it in an attested product or otherwise market the trusted provenance relationship. These approaches are complements rather than substitutes: better data protection may be needed to get participation off the ground, but attestation changes the long-run market game by moving value toward attestations rather than raw tokens.

## V. Why attestation improves incentives

We need to address three fundamental constraints that affect value measurement and value transfer in the context of AI:

-   the [economic properties of information][Arrow on the economics of information], non-rivalry and non-excludability, make it very hard to create efficient markets for information. But if markets attach value to attestations rather than bits, we may be able to have our cake and eat it too: widely distribute information via AI as a public good while retaining some of the coordinating benefits of markets

-   the value of data, as defined by any kind of [data counterfactual estimation method] (”how does accuracy change if unit or bundle of data is removed from training”), is generally small in raw magnitude unless data is grouped together as some kind of collective

-   open data can, in some cases, directly disempower certain subsets of workers by making the relevant knowledge easier to copy than to bargain over. An attestation layer offers one possible way to preserve some openness while still giving those groups something commercially salient to negotiate around

We could somewhat address these challenges by just trying to coarsely distribute value to data creators: just worry less about provenance and distribute resources through something like a data-dividend public wealth fund. I think that may be a useful transitional approach in the short term, but likely not the ideal end state.

### Why AI buyers care

For buyers, the benefit is straightforward: inputs and outputs become inspectable product features. Instead of relying only on benchmarks, reputation, or vibes, a buyer could ask more specific questions: How many credentialed authors contributed to training data? What process verified their work? What upstream sources were actually licensed? Was this particular output generated by a model version whose provenance and evaluation records I can inspect? In higher-stakes domains, that still does not replace output inspection, but it gives downstream choice much more structure.

In some settings, we can expect transparency around model outputs themselves to become a requirement rather than a premium feature. A regulator or enterprise buyer may increasingly want not just “trust us” but verifiable disclosure that a given artifact came from a given model and from a model with a certain attested pedigree.

If those attestations become known to be predictive -- e.g. the AI model with stronger attestations around its training data is actually better at giving health advice -- they also reduce some of the appeal of indiscriminate scraping or distillation. A rival might still imitate outputs, but the attested relationship itself becomes part of what the buyer is purchasing.

### Why contributors might care

For creators, evaluators, and data workers, the important shift is from selling anonymous tokens to participating in visible, renewable labor relationships. Attestations for training and evaluation can be managed and aggregated by some kind of intermediary, collective, or union so people do not need to transact individually with AI companies.

If verified attestations become important to consumers or regulators, that would immediately bring more data work out into the open. It would make it easier to treat these jobs as real careers and harder to treat data workers as invisible or precarious labor. Note that while I’ve been using doctors as a convenient running example -- a relatively small group with easy credentials to verify and existing social infrastructure for collective action -- the same logic applies to many other kinds of knowledge work.

The economics of maintaining a trusted relationship are also very different from the economics of acquiring tokens. The actual bundles of information in training data are and will remain mostly non-rival, and often hard to exclude. But contracts with people or collectives are not just about buying rights to transfer bits. These are contracts for labor which must be renewed and maintained. A world of data-with-attestations is therefore a world with more ongoing relationships and more room for bargaining.

### Why labs, regulators, and public AI builders might care

For labs, credible attestation could become a meaningful source of differentiation, though adopting any particular standard is a collective action problem. This is where auditing, evaluation, and safety cases begin to connect to regulation, insurance, procurement rules, and industry self-governance.

The building blocks for this market already exist in the upstream markets described above. The main difference with attestations is that the fact a person made or evaluated some portion of the data would no longer be hidden, but rather made prominent. If an AI builder who uses attested or full-consent data early on is able to produce good models and prove that buyers care about those records, that creates pressure for other AI developers to play along as good-faith actors in the market.

An immediate downside for some labs is that data and evaluation may cost more.

A version of an attestation-based provenance system that gets things really right could be good for AI developers, data creators who want to add knowledge via pretraining, content creators who want to be rewarded when their content is retrieved, public-interest model builders who want to distinguish civic from purely commercial use, and people who want to use AI to produce things and sell them, e.g. software developers selling vibe-coded software. In the strongest version, the flow of attested data and AI outputs also becomes a governance lever, in the sense that healthy markets for anything act as both a kind of computation over preferences and a kind of governance.

## VI. Implementation and caveats

### Enforcement

Here I’ve talked in broad strokes about attestation, provenance, and verification a bunch, but have remained relatively agnostic to any particular implementation details. Attestation and verification will involve a mix of technical and social means of enforcement. They might lean more heavily on technical innovations, e.g. new approaches for embedded cryptographic signatures, or more heavily on social forces, e.g. organizations that enforce attestations through reputation.

At a high level, there are at least six areas of existing/ongoing work that could support attestation:

-   [C2PA] is, I think, currently the closest technical analogue. It already supports signed provenance for AI/ML models, training datasets, outputs, fine-tuning, and versioned releases. If one wanted to implement parts of this proposal tomorrow, C2PA is an obvious place to start.

-   [in-toto] and [SLSA] provide a generic supply-chain pattern for authenticated statements about subjects, materials, builders, and verification.

-   The web3 and verifiable-credentials worlds have also spent years experimenting with portable attestations, signed claims, and selective disclosure. I do not think AI provenance needs blockchains by default, but that design space is still relevant as a source of ideas about interoperable attestations. See e.g. [Attest].

-   [Model cards], [datasheets][2], and related documentation frameworks make model and dataset facts legible via standardized processes.

-   [Frontier AI auditing] focuses on institutional assurance: who gets access, what independence standards matter, what level of assurance an audit provides, and how results should be communicated.

-   [Data licensing] explores the contractual layer around who can use what data, for which purposes, and under what terms. That layer is not itself an attestation format, but it helps define the claims an attestation system would need to make legible and enforceable.

### How we might transition towards attestations

Recent trends in dataset documentation suggest a world of transparent data for AI models is not yet around the corner. Dataset details in model and system cards remain extremely short and vague, as reflected in the [Foundation Model Transparency Index], and understandably are likely to remain short and vague until additional legal clarity is achieved. That said, for both researchers and consumers, it will be very valuable to keep an eye out for new open releases, such as models from [EleutherAI], [AI2], and academic groups (see e.g. recent [work] from Fan et al. on model training using highly compliant web data).

But critically, almost all the actions that data protectors might take now, including developing and offering anti-scraping technologies, helping to socialize anti-scraping and AI preference signals, and supporting related research on data value estimation, full-consent LLMs, partnerships with national labs, etc., are likely to also make it easier to work toward attested data.

# Changelog

-   *Sep 12, 2026: This topic is seeing a lot of attention. I took another pass to try to make the “standing” version of this post tigher. I removed the Appendices, including the “toy example” attestation scehema as I expect it will soon be easier to simply link relevant OSS standards in this space.*

-   *April 27, 2026: I made some edits throughout to condense this longer post and improve flow. I also wrote an additional bullet point summary.*

------------------------------------------------------------------------

*\[You can also find this [post] on leaflet; More on atproto blogging experiments in a later small post!\]*

  [blue and white light streaks]: ../media/attestation-across-the-ai-supply/1f620f239a935feda586.jpg "blue and white light streaks"
  [Solen Feyissa]: https://unsplash.com/@solenfeyissa
  [Unsplash]: https://unsplash.com
  [datasheets]: https://arxiv.org/abs/1803.09010
  [model cards]: https://research.google/pubs/model-cards-for-model-reporting/
  [data provenance]: https://www.dataprovenance.org/
  [Frontier AI Auditing]: https://www.averi.org/ourwork/frontier-ai-auditing
  [C2PA]: https://spec.c2pa.org/specifications/specifications/2.3/ai-ml/ai_ml.html
  [“Introducing ChatGPT Health”]: https://openai.com/index/introducing-chatgpt-health/
  [METR]: https://metr.org
  [Apollo Research]: https://www.apolloresearch.ai/
  [AI Security Institute]: https://www.aisi.gov.uk/
  [fragmented]: https://research.brickroad.network/neurips2025-data-deals
  [public procurement guidance]: https://www.whitehouse.gov/wp-content/uploads/2024/03/M-24-10-Advancing-Governance-Innovation-and-Risk-Management-for-Agency-Use-of-Artificial-Intelligence.pdf
  [regulatory transparency requirements]: https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act
  [Arrow on the economics of information]: https://www.nber.org/books-and-chapters/rate-and-direction-inventive-activity-economic-and-social-factors/economic-welfare-and-allocation-resources-invention
  [Jones and Tonetti on the non-rivalry of data]: https://www.aeaweb.org/articles?id=10.1257/aer.20191330
  [data dividends]: https://www.nickmvincent.com/static/eaamo_data_dividends.pdf
  [Deng et al. on training/evaluation overlap via benchmark contamination]: https://aclanthology.org/2024.naacl-long.482/
  [Raji et al. on the limits of “general” benchmarks]: https://openreview.net/forum?id=j6NxpQbREA1
  [Liang et al. on holistic evaluation and coverage gaps]: https://arxiv.org/abs/2211.09110
  [Castro Fernandez on auditable data-sharing arrangements]: https://doi.org/10.1145/3589317
  [evalstats]: https://github.com/ianarawjo/evalstats
  [“Evaleval”]: https://evalevalai.com/about/
  [“Every Eval Ever”]: https://evalevalai.com/projects/every-eval-ever/
  [“everything in the whole wide world benchmarking”]: https://arxiv.org/abs/2111.15366
  [1]: https://metr.org/
  [Google reportedly paying Reddit roughly \$60M/year for access to Reddit data]: https://apnews.com/article/a7f131c7cb4225307134ef21d3c6a708
  [S-1]: https://www.sec.gov/Archives/edgar/data/1713445/000162828024011789/reddit-sx1a3.htm
  [12 months of “Anonymized, non-aggregated granular consumer-level data across all asset classes” from Equifax for \$175k]: https://aws.amazon.com/marketplace/pp/prodview-vgmxklm42lhmq
  [via Prolific]: https://www.prolific.com/pricing
  [at least \$8/hr, and typically more like \$12/hr]: https://researcher-help.prolific.com/en/article/2273bd
  [Swash]: https://swashapp.io/about
  [Brave Rewards]: https://support.brave.app/hc/en-us/articles/360027276731-Brave-Rewards-FAQ
  [101M monthly active users as of September 30, 2025]: https://brave.com/blog/100m-mau/
  [1% of worldwide desktop browser share]: https://gs.statcounter.com/browser-market-share/desktop/worldwide
  [Saiph Savage]: https://www.saiph.org/
  [Data Workers’ Inquiry]: https://data-workers.org/
  [Cloudflare’s public support of anti-scraping]: https://www.cloudflare.com/en-ca/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/
  [data counterfactual estimation method]: https://arxiv.org/abs/1904.02868
  [in-toto]: https://in-toto.io/docs/what-is-in-toto/
  [SLSA]: https://slsa.dev/spec/v1.2/
  [Attest]: https://attest.org/
  [2]: https://www.microsoft.com/en-us/research/project/datasheets-for-datasets/
  [Data licensing]: https://datalicenses.org/
  [Foundation Model Transparency Index]: https://crfm.stanford.edu/fmti/December-2025/index.html
  [EleutherAI]: https://www.eleuther.ai/
  [AI2]: https://allenai.org/olmo
  [work]: https://arxiv.org/abs/2504.06219
  [post]: https://dataleverage.leaflet.pub/3mizn5hsjg5vo
