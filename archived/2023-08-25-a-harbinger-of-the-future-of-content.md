---
title: "A Harbinger Of The Future Of Content"
subtitle: "The New York Times is trying to remove its content from OpenAI models, surfacing tensions around copyright, economic harms, privacy, and the distribution of AI benefits."
date: 2023-08-25
original_url: "https://dataleverage.substack.com/p/a-harbinger-of-the-future-of-content"
---

> **Original Substack post:** [https://dataleverage.substack.com/p/a-harbinger-of-the-future-of-content](https://dataleverage.substack.com/p/a-harbinger-of-the-future-of-content)

![](https://substack-post-media.s3.amazonaws.com/public/images/570a4dcb-47f1-4a25-be66-3be373eb78bb\_3968x2957.jpeg "")

Photo by [David Smooke](https://unsplash.com/@smooke?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/En_wELYYhD4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

A major development in ongoing discussions about the future viability of generative AI: the New York Times has [emphatically](https://www.npr.org/2023/08/16/1194202562/new-york-times-considers-legal-action-against-openai-as-copyright-tensions-swirl) [stated](https://www.theverge.com/2023/8/21/23840705/new-york-times-openai-web-crawler-ai-gpt) it does not want to be in the ChatGPT dataset and has taken action accordingly. Specifically, amidst ongoing negotiations it seems the Times is considering intellectual property-based legal action, and in the meantime has added GPTBot to its robots.txt file (i.e., the Times indicated OpenAI should no longer scrape its content). Other organizations like CNN have [followed suit](https://www.theguardian.com/technology/2023/aug/25/new-york-times-cnn-and-abc-block-openais-gptbot-web-crawler-from-scraping-content).

In other words, the Times is gearing up for a [data strike](https://dl.acm.org/doi/10.1145/3308558.3313742) aimed at OpenAI (and potentially other LLM operators like Anthropic, Google, Microsoft, Meta, etc.), echoing [posturing](https://www.nytimes.com/2023/04/18/technology/reddit-ai-openai-google.html) from Reddit.

In this post, I want to lay out some factors that might play into decision-making when an organization like the New York Times – or a small group like you and some friends who write a blog or host a podcast together – is thinking about trying to enter or exit an AI training dataset. These factors might include property dispossession, economic harms, privacy, the benefits of personalization, and concerns with representative data.

These factors are all part of a broad challenge with *dataset preference elicitation*: how can we built datasets that minimize “inclusion errors” and “exclusion errors”, i.e. contain contributions only from people who want to be in a particular dataset (taking into account that there are both costs and benefits associated with contributing to AI).

In a follow up post, I’ll delve deeper into what I think we can say at this juncture about the likely efficacy of the data strike and how we’d measure the impact of data-related collective action more generally in the new AI paradigm.

In case the data strike idea is new, here’s a quick refresher: In many contexts, content we contribute online – like the text that a journalist writes for a NYT article, or the text you write in a social media post – is a crucial component in making AI systems work; in a certain sense, it looks like the NYT and quite a few bloggers are “working for” major AI operators. There’s some [insight](https://www.aeaweb.org/articles?id=10.1257/pandp.20181003) to be [had](https://arxiv.org/abs/2305.13238) from thinking about “data as labor". Withholding past or future data – whether by updating your robots.txt file, through legal action, or by going offline for a week – can impact AI systems and give people bargaining power. And just like in the context of labor, this only works when data creators achieve collective action (it typically takes the combined efforts of an entire union to negotiate major pay raises or working condition improvements).

So the New York Times has been “working for” AI operators, and they want more bargaining power. And it seems they’re not pulling any punches, given they are considering both legal action to remove past data *and* using robots.txt to withhold future data.

## Reasons to Opt Out or Data Strike

The primary concern voiced by the anonymous New York Times employees who made the public aware of potential legal action is an increasingly prominent one: AI operators can use your content, traces, and records to “compete against you”. Some have called AI data practices a “[property land grab](https://www.telegraph.co.uk/business/2023/08/21/internets-original-sin-ai-nightmare/)”, with the assumption that a good portion of training data (like the words that make up a New York Times article, or your blog post or podcast transcript) are considered intellectual property (and subject to relevant laws).

Even if you’re not a fan of intellectual property or a framing that treats data as something to be governed with property law (see e.g. writing from [Viljoen](https://www.phenomenalworld.org/analysis/data-as-property/) on the topic of “data as property”), you might view ML/AI systems as likely to enact *economic harms via competition*. It seems fair to assume the probability that an AI system can replicate your style or ideas increases when there’s more content (i.e. more sequences of text in the context of LLMs) created by you or people like you in the training data.

A related reason to want out of training data is privacy. Diffusion models (used in some of the popular image-generation products) definitely [can](https://floriantramer.com/publications/diffusion23/) output exact copies of training inputs (for instance, a picture of your face!). Language models similarly might memorize your writing and spit it out [verbatim](https://floriantramer.com/publications/verbatim22/), leading to a host of thorny questions about how to handle such situations.

We might think of these concerns – property dispossession, economic harms via competition and privacy risks – as emerging from the same underlying truth about LLMs and similar technologies: when there are more sequences or patterns in the training data that come from a particular group (like a news company), downstream models are more capable of producing output sequences that look like that group’s sequences. If keeping your sequences (broadly construed) somewhat hidden is important to you, you might want to consider opting out.

## Reasons Not to Opt out

Of course, there are good reasons to believe that having content and other contributions in a training dataset provides you (or the New York Times) with benefits. If a model is devoid of any training data that covers your area of interest, you’re unlikely to be able to use the model in cases in which it could be useful. While the many potential [hazards](http://a) of LLMs (some stated quite [early](https://dl.acm.org/doi/10.1145/3442188.3445922) on) persist in current products, it remains a possibility that another large newspaper that embraces generative AI might out-compete an organization like the New York Times. Depending on how things play out, it could be the case that some organizations who opt-out of generative AI training do not end up winning in the long term. Ultimately, there is an industry wide collective action problem here with major parallels with [sectoral bargaining](https://www.economicpossibility.org/insights/codetermination-is-not-a-standalone-institution-rather-it-is-part-of-a-broader-in). This society-level collective action problem is a separate topic.

There’s another reason a group may *not* want to opt-out (or may want to opt-in given the chance): dataset representation. Opt-out decisions intersect with long-standing concerns about fairness and bias in a wide array of ML and AI systems. While AI systems often contribute to injustice because of inequities present in the social networks or physical infrastructures in which they are deployed (in a [variety](https://virginia-eubanks.com/automating-inequality/) [of](https://www.katecrawford.net/) [contexts](https://pubmed.ncbi.nlm.nih.gov/33982031/)), it’s also true that AI systems can exhibit sometimes severe group-level performance gaps because of representation issues in training data. Put simply, if an entire organization or group were to truly disappear from generative AI training data, we’d expect to see major responsible AI issues. For instance, while ML/AI technologies often exhibit geographical biases, e.g. centering the US and western Europe, we could imagine a bizarro-world LLM that literally has seen evidence of that any country other than the US exists. Such an LLM would probably produce an enormous amount of errors, leading to major blunders for users.

Finally, it’s worth discussing the practical costs of data strike actions. This case highlights two concrete examples of specific actions an organization might take to data strike: [updating robots.txt](https://www.theverge.com/2023/8/21/23840705/new-york-times-openai-web-crawler-ai-gpt) and taking legal action. In this case, the possibility of legal action suggests quite high costs. On the other hand, it’s interesting to see NYT just updating their robots.txt – that’s something anyone with a website can do (see [ai.txt](https://site.spawning.ai/spawning-ai-txt) as well). However, updating these txt files is still non-trivial considering the platform-centric way the vast majority of the world interacts with the web.

These aren’t the [only](https://www.datalevers.org) options. In general though, the most efficacious actions will probably require pretty serious costs. This isn’t necessarily a total non-starter, because effective data strikes require collective action anyway (probably at the scale of a coalition of firms, or large group of consumers).

## What’s next

I hope add an appendum to this post as more information about the NYT’s plan is made public. Additionally, look out for part 2, discussing how we might predict the efficacy of this data strike, and how we might measure the efficacy from an external or internal perspective.

Thanks for reading Data Leverage! Subscribe for free to receive new posts and support my work.
