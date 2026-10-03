---
title: "On AI-driven Job Apocalypses and Collective Bargaining for Information"
subtitle: "Reacting to a fresh wave of discussion about AI's impact on the economy and power concentration, and reiterating the potential role of collective bargaining."
date: "2025-06-05"
original_url: "https://dataleverage.substack.com/p/on-ai-driven-job-apocalypses-and"
content_id: "substack/post/165138164"
authors: ["Nick Vincent"]
published_at: "2025-06-05T17:24:21.580Z"
source_updated_at: "2025-09-25T16:42:51.894Z"
archived_at: "2026-09-25T20:33:47+00:00"
source_body_sha256: "2328236c8d18430f966a6bfe6150acbff0982014fa0c81953a5063e6fd1ee451"
---

There has been another, fresh news cycle triggered by high-profile people in AI commenting on the potentially *very* disruptive economic impacts of AI. Of particular note, Dario Amodei, the CEO of Anthropic recently spoke very bluntly about his views on the potential impact of AI on jobs and the economy, inviting responses from many high-profile [figures].

![File:Sedan Plowshare Crater.jpg]

The Sedan Plowshare Crater. [Wikimedia Commons.]

## Part 1: Links Round-up

First, let’s just review some links. This may be handy if you want to catch up on various interrelated new essays and news coverage (and I will update this, with a change log, if anything else comes up!)

-   Amodei quoted in [Axios][]: “AI could wipe out *half* of all entry-level white-collar jobs — and spike unemployment to 10-20% in the next one to five years” and “possible mass elimination of jobs across technology, finance, law, consulting and other white-collar professions”

-   Kevin Roose covered the [topic] in the New York Times

    -   The Hard Fork [podcast] had Mike Krieger, Chief Product Officer of Anthropic, on to talk about AI and jobs.

There’s also been several widely circulated essays that are highly related:

-   Gradual Disempowerment from Kulveit et al. ([essay] and arXiv [paper])

    -   And follow-up posts ([tweet] / longer [post])

-   The Intelligence Curse from Drago and Laine ([essay][1] and twitter thread [summary])

    -   And Time Op-ed, “[What Happens When AI Replaces Workers?]” from the same authors

-   “Estimating the Substitutability between Compute and Cognitive Labor in AI Research” from Whitfill and Wu (Effective Altruism forum [post][2] — with model and empirical analysis)[^1]

-   Another piece in Time [published] on June 4 (after the first draft of this post was written): "AI Will Devastate the Future of Work. But Only If We Let It” from Gary Rivlin, quoting Brynjolfsson and others

-   See also “[Addressing the U.S. Labor Market Impacts of Advanced AI]” from Sam Manning

And importantly, there’s also been pushback to the narrative of inevitability

-   “The ‘AI jobs apocalypse’ is for the bosses” from Brian Merchant: see [tweet][3] and longer [essay][4].

-   The “AI as Normal Technology” [essay][5] from Narayanan and Kapoor also provides a set of counterpoints to some of the above claims.

## Part 2: Adding Collective Bargaining for Information into the Conversation

What do I want to add to this conversation?

First, while I think the totality of above essays/articles/posts already provides a very comprehensive set of perspectives, considerations, and possible interventions, I of course want to reiterate the potential role of data leverage, and more specifically, “collective bargaining for information”:

-   With Matt Prewitt and Hanlin Li, we have a preprint [paper][6] out that specifically lays out this vision for Collective Bargaining for Information (which we abbreviate as CBI), tying the CBI argument to both classical information economics and more modern power concentration and AI safety concerns

-   Our arguments very much resonate with the above, with particular focus on concrete policy and research actions needed to actually achieve real countervailing force through collective bargaining

-   I’d like to think that CBI can help with coalition building, with opportunities for both (a) people very concerned about near term economic impacts and (b) those more worried about AI hype and other risks to contribute to a shared cause (though of course this needs battle testing!)

