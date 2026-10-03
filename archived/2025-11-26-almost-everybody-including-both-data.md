---
title: "Almost Everybody -- Including Both Data Creators and AI Companies -- Stands to Benefit from Clearer \"Data Rules\"."
subtitle: "In fact, anyone who doesn't think they will be a \"big winner\" long term benefits from clear rules, even if it means training data costs more in the short term."
date: "2025-11-26"
original_url: "https://dataleverage.substack.com/p/almost-everybody-including-both-data"
content_id: "substack/post/178625271"
authors: ["Nick Vincent"]
published_at: "2025-11-26T17:24:37.654Z"
source_updated_at: "2026-09-13T13:52:12.201Z"
archived_at: "2026-09-25T20:33:46+00:00"
source_body_sha256: "c718090febc0b9602a1d0c6b284afd165f14f8b300509c05240a83f405296cf7"
---

*Note to the reader: this is a very long post! I’d really love to hear what’s convincing here, what you’re skeptical of, etc.*

![File:Shichiri Ferry Boat.jpg]

"Shichiri Ferry Boat”, Utagawa Hiroshige, [Wikimedia Commons].

## Part 0: Introduction

This post will synthesize several related points about AI data flow from several recent Data Leverage Newsletter posts. I’ll frame the entire (long) post around the idea of creating new “Data Rules” that can address the incentives of data creators (the archetypal “Author”) and AI developers (the archetypal “Model Builder”) while simultaneously attempting to minimize tensions between a transactional, market-focused approach to data flow and the sustenance of [digital commons] and [open knowledge] culture.

First, in Part 1, I’ll make a renewed argument that data creators and (most) AI companies are in the same boat, in that they stand to benefit from clear “Data Rules”: widely accepted and enforced rules and norms that allow data creators/stewards to share, license, and otherwise transact with their data with a clear set of options that impact the specific usage of data in AI pipelines (training, retrieval, eval, etc.).

This is because **AI companies are, for now, mainly just selling “outputs**”. With some risk of being overly reductive, we can observe that most of the money flowing into AI companies for AI services (i.e., money from individual consumers or enterprise customers, not investing money) is basically some “user” paying money to access payloads of text and/or multimedia. Consumer subscriptions, enterprise contracts, and pay-per-API-call are all, at a surface level, ways to pay for just payloads of tokens. These AI outputs have very similar economic properties to training data (the actual artifacts here are still mainly just text or media files!)**,** which means that data policy debates should not be reduced to “Tech vs. Everyone Else”, but rather there is the potential for **alliances between data creators and AI companies**. The same policy changes that might help prevent AI companies from “stealing” data from creators could also help prevent AI companies stealing from each other, ultimately benefiting AI companies.

(There’s more writing to be done about the very granular similarities and differences in the economic properties of human- and AI-generated content; here we’re just making the high-level argument).

Then, in Part 2 we’ll concretize discussion of “Data Rules” that can benefit both data creators and AI companies by walking through one relatively specific proposal (much of this will repeat arguments from Collective Bargaining for Information writing and public AI advocacy). This will involve a focus on collectives as the main bargaining unit and an integration of technical data valuation work into the bargaining process. There will be specific discussion of standardized contract templates and enforcement.

In Part 3, we’ll further address the tension between advocacy for stricter Data Rules and efforts to support the constellation of related “open” ideologies and initiatives that includes [open knowledge], [free-culture], open source software, open source AI, peer production, and citizen science. This tension is a **really big deal** and I believe that having a clear path to resolve it will be a big coalition building unlock for innovation on data paradigms for open source AI, and for public AI. In short, the tension stems from this fact: Open knowledge/open source efforts, in general, try to make information and code *non-exclusive* (anyone can copy, modify, share), whereas financialization/markets for information, in general, depend on making information *exclusive* (pay to access, use, or resell). Of course, there is nuance here and cases where open knowledge can complement private goods (you buy a book *because* you read about it on Wikipedia).

Stricter Data Rules will likely cause more overall knowledge to be governed by market-like mechanisms (in some sense, the “Walled Garden” response to AI developments has already created a long-term setback for an “open knowledge” agenda). We’ll likely have to swallow some bitter pills: in some cases, open data shared by one group of people may reduce another group’s bargaining power. And in some cases, open data sharing may preferentially benefit private actors with more compute over smaller players like non-profits or public AI initiatives. However, we can resolve much of this tension by:

1.  ensure that any new Data Rules still make it easy for communities to elect, in a bottoms-up fashion, to publish content into the open, subject to commons governance. Don’t market-ize everything!

2.  maintain pathways for open but use restricted data sharing (e.g. the Creative Commons Preference Signals [proposal]).

3.  continue efforts to document the *contents* of our knowledge commons so people have a realistic understanding of how commons stock affects data that might enter private markets. This would ensure that creators are not being misled about the value of their data.

4.  potentially controversially: consider a top down effort to define certain categories of content and knowledge that are “commons by default”, or at least attempt to create clarity around currently existing de facto carve-outs. This might enable some kind of “détente” for current legal and cultural battles (for instance, it would probably be net good for certain organizations to get a cleaner “green light” for training on the Common Crawl, and clarify the exact organizational boundary: non-profits? universities? public benefit corporations? etc.).

