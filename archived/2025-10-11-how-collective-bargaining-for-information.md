---
title: "How collective bargaining for information, public AI, and HCI research all fit together"
subtitle: "Another recap post for the Data Leverage newsletter!"
date: "2025-10-11"
original_url: "https://dataleverage.substack.com/p/how-collective-bargaining-for-information"
content_id: "substack/post/165472694"
authors: ["Nick Vincent"]
published_at: "2025-10-11T16:55:48.834Z"
source_updated_at: "2025-11-18T21:40:07.344Z"
archived_at: "2026-09-25T20:33:46+00:00"
source_body_sha256: "1bbab3ffd7a52b8443ffdbecb2c5ce66a5e741dc42986bdc3724a0c9a4f3b452"
---

![white and gray checked board]

Photo by [Kelly Sikkema] on [Unsplash]

*This is a recap post (a big round-up of links to content I’ve written recently). It will likely be updated once or twice, with a change log up top.*

Change log:

-   Nov 18: minor prose clean-up.

I’ve written quite a few newsletters in the past months. One of my reasons for working on all these newsletters is to write, and thus think, in public. (I’ve also been trying to populate more content on several sites that provide “externalized notes”, e.g. on [data licenses] and [data napkin math]). To contextualize these numerous posts, I’m going to summarize the various positions I’ve taken. I’ll also try to pull out a few resolvable predictions from my “positions”. Also: nothing in this post is meant to reflect the opinions of my co-authors, i.e., *opinions expressed here are my own, do not reflect my employer or colleagues, etc.*

At a high level, (I think) my “core positions” consist of two distinct ideas:

**Data leverage**: Data flow can, and should, be used as a governance lever. \[2020 FAccT paper: [ACM DL] \| [arxiv]\] \[[2022 Dissertation]\]

-   **Collective bargaining for information (CBI)**: Specifically, for data flow to be an effective governance lever, society should enable collective bargaining for information. This can enable more efficient markets for information, healthier information ecosystems, and mitigate some harms from AI \[2025 NeurIPS position paper: [arxiv][1]\].

-   Concretely, CBI requires legal support for appropriate bargaining institutions. It also requires the design and deployment of interfaces for actually making preference choices, as well as technical support for the actual transfer of data between database systems (see e.g. recent work on a “[Human Context Protocol]”).

-   One immediate ask to make CBI viable: we need clear rules about how anti-trust will, or will not, be applied to content producers in the AI age. In our recent paper, we argue this is quite urgent.

**Public AI (pAI):** we should build AI systems that are publicly accessible and accountable \[public AI network [website]\] \[[publicai.co] inference utility product\]

-   pAI as a concept encapsulates more than just data flow (building pAI requires also thinking about energy, compute, geopolitics, etc.), but in general pAI connects with data leverage and CBI in two ways. First, the accountability element of public AI can help to foster healthier data flow. Second, data leverage and CBI can provide a source of accountability for the public.

-   Further, there are other ways that PAI and data-centric AI connect, especially around the potential for dataset documentation and data appraisal.

-   Public AI can support “public AI Data flywheels” \[GitHub [repo] for a “mini-book” + example implementation\].

-   Public AI can also massively complement open source AI efforts \[CodeML @ ICML paper: [arxiv][2]\]

While not positions *per se,* in my writing and research I also promote a more general “we should bring empirical human-computer interaction and computational social science to AI” attitude. This involves writing about interfaces for data-dependent technologies, evaluating new AI models (e.g., [auditing] and analyzing LLM behavior in high-stakes contexts), studying online platforms (e.g., continuing to study [knowledge gaps] in Wikipedia, [studying] governance and responsible AI practices on HuggingFace), and thinking about “AI literacy”.

To recap chronologically, here is a list of blogs, summarized in one or two sentences, starting from November 2023:

-   In most policy contexts, we need to consider a systems-level data pipeworks model that emphasizes feedback loops \[[substack]\]. More recently, I summarized this model in Section 1.3. of the “Public AI Data Flywheel mini-book” \[[GitHub pages]\].

-   We should focus on “[diffs]” when we work with LLMs, and consider using multiple models at once \[[substack][3]\].

    -   Note: I’d like to think this was reasonably forward looking re: the success of CLI tools like Codex and Claude Code. I like using these tools much more than web based LLM interfaces!

-   Data value estimators should focus on group-level data values \[[longer substack]\] \[[substack microblog]\].

-   Dataset details might become important to consumers, in a similar vein to how we think about “proprietary blend” vs. “open” supplement blends \[[substack][4]\].

    -   Concrete prediction: As AI products become even more widespread, we will see a new market segment emerge of consumers who care about *which people contributed to training or evaluation*.

-   The possibility of model distillation means that the current data paradigm is “live by the sword, die by the sword” for AI companies, meaning that AI companies may face the similar challenges to content organizations. \[[substack][5]\]. One way to improve the current paradigm might involve AI labs sharing their data protection technologies \[[substack][6]\].

    -   Concrete prediction: We will see at least one or more serious AI player come out in favor of some kind of technical or regulatory IP protection for AI outputs.

-   We should consider the possibility of “tipping points for content ecosystems” that actually cause AI to get worse in some domains \[[substack][7]\].

    -   Concrete prediction: In 2026, we will see evidence of some capability domains that have clearly been negatively impacted by “content ecosystem impacts”.

-   Evaluation data leverage has massive potential \[[substack][8]\].

    -   Concrete prediction: We will see at least one professional organization (medicine, law), use evaluation data leverage by refusing to “approve” the use of some high functioning AI model.

    -   Concrete prediction: We will see AI companies seek to dissolve evaluation data leverage by structuring most evaluation jobs as contract, non-permanent positions with little workplace communication.

