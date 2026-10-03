---
title: "The AI \"Evaluation Crisis\" Is an Opportunity to Get Data Flow Right"
subtitle: "Why the AI evaluation crisis could force a reckoning on dataset provenance, attribution, and consent."
date: "2026-05-07"
original_url: "https://dataleverage.substack.com/p/the-ai-evaluation-crisis-is-an-opportunity"
content_id: "substack/post/196792743"
authors: ["Nick Vincent"]
published_at: "2026-05-07T15:33:24.121Z"
source_updated_at: "2026-05-07T15:34:49.124Z"
archived_at: "2026-09-25T20:33:40+00:00"
source_body_sha256: "bcb33935b6d3e210c196d868b6a3f2a689cc27205c7cd12709a35d6844a253d6"
---

This is a follow-up to the previous post on an [attestation-forward data strategy] (or put another way, an argument to focus on markets for trusted data generation flow, *not* markets for raw tokens). This post will be focused on capturing why I think the evaluation crisis in AI is going to force a reckoning on thus-far-suppressed issues with dataset provenance, attribution, and consent; we can act now to use evaluation as a “foot in the door” to create better AI and better societal outcomes.

To be more specific: The AI evaluation crisis will force / is forcing labs to rebuild the [provenance] relationships they skipped during pretraining. To make credible claims about model capabilities -- especially in domains that are high-stakes with legally embedded and professionalized quality standards, like medicine, law, and finance -- AI labs need fresh, trusted, expert-adjudicated data. This is creating an opening to decide whether future AI data work becomes centralized gig labor or a more plural ecosystem of data guilds, trusts, unions, and professional communities. We can understand some of the forces at play (and make some predictions about how the rebuilding of provenance will play out) by looking back at the history of pretraining data acquisition practices and comparing modern AI evaluation to now “classical” supervised learning.

Some relatively fresh takes and insight I hope to add here:

-   Privately-led data firms like Mercor are going to end up building top-down equivalents to Wikipedia; community-led evaluation projects like WeVal are going to end up “doing peer production”

-   In a really healthy and abundant data ecosystem, we may not even have a notion of “evaluation data” or “benchmarks”; we might just create “holdout datasets” as needed like the good old days of supervised learning

-   Good evals are just good data. In 2027, some of the most valuable documents to train on might be the really high-effort “eval artifacts” from 2026

## The ongoing “reestablishment of provenance”

The “reestablishment of provenance” is already starting. For “data-for-labs” firms like [Mercor], [Surge], and [Scale], part of the value proposition is intermediating relationships between labs and expert workers in domains like [medicine], law, and finance. Mercor offers: “we’ll go find you some doctors or chemistry PhDs”. I think some degree of provenance will be reestablished no matter what researchers or policymakers do, because data-with-provenance is a hard prerequisite for ever making statistically valid claims about AI capabilities. That is, any particular claim about a model’s medical abilities is (for now) some kind of quantitative claim about agreement with, or distance to, some human reference set.

What I think will happen is that in the process of producing artifacts needed for evaluations, a variety of efforts -- both top-down (Mercor-style) and bottom-up ([WeVal]-style) -- will end up doing something that looks a lot like the structured data creation processes found across peer production projects like Wikipedia, online Q&A efforts like Stack Exchange, research communities, etc. That is, the work needed to build “evals” will involve creating rich structured data with embedded notions of success and utility, but this time, the relevant attribution information will be retained. In some sense, the data-play firms are going to look like they’re building a top-down privatized Stack Exchange, and the community-led evaluation efforts will look a lot like WikiProjects!

It’s unclear if the top-down or bottom-up approach will win (of course the top-down approach has a massive advantage in current levels of capital; I think a balance is likely and could be great!). Either way, society has a window of opportunity to shape the eventual power dynamics that emerge. Will we end up in a world where data contributions have provenance tracking, but this provenance is achieved through top-down surveillance from a dominant AI lab or “data firm” via centralized requests to precarious gig workers (e.g. a world where all knowledge work is MTurk-style gig work)? Or, can we build an ecosystem of sometimes-competing-sometimes-cooperating “data guilds” that operate in a playing field with [clear data rules] and maintain decent jobs for their members while feeding high-quality data into AI pipelines?