Before we dive in (or if you don’t want to dive in immediately), here are the key takeaways for different potential audiences of this article:

-   For people building and operating AI systems: the current Ambiguous Data Rules have some upsides (immediate access to training data like Common Crawl) but also massive downsides (legal risk, model stealing). **It really might be the case that embracing a “clean data flow” initiative — embracing data markets, sharing and promoting data control tools, engaging in data policy discussions — will help some AI companies succeed; if we continue on our current path of ambiguity this will only benefit a few actors in the long run.**

-   For those who create data: Collective bargaining and assessing data value on the creator side will be critical for effective bargaining; don’t go to the (data) bargaining table alone!

-   For open knowledge: In the wake of AI progress (and corresponding externalities), we need to take explicit efforts to support data commons (enabling contribution and self-governance, financial support via both public funding and structured deals like Wikimedia Enterprise). To reduce possible conflicts between open knowledge and data markets, we need make it very clear what is in various commons, and potentially even create a top-down definition of “free to train” content (i.e., an “AI Aware” public domain-like designation)

-   For AI users: Better Data Rules mean models trained on higher-quality, consented data with clearer provenance — and less legal risk for products that people might start to rely on.

------------------------------------------------------------------------

## Part 1: Issues and Archetypes

### A Big List of Open Issues in AI

First, I’ll recap a number of “open issues” in the AI world. These will be attempts to summarize issues that exist in the current discourse in about one line (and a few additional bullet points).

First, there are (at least) four distinct open issues that relate to copyright and licensing. Here, I’ll use “intellectual property” very broadly to refer to content that might be used for AI research and development and might be impacted by copyright law or licensing. For a comprehensive technical discussion of model memorization and its relationship to copyright, see Cooper and Grimmelman \[[arXiv]\].

1.  The “Training on IP” issue: Model builders have been accused by various copyright owners of illegally acquiring (via direct download, torrent, etc.) IP in a way that violates copyright law to **train** AI models (example: coverage from [NPR] of author lawsuit against Anthropic).

2.  The “Retrieving IP” issue: Model builders have also been accused of building systems that **retrieve** IP at “inference time” and then presenting that content in a non-compliant way (example: coverage from [Reuters] of the New York Times’ cease and desist against Perplexity).

    -   Note the distinction between **access**, **training**, and **retrieval** is something that is (1) underappreciated in the ongoing Data Rules debates, and (2) something that will come up again.

3.  The “IP Memorization/Regurgitation” issue: Combining the above two issues, model builders have been accused of building systems that memorize and then regurgitate content (example: see long-running, high profile NYT lawsuit against OAI which centers this concern)

4.  The “Who Owns the Outputs” issue: When a model generates content, it is unclear which person or organization owns that output (example: [Reuters][1]).

Next, four issues that are about consent, compensation, and credit (“3 C’s”, as referenced in works like Kyi et al \[[arXiv][2]\]).

1.  The “consent” issue: Creators and data subjects often don’t know their work or likeness is being used for training and have no way to signal consent or opt out.

2.  The “compensation” issue: Most scraped data is entirely uncompensated.

    -   Note that this is distinct from the consent issue.

3.  The “credit” issue: Separate from the consent and compensation, the current AI paradigm rarely offers any avenue for data creators to receive credit for their contribution (ranging from a general “thank you to people who edit Wikipedia” from AI companies to a much more detailed “credits page” for each LLM, arguably *currently required* but ignored for some attribution-requirement-licensed content).

4.  The “traffic siphoning issue”: Finally, models and services built using scraped content siphon clicks, ad-revenue and attention away from the original creators/publishers.

    -   “Traffic siphoning” is not just an issue for organizations that had their content scraped; a content org could agree to a data licensing contract, but the total traffic loss outweighs the payment they receive!

    -   Also not just an issue for for-profit entities; also an issue for e.g. Wikipedia and StackOverflow, as I’ve been writing about for a while!

    -   References: \[[Washington Post]\]

Next, three issues facing AI companies:

1.  The “Model Stealing” issue: One company’s models or outputs are used to build new models without clear licensing or compensation.

    -   References: OpenAI and Deepseek \[[The Financial Times]\]

2.  The “Benchmark Contamination” issue: Evaluation data is intentionally or accidentally used in training, which misleads model builders and/or their customers about model capabilities.

    1.  See this anti-scraping tool developed primarily with benchmark contamination in mind: \[[GitHub]\]

3.  The “Private Training Data Reconstruction” Issue: Models unintentionally memorise and leak sensitive data from their training sets, creating privacy liability for model developers.

    -   References: \[[Meng et al.] arXiv link\]

    -   Highly related to the regurgitation issue above, but a distinct source of liability.

Finally, there are also some problems with the current paradigm for people who just want to access or share knowledge:

