---
title: "\"People First\" Policy Ideas that Complement Each Other (through better data flow)"
subtitle: "Reacting to a wide-ranging set of policy ideas from OpenAI."
date: "2026-04-06"
original_url: "https://dataleverage.substack.com/p/people-first-policy-ideas-that-complement"
content_id: "substack/post/193373044"
authors: ["Nick Vincent"]
published_at: "2026-04-06T18:06:17.850Z"
source_updated_at: "2026-04-06T20:55:14.971Z"
archived_at: "2026-09-25T20:33:40+00:00"
source_body_sha256: "80e8e248134d6b1eec115ba769b4ba149af4446fe68547c3dd40e64c6418b76d"
---

Today, OpenAI published a policy paper titled “Industrial policy for the Intelligence Age: Ideas to keep people first” (the announcement is [here] and the PDF is [here][1]). I wanted to briefly document some reactions — I think the range of ideas is quite exciting (this is meant as a “starting point for discussion”) and I think many of the ideas are quite good. I’d love to see many of them taken seriously in the AI industry and the human- and data-centric research communities. I also think these ideas have an exciting data leverage-flavored through-line that I wanted to highlight.

![][2]

The piece starts by reiterating the value of sharing prosperity broadly while minimizing risks from AI. While folks in the AI space do like to joke about overused adages of this nature (“we should minimize the risks and maximize the benefits!”), I think it’s worth restating. It’s good to state explicit goals and missions, and to keep track of them over time! Then, the piece separates proposals into two categories: things that will build an “open economy” and things that will build a “resilient society”.

The specific sections that I found particularly exciting were:

-   “Worker perspectives”: this section argues for empowering workers to participate in decision making about AI use in the workplace, the deployment of new systems, guardrails, etc. Here, I’d argue there’s a strong connection to data empowerment: a major source of “hard leverage” for workers will be their data, and *especially* evaluation data they produce when new AI systems roll out. Even in domains where there’s a lot of training data out there already, evaluation data remains crucial.

-   “Right to AI”: this section argues for access to AI, which also entails AI literacy efforts. Such efforts will also enable users to choose AI products more carefully, to create more valuable traces with their AI tools, and to reason about how different artifacts may flow into AI training or retrieval pipelines. A more AI-literate population is more equipped to enact their inherent data leverage.

-   “Public Wealth Fund”: highly resonant with past discussions of [data dividends]. Empowering workers and the public more generally (with direct data leverage and otherwise) can enable them to directly advocate for such a fund (or advocate to change certain implementation choices).

-   “AI trust stack”: this is where I think the complementary nature of these ideas gets very exciting. Basically, this idea involves tracking the provenance of AI outputs. An obviously urgent use-case here is around AI-generated images and videos. There’s also great immediate value in providing provenance for AI-generated code. A really good version of this system (as the report notes, this requires navigating major privacy challenges) would help with open challenges around assessing information quality (reviewing AI-assisted pull requests and research papers).

    -   Critically, the point I really want to elevate in the discussion (and I’ve written a [longer] post on the topic + will continue to write more) is that any systems for tracking provenance/attestation objects aimed at AI outputs can also be used to track the provenance or “attested nature” of inputs used for training or retrieval! There’s a win-win here. If AI outputs (such as code) have verifiable provenance, it may be valuable for users of the AI (e.g. the author of an AI-assisted piece of software) to be able to prove they used a “good AI”. The goodness of this AI might be dependent on a particular evaluation being performed or certain training data being used. This means such a system could directly “loop in” data creators and evaluators into the value chain, aligning incentives for good data quality creation, good evaluation, good models, and good AI outputs.

-   “Auditing regimes”: auditing is urgently required in its own right, but also will help to boost information for AI users/consumers in a way that enhances people’s ability to selectively choose AI products and choose where data flows in a way that aligns with their values.

-   “Mechanisms for public input”: finally, one exciting way to enable “structured ways for public input so that alignment isn’t defined only by engineers or executives behind closed doors” is to let people use their data contributions directly as votes for specific value systems, proposals, and ideas (again, as a complement to other ways to collect public inputs).

    -   I’m pretty excited about the coding agent paradigm as potentially enabling more interaction patterns for users either directly expressing values within or alongside their session data (e.g., sharing data about one’s own preferences regarding agent behavior, incorporating surveys into one’s workflows, creating rituals around reviewing and reflecting on transcripts).

There’s a lot of other interesting ideas in the document that resonate with long-standing policy ideas that predate “societal AI readiness” discussions, so there will be a lot of past policy work and even some empirical evidence to draw on.

That’s all for this post — I mostly wanted to quickly capture that this is exciting, these ideas can enhance each other in exciting ways, and I hope there is sustained excitement around these kinds of ideas!

  [here]: https://openai.com/index/industrial-policy-for-the-intelligence-age/
  [1]: https://cdn.openai.com/pdf/561e7512-253e-424b-9734-ef4098440601/Industrial%20Policy%20for%20the%20Intelligence%20Age.pdf
  [2]: ../media/people-first-policy-ideas-that-complement/011881e3d39944e6911e.jpg
  [data dividends]: https://www.datadividends.org/
  [longer]: https://dataleverage.substack.com/p/almost-everybody-including-both-data
