---
title: "Don’t give OpenAI all the credit for GPT-3: You might have helped create the latest “astonishing” advance in AI too"
subtitle: "The much-celebrated GPT-3 that can answer questions, write poems, and more wouldn’t be possible without content written by millions of people around the world. Shouldn’t they get some credit?"
date: "2020-09-22"
original_url: "https://dataleverage.substack.com/p/dont-give-openai-all-the-credit-for"
content_id: "substack/post/117952295"
authors: ["Nick Vincent"]
published_at: "2020-09-22T19:23:00.000Z"
source_updated_at: "2023-08-14T20:50:26.023Z"
archived_at: "2026-09-25T20:34:11+00:00"
source_body_sha256: "541e25325e50a621c81de73be4ea0d99c2b5dc8e4cc1c324ef9f2e1e918e037a"
---

*This is a blog post I originally wrote the for the People, Space, and Algorithms blog in September 2020 (you can find the original [here]). I’ve copied it here because I think the perspective here is a useful data point for ongoing discussions about generative AI.*

![][1]

*.*

You may have heard about OpenAI’s “[GPT-3]”— an “[astonishing]” machine learning system that can produce impressive [poems], [code] and [op-eds]. However, it wasn’t just OpenAI that built this: it was also millions of people writing, posting, and voting on content. In fact, it’s possible that you played a role in creating GPT3!

Indeed, content and data you helped generate may have been used to build AI systems like GPT-3 in the past. It’s even more likely your data will be used to build AI systems in the future. Do you deserve some of the credit for AI’s success? What about the profits (for instance, through a “[data dividend]”)? What might you do if you aren’t happy about the AI systems your data has helped to create?

GPT-3, like many modern AI systems, needs to be “trained”: in order to produce text, GPT-3 needs to be fed examples of existing text. In the case of GPT-3, the training data is sourced from across the web. One source is called “WebText”, which consists of the text from webpages that were posted on Reddit and had a “karma” (“upvotes” from Reddit users minus “downvotes”) of 3 or more. Another was the English version of Wikipedia. Finally, the researchers also trained GPT-3 on a large number of published books and the “[Common Crawl]”, a collection of text from across the web that includes everything accessible to web-scraping bots.

If you’ve edited English Wikipedia, posted links to Reddit, voted on Reddit posts, or written text that appeared in a book or the Common Crawl, you almost certainly played a role in creating GPT-3! In a sense, you were an “employee” working on creating this widely-celebrated AI system. This is just one example of what some authors have called [“data labor”], in reference that the fact that your labor (editing, reading, voting) helps create the data that fuels AI. Other examples of data labor include [contributing to Wikipedia,] writing [restaurants reviews], and most other interactions with online platforms that can be recorded.

Wikipedia and Reddit contributions may have been especially important, as OpenAI’s researchers emphasized datasets that are “higher-quality”. Specifically, GPT-3 only looked some of the text from published books and the Common Crawl, but it looked at all of English Wikipedia and Reddit-filtered web links “2-3 times”. If you’ve edited Wikipedia, GPT-3 may have “read” your Wikipedia edit, not just once, but three times!

For massive systems like GPT-3, it likely isn’t helpful to try to make claims like, “you helped with 1% of the training and I helped with 2%”. Nonetheless, it is meaningful to claim that the success of GPT-3 (and similar projects) is attributable to **collective effort** by millions of people engaging in (frequently unwitting) “data labor”.

As tech and tech companies become more powerful, there may be opportunities to leverage your valuable data labor. For instance, a group of people could delete or withhold their data (perhaps exerting rights defined in  [privacy][] [regulation]) to harm an AI system, an idea we’ve called a “[data strike]”. For cases where “data strikes” aren’t feasible, you could instead [funnel your data labor] towards organizations that align with your personal values. Our data fuels AI, so the more powerful AI becomes, the more powerful our “[data leverage]” may be. In the long run, data leverage could be a path towards an AI paradigm that shares its benefits more broadly, perhaps through a “[data dividend]”.