Second, I want to provide another stab at a bullet point level analysis of the current evidence and the “mechanistic argument” for why economic power concentration is possible and even likely. I’ll also touch on how this prediction is compatible with “hype concerns” and the possibility that in some domains AI will face some data-related challenges.

I certainly think considering both theoretical and empirical work to understand the potential impact of AI on jobs and power will be critical. It’s also important to keep in mind that most people making predictions have wide bounds on their estimates right now (note Amodei’s “1-5 years” qualifier), and that there’s a split between people who want to focus more heavily on the data (the “it’s not something to freak out about until we actually see sectoral unemployment spiking” stance) vs. the theory (the “it’s something to freak out about because of the nature of information, cognitive labour, compute, power accumulation feedback loops” stance).

## Part 3: Another simple model for thinking about AI impacts

-   **One way to think about labour substitution — a very simple**[^2] **model in which “workers output information sequences at each turn”**

    -   In general, workers are always competing to keep their job — they always need leverage against their employer (“without my unique information sequences, you’re sunk, so keep paying me!”)

    -   To state plainly: worker needs to perform their job duties or they may lose said job

        -   But the worker also needs to fulfill a variety of network-embedded social obligations, and account for the sociology of work more generally.

        -   For instance, if your boss personally likes you, this will affect how your performance is assessed

        -   A worker’s information output alone does not perfectly predict their job retention, likelihood of promotion etc.

        -   We’re going to mostly ignore this for now, though it will create some friction for how fast impacts diffuse

    -   In white collar work, job duties often entail being able to produce an appropriate sequence of information chunks for a circumstance

        -   Write the code, report, email, PowerPoint

        -   If you stop responding to all your work email or producing your expected code outputs, you will likely be replaced (eventually)

        -   All workers are constantly competing with other workers to produce these info sequences

        -   Some AI tools may compete with particular tasks, and eventually even entire jobs

        -   Where the uncertainty comes in: there are open questions about this exact set of interactions between tasks and jobs, and we can’t firmly predict how new jobs may (or may not) emerge

            -   People love to point to Industrial Revolution here, but AI is really different in key ways: the number of domains affected at once, the focus on actually automating reasoning itself, increased potential for power concentration (as laid out in many of the above links)

```{=html}
<!-- -->
```
-   **More on this model**

    -   We can imagine an “[agent-based model]”: We have a set of workers with certain skill levels and wage. At each turn, each worker is presented with some context and then must output an appropriate “information sequence”

    -   The quality and appropriateness of this sequence is evaluated by others in their broader social network (e.g. their client and/or their boss)

    -   At some interval the output sequences from individual workers or groups are compared to alternatives (from some “domestic labour market”, from some “global labour market”, and from AI)

    -   If any alternative wins, it may “take over” the job

    -   At some regular interval, AI models either get better (or worse) at each task

        -   Of course, it could be the case that AI progress slows down because of data issues (see e.g. [Tipping Points] and various recent empirical [works] on online platforms that curate knowledge), and this will limit which jobs are affected.

        -   AI gets better when it has more data and/or when the AI operator has more capital (for compute, talent, etc.)

        -   Critically, because of recent progress, AI may be able to get better at certain tasks using a wider set of data sources than we previously possible (models can “learn reasoning” using data from across many domains, we can increasingly apply reinforcement learning and synthetic data to new tasks — though see previous posts for my rant-y caveats on how RL and synthetic data are currently being framed)

    -   If AI keeps getting better over time, more jobs go to AI

        -   (Note also as AI does more tasks and jobs, this allows for organizations with already concentrated power to accumulate more information and make better AI, potentially creating a “capital singularity”)

    -   So: Large models with sufficient data from workers can indeed compete directly with those workers.

## Part 4: We should keep in mind the goal of the AI field and the plausbility of “augmenting AI”