1.  The “changing incentives to share knowledge openly” issue: Because the “rules” of information flow in the post-AI age remain nebulous, there’s arguably a “damping effect” on contributions to open knowledge.

    1.  Includes loss of traffic (overlaps with “traffic siphoning” issue), technical challenges from scraper bot traffic, deluges of “slop” contributions (some might be good faith) \[[Washington Post][3]\], threat to contributor motivation if their “open” contributions benefit private actors, etc.

    2.  Very concerningly, threats to contributor energy creates the potential for [Tipping Points for Content Ecosystems].

2.  The “paraphrase dominance” issue: People increasingly consume paraphrased versions of works rather than the works themselves.

    -   Paraphrases can flatten style, might destroy chains of provenance, and might seriously hinder pluralism (current interfaces tend to present a single “best answer”).

    -   See this Nov 10, 2025 [tweet] from Ivan Vendrov: “I still can’t have full-text search over the world’s books, but because the LLM providers are de facto allowed to train on them, the incentives point me to read bastardized LLM-paraphrases vs direct quotes from human authors”

There are other big debates about AI, of course! We won’t talk much about chip exports, compute build-out, energy usage, etc. here.

### Three Archetypal Perspectives

Even with some attempted categorization, that’s still a lot of issues. I think we can further organize this larger set of issues by considering three archetypal perspectives:

-   The archetypal creator, who we’ll call the “**Author**”. This will cover all people who want to create something and get credit for it: artists, coders, writers, researchers, almost all white-collar workers, etc. The “Author” is someone who has created some knowledge artifact (like a book) and wants to get some kind of compensation for it (direct payment, royalties, a salaried job, etc.).

    -   This perspective is concerned with all four IP issues above and the four consent/credit/compensation issues, and is also affected by “Private Training Data Reconstruction”.

-   The archetypal “**Model Builder”**. This covers people who want to build models and make money off of them. Of course, this includes anyone working on AI products in industry (both start-ups and incumbents.) But it also includes, indirectly, academics who work on “applied AI”. Generally, support for many “applied” subfields in academia rely on the existence of profitable companies selling the technologies they work on (to supply grant funding, collaboration, student internships, etc.)

    -   This perspective is concerned with copyrighted outputs, and especially with Model Stealing and Benchmark Contamination.

-   The archetypal “**Open Knowledge Advocate”**. This covers people who want to share knowledge with the world, for instance ideologically motivated contributors to peer production (like Wikipedia) and open-source software projects. The perspective is concerned with [commons governance problems].

    -   An Open Knowledge Advocate is almost always an Author too; they just create documents that are contributed to commons instead brought to a market.

It may also be helpful to consider the Reader: the person who will actually consume/attend to a Book, a Model Output, or a Wikipedia article. We might consider both individual Readers (what we typically think of as “consumers”) and enterprise Readers (entire organizations that subscribe to enterprise AI plans, buy organizational access to scientific journals, etc.).

### Simple Model of the Author and Model Builder Incentives

Our archetypal “author” wants to sell their “book” for the highest price possible (subject to supply and demand and the economic properties of information and cultural goods). Our archetypal AI model builder wants to get as many “books” as possible for free, but wants to sell access to their model (consumer subscriptions, API credits, enterprise contracts) for the highest price (again, subject to economic constraints).

It’s worth thinking through how people might become an Author, Model Builder, or Open Knowledge Advocate, and the general prevalence of each actor. Many people are really a mix of multiple of these archetypes. And pretty much everyone is a Reader at one point or another.

We can paint with a broad brush and say that most people are Authors in some capacity. In the increasingly digital world, many people who work for a living rely on the production of *some* kind of digital assets.

In comparison, only a small set of people are really Model Builders, and these people likely started as Authors (writing code, papers, and the like for their money) until they reached a position where Model Building incentives dominate (note there is a broader discussion to be had about the fundamentally managerial nature of AI/ML as an endeavour).

A small set of Authors become Open Knowledge Advocates, typically via social processes (finding out about an open source software project, etc.). And finally, there’s a set of people at the full intersection: AI researchers who write papers and code, are primarily funded by Model Building activities, but contribute (or used to contribute to) to open source and peer production. This is a non-trivial population, because as noted above, Open Knowledge culture is especially influential in CS and AI, driven in large part by the open source software movement and the particular influence of Wikipedia on natural language processing research.

Considering the perspectives of Authors and Model Builders, we start to see an argument emerge for why Model Builders might want stricter data rules: some Data Rules might require Model Builders to pay for their content but that set of rules could mean that that they can sell their AI outputs for more money! (Obviously if a particular model builder can have a “special model builder exemption” and get all their stuff for free, they’d want that. But, the point I want to make here is that policies that give model builders some kind of exemption for paying for stuff might in the long term *hurt* their ability to sell model outputs.)

Concretely, imagine this toy scenario (inspired by real events): a big American lab is at risk of losing \$5B in corporate contracts because their customers will use a cheaper model distilled by another lab. The American lab can support a new set of Data Rules that will require them to pay \$2B in retroactive payments to people in scraped Internet data and creates an additional \$1B in projected data costs for the next year, but the “stolen models” getting cracked down on means that the company is up \$2B.

### Tension with Digital Commons

