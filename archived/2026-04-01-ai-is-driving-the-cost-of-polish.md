---
title: "AI is driving the cost of polish down; some musings on fancy versus terse artifacts"
subtitle: "AI progress means the \"polish\" of a figure or website no longer proxies for quality. Can we try to turn this into a good thing for curation, attention allocation, and even AI progress itself? "
date: "2026-04-01"
original_url: "https://dataleverage.substack.com/p/ai-is-driving-the-cost-of-polish"
content_id: "substack/post/190836930"
authors: ["Nick Vincent"]
published_at: "2026-04-01T18:07:53.744Z"
source_updated_at: "2026-09-21T17:26:48.435Z"
archived_at: "2026-09-25T20:33:42+00:00"
source_body_sha256: "bba083429dd81c287927c1ef5b2003915f77feecf5ebddcc6970b7ebfc2b5041"
---

*September 21, 2026: Revisited this in light of ICLR and CHI review discourse; fixed a few typos.*

In short: many have pointed out that AI progress is decreasing the cost to “polish” or “embroider” all sorts of artifacts. This means that communities that once used polish (broadly construed) as a cheap proxy for community-specific measures of “real value” are being forced to consider other signals of provenance and verifiability (or are simply losing the ability to curate information). This is a problem that communities and institutions face every time there’s new ways to get “cheap polish”, but it’s especially bad right now. Even communities with careful review processes to prevent “false positives” are affected.

![File:Lace Its Origin and History Real Guipure.png]

Lace. Samuel L. Goldenberg, Public domain, via Wikimedia Commons

This is a topic that’s already been discussed a lot![^1] This post is an attempt to connect ongoing, well-trodden discussions to ideas for improving curation and introspecting, with a focus on peer review in particular. It’s also an opportunity to highlight the data leverage angle. Threats to the production of high quality information artifacts is also a problem for the AI field itself; the communities and institutions that curate knowledge are providing data for pre-training and for some kinds of [post-training]. And the training of information producers like scientists is itself a critical process for the eventual evaluation of AI systems. Finally, at the end of the post, I’ll foreshadow another possible solution to this problem: what if we go “full transparency” and just post the full AI-interaction transcripts for any AI-touched artifacts we produce?

In the spirit of this post, here’s the bullets in case you want to stop here:

-   (Recapping what others have said) AI progress is decoupling presentation quality from underlying quality. This is breaking or will break curation processes that relied on polish as a proxy signal (including negative signals like "no polish = sloppy, and likely ‘bad’").

-   (Reiterating common advice) Iterating on our on work (sometimes with AI, and oftentimes without) is useful for the sake of our own thinking.

-   (Somewhat novel take) Even in cases in which people use AI heavily (to e.g. produce dozens of complex analyses or visualizations while iterating on a project), it may best for collective knowledge to allow and incent people to ship dense/terse/focused artifacts (i.e., no pressure to ship the AI-fancified version).

    -   We do this now in many small ways: the notion of an abstract, the bulleted “contribution statement” at the end of Introduction, the fact we sometimes restrict papers to 8 pages with many details thrown in Appendices, etc. But we can do more!

-   One way to do this: we should endeavour to create small, carefully chosen sets of fancy artifacts, establish an expectation that fancy artifacts also expose a simple view (the spreadsheet, the API, the raw data) such that readers can add their own consumption layer if they want, and also reward focused, not-fancy artifacts (e.g., focused datasets, demos, methods code, etc.).

    -   Most importantly: we need to adjust credit allocation to create a desirable distribution of fancy:simple artifacts

-   We can escape a particular “trap” in which: human writes bullet points → send to AI to generate long AI output → send that long output to colleague → AI takes long prose and converts to bullets → human reads bullets.

-   (The data leverage angle) Dense-but-high-quality artifacts may also be more useful as training data and more amenable to retrieval.

------------------------------------------------------------------------

## A new-ish problem