-   The whole goal of much of the AI field is to be able to replicate or surpass human-level capabilities on “produce the right sequence of information in response to some context”

    -   See e.g., information on the new venture [Mechanize] with backing from various big names in Silicon Valley

    -   See also OpenAI charter, which emphasizes building (safe versions of) “[highly autonomous systems that outperform humans at most economically valuable work]”

        -   And note that Anthropic, DeepMind, etc. are effectively competing to build nearly identical products to OpenAI’s offerings, even though they don’t have this exact text in a “charter”

            -   And of course, one of the news hooks for this article was the concerns raised in public by Anthropic leadership

    -   There is absolutely a case to be made for why achieving these outcomes (“full automation of the economy” or “systems that outperform humans at most economically valuable work”) could be good, **if sufficient governance / countervailing force / guarantees against power concentration are made**. But we should be crystal clear in acknowledging the explicit goals of various actors in the AI industry!

```{=html}
<!-- -->
```
-   **“Just make augmenting AI”**

    -   While various AI leaders are increasingly alluding to ideas like “let’s do augmentation”, there hasn’t yet been much in the way of hard commitments on this front (to my knowledge)

        -   See e.g. a [piece] from De Cremer and Kasparov in Harvard Business Review from back in 2021

        -   In the Hard Fork Interview above, the Anthropic CPO is asked, (roughly) “what do you say to someone who asks, why are you trying to take my job, why should I root for you” and the answer is “we’re trying to build things that augment not replace”

    -   However! I don’t think the “let’s just do augmentation instead” concept has really been well defined in the context of the training/modelling step of AI (please let me know if you disagree): in particular, I haven’t seen any high-profile and compelling argument about how to train a model that’s good at augmenting but *not* good at substitution

        -   To do this very formally would likely involve some kind of constraints or modification to the training objective, à la techniques in fair machine learning (e.g. [work] from Agarwal et al.), but I haven’t seen this operationalized

            -   Maybe some of the anti-memorization work and anti-copyrighted outputs work on LLMs is closest

        -   I think it’s much more coherent to train a *system* that’s augmenting, by designing into the system hard requirements feedback from people, etc., but the upstream models — the sets of weights that map inputs to outputs — will either be capable of substituting for tasks, or not.

            -   Which models can substitute for which tasks? This is a thing that can, and will be measured, it will just be laborious to do so.

        -   I think the AI field can be pushed towards augmentation-friendly models via data consent / opt-in heavy approach: only train on data that people have offered up as “augmenting”.

            -   With enough data, the model would still be useful for *some* substitution.

            -   It’s probably only a partial solution.

            -   It’s probably useful to conceptualize a personalization / substitution frontier that exists from any given configuration of data + compute. This frontier will be tricky to navigate — if we want personalization, and sometimes want to prevent substitution, what do we do as AI developers or as data contributors?

        -   Probably the only high-level solution is to *foster countervailing power*

            -   And at least part of said power should come from collective bargaining over information

            -   But again, lots of other ideas in e.g. Gradual Disempowerment posts, Intelligence Curse posts, and others.

So, large scale economic disruption from AI is possible. This disruption should be roughly forecastable based on task-specific and job-specific data availability (and it’s great to see more research on these topics, e.g. [work][7] from Labeskin et al. extending the “GPTs are GPTs” [paper][8] from Eloundou et al.), and there are some levers (see also a recent AI Now [report] that discusses, among other things, labour organizing for this purpose).

## Part 5: In conclusion

Much of the AI field is focused on taking records of human work and creating compressed artifacts that can replicate the “output sequence of information” actions that workers must take regularly to maintain the leverage needed to keep their jobs.

One of the main goals of the field is to get better at replicating these sequences!

So if the field is successful, this will disrupt the economy.

AI might be limited in certain domains because of data availability (and in particular, will be limited in where it can be deployed because of [eval data leverage]).

But the core challenges in designing markets for information create conditions where powerful actors with existing capital needed to operate AI systems can create feedback loops to accumulate more information and build more powerful AI systems.