There is tension between open knowledge (digital commons) and data markets; efforts to make certain types of information true public goods will affect markets for related information goods (I’m still very fond of making a comparison to [maps] here).

One obvious example here was the impact of Encarta, and eventually Wikipedia, on private encyclopedia-producing firms \[[HBR]\]. As another example, the growth of open source projects like R likely drove down potential consulting revenues for Stata experts (though hard to say for sure). A really good Wikipedia article may reduce sales of a relevant book, but could also boost sales (of course, it’s complicated, see e.g. coverage of work showing Wikipedia articles boost tourism \[[The Guardian]\], the [history of statistical software], the [value] of open source software more generally).

Anyone who is an Author, Model Builder, Open Knowledge Advocate, or Reader will be heavily impacted by what we’ll call the “Data Rules” — the big set of regulations, norms, and marketplace design decisions that impact how transactions for information are conducted. Is scraping legal? Who can scrape, and what can they scrape? When a creator adds a license or “preference signal” to a project, how does this impact what kinds of training or retrieval activities by model builders are allowed? How are preferences enforced, how do they flow between model weights and synthetic data? Etc. (See an overview of different license and preference signals proposals [here]).

Let’s discuss tensions between the Author and the Model Builder. Then we’ll get back to the tension between stricter Data Rules and open knowledge.

------------------------------------------------------------------------

## The Author and The Model Builder: In the Same Boat?

### A brief note on incentives and “favoring” Authors vs. Model Builders

First, as I’ve argued at length in this blog, giving people agency over their data can provide important [leverage] to the public that can mitigate power concentration. Many of the empirical projects that I work on and follow closely are relevant to the copyright/consent debates and a lot of my proposals lean towards the direction of giving more information and agency to “creators” — our archetypal Author.

However, it’s also important to restate that I myself (and many others in my kind of position) have conflicting incentives here! As someone who writes papers, code, etc. I have good reason to be aligned with the creator perspective. It’s important to me that I get (some) credit for my papers. In an extreme scenario, if starting tomorrow, all of an academic’s papers begun to receive zero citations or reads, this would negatively impact that academic’s career.

However, for CS researchers, the story is a bit different. CS academics stand to benefit from tech/AI companies making money (to fund student internships, grants, etc., and to prevent a sense of precarity in the field; if tech crashes it will be bad for CS academia in the short term). I also do generally believe that the computing industry creates a lot of value for humans, which is worth stating.

Finally, part of my whole motivation for my PhD was a deep personal interest in peer production; I’m a fan of open knowledge advocacy. I’m sure many others in academia have a similar story (and in particular the computing and AI academics have a strong connection to open source) ! It matters a lot to note these things, because many of the key decision makers in this space are facing conflicting incentives here. Like many others with similar conflicting incentives, I try to take a zoomed out, systems thinking-heavy perspective: how do we balance power for good long-term feedback loops? But it’s useful to restate the incentives here.

### AI Companies Sell Something that Looks a Lot like “Content”.

*Or, just how different is it to spend \$20 on a book versus spending \$20 on an AI subscription and having a model give you a bunch of textual outputs that look like a book and serve a similar purpose to reading a book? See also, Google memo “[We Have No Moat, And Neither Does OpenAI]”).*

With the above archetypes and tensions in mind, two points that I think are important and underappreciated in current discourse:

First, I’d argue that **AI companies are, by and large, selling “content”.** This is something of a big leap, so let’s break this down and add some caveats.

Consider just the very literal comparison between a chapter of a book and the output you get from an AI model when you ask “give me something that looks like a chapter of a book”:

![][4]

GPT 5.1 via web app. “give me something that looks like a chapter of a book”

On surface level inspection, the outputs are the same. They’re both just a sequence of words. On your computer, you could save both as a plain text file or even a fancier “epub” file. Further, we might even do some kind of blinded test and ask people to say which is which, and for certain books and AI outputs people might not be able to tell them apart!

Looking upstream, of course the production process for a book and an AI output are different. One involved a person writing text; the other involved a bunch of people writing text, and that text being passed through a complicated and expensive training process (etc.). Furthermore, the process of serving you AI-generated tokens is fundamentally different from serving a static artifact. AI output is probabilistic; you might struggle to get the same chapter twice, and you’re unlikely to get the same output as somebody else.

So, you pay for an AI subscription and you get something that looks like a book, or like an essay, or like answers from a Q&A site. The literal thing you’re getting is probably a JSON payload that renders in your browser or app as a “chat”. But you’re really buying something that is *very much* like a book/document/webpage. AI companies are like creators in that both groups are trying to sell you information (until they’re not, e.g. some AI firms might be interested in selling records to consumers only as a *temporary step* so they can acquire power and then make money other ways).

You buy the archetypal “Book” from an “Author” because of some presumed assessment of quality or utility. Similarly, people buying outputs from AI presume quality (perhaps because of some benchmarks post, word of mouth, etc.; see previous [post]).

But right now if you spend \$20 on a book or \$20 on API credits that you use to ask an AI “give something that looks like a book”, you’re just buying outputs. The economic properties of a text file sold to you by a person and an AI company are the same; without Data Rules, it’s hard for the Author to prevent you from sharing your book with your friends or with data-hungry AI developers. Similarly, it’s hard for a Model Builder to prevent somebody sharing your AI outputs with your friends or a competing Model Builder.