## Why attribution and evaluation stem from the same data-flow problem

Much ink has been spilled over the use of large-scale scraped content for LLM pretraining; the *New York Times* called this [“AI’s original sin”], and others have called [it][] [theft] ([here] are some of my thoughts from back in December 2022). There has also been a parallel ongoing discussion about AI’s [evaluation crisis], including the emergence of groups like the [EvalEval Coalition] and structural changes like an “Evaluations and Datasets” [track] at NeurIPS. AI as a field now has more visible model impact than ever before in history, but is facing well-documented issues with [benchmark contamination], [benchmark saturation], weak [construct validity], reproducibility issues, and conflicts of interest that cause marketing and measurement to be muddled together. Both the concerns about scraping’s morality/legality and the evaluation crisis can be understood as consequences of how pretraining data acquisition was actually executed. The [Common Crawl] had a noble non-profit mission archiving the web. Early AI researchers carried their noble academic missions (and corresponding “scrappy” practices) from their PhD offices to their tech company campuses. As carefree attitudes towards training data were imported into for-profit entities, what happened across the industry was that data was acquired via a one-shot extraction and not via an establishment of renewable relationships between AI developers and data creators.

## How pretraining cashed in on structured knowledge

Painting in broad strokes, we might say that large-scale self-supervised pretraining worked because it “cashed in” on two empirical regularities in structured human text: [(1) transfer] — training on text from one domain can still improve performance on tasks from a seemingly unrelated domain — and [(2) scaling] — more data and compute generally meant more capabilities, at least over the range where scaling laws held up. The open web contained a large, diverse body of human text with enough structure and meaning to produce capable base models, which could then be further enhanced through post-training, RLHF, efficiency improvements, tool use, and so on. (Note: I’m not trying to say that this is *all* that matters, of course: large-scale self-supervised pretraining *also* worked because an immense amount of effort was put into research on architectures, tokenization, deduplication, filtering, etc.).

The open web was full of *structured* human text because people and their institutions created *incentives* to embed structure into digital records: norms on platforms like [Wikipedia], expectations in academic peer review, Q&A moderation practices, the professional and ethical incentives in journalism, software documentation, open-source maintainership, product reviews, platform reputation systems, and so on. I’d go so far as to say that we can directly map specific elements of structure in the data (e.g., consistent patterns in word choices on Wikipedia) to specific incentives. Web text is valuable because that text has been shaped by communities, professions, interfaces, and institutions. This is perhaps obvious, but worth continuing to restate many times over.

A strong claim I would add here — and one that is testable via large pretraining ablation experiments (with some data-centric [work][] [providing][] [some][] [early] evidence along these lines) — is that without organizations and communities that create incentives for people to give structure to human text, the whole LLM/foundational model endeavor would not have worked. If there existed fewer institutions like Wikipedia, fewer Q&A communities, fewer newsrooms, fewer open-source projects, and fewer online spaces where people had reasons to organize knowledge, it would have taken longer to prove the viability of the pretraining / foundation model paradigm. Perhaps in 2030 some mega-firm would have discovered the value of pretraining a transformer on their massive corpus of internal documentation.

## Comparing evaluation of LLMs and “idealized supervised learning”

Looking back at how evaluation works in canonical supervised learning settings can be useful for understanding the value of “incentives to structure digital records”. In the centralized managerial [MTurk]-ish approach to executing a supervised learning project, a researcher describes some labeling process, with an explicit or implicit notion of utility and success, and then delegates that process to students, gig workers, contractors, domain experts, or sometimes themselves. This ensures that training and evaluation at least have a fairly direct relationship: if you have a steady flow of new examples from the label-production process, then held-out evaluation can tell you something meaningful about whether the model is learning the thing you meant to measure.

