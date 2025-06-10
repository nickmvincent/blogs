---
title: "Live By The Free Content For Training"
subtitle: "There's deep tension in the current ask-for-forgiveness-free-for-all approach to acquiring data for model training. Will "open" models cause this tension to reach a breaking point?"
date: 2025-01-28
original_url: "https://dataleverage.substack.com/p/live-by-the-free-content-for-training"
---

> **Original Substack post:** [https://dataleverage.substack.com/p/live-by-the-free-content-for-training](https://dataleverage.substack.com/p/live-by-the-free-content-for-training)

![File:Petardsketch2.jpg](https://substack-post-media.s3.amazonaws.com/public/images/93839e8b-a61f-4041-aa8b-7adcecb77f88\_800x559.jpeg "File:Petardsketch2.jpg")

*Illustration of a petard, 17th century. Famously known to [hoist](https://en.wikipedia.org/wiki/Hoist_with_his_own_petard) engineers who built them. Library of Congress, [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Petardsketch2.jpg).*

OpenAI, Anthropic, Google, and more all offer subscription-based AI products. You pay them, and you get access to an interface that provides you with model-generated outputs for all sorts of queries. Like many tech products, you agree to certain Terms of Service (though you probably haven’t read them all) that restrict what you can do with these outputs. One theme that cuts across these Terms:

* You cannot extract data programatically
* You cannot use “The Output” to compete with the provider

Together, these clauses mean you are expressly violating the Terms of Service if you were to try to collect model Output in bulk and train a new model using said Output (I’ve captured a some relevant text from various Terms at the end of this post).

At the same time, none of these organizations (to my knowledge) have posted a public document describing the full set of inputs that were used for training their models (although non-profit labs like AI2 *have* produced fully documented models like [OLMo2](https://allenai.org/olmo)). Unsealed [documents](https://chatgptiseatingtheworld.com/2025/01/15/kadrey-refiles-motion-to-file-third-amended-consolidated-complaint-with-partially-unredacted-exhibits-per-judge-chhabrias-order/) from a case against Meta suggest that the inputs used by the major labs include, among other things, clearly pirated content, and that there is an “[everybody is doing it](https://www.theverge.com/2025/1/14/24343692/meta-lawsuit-copyright-lawsuit-llama-libgen)” impression that is widely shared in the industry. To quote directly, “it is known that OpenAI and Mistral are using the library for their models (through word of mouth)”.

So, what gives? Doesn’t the idea that these firms are simultaneously [arguing](https://www.reuters.com/legal/litigation/tech-companies-face-tough-ai-copyright-questions-2025-2024-12-27/) for the right to train on anything they can get their hands on while denying their competitors the right to train on model outputs seem a little bit inconsistent? Rules for thee, but not for me? Such behaviour is by no means unprecedented or really all that shocking — in fact, it’s the sort of thing that can be explained easily in terms of rational decision-making. If you think you can get away with it, why wouldn’t you try to take your grocery cart with 30 items into the express lane and skip the line, or hop into the carpool lane by yourself while nobody is looking?

Well, one rejoinder is that in doing so, you’re taking the first step towards demolishing a valuable system of norms. Another one is: often times, you will get caught and rebuffed or punished!

In the case of AI training, there haven’t been any police sirens quite yet (though major decisions are looming). But, the cascade of norm violation has started: it’s now widely assumed that many models are being trained on ostensibly Terms of Service-locked outputs, and as far as I know, no AI lab has tried to take any major enforcement actions yet. In other words, it’s considered very likely that the outputs from powerful models produced by OpenAI, Anthropic, and company are indeed being used to train models operated by other firms.

Of course, the optics of taking enforcement action would not be great — it could look an awful lot like a lone driver in the carpool lane trying to make a citizen’s arrest of another lone driver. It would be hard to enforce these Terms of Service against a sympathetic actor without drawing attention to the extant tension in the current training paradigm.

So, it seems that AI labs may need to [live by the sword, and thusly die by the sword](https://en.wikipedia.org/wiki/Live_by_the_sword,_die_by_the_sword). Or, to draw on another idiom, perhaps the industry will be [hoisted with its own petard](https://en.wikipedia.org/wiki/Hoist_with_his_own_petard).

And this week, a new model has rocked the AI world (well, at least online AI discourse focusing on [investment](https://www.reuters.com/technology/chinas-deepseek-sets-off-ai-market-rout-2025-01-27/) and [policy](https://www.wired.com/story/deepseek-ai-china-privacy-data/) — as far as I can tell, most researchers are reacting much more soberly). DeepSeek’s R1 product — which has accompanying MIT-licensed model [weights](https://huggingface.co/deepseek-ai/DeepSeek-R1) — seems to perform extremely well. The release also includes a detailed [technical report](https://arxiv.org/abs/2501.12948) with details about the reinforcement learning-based post-training and efficiency improvements that led to such results, but no mention of training data.

It’s likely the case that AI model outputs made their way into the training set, either directly or because these outputs have diffused into the open Internet (see Wiggers in TechCrunch on “[Why DeepSeek’s new AI model thinks it’s ChatGPT](https://techcrunch.com/2024/12/27/why-deepseeks-new-ai-model-thinks-its-chatgpt/)” for full reporting on this). The tension at the heart of arguing for free-for-all training while restricting output use has been lurking under the surface since the generative AI boom began, and now proliferation of open models may bring this tension fully into the open.

I think a few things may happen in response. On one hand, given that the discussion around DeepSeek and the US AI industry is deeply entangled with national security discussions (for better or worse), it could be the case that US politicians start to express concern with the status quo around model distillation. For instance, it could the case that a senator or other figure who wants the US to win the “[AI race](https://www.cnbc.com/2025/01/23/scale-ai-ceo-says-china-has-quickly-caught-the-us-with-deepseek.html)” could see the R1 release as evidence that US-based AI labs need to do even more to gate their model outputs, perhaps leading to increased efforts to actually enforce these terms of service.

It could also be the case that increased discussion of data practices highlights what is arguably hypocrisy that favors Big Tech over consumers and “Little Tech”, perhaps leading regulators who are upset with Big Tech (an issue that cuts across the political aisle) to amplify efforts to regulate data transparency (looking back towards efforts like the [Dashboard Act](https://www.clarip.com/blog/senate-dashboard-act/)).

Finally, while not extremely likely in the short term, I am hopeful that these discussions could invigorate consumer appetite for AI models that do not use proprietary blends of training data. While the current menu of AI products does not allow for much flexibility in terms of picking a model that aligns with one’s values, the future may provide such flexibility.

Importantly, as the tension inherent in a “live by the sword, die by the sword” approach to AI data becomes prevalent (and as the the tech industry starts to get more concerned about being hoisted by its own petard), there could emerge a massive opportunity for existing technology companies or new start-ups to carve an identity as especially focused on data supply chain integrity and trust, and offer a product that has no such tension. This could turn into a major win on the basis of changing consumer demand, and would also provide first mover advantage if regulators put an end to the current set of practices.

Overall, I’d be surprised if the current status quo doesn’t face some degree of reckoning because of proliferation of open models, and I’m hopeful that the reaction can be positive in the long run for the tech industry. As usual, I expect that supporting more data transparency and collective action by data creators will play a major role in creating momentum towards a better paradigm.

—

Relevant Terms of Service sections, captured Jan 27, 2025.

[OpenAI](https://openai.com/policies/row-terms-of-use/)

![](https://substack-post-media.s3.amazonaws.com/public/images/145712bc-cb0c-4578-a1b2-16916c89b65f\_1858x1096.png "")

[Anthropic](https://www.anthropic.com/legal/consumer-terms)

![](https://substack-post-media.s3.amazonaws.com/public/images/039293a8-72b1-49d2-89c5-cc4530e8f518\_1812x1316.png "")

[Google Gemini](https://ai.google.dev/gemini-api/terms)

![](https://substack-post-media.s3.amazonaws.com/public/images/ecdc4516-96fa-4c04-b0a2-cb1bd1b9c072\_1804x1068.png "")