### Some Model Builders Also Sell Pickaxes

Some companies also sell tools for content creation (e.g., Microsoft, Adobe; Google sort of fits here with the doc suite). Companies that sell tools for content creation have somewhat different incentives than companies that only sell AI outputs. Critically, they cannot entirely alienate the “Author” group. More specifically, they want Authors to have money so they can spend that money on subscriptions.

But, both types of companies have a reason to get on board with better Data Rules. “Pure model companies” need rules and norms so they don’t get fully killed by model stealing. And hybrid model and tool companies need these rules and norms so that the customers of the tools don’t get put out of business (e.g., if all writers everywhere lose their jobs, who will buy Word/Docs subscriptions).

Continuing on a path towards Data Rules that include de facto carve-outs for AI companies will ultimately benefit only a small set of AI companies — whoever “wins” (moves from trying to sell AI products to acquiring broader power).

### It’s not “Tech vs. Society”

Copyright/consent/traffic stealing issues are sometimes framed as “AI companies vs rest of society” (or more broadly, “tech industry vs rest of society”). However, I don’t think this framing is right! Many AI/tech companies also stand to benefit from clear rules and norms around transacting for information, and right now are not able to fully participate in the policy discussion around Data Rules because legal uncertainty has created a default behavior of “write just 2-3 paragraphs in the model card — the model uses ‘publicly available datasets’ — and otherwise avoid any comments on the Data Rules Debate”.

But in fact, most model builders stand to benefit from rules that help them sell more model outputs. This fact is **really important** for coalition building: I really do think we can outline many proposals for Data Rules that would be good for most creators and for most tech companies.

Of course, there are incentives against supporting clear rules and norms, especially if the new rules are stricter. The main reason an organization might want to keep the status quo is if they think they’re going to be a “big winner” (perhaps the only winner). Who will be the big winner? This **legitimately unclear at this point**. So importantly, I think it’s possible to make a case to leadership of *any* AI lab at this point to support clarified, stricter-in-certain-ways Data Rules.

So, with all this in mind: regulators, AI lab leadership, and AI policy pundits need to keep iterating on a set of enforceable rules and norms that establish economic incentives for creating and selling “informative records”. This can simultaneously address concerns on the creator side and the model builder side. In the short term, this will mean that model builders have to pay more for data, but I believe it will pay off in the long-run (for everyone except the organization(s) that would have “come out on top” after a vicious battle of scraping, model stealing, etc.). Additionally, if public actors provision more commons datasets, this could offset some of the additional data costs that slow down AI progress in the short term (see below).

------------------------------------------------------------------------

## Part 2: What might the Data Rules look like, specifically?

What concretely am I proposing?

One general idea is to focus on Data Rules that enable [Collective Bargaining for Information]. Another related idea is to focus on advancing “public AI” institutions, which could serve as exemplars with respect to data access (see e.g. Section 3 of this [policy paper]), provide clarity on what is truly “commons” data (more on this below!), fund commons, and help bring the people writing new Data Rules closer to actual AI builders. Note: if more AI systems move from the private sector into “public AI” governance, many of the data issues described here may become lower stakes overall.

Any concrete solution will likely involve creating platforms where sellers (data creators) can (1) pool data in a way that creates meaningful utility for model builders (optimal size of pooling to be a subject of future research), (2) become informed about data value, and (3) and meaningfully impact downstream use. Critically, the whole “coalition unlock” pitch in this article is that the mechanisms for controlling downstream use (e.g., “AI-aware contract templates that stipulate allowable usage in training, retrieval, evaluation, and other modules”) will simultaneously help creators and model builders.

Here’s what this might look like in practice:

### Data Collectives as the Primary Transaction Unit

Across most data markets, we can expect individual creators to almost always have near zero individual leverage. A single blog post, image, or research paper is worth nearly nothing to a model builder who already has billions or trillions of tokens. The solution to this additional problem (let’s call it the “near zero individual leverage” issue) is **data collectives** - organizations that pool creators’ data to create bundles with meaningful value.

(Note: this is going to be extremely repetitive with my past posts, but I’m including for completeness and perhaps some updated thinking).

Writers, researchers, artists, or other creators might join data collectives. These could be organized by sector, geography, content type, or other dimensions. They might exist within or branch off from organizations, such as labor organizations.

The actual logistics of joining a data collective might look a lot like joining an online community. Make an account, get a browser extension, VPN-like software, or a login for a particular intermediating app (even just an LLM interface like the publicai.co Inference Utility). Ideally, joining needs to be very low friction — even lower friction than the existing sign up processes for many platforms and apps. An emerging possibility is to use AI agents to help individuals join collectives or to transact on behalf of individuals such that collective-like behavior is created.

Institutionally, collectives might be nonprofits, public benefit corporations, actual cooperatives, public bodies that are part of a government, or truly decentralized organizations. The collective would maintain some registry of member data (perhaps hosted on servers the collective controls, or using some technical mechanism to track data while it lives elsewhere). Collectives may be able to benefit from decentralized approaches, e.g. using AT Proto with “group-private data” ([WIP]).