For this reason, in supervised learning, the notions of “evals” and “benchmarks” were quite different than how these terms are used in the LLM context. In many *individual* supervised-learning projects, evaluation could be handled by a held-out split or temporal holdout from the same label-generating process. Field-level benchmarks and shared tasks certainly existed, but they were usually tied to relatively well-specified tasks and could often be defined in terms of a holdout from some dataset. Assessing accuracy or other measurements of usefulness/impact was actually quite simple: you just run your model against the holdout.

**Critically, this only worked because the data creation and labeling processes imposed a great deal of structure (as described above) onto the data!**

In some cases, supervised learning projects piggybacked on structure that came from outside the ML pipeline, oftentimes avoiding the need to generate labels by taking advantage of the fact that some people out in the world had already loosely labeled some records. For instance, collaborative filtering used interaction data that’s downstream of interface design. Search and recommendation used clicks, links, dwell time, purchases, ratings, and other traces produced by people responding to products and platforms. Wikipedia and Q&A sites generated categories, quality judgments, accepted answers, reputation scores, and moderation traces, and academic and journalistic institutions produced text filtered by professional norms.

Enter self-supervised pretraining. The key “realization” was that a great deal of “learning signal” could be found entirely within certain types of self-contained documents: predict the next token, masked token, corrupted span, or similar self-supervised target, rather than relying primarily on externally supplied task labels. If you pretrain on enough good data, next-token completion can capture a lot of the structure that previous communities had already embedded in text.

Neural language modeling had been studied for quite some time, and unsupervised or semi-supervised pretraining was already visible in NLP before transformers. But the 2018–2020 period (ELMo, ULMFiT, GPT, BERT, GPT-2, GPT-3 -- see e.g. Wikipedia [article] on BERT) and scaling law findings helped make pretrained language models the dominant general-purpose route to NLP capability.

## The Disconnect Introduced by One-way Scraping

The use of pretrained base models for widely used AI systems creates a new major challenge: it created a strong disconnect between the organizations doing training and evaluation and the people putting structure into digital records. In an MTurk-style supervised ML project, the researcher might take on a managerial role and might underpay data labelers, but they were at least connected (via MTurk) to the labelers. Now, labs have a one-way relationship to their largest source of data (and thus, are starting to turn away from scaling pretraining by instead buying data from Mercor-type organizations, starting their own human data efforts, etc.).

This meant that the organizations doing the self-supervised pretraining did not face structural forces pushing them to sustain the creation of new structured data. We’re also seeing that the rise of AI-generated “slop” and the erosion of search/social traffic to original sources may make the renewable production of high-quality public text harder, not easier. The story here is complicated, as most well-resourced actors can most easily filter out slop and differentially benefit from high-quality synthetic data; see e.g. [here][1] for discussion of these issues.

Further, we have not yet carefully documented the mappings between specific structural characteristics of pretraining data and their upstream incentives. A peer-reviewed paper, a high-quality Wikipedia article, a good Stack Overflow answer, or a carefully written clinical note all carry traces of judgment/curation, but some of the details of those judgments (and especially the social dynamics) have been “lost to time”; this makes it harder to replicate past success.

This is to some degree correctable; many works in the dataset documentation genre ([Datasheets for Datasets], [Data Statements for NLP], [Model Cards], and the [Data Provenance Initiative]) have been advocating for improvements for a while now. Interestingly, Gao et al’s [Metadata Conditioning Accelerates Language Model Pre-training] suggests that including “metadata (e.g., URLs like [www.wikipedia.org]) alongside the text during training” can improve performance, which may motivate more retrospective documentation efforts.

## The test set is what you test on (in supervised learning)

To understand some possible trajectories for LLM evaluation efforts, referring again to an “idealized supervised-learning” set-up is useful. In this setting, we often do not have a special category of “eval data.” Instead we can just perform evaluation using any random holdout from the same renewable process that produced training data. Indeed, if we have a high-stakes model running live, we should be testing against a new random set of “live/online” data each day or week!

If we have a living stream of structured records, some notion of utility, and a way to sample fresh examples that the model has not already seen, then we can easily check whether a given model can actually create value when that model is given actuation power. Evaluation in the classical setting did not necessarily involve a separate set of institutions, though having a separate evaluator is a nice-to-have to enforce strict holdout.

