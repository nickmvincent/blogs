---
title: "Google And Tiktok Rank Bundles Of"
subtitle: "Google and others solve our attentional problem by ranking discrete bundles of information, whereas ChatGPT ranks more granular chunks. This lens can help us reason about AI policy."
date: 2025-05-27
original_url: "https://dataleverage.substack.com/p/google-and-tiktok-rank-bundles-of"
---

> **Original Substack post:** [https://dataleverage.substack.com/p/google-and-tiktok-rank-bundles-of](https://dataleverage.substack.com/p/google-and-tiktok-rank-bundles-of)

![File:Bonifacio falaises Grain de Sable.jpg](https://substack-post-media.s3.amazonaws.com/public/images/87212bbc-0d14-4869-8670-ece4d5a560b1\_960x762.jpeg "File:Bonifacio falaises Grain de Sable.jpg")

In this post, I want to share some thoughts on a very general model for thinking about a wide variety of “AI”[1](#footnote-1) uses. This post complements a forthcoming FAccT paper ([preprint](https://arxiv.org/abs/2405.14614) on ArXiv) on operationalizing and measuring “attentional agency”[2](#footnote-2), focusing on one aspect of the paper: understanding many different types of platforms as all performing highly related ranking tasks allows us to view old and new AI in the same light.

In short, it can be useful to think of a wide variety of platforms — including Google, TikTok, and ChatGPT, as mentioned in the title, but also Spotify, Amazon, YouTube, and more — as delivering the same fundamental service. They are all taking some **bundles of information**, ranking these bundles, and delivering them to us to consume.

These bundles vary heavily in terms of their content, format, length, and critically, the **social and institutional processes** by which the bundles are created. A webpage delivered by Google is different in many ways from a song or album delivered by Spotify, which is different from a 30-second-long user-generated video delivered by TikTok. On the content, format and length fronts, these differences are rather apparent. Of course an HTML page with links is different from a set of audio files or a video file and associated likes and comments. On the social/institutional front, some differences are apparent (e.g., we might be able to succinctly describe the difference between how a Wikipedia article was created vs. a TikTok video), but in many cases understanding the full “context of creation” is challenging (but important, and often critical to the actual value of the information bundle; **we often want to know that “effort” was put into the information we consume**).

If we pick two large platforms — let’s say, Google and TikTok — we can understand both platforms as competing in the same giant ranking exercise. The candidate set for each platform is different, though the overall information needs may overlap. As an example, users could use both platforms to search for recommendations for restaurants in Chicago; for a population of users with this particular information need, these platforms compete directly against each other for those users’ attention. In both cases, the set of outputs is restricted based on all the available discrete bundles of information that people created (again, with some constraints on content, format, length, social processes, and institutional processes).

Enter “generative AI”. On one hand, these tools seem incredibly *different* from existing platforms. Isn’t this difference why generative AI tools have received massive attention in the press, academic literature (extending well beyond ML and AI), and even from investors?

On the other hand, even early generative AI tools threatened to compete with Google and TikTok. And newer ones do so much more explicitly, either by adding search to chat tools (ChatGPT with deep research) or adding generative outputs to a search tool (Google AI Overviews).

So, what’s changed? One way to think about this is that generative AI is indeed competing in the same giant ranking exercise as past platforms. But, generative AI “frees us” from the need to rank over discrete bundles of information. Instead, we can begin to rank increasingly granular chunks of information. Rather than explicitly optimizing whether someone will click a link or dwell on a video, we can do the ranking using a mixture of what’s statistically likely to come next in a sequence of information, or whether a sequence is likely to be seen as “good” by some users.

The critical, and potentially controversial, assertion here is thus: An output from ChatGPT can (and should) be thought of as an evolution of “ten blue links”.

In many ways, working with more granular information is what enables new capabilities. Writing customized poems or bespoke code simply isn’t possible when our candidate set is fixed. However, as upstream models move away from working with discrete bundles of information, this creates new technical and social challenges for the downstream systems (and it’s striking that many “fixes” for generative AI’s weaknesses involve trying to *reestablish bundling*).

In particular, many of the serious issues facing generative AI systems can be understood in terms of characteristics that we lose from going too granular with our information chunking. Factuality and provenance become difficult when we lose track of the social/institutional processes that created a given bundle. We can check the history of a Wikipedia article in a way that’s not possible for a generative AI output yet.

Critically, by ranking chunks (tokens) and not bundles (webpages, songs), we break almost all of the economic arrangements that incentivized the creation of the bundles in the first place. The lens described above neatly explains much of the furor around generative AI, copyright, and intellectual property more broadly. This also explains why many of the suggested solutions can be seen as reasserting some degree of bundling, via copyright or other avenues.

Our paper discusses a number of policy implications (and hopefully, a future blog post will unpack the specific suggestions in our paper). One key idea is that we might measure the level of attentional agency afforded by platforms, in terms of whether they are prioritizing *what the platform thinks users want* (i.e., using all the information and algorithmic capabilities available to the platform, what’s their best case regarding the perfect set of links or videos to deliver) vs. what other “advocates” want users to see (advertisements, content being pushed by other users, public service announcements from a government agency). This could be extremely useful as a framework to force early transparency around the incorporation of advertising or persuasive content into generative AI.

The goal of this post is just to introduce this set of ideas. We very much welcome feedback and discussion! While our paper introduces a particular set of definitions, we note that there are many [related](https://arxiv.org/abs/2107.10939) [ideas](https://arxiv.org/abs/2406.18682) in this space around aligning both recommender systems and generative AI systems, and we hope this work can contribute to that broader conversation.

[1](#footnote-anchor-1)

Why am I still scare quoting “AI”? For some related thoughts, you might also enjoy this draft microblog: “[Some Semi-Serious Naming Proposals to Improve AI Discourse](https://github.com/nickmvincent/blogs/blob/main/microblogs/2025-05-17_three_terms.md)”.

[2](#footnote-anchor-2)

The [paper](https://arxiv.org/abs/2405.14614) focuses on measuring how different digital platforms — broadly defined to include anything from Google to TikTok to ChatGPT — afford (1) users the ability to “pull” information they want and (2) advocates (like organizations that buy advertising or government agencies pushing public service announcements) the ability to “push” information to users.