There’s a new emerging category of negative impact from AI progress that you’ve likely seen or experienced firsthand. It looks like this: in some community (or institution/organization), it used to be the case certain dimensions of *presentation quality* were highly correlated with the quality dimension that the community actually cares about. This meant that presentation used to be a reasonable proxy for quality, which was helpful when quality assessment needed for the community to allocate attention and/or resources is expensive. The problem that is arising (rapidly) is that AI progress makes it very easy to produce artifacts where previously useful dimensions of presentation quality become uncoupled from what the community really cares about. This has the potential to temporarily “break” processes that curate and allocate.

For instance, in academic peer review, having a uniquely well-crafted figure early in a paper might make a reader/reviewer more likely to believe the methods are reasonable. Of course, a diligent reviewer should be wary of making of this assumption and still read the methods carefully. It’s always been a challenge that reviewers judge books by their covers, but generally there was some signal here. Someone choosing whether to read an essay or blog might look for the presence of certain linguistic markers early on. A standout personal website or CV might catch the eye of recruiters or hiring managers, and a unique personal project on GitHub might signal coding skills for somebody trying to break into the industry.

Because it’s always been the case that people can “juice” the presentation-related characteristics of an artifact without improving the true quality, communities typically have some defences against over relying on these proxies. For instance, a fancy figure alone is *not* enough to cause a paper through most rigorous review processes. But even when communities have strong defences against low quality artifacts with very high polish, these communities often still use “no polish at all” as an important *negative signal*. Reviewers can use very poor presentation as a signal of overall sloppiness; they see some bad signs early on and become more attuned to other issues. throughout. This is important is the use of negative signals also lowers the overall cost for a community to perform curation. For more on the academic peer review context specifically, see this recent recent work on “[peer review death spiral]”

We might give this a wordy name: the “AI progress kills certain-presentation-dimensions-as-quality-proxies” problem, or just call it “decoupling of presentation and quality”.

## Is this problem going to get worse?

As AI progress continues (I think it will), we should expect this problem to get worse. It’s very easy to use frontier AI models to make a beautiful and impressive figure that doesn’t mean anything. Writing prose without AI smell remains challenging (but I believe this will absolutely be solved in time with feedback loops to get the data; I actually think cross-platform posting may be a big unlock here, e.g. people on Twitter making fun of AI slop on LinkedIn, etc.).

We now face new challenging questions: how should communities change our expectations around presentation, how should curation processes adjust, and how should individuals make choices about effort allocation?

Importantly, for researchers trying to choose how we spend our limited time, we must answers: Should I spend 10 hours agentically vibe-coding 50 different visualizations? Should I spent 10 minutes and just take the very first output from the agent? Should I *just* make a matplotlib default bar plot (or even just paste the raw data into my supplement!?) and let my reader code up their own personalized viewer?

## We should still make our artifacts look nice

Before we proceed, I should make it very clear that **I definitely do think we should still try to make our artifacts look nice**; we should create clear and insightful figures for our papers, make our websites interesting and useful, etc.

I also believe deeply in the value of iterating on writing and other research outputs in order to improve one’s own clarity of thinking and thereby improve future versions of the topic. Re-writing can improve your thinking; marinating on your figures may cause you to rethink your interpretation; soaking in your data may cause you to identify new connections between ideas or interpretations of a past finding, and so on. I’ve rewritten parts of this blog post several times; sat on it, came back to it, etc. I’m definitely not saying we should only be shipping raw bullet points and early data[^2].

So regardless of the impact on community curation, iterating on writing and visualization is important just to improve research outcomes.

## Choosing to ship simpler artifacts

With all that said, I am hopeful that in some cases, AI’s ability to make beautiful figures can free us from the need to make beautiful figures. We’ll still have a few *very fancy artifacts*, but in many cases we can ship terse but dense blogs, bullets, and data files.

One response to the above is that AI progress can just raise the floor for presentation quality. Because we can employ swarms of frontier AI agents to make a truly top tier website, every academic should be using modern web technologies to create a bespoke search and filtering system over their own papers. For every paper we release, we should create a dedicated static site with a fully interactive explorer (I do think the potential for multiverse analysis is in many ways exciting).