Collectives would negotiate with model builders, and then distribute revenue or benefits back to members. Just like individual workers have little power but unions can shut down factories, individual data creators have little power but collectives can meaningfully impact model performance. Prior research on data strikes (and the broader literature on data poisoning, selection, scaling, etc.) is promising (in our view).

**Near-term examples:** We’re already seeing early versions. Some relevant “sort of related examples” include: News/Media Bargaining [Codes] (Australia, [Canada]), the partnership between OpenAI and News Corp, Stack Overflow’s [agreements] with AI companies, and many other. See also this [Data Deals Tracker].

### Data Valuation Infrastructure

For collectives to negotiate, they need to know (or at least estimate) what their data is worth. This requires building valuation infrastructure.

**Technical support for valuation:** The technical side of data valuation infrastructure would mainly involve making data value estimates more readily available to data creators. This might mean directly sharing the results of dataset ablation studies, but it might also mean continuing to improve open source software for value estimation (influence functions, Shapley values, etc.). Much of this can be accomplished by just continuing to fund and support research on data value estimation and by pursuing human-centered research on practical valuation tools (e.g., communicating key insights from ablations, scaling experiments, and specific value estimates that are actually useful at the bargaining table).

Ablations, scaling experiments, and value estimation are all dependent on the selection of certain benchmarks/test sets. Market-based discovery, i.e. actual transactions that reveal what buyers will pay, will also help to provide some pricing transparency. Of course, there’s some circularity here, since buyers are presumably doing some ablation studies, value estimation, etc.

**Institutional support for valuation infrastructure:** Governments, universities, or other organizations with similar incentives could run services that help collectives estimate data value (analogous to how USDA provides crop pricing data to farmers). “Public AI”-aligned labs that are already doing data ablation experiments and tend to share most of their results in an open fashion would already be contributing to “coarse” appraisal just by doing the experiments they are already doing. Many more labs could be brought into an appraisal-sharing consortium with relatively minimal coordination — the specific asks here would be very similar to existing asks around increased data sharing (“Hey folks from university or national labs, do you mind sharing the raw data that accompanies the Appendix from your latest paper”).

Alternatively, rather than a “join the consortium” approach, value estimation sharing might be part of mandatory transparency requirements. Model builders could be required to report what data they use and how it affects model performance, and this might be enforced via third-party auditors.

**Example:** A journalism collective wants to negotiate. A valuation service runs experiments showing that news data improves model performance on current events questions by 15%. The collective uses this in negotiations, plus looks at what similar collectives received.

### Standardized Contract Templates — for both data creators selling data and AI builders selling model outputs

Rather than negotiating from scratch every time, we need **default contract templates** for different types of data usage. There is an ongoing discussion around different approaches to schemas, protocols, and defaults for data licensing and contracts (I’ve been trying to maintain a live updated list [here] — additions very welcome). Wherever possible, contracts and licenses should build off existing and proven approaches.

Different contract templates might handle:

-   Training vs. retrieval: Different terms for training on data vs. retrieving and displaying it

    -   And maybe even some special handling of evaluation data.

-   Commercial vs. research

-   Derivatives / flow down (See e.g. Jernite et al. \[[ACM DL]\]): What happens to model outputs? Can they be used to train other models?

    -   Note that because of the possibility for training on synthetic data, there are really many possible “levels of depth”; so contracts need to account for this!

-   Attribution: How are creators (or upstream mode; builders) credited?

-   Compensation structure: Fixed fee, per-query, revenue share, etc.

-   Termination: Can creators (or upstream model builders) revoke access? With what notice?

    -   Note: In many cases, data collectives may be better off aiming to have recurring flow of data that can be stopped, as revocation of already-used data is tricky.

Considering these dimensions (doing so exhaustively is likely to require an additional post/paper, and there’s a lot more related work to cover here from law and computer science, see e.g. the [GenLaw] workshop archives for one starting point), we might see template names like: “Training-Commercial-Standard” (train on our data for commercial models, revenue share), “Retrieval-Attribution” (retrieve and display with citation, fixed fee), “Research-Open” (academic use only, free with attribution), or “Eval-Public” (evaluation use, freely available to all).

Ideally, information about these contracts can be public or semi-public (with parallels to information sharing requirements for publicly-traded firms). This would further reduce information asymmetry and make it easier to share and re-use “good” contract terms.

To enforce these contracts, the Data Rules would rely on a variety of mechanisms, including watermarking, provenance audits (like the [Data Provenance Initiative]), API-level controls (see e.g. RSL, copyright.sh), model checkpointing (e.g. requirements to save training checkpoints, to share data ablations at regular intervals), and perhaps cryptographic techniques.

In terms of legal mechanisms, AI data will likely require a combination of copyright law, contract law, and other frameworks (labor, human rights, privacy, etc.) Contracts may help to address some of weaknesses of existing copyright law (though two big caveats here — I’m not a lawyer, and depending on how various copyright-focused cases are resolved it is possible that copyright will remain the dominant legal mechanism for handling AI data usage).