We should work to prevent this.

## Recap of all links above:

-   Acemoglu, D. (2024). *The Simple Macroeconomics of AI* (NBER Working Paper 32487). National Bureau of Economic Research. <https://economics.mit.edu/sites/default/files/2024-04/The%20Simple%20Macroeconomics%20of%20AI.pdf>

-   AI Now Institute. (2025). *Artificial Power: 2025 Landscape Report*. <https://ainowinstitute.org/2025-landscape>

-   VandeHei, J. & Allen, M. (2025, May 28). *Behind the Curtain: A White-Collar Bloodbath*. *Axios*. <https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic>

-   *Hard Fork* (2025, May 30). *The A.I. Jobpocalypse + Building at Anthropic with Mike Krieger* \[podcast episode\]. <https://www.nytimes.com/2025/05/30/podcasts/hardfork-ai-jobpocalypse.html>

```{=html}
<!-- -->
```
-   De Cremer, D., & Kasparov, G. (2021, March 18). *AI Should Augment Human Intelligence, Not Replace It*. *Harvard Business Review*. <https://hbr.org/2021/03/ai-should-augment-human-intelligence-not-replace-it>

-   Drago, L. (2025, January). *The Intelligence Curse* \[Substack essay\]. <https://lukedrago.substack.com/p/the-intelligence-curse>

-   Drago, L., & Laine, R. (2025, May 30). *What Happens When AI Replaces Workers?* *TIME*. <https://time.com/7289692/when-ai-replaces-workers>

-   Narayanan, A. & Kapoor, S. (2025, April 15). *AI as Normal Technology*. Knight First Amendment Institute. <https://knightcolumbia.org/content/ai-as-normal-technology>

-   Kulveit, J., Douglas, R., Ammann, N., Turan, D., Krueger, D., & Duvenaud, D. (2025). *Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development* (arXiv:2501.16946). <https://arxiv.org/abs/2501.16946>

-   Labaschin, B., Eloundou, T., Manning, S., Mishkin, P., & Rock, D. (2025). *Extending “GPTs Are GPTs” to Firms*. *AEA Papers and Proceedings*, 115, 51–55. <https://doi.org/10.1257/pandp.20251045>

-   Manning, S. (2025, March). *Addressing the U.S. Labor Market Impacts of Advanced AI.* <https://cdn.governance.ai/RFI_Labor_Impacts_March-2025_Sam_Manning.pdf>

-   Merchant, B. (2025, May 31). *The “AI Jobs Apocalypse” Is for the Bosses*. <https://www.bloodinthemachine.com/p/the-ai-jobs-apocalypse-is-for-the>

-   OpenAI. (2018). *OpenAI Charter*. <https://openai.com/charter>

-   Rivlin, G. (2025, June 4). *AI Will Devastate the Future of Work — But Only If We Let It*. *TIME*. <https://time.com/7290751/ai-future-of-work-essay>

-   Roose, K. (2025, May 30). *For Some Recent Graduates, the A.I. Job Apocalypse May Already Be Here*. *The New York Times*. <https://www.nytimes.com/2025/05/30/technology/ai-jobs-college-graduates.html>