In contrast, the current situation for evaluating LLM-based systems is that we cannot just hold out some data from a pretrain or posttraining dataset. Instead, we need dedicated evaluation and auditing organizations.

## Eval-building processes that look a lot like running a Q&A site

This brings us back to a point introduced above: the processes that evaluation-focused organizations (including community efforts like [WeVal]) will end up implementing will probably look quite similar to the practices and norms in platforms like Wikipedia and Stack Exchange and professional communities like academia and journalism. In some domains like coding and math, synthetic data and verification-based reinforcement learning can reduce the dependence on human judgment. But in most domains (medicine, law, policy, everyday professional life, etc.) evaluation will likely continue to require ongoing relationships with experts. It will require fresh tasks, provenance, rubrics, adjudication, disagreement tracking, and incentives for people to keep doing high-quality knowledge work.

OpenAI’s [HealthBench] is, in my view, a useful bellwether for how evaluation needs will reintroduce provenance: it uses physician-created rubrics and realistic health conversations to evaluate AI systems in health. The more recent blog post on [HealthBench Professional / ChatGPT for Clinicians] provides a further example -- the amount of detail about, e.g., the exact number of model responses reviewed by physicians is striking.

Very critically, something we should consider is that really good eval artifacts are just going to be *good data*. Firms and communities will -- motivated by AI-related incentives and not necessarily “Q&A community incentives” -- likely end up building corpora that look like high-quality Stack Exchange dumps.

It may be the case that in 2027, once the 2026 evals are “old”, these evals become prime data to train on!

## Our branch point

So, to get to a conclusion: I think the AI field will reinvent, on the evaluation side, some of the social and economic relationships it skipped on the training side, and this is already happening. This means all developments in the eval space right now have the potential to also shape the future of markets and incentives for training data.

A potential bad future we might worry about is a world in which we end up with a few winners that effectively do privatized central planning of data acquisition, possibly creating a huge pool of very precarious jobs. The large literature on the hidden labor behind AI systems does not paint the working conditions that have existed thus far in a favorable light: [Mary Gray and Siddharth Suri’s] *[Ghost Work][Mary Gray and Siddharth Suri’s]*, [Partnership on AI’s responsible sourcing work], [Fairwork’s work on fair AI supply chains], and the [Data Workers’ Inquiry] all point to a myriad of issues. In some cases, there has been collective response (e.g. the establishment of the [Data Labelers Association]).

A point I like to bring up from time to time (drawing on this Kittur et al. 2013 CSCW [paper] on “The Future of Crowdwork” which asks “Can we foresee a future crowd workplace in which we would want our children to participate?”): as far as I know, there is not even a single tech executive or other prominent figure who has endorsed sending their kid off to do data labeling for MTurk or Mercor.

What I think we should shoot for is a plural ecosystem of collective units with enough leverage to maintain good working conditions and agency for their members. We might call them data guilds, data trusts, worker cooperatives, expert networks, professional associations, data unions, or something else (and they might grow out of a number of existing organizations, ranging from academic groups like the ACM, medical specialty groups, existing unions, consumer advocacy groups like Consumer Reports, and so on). Critically, these guilds would not merely sell labor into centralized pipelines. They would also maintain standards, preserve provenance, bargain over terms, adjudicate quality, represent members, and could play a role in deciding when a task is safe, meaningful, or socially useful. They would keep track of their own incentives to add structure to data!

This better future would draw on older proposals around [data as labor], [data dignity], [data trusts], and broader attempts to create countervailing power in data markets. But I think the evaluation crisis is giving these ideas a massive window to establish a very concrete foothold.

Of course, this vision has its own failure modes (guilds becoming cartels, credentials turning too exclusionary, etc.) and finding the perfect balance of top-down and bottom-up will be challenging. But as of right now, the balance of power is such that any efforts to shift power towards data labelers will, I think, be beneficial.