Ideally, in order to begin to have a stable playing field, we can try to work towards a faster dispute resolution process, perhaps facilitated by new or existing agencies (a “Data Relations Board”).

**Critically, a unique argument I want to advance in this article is that we should try and design a menu of contract templates that’s useful for both data creators and model builders. All these questions: credit, provenance, downstream control, etc., are relevant to both parties!**

------------------------------------------------------------------------

## Part 3: Open Knowledge and Post-AI Data Rules

Finally, to make data markets work well, we’ll also need to address the tension between (1) moving more data into the realm of economic transactions (with stricter rules) and (2) the benefits of open knowledge and free-culture.

This tension is a big deal to me, because (1) I personally believe there’s a ton of value that’s been added to the world by the open knowledge and free-culture ideologies and downstream/related projects and (2) I think this ethos is especially important to the overall culture of tech/computing (a culture that is now becoming more influential globally because of the diffusion of AI). There’s a much longer discussion to be had (and the discussion is being had in many forums!) about tech culture, the normative goals of tech, secularism, compassion, giving, etc.

Long story short, I think ragging on open knowledge, free culture, and open source is intrinsically bad because these ideas have massive intrinsic value, but also instrumentally bad because threats to open knowledge and free culture will actually hurt a force that makes tech a more compassionate industry and culture.

There is tension between “openness” and strict Data Rules. In some cases, the roll out of new rules might indeed restrict the flow of some knowledge, and will in the short term reduce access to certain knowledge. This is a bitter pill to swallow!

In the extreme, a global mandate that *all* data transactions must be made using some standardized contract template via data collectives could effectively shut down peer production and open source overnight. In fact, anything that adds friction to an already challenging contribution process (people often complain about the social experience of trying to join Wikipedia or StackExchange these days) could seriously hurt contributions.

Consider this less extreme scenario: a group of writers spends a bunch of effort to create a new data collective, builds their own platform for doing data value estimation, and engages in collective bargaining with an AI builder. Simultaneously, a very altruistic research group releases a giant set of textbooks — that are very related in topic to the expertise of our imaginary writer collective — under an open license. This could blow up the negotiations for that data collective by driving the new price down to zero (if the AI builder trains on the new open data, this would immediately “show up” in data value estimates). Or, as I’ve written in past [newsletters], in the data labor market, there’s a very high chance of “accidental scabbing” or people being “conscripted into scabbing”.

Even fully altruistic commons contributions can impact the overall market for information (again, it’s complicated: in some cases open knowledge might drive sales for certain types of goods). I think there are three big solutions.

### Keep current pathways for bottoms-up commons contribution (and support peer production with money and software)

First, we should continue to enable bottoms-up decisions from people who contribute to existing commons projects to choose to keep sending data into the commons. There will be internal governance decisions within open-source projects, projects like Wikipedia, etc. about licensing practices in the wake of AI. There will also be similar discussions in more “grey area” communities (for instance, subreddits that have a peer production-style mission).

So, as a general heuristic: if any new “post-AI Data Rules” would make Wikipedia or an OSS project on GitHub non-compliant, that’s probably a bad set of rules.

Furthermore, we should definitely continue to promote programs like Wikimedia Enterprise that allow well-funded organizations to formally provide financial support to peer production while keep the core content free and open.

### Combine Open Source AI and Public AI

Second, in the short term, coming back to the “public AI” concept ([see this ICML workshop paper]), public AI institutions can help provision the non-information components of the AI pipeline as public goods, while leaving some of this to private actors to provision via traditional markets.

This might involve some initiatives that are mostly unrelated to data: public bodies might just help provide compute or logistical support for AI services provided by non-private AI company actors. It might also involve dedicated campaigns to contribute data to use-restricted commons; data that’s in the open but can only be used by a certain category of actors.

### The tough part of the conversation: we probably should have *some* training carve-out or at least a “pardon” to achieve some détente

Finally, as mentioned above, in the long term, I believe the new Data Rules need to include the implementation of a democratically governed classification system for “stuff that’s commons by default”. The classification system itself (which might be a set of rules, or a literal classifier) should be updated at regular intervals via some democratic non-market process.

You should be able to go to a public website and see a list of all the stuff that’s in the data commons. This should be the first stop for getting commons-y data. The contents of the commons must be clearly communicated to potential creators to prevent misallocation in resources (spend a bunch of money to produce data you might think is valuable on the market, but actually is “redundant” with what’s in the commons).

Of course, actors should still be able to allocate resources to release openly licensed datasets in a domain (driving down the price for data in that domain, but enabling new markets for fine-tuning on top of it) but ideally would do so with full knowledge of the implications.

For some current AI training resources, it might be contentious to decide if data goes in this commons or not (e.g., scholarly papers). We should leave this up to communities to decide.

Finally, we might also want to consider this question: “If just try to make things even more open — we maintain a free-for-all data paradigm, couldn’t model stealing *prevent* concentration of power by one AI lab?” I think it is worth discussing the case for embracing a real “data free-for-all” approach (basically giving up on data control, let AI companies scrape everything and scrape from each other), but I think the net effect of losing the benefits of bargaining, leverage, and friction will be net bad. See more in the [CBI] paper.