If you want to learn more about how the data you generate contributes to AI – and emerging research about how you might leverage those contributions in your relationships with tech companies – below are a few good resources:

-   Various PSA research papers relate to “data as labor” concepts. These projects have involved studying “[data strikes]“, “[conscious data contribution]“, [user-generated data in search engine results], [restaurant review platforms][restaurants reviews], and “[data leverage]“.

-   The “Data as Labor” FAQ on the Radical Markets website: <http://radicalmarkets.com/chapters/data-as-labor/frequently-asked-questions/>

-   Our blog post on “data strikes”: <https://blog.datadividendproject.com/data-strikes/>

-   This blog post on “data refusal”: <https://citizensandtech.org/2020/08/collective-refusal/>

-   This [report][data dividend] providing on overview of “data dividends”

-   This [project] aiming to create a near-term data dividend:

Some additional notes:

-   While many commenters have highlighted the impressive potential of GPT-3, others have it called it [overhyped] and a [bloviator.]

-   If you’re interested in the WebText dataset (upvoted Reddit links), you can find several attempts to create an open source WebText dataset [here][2] and [here][3].

-   You might be wondering: “Well, exactly how much did I help create GPT3?” Unfortunately, given GPT3’s enormous price tag ([estimated] at around \$4.6m), it won’t be feasible anytime soon to try to answer this question by retraining GPT3 from scratch with an individual or group’s data contributions removed. You could try to count up how many Wikipedia edits you’ve made or how many Reddit posts you’ve voted on, but actually translating this to a concrete measure of the impact you had on GPT3 requires making a huge number of assumptions and quickly becomes convoluted.

  [here]: https://www.psagroup.org/blogposts/62
  [1]: ../media/dont-give-openai-all-the-credit-for/789e399201e21f327096.jpg
  [GPT-3]: https://arxiv.org/abs/2005.14165
  [astonishing]: https://www.theverge.com/21346343/gpt-3-explainer-openai-examples-errors-agi-potential
  [poems]: https://www.economist.com/science-and-technology/2020/08/08/a-new-ai-language-model-generates-poetry-and-prose
  [code]: https://twitter.com/mattshumer_/status/1287125015528341506
  [op-eds]: https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3
  [data dividend]: https://www.datadividends.org/
  [Common Crawl]: https://commoncrawl.org/
  [“data labor”]: https://www.brookings.edu/blog/techtank/2018/02/21/should-we-treat-data-as-labor-lets-open-up-the-discussion/
  [contributing to Wikipedia,]: http://www.nickmvincent.com/static/WikiSerp2020.pdf
  [restaurants reviews]: https://brenthecht.com/publications/cscw2020_restaurantratings.pdf
  [privacy]: https://en.wikipedia.org/wiki/General_Data_Protection_Regulation
  [regulation]: https://en.wikipedia.org/wiki/California_Consumer_Privacy_Act
  [data strike]: https://dl.acm.org/doi/10.1145/3308558.3313742
  [funnel your data labor]: https://brenthecht.com/publications/CollectiveIntelligence2020_ConsciousDataContribution.pdf
  [data leverage]: https://arxiv.org/abs/2012.09995
  [data strikes]: https://dl.acm.org/citation.cfm?id=3313742
  [conscious data contribution]: http://www.brenthecht.com/publications/CollectiveIntelligence2020_ConsciousDataContribution.pdf
  [user-generated data in search engine results]: http://www.nickmvincent.com/static/icwsm2019_ugcinsearch_arxiv.pdf
  [project]: https://www.datadividendproject.com/
  [overhyped]: https://www.forbes.com/sites/robtoews/2020/07/19/gpt-3-is-amazingand-overhyped/#466f2b651b1c
  [bloviator.]: https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/
  [2]: https://skylion007.github.io/OpenWebTextCorpus/
  [3]: https://github.com/jcpeterson/openwebtext
  [estimated]: https://lambdalabs.com/blog/demystifying-gpt-3/