However, I think we should not set a new expectation that we have maximally fancy views over all our artifacts. Even as AI gets better, this has an opportunity cost. (Time spent iterating on figures is time not spent collecting new data, for instance).

Furthermore, (I think) there is a lot of charm — and legitimate value — in the “classic CS professor website” experience. Typically this experience is characterized by plain HTML, bulleted lists, and a focus on getting right to the content: “Here’s my list of publications” or “here’s the top three things I’ve been thinking about lately”.

**Most importantly, if we ship more “stripped down” objects, this may in some cases impose less overall review costs on the community/ecosystem.**

I’m hopeful that instead of starting a race to deploy a full web app for every paper and blog post, we can instead do the following: deploy AI-enhanced applications that use modern web technologies for *certain* select artifacts, but actually err more on the side of the “CS professor website philosophy” for *most* artifacts, with the consideration in mind that our reader can use the same tools that we have access to to add polish as necessary. If you hate the default styles for HTML papers on arxiv, there’s never been a better time to code your own arxiv-reader!

In other words, I’m starting to feel more inclined to try to create a larger number of simple blogs, notes, and spreadsheets (but still make sure these are good and thoughtful) and a smaller number of fancy artifacts. And even for fancy artifacts, I want to make the “simple view” very prominent. For instance, for apps that are really a fancy view over some spreadsheet, be sure to just show people the spreadsheet view and let them apply styles to your spreadsheet if they want to.

## Sometimes, the people want simple bullet points; let’s cut to the chase

You may have also seen this [marketoonist] comic[^3] or variations of the joke contained within:

![AI Written, AI Read cartoon]

From Tom Fishburne. Licensing info [here].

This comic is funny and points to a real problem: obviously, if everyone is going through this process for all their emails, this may just create a new source of miscommunication and it’s certainly wasting both electricity and human energy.

But it also suggests the potential for a good-for-all-parties improvement (a “strong Pareto improvement”) in communication: if both parties in this kind of exchange identify what is happening, they can just go back to sharing the bullets! I think most people will also agree that this is how communication in many of their best working relationships functions — people just send each other quick, information dense messages.

One promising direction to solve this problem is by building social technologies that surface unstated, shared preferences, i.e. breaking through the norms that cause people to act out the cartoon above instead of just sending the bullet points that the both sides prefer.

## Reflecting on some recent projects

In December 2025, I had a resurgence in motivation making all sorts of fancy static sites for sharing scholarly work, ideas, promoting AI and data literacy, etc. “Now that I have coding agents”, I thought, “I can clear my backlog”. (See e.g. [datacounterfactuals.org] , [datalicenses.org], [exploringai.org]).

I remain very excited about the ideas. But I’m also becoming more convinced that for many data-related projects, the most important parts are selecting and designing schema, maintaining raw data, and maybe providing one or two opinionated UX flows over that data. Increasingly, people can just insert their own consumption layer and analysis. So for these kinds of projects, I think it’s important that any fancy websites also expose a simpler “spreadsheets” view or “API view”.

We should still be thinking deeply about our core claim/data/etc. And to do so, that might mean we build a local fancy interface over our data, run many analyses, and so on. But the artifacts we broadcast more widely should oftentimes just be the bullet points. All the time we spent iterating on different analyses and increasingly complex views over the data served, most importantly, to improve the final “terse contribution”. In many scholarly communities, writing norms handle this already: you have a “contribution paragraph” at the en of your Introduction with 2-4 bullet points. And there are incentives to write tweet threads, news briefs, etc. for your papers.

Applied at scale this approach can help us solve a number of more foundational communication-related social dilemmas: we feel compelled to expend effort on presentation efforts that we don’t even think our intended recipient cares about; we’re expending this effort purely because we’re trapped in a collective action problem.

Ideally, we should try to set up our new institutional rules and norms such that individual contributors can iterate on presentation-related variables *up to point the stops being useful for them* and stop there; any reader can continue iterating to their heart’s desire.

## Crediting people for more focused contributions