-   Sun, J. (2025, April 26). *Deconstructing “The Aesthetic Genealogy of the Beige Tech Microsite”* (Macrodoses #7). *Reboot*. <https://joinreboot.org/p/macrodoses-7>

-   Vincent, N., Prewitt, M., & Li, H. (2025). *Collective Bargaining in the Information Economy Can Address AI-Driven Power Concentration.* <https://nickmvincent.com/static/cbi_paper.pdf>

-   Whitfill, P., & Wu, C. (2025, June 1). *Estimating the Substitutability Between Compute and Cognitive Labor in AI Research*. Effective Altruism Forum. <https://forum.effectivealtruism.org/posts/xoX936hEvpxToeuLw>

## Change log

-   June 5, 2025: published. Made minor tweaks to bibliography.

[^1]: While putting this together, I was repeatedly reminded of Jasmine Sun’s [post][9] on “The Aesthetic Genealogy of the Beige Tech Microsite”, which touches on all of the above, and feel called about recently reworking my personal site to use the Crimson Pro font…

[^2]: Note this is simpler than the conceptual frameworks in other, more elaborate work:

    -   [Simple Macroeconomics of AI] - “The production of a unique final good takes place by combining a set of tasks” defined via a function that accounts for elasticity of substitution, dependence between tasks, etc.

    -   Whitfill and Wu focus on a “theoretical model of researching better algorithms”.

  [figures]: https://x.com/BernieSanders/status/1930613586331635830
  [File:Sedan Plowshare Crater.jpg]: ../media/on-ai-driven-job-apocalypses-and/f315b55b53fcc98faf00.jpg "File:Sedan Plowshare Crater.jpg"
  [Wikimedia Commons.]: https://commons.wikimedia.org/wiki/File:Sedan_Plowshare_Crater.jpg
  [Axios]: https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic
  [topic]: https://www.nytimes.com/2025/05/30/technology/ai-jobs-college-graduates.html
  [podcast]: https://www.youtube.com/watch?v=nG_jGZuRBxs
  [essay]: https://gradual-disempowerment.ai/
  [paper]: https://arxiv.org/abs/2501.16946
  [tweet]: https://x.com/DavidDuvenaud/status/1928682244052496446
  [post]: https://www.lesswrong.com/posts/GAv4DRGyDHe2orvwB/gradual-disempowerment-concrete-research-projects
  [1]: https://intelligence-curse.ai/
  [summary]: https://x.com/luke_drago_/status/1915376929542111353
  [What Happens When AI Replaces Workers?]: https://time.com/7289692/when-ai-replaces-workers/
  [2]: https://forum.effectivealtruism.org/posts/xoX936hEvpxToeuLw/estimating-the-substitutability-between-compute-and
  [published]: https://time.com/7290751/ai-future-of-work-essay/
  [Addressing the U.S. Labor Market Impacts of Advanced AI]: https://cdn.governance.ai/RFI_Labor_Impacts_March-2025_Sam_Manning.pdf
  [3]: https://x.com/bcmerchant/status/1929654074875826315
  [4]: https://www.bloodinthemachine.com/p/the-ai-jobs-apocalypse-is-for-the
  [5]: https://knightcolumbia.org/content/ai-as-normal-technology
  [6]: https://nickmvincent.com/static/cbi_paper.pdf
  [agent-based model]: https://en.wikipedia.org/wiki/Agent-based_model
  [Tipping Points]: https://dataleverage.substack.com/p/tipping-points-for-content-ecosystems
  [works]: https://www.inet.ox.ac.uk/publications/large-language-models-reduce-public-knowledge-sharing-on-online-q-a-platforms
  [Mechanize]: https://www.mechanize.work/
  [highly autonomous systems that outperform humans at most economically valuable work]: https://openai.com/charter/
  [piece]: https://hbr.org/2021/03/ai-should-augment-human-intelligence-not-replace-it
  [work]: https://proceedings.mlr.press/v80/agarwal18a.html
  [7]: https://www.aeaweb.org/articles?id=10.1257/pandp.20251045
  [8]: https://www.science.org/doi/10.1126/science.adj0998
  [report]: https://ainowinstitute.org/publications/research/ai-now-2025-landscape-report
  [eval data leverage]: https://dataleverage.substack.com/p/evaluation-data-leverage-advances
  [9]: https://joinreboot.org/i/162295663/a-site-for-every-soliloquy
  [Simple Macroeconomics of AI]: https://economics.mit.edu/sites/default/files/2024-04/The%20Simple%20Macroeconomics%20of%20AI.pdf