The AI policy, safety, and governance communities can act now: anything that supports the organization of knowledge workers (likely through existing professional organizations or through new community platforms) and pushes for attestation standards that make labor legible and portable can have very outsized impact. More concrete ideas in the previous [post]!

  [attestation-forward data strategy]: https://dataleverage.leaflet.pub/3mizn5hsjg5vo
  [provenance]: https://www.dataprovenance.org/
  [Mercor]: https://www.mercor.com/research
  [Surge]: https://www.surgehq.ai/
  [Scale]: https://scale.com/
  [medicine]: https://openai.com/index/introducing-chatgpt-health/
  [WeVal]: https://weval.org/
  [clear data rules]: https://dataleverage.substack.com/p/almost-everybody-including-both-data
  [“AI’s original sin”]: https://www.youtube.com/watch?v=CJWPezMVNdQ
  [it]: https://authorsguild.org/news/meta-libgen-ai-training-book-heist-what-authors-need-to-know/
  [theft]: https://www.theguardian.com/commentisfree/2025/sep/10/tech-companies-are-stealing-our-books-music-and-films-for-ai-its-brazen-theft-and-must-be-stopped
  [here]: https://dataleverage.substack.com/p/ai-artist-or-ai-art-thief-innovation-public-mandates-and-the-case-for-talking-in-terms-of-leverage
  [evaluation crisis]: https://aitopics.org/doc/news%3A87AE91F4
  [EvalEval Coalition]: https://evalevalai.com/
  [track]: https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets
  [benchmark contamination]: https://aclanthology.org/2024.naacl-long.482/
  [benchmark saturation]: https://hai.stanford.edu/ai-index/2025-ai-index-report
  [construct validity]: https://arxiv.org/abs/2111.15366
  [Common Crawl]: https://commoncrawl.org/
  [(1) transfer]: https://openai.com/index/language-models-are-few-shot-learners/
  [(2) scaling]: https://openai.com/index/scaling-laws-for-neural-language-models/
  [Wikipedia]: https://en.wikipedia.org/wiki/Wikipedia:Featured_article_criteria
  [work]: https://arxiv.org/html/2406.11794v1
  [providing]: https://arxiv.org/html/2402.11537v3
  [some]: https://arxiv.org/abs/2305.10429
  [early]: https://arxiv.org/abs/2203.15827
  [MTurk]: https://www.mturk.com/
  [article]: https://en.wikipedia.org/wiki/BERT_(language_model)
  [1]: https://www.cip.org/research/generative-ai-digital-commons
  [Datasheets for Datasets]: https://cacm.acm.org/research/datasheets-for-datasets/
  [Data Statements for NLP]: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00041/43452/Data-Statements-for-Natural-Language-Processing
  [Model Cards]: https://research.google/pubs/model-cards-for-model-reporting/
  [Data Provenance Initiative]: https://www.nature.com/articles/s42256-024-00878-8
  [Metadata Conditioning Accelerates Language Model Pre-training]: https://arxiv.org/abs/2501.01956
  [www.wikipedia.org]: http://www.wikipedia.org
  [HealthBench]: https://openai.com/index/healthbench/
  [HealthBench Professional / ChatGPT for Clinicians]: https://openai.com/index/making-chatgpt-better-for-clinicians/
  [Mary Gray and Siddharth Suri’s]: https://hls.harvard.edu/today/the-hidden-labor-supporting-algorithms/
  [Partnership on AI’s responsible sourcing work]: https://partnershiponai.org/workstream/responsible-sourcing/
  [Fairwork’s work on fair AI supply chains]: https://fair.work/en/fw/certification/
  [Data Workers’ Inquiry]: https://data-workers.org/
  [Data Labelers Association]: https://datalabelers.org/about/
  [paper]: https://dl.acm.org/doi/10.1145/2441776.2441923
  [data as labor]: https://www.aeaweb.org/articles?id=10.1257%2Fpandp.20181003
  [data dignity]: https://www.techtarget.com/searchenterpriseai/definition/data-dignity
  [data trusts]: https://theodi.org/insights/projects/defining-a-data-trust/
  [post]: https://dataleverage.substack.com/p/attestation-across-the-ai-supply