-   A consortium of public AI labs can share experiments and checkpoints in a way that will provide some level of “natural data appraisal” \[[substack][9]\]. This idea connects with public AI x open source AI and public AI in the context of Canada.

-   We can (and should) view many types of platforms as competing in the same ranking tasks. \[[substack][10]\]

-   We can (and should) view the utility from AI systems as stemming from upstream acts of human knowledge curation. A search result or AI output is the culmination of efforts from various people: people who actually wrote the Wikipedia article, people who completed the post-training data tasks, computer scientists who write the data ingestion pipeline or designed the training objective, engineers who solved the practical engineering challenges, etc. \[[substack][11]\]

-   Dataset documentation, auditing, LLM social simulation, assessing the ethics of a particular AI use case, and more are all connected via this broader point: “when we use AI models, we’re making our decision through either formal or informal feedback about whether the weighted combination of chunks of information we got met our needs” \[[substack][12]\]

-   AI does pose a credible threat of creating large shocks to labor markets. This may also cause large shifts in the overall concentration of wealth, and importantly, power. Collective bargaining for information is a critical countervailing force. \[[substack][13]\]

-   At some point, for certain models/datasets, it might be time to assume most public information *is* “in” the model and instead try to count up the information that’s not in the model. Society should also have a normative discussion about what data sources should be included and expected by default in AI model weights or retrieval sets \[[substack][14]\]

During this time, various research projects I’ve been involved with also intersect with these various positions (some are mentioned above):

-   Furthering understanding of algorithmic collective action \[FAccT 2025: [substack][15], [arxiv][16]\]

    -   Connects especially with CBI arguments — we need to advance our overall empirical understanding of collective action’s impact on AI capabilities to foster effective bargaining

-   Measuring and improving “attentional agency” \[FAccT 2025: [arxiv][17]\]

-   Evaluation of LLMs in high-stakes context such as medical misinformation jailbreaks \[AIES 2025: [arxiv][studying]\]

-   Understanding governance practices empirically \[AIES 2025: [arxiv][studying]\]

Some topics that I’ve micro-blogged about (I sometimes microblog directly to a “[blogs]” GitHub repo), and hope to write some longer thoughts on:

-   The use of the term [synthetic data]. See also discussion on this [Tweet].

-   A number of externalized notes on “ideas I think are interesting” [here]

  [white and gray checked board]: ../media/how-collective-bargaining-for-information/f4c0bd90fb22e04c04cf.jpg "white and gray checked board"
  [Kelly Sikkema]: https://unsplash.com/@kellysikkema
  [Unsplash]: https://unsplash.com
  [data licenses]: https://datalicenses.org/?sort=recent
  [data napkin math]: https://exploringai.org/
  [ACM DL]: https://dl.acm.org/doi/10.1145/3442188.3445885
  [arxiv]: https://arxiv.org/abs/2012.09995
  [2022 Dissertation]: https://arch.library.northwestern.edu/concern/generic_works/jq085k38d?locale=en
  [1]: https://arxiv.org/abs/2506.10272
  [Human Context Protocol]: https://miba.dev/assets/publications/HCP_ArXiv_2025.pdf
  [website]: https://publicai.network/
  [publicai.co]: https://publicai.co/
  [repo]: https://github.com/nickmvincent/paidf_consultation
  [2]: https://arxiv.org/abs/2507.09296
  [auditing]: https://arxiv.org/abs/2508.10010
  [knowledge gaps]: https://arxiv.org/abs/2505.24195
  [studying]: https://arxiv.org/abs/2409.19104
  [substack]: https://dataleverage.substack.com/p/building-a-data-pipeworks-for-democratic
  [GitHub pages]: https://nickmvincent.github.io/paidf_consultation/01c_pipeworks.html
  [diffs]: https://en.wikipedia.org/wiki/Diff
  [3]: https://dataleverage.substack.com/p/many-models-and-track-changes-for
  [longer substack]: https://dataleverage.substack.com/p/is-zuckerberg-right-to-say-that-your
  [substack microblog]: https://dataleverage.substack.com/p/microblog-one-book-is-worth-006-benchmark
  [4]: https://dataleverage.substack.com/p/selling-agi-like-ag1-will-the-market
  [5]: https://dataleverage.substack.com/p/live-by-the-free-content-for-training
  [6]: https://dataleverage.substack.com/p/ai-labs-could-open-source-data-protection
  [7]: https://dataleverage.substack.com/p/tipping-points-for-content-ecosystems
  [8]: https://dataleverage.substack.com/p/evaluation-data-leverage-advances
  [9]: https://dataleverage.substack.com/p/public-ai-data-appraisal-and-data
  [10]: https://dataleverage.substack.com/p/google-and-tiktok-rank-bundles-of
  [11]: https://dataleverage.substack.com/p/each-instance-of-ai-utility-stems
  [12]: https://dataleverage.substack.com/p/how-do-we-know-our-ai-output-is-good
  [13]: https://dataleverage.substack.com/p/on-ai-driven-job-apocalypses-and
  [14]: https://dataleverage.substack.com/p/which-datasets-should-we-assume-are
  [15]: https://dataleverage.substack.com/p/algorithmic-collective-action-with
  [16]: https://arxiv.org/abs/2505.00195
  [17]: https://arxiv.org/abs/2405.14614
  [blogs]: https://github.com/nickmvincent/blogs/
  [synthetic data]: https://github.com/nickmvincent/blogs/blob/main/microblogs/2025-05-17_three_terms.md
  [Tweet]: https://x.com/iamtrask/status/1971197830258950236
  [here]: https://github.com/nickmvincent/blogs/blob/main/ideas.md