## Thanks

A big thanks to B Cavello and Jacob Thebault-Spieker for comments on this post!

The original header image (perhaps a bit too dark for social media thumbnails, I realized upon seeing the Bluesky preview card!)

![undefined]

*Ship of Fools*, Hieronymus Bosch, Public Domain. From [Wikimedia Commons][5]. We’re all in the same boat!

  [File:Shichiri Ferry Boat.jpg]: ../media/almost-everybody-including-both-data/d3cb76052961b6a6343f.jpg "File:Shichiri Ferry Boat.jpg"
  [Wikimedia Commons]: https://commons.wikimedia.org/wiki/File:Shichiri_Ferry_Boat.jpg
  [digital commons]: https://www.cip.org/research/generative-ai-digital-commons
  [open knowledge]: https://en.wikipedia.org/wiki/Open_knowledge
  [free-culture]: https://en.wikipedia.org/wiki/Free-culture_movement
  [proposal]: https://github.com/creativecommons/cc-signals
  [arXiv]: https://arxiv.org/abs/2404.12590
  [NPR]: https://www.npr.org/2025/09/05/nx-s1-5529404/anthropic-settlement-authors-copyright-ai
  [Reuters]: https://www.reuters.com/technology/artificial-intelligence/nyt-sends-ai-startup-perplexity-cease-desist-notice-over-content-use-wsj-reports-2024-10-15/
  [1]: https://www.reuters.com/world/us/us-appeals-court-rejects-copyrights-ai-generated-art-lacking-human-creator-2025-03-18/
  [2]: https://arxiv.org/abs/2501.11457v1
  [Washington Post]: https://www.washingtonpost.com/technology/2025/02/25/chegg-google-ai-lawsuit/
  [The Financial Times]: https://www.ft.com/content/a0dfedd1-5255-4fa9-8ccc-1fe01de87ea6
  [GitHub]: https://github.com/Responsible-Dataset-Sharing/easy-dataset-share
  [Meng et al.]: https://arxiv.org/abs/2502.12658v1
  [3]: https://www.washingtonpost.com/technology/2025/08/08/wikipedia-ai-generated-mistakes-editors
  [Tipping Points for Content Ecosystems]: https://dataleverage.substack.com/p/tipping-points-for-content-ecosystems
  [tweet]: https://x.com/IvanVendrov/status/1988134758199578993?s=20
  [commons governance problems]: https://tn.boell.org/en/2023/04/19/5-elinor-ostrom-et-les-huit-principes-de-gestion-des-communs
  [maps]: https://dataleverage.substack.com/p/ai-technologies-are-system-maps-and-you-are-a-cartographer
  [HBR]: https://www.hbs.edu/faculty/Pages/item.aspx?num=50951
  [The Guardian]: https://www.theguardian.com/technology/2020/sep/18/wikipedia-edits-have-massive-impact-on-tourism-say-economists
  [history of statistical software]: https://en.wikipedia.org/wiki/Rexer’s_Annual_Data_Miner_Survey
  [value]: https://www.hbs.edu/ris/Publication%20Files/24-038_51f8444f-502c-4139-8bf2-56eb4b65c58a.pdf
  [here]: http://datalicenses.org
  [leverage]: https://arxiv.org/abs/2012.09995
  [We Have No Moat, And Neither Does OpenAI]: https://newsletter.semianalysis.com/p/google-we-have-no-moat-and-neither
  [4]: ../media/almost-everybody-including-both-data/27233a50478224a8da48.jpg
  [post]: https://dataleverage.substack.com/p/how-do-we-know-our-ai-output-is-good
  [Collective Bargaining for Information]: https://arxiv.org/abs/2506.10272
  [policy paper]: https://www.nickmvincent.com/static/canada_publicai.pdf
  [WIP]: https://atproto.wiki/en/wiki/reference/core-architecture/pds
  [Codes]: https://en.wikipedia.org/wiki/News_Media_Bargaining_Code
  [Canada]: https://crtc.gc.ca/eng/industr/info.htm
  [agreements]: https://techcrunch.com/2024/05/06/stack-overflow-signs-deal-with-openai-to-supply-data-to-its-models
  [Data Deals Tracker]: https://sr.ithaka.org/our-work/generative-ai-licensing-agreement-tracker/
  [ACM DL]: https://dl.acm.org/doi/10.1145/3531146.3534637
  [GenLaw]: https://www.genlaw.org/
  [Data Provenance Initiative]: https://www.dataprovenance.org
  [newsletters]: https://dataleverage.substack.com/p/perplexity-ceos-interaction-with
  [see this ICML workshop paper]: https://arxiv.org/abs/2507.09296
  [CBI]: https://cb4i.org/
  [undefined]: ../media/almost-everybody-including-both-data/6ef88f81d38b28230ad6.jpg "undefined"
  [5]: https://commons.wikimedia.org/wiki/File:Jheronimus_Bosch_011.jpg