If more communities agree that sometimes, just providing a more “raw” contribution (with appropriate guarantees of validity) can be useful, this may open the door for systems that credit more focused contributions. In the realm of science, there’s an argument for more cleanly separating review of the actual data from the surrounding paper and discussion (normally, these do map to different sections in the peer reviewer “rubric”). In the realm of semi-speculative blogging, we might separate the current events commentary from the thought experiments.

I think various academic communities might benefit from more venues that accept focused contributions (e.g., datasets only, methods code only) without forcing authors to jump through additional hoops just to make their data contribution look like another type of paper or artifact. In the context of HCI and design, there’s a lot of value in giving people credit for just creating new demos without requiring every project to be a groundbreaking contribution to the literature. Of course, individuals will stand to benefit from making some contributions that are durable, but it should be more acceptable to have e.g. a durable contribution followed be a related, supporting set of smaller demos and validations.

Any changes along these lines could also support proposals to improve the evaluation of scientific careers by focusing much more on quality over quantity, e.g. by having hiring process or review processes that focus more on “tell me about your 1-2 most important papers”.

## Some implications for data quality

One interesting consideration is that focused bullet points in markdown combined with raw data and clean, terse code could be more useful as AI training data than PDF files, but will almost certainly be more amenable to retrieval by AI systems. Simple artifacts could, in many cases, be easy to add or infer structured metadata. And very importantly, increasing the number of people that deeply engage with the artifacts actually enables more effective collaborative filtering.

This topic deserves longer treatment (full empirical study, ideally!) but I’m decently confident about the general idea.

Another idea to throw into the mix: one way to reduce doubts about whether AI polished an artifact without improving it’s quality would be to share the actual AI transcripts. This might enable readers to assess the quality of AI intervention (did you ask the right prompts? Which parts of the code were “one shot” and which parts were iterated upon?). This is, in some sense, a very natural extension totally open science to the AI agent era. It also has massive implications for privacy, reputation, and trust. And would impact the supply of training/eval data for future models. Also, worthy of much more thought!

[^1]: See e.g. Mike Elgan’s “[In an AI-perfect world, it’s time to prove you’re human]”, “[workslop]”, Jessica Hullman’s “[Living the metascience dream (or nightmare) with AI for science]”, [OpenAIReview][peer review death spiral]’s introductory blog post, and/or this [tweet] from Alex Imas (and ensuing discussion).

[^2]: These caveats feels especially important, as I’ve been teaching a graduate research communication course this term, and thus have been earnestly discussing these topics with students, and trying to come up with good answers for how standards and best practices will change.

[^3]: (I found this using prompt: “did someone make a comic or joke about in the era of generative ai, someone writes 3 bullets as a prompt, ai makes a flowery email, and then the recipient uses ai to condense back to 3 bullets?”)

  [File:Lace Its Origin and History Real Guipure.png]: ../media/ai-is-driving-the-cost-of-polish/f512f05b68eba5ed02f9.jpg "File:Lace Its Origin and History Real Guipure.png"
  [post-training]: https://www.businessinsider.com/anthropic-surge-ai-leaked-list-sites-2025-7
  [peer review death spiral]: https://openaireview.org/blog.html
  [marketoonist]: https://marketoonist.com/2023/03/ai-written-ai-read.html
  [AI Written, AI Read cartoon]: ../media/ai-is-driving-the-cost-of-polish/37a65b01c7b834d6d198.jpg "AI Written, AI Read cartoon"
  [here]: https://marketoonist.com/faq
  [datacounterfactuals.org]: http://datacounterfactuals.org
  [datalicenses.org]: http://datalicenses.org
  [exploringai.org]: http://exploringai.org
  [In an AI-perfect world, it’s time to prove you’re human]: https://www.computerworld.com/article/4114605/in-an-ai-perfect-world-its-time-to-prove-youre-human.html
  [workslop]: https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity
  [Living the metascience dream (or nightmare) with AI for science]: https://jessicahullman.substack.com/p/living-the-metascience-dream-or-nightmare
  [tweet]: https://x.com/alexolegimas/status/2037173080741523742?s=20
