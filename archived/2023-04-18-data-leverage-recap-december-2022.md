---
title: "Data Leverage Recap December 2022"
subtitle: "The Last Three Months in Review: What's New and What's Next"
date: 2023-04-18
original_url: "https://dataleverage.substack.com/p/data-leverage-recap-december-2022"
---

> **Original Substack post:** [https://dataleverage.substack.com/p/data-leverage-recap-december-2022](https://dataleverage.substack.com/p/data-leverage-recap-december-2022)

![](https://substack-post-media.s3.amazonaws.com/public/images/58a3e73f-5147-4fdd-b00e-896b7ce302cb\_2614x2268.jpeg "")

*The waves never stop; photo from [Unsplash contributor Photoholgic](https://unsplash.com/photos/RGvwatYi0-Q).*

This post will be a short review of the blog so far. There’s two goals here: to provide a quick catch up for anyone who’s new to the blog, and to give me a chance to reflect on how these ideas have held up against a barrage of AI product releases, research outputs, and news.

Thanks for reading Data Leverage! Subscribe for free to receive new posts and support my work.

### Summary

In this post, I discuss the concern that language model applications like ChatGPT could erode their own foundations. Platforms like StackExchange and Wikipedia provide infrastructure and incentives for users to participate in the creation and sharing of knowledge. These platforms need traffic and users, which creates a key concern: if generative AI systems like ChatGPT (which rely on StackExchange and Wikipedia for training data!) are good enough that users replace their StackExchange and Wikipedia visits with a ChatGPT conversation, could GPT-4 hinder our ability to train GPT-5?

### How the Key Points Hold Up

On March 17th, we got to see some early [evidence](https://twitter.com/DominikGutt/status/1636732846948663298?s=20) for this effect. In the linked Tweet, Dominik Gutt describes a preliminary results showing a negative effect from Large Language Models (LLMs) on Q&A activity.

About a week later, a similar [point](https://twitter.com/peternixey/status/1640002493630369792?s=20) was made by an authoritative source: Peter Nixey, a top 2% StackOverflow (SO) contributor, who highlighted the concern that LLMs may prevent users like him from contributing to SO, and “When it comes time to train GPTx it risks drinking from a dry riverbed.”

Finally, on April 17th, StackOverflow’s CEO wrote a blog [post](https://meta.stackexchange.com/questions/388401/new-blog-post-from-our-ceo-prashanth-community-is-the-future-of-ai) discussing generative AI. While the post was controversial in the community for alluding to integrating generative AI into the platform, I was excited to see direct references to the importance of SO training data and the potential tragedy of the commons at play here. “AI is built on our collective knowledge, and we must all participate in building its future”.

### What’s next

The core argument is this piece (and the similar arguments linked above) rely on making assumptions about how people will use LLMs and online platforms. It’s certainly possible to imagine scenarios in which LLMs benefit users and online platforms (a point to which we’ll return shortly!) For instance, if LLMs primarily address what would be duplicate questions, reducing the need for humans to flag these questions and freeing up more time answer interesting questions, this could be great (though I think it’s unlikely without substantial effort).

One direction for future work is to use some combination of agent-based modeling and continued empirical investigation to specify the conditions necessary for positive sum outcomes. I’ll definitely be keeping an eye out for more empirical work in this space.

## **[ChatGPT is Awesome and Scary: You Deserve Credit for the Good Parts (and Might Help Fix the Bad Parts)](https://dataleverage.substack.com/p/chatgpt-is-awesome-and-scary-you-deserve-credit) (Dec 4, 2022)**

### Summary

You and most everyone you know probably helped build the new wave of generative AI technologies like ChatGPT. This post provides an overview of all the specific details we know about past GPT training data sources, and how we can use that to engage in some educated guesswork regarding the data underlying ChatGPT, GPT-4, Bing chat, and more.

### How the Key Points Hold Up

The public is still mostly in the dark regarding specific ChatGPT training details. However, the sources highlighted in the original post still hold up; I think this is pretty close to the best guess we can make right now.

OpenAI’s [stance](https://www.theverge.com/2023/3/15/23640180/openai-gpt-4-launch-closed-research-ilya-sutskever-interview) on sharing information about training data going forward suggests it may be hard to do this kind of data documentation in the future. I do think we can still learn a lot about ChatGPT from studying more transparent models and datasets like [LLaMa](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) and [The Pile](https://pile.eleuther.ai/) — I’d be surprised if there are massive deviations in pre-training data collection strategies.

I also came across this great [post](https://gist.github.com/veekaybee/6f8885e9906aa9c5408ebe5c7e870698) from Vicki Boykis provides a similar perspective on the ChatGPT training data, as well as info about the model architecture and other details.

### What’s Next?

I think there’s a lot of value in learning and sharing as much as we can about the role of data in producing generative AI. Please reach out if you’re interested in collaborating. This will involve hunting down datasheets, advocating for the scientific value of sharing datasheets, and perhaps conducting audits that help us make educated guesses about data usage (e.g., asking ChatGPT a question it can only answer with access to a particular source).

## **[AI Artist or AI Art Thief? Innovation, Public Mandates, and the Case for Talking in Terms of Leverage](https://dataleverage.substack.com/p/ai-artist-or-ai-art-thief-innovation-public-mandates-and-the-case-for-talking-in-terms-of-leverage) (Dec 15, 2022)**

### Summary:

In this post, I review ongoing discussions about how generative AI can be seen as “stealing” in a moral or legal sense. The core argument here: whenever we have a major new innovation, it’s practically impossible for the broad public to “consent” to contributing to these technologies, so the technologies cannot come out the of gate with a public mandate. I also argue that although it may be tough to get agreement on exactly what it means for ML and AI technologies to steal, it can be very productive to talk in terms of which groups have leverage because they can impact model capabilities.

### How the Key Points Hold Up

Overall, I think the arguments in this post hold up in the face of an ever-evolving conversation. The original posts states that we were waiting for a firm legal answer, and as of April 2023 that’s still true. The implications of any legal decisions here will be huge, so to a certain extent we do have to keep waiting with bated breath.

I still stand by the value of a leverage-based framing (it’s a pretty big part of my dissertation), and will keep advocating for this line of thinking.

### What’s next

I’m in the process of iterating on a [website](https://www.datalevers.org/) for crowdsourcing and highlighting tools that help you use “data levers”. I’d love your help in improving it!

Another angle for making concrete progress on this issue is through the development of Responsible AI Licenses for Data. If you’re interested, consider getting involved in [RAIL](https://www.licenses.ai/blog/2023/1/17/rail-initiative-call-for-participation).

## **[AI Technologies are System Maps, and You are a Cartographer](https://dataleverage.substack.com/p/ai-technologies-are-system-maps-and-you-are-a-cartographer) (Feb 2, 2023)**

## Summary:

Much of my academic work has been at least partially motivated by an argument for thinking of “data as labor”. Here, I make the case that this particular “data as *X*” metaphor can be made even stronger by comparing data generation to cartographic labor. The comparison with map-making can be especially useful for thinking about how time might be on on the side of the data laborer (the world is ever-changing, so over time data leverage grows).

### How the Key Points Hold Up

I’ve been reflecting more on this “Data isn’t labor” [post](https://digifesto.com/2018/12/06/data-isnt-labor-because-using-search-engines-is-really-easy/) from Sebastien Benthell. It makes some compelling arguments against data as labor metaphor in the context of search engines and Google. I think it’s worth discussing the tensions with different data as *X* metaphors.

On the technical side, I haven’t seen anything yet that makes me think that data as cartographic labor is completely lacking in predictive value, or in instrumental value as a rallying cry for collective action.

I do think it’s worth making a distinction between the predictive value of a “data as (cartographic) labor” theory (can we actually predict how data economies work with a labor lens) and the aspirational value of this metaphor (we should try to foster a sort of data labor solidarity to support collective action).

### What’s next

I believe this remains a ripe conceptual lens for both academic research in the data governance space, and for public-facing arguments about data’s value. I plan to continue developing the idea, and have some work in the oven (stay tuned). The planned [datalevers.org](http://datalevers.org) FAQ may also help here.

## [Plural AI Data Alignment](https://dataleverage.substack.com/p/measuring-relative-ai-alignment-in-terms-of-data-pipelines) (Mar 1, 2023)

### Summary:

I propose a definition for measuring when an AI system is aligned with a group of people in terms of data agency:

“An AI system is more aligned with a coalition if members (1) know how their data contributions flow to that system, (2) can reason about how changes to data flow might impact AI capabilities, and (3) have agency to reconfigure these data flows.”

### How the Key Points Hold Up

I still think this definition has a lot of value to add to ongoing discussions of AI alignment, building “full-consent” generative AI, and thinking about AI in terms of how it serves different groups (i.e., *AI for social good, but social good for whom*).

An open question I remain unsure about is whether it’s useful to frame this as part of “alignment” or something else entirely. There is a growing movement for full-consent AI, and these ideas are much more naturally *aligned* with this movement than any one “AI Alignment” faction. Let me know what you think about this — is it important to try and insert this idea into the alignment debate, or better to avoid the topic of alignment and talk more about consent and agency?

### What’s next

I plan to continue developing this definition and trying to find venues and communities that find it useful. I don’t expect any shocking new AI releases to cause me to majorly revise it, but that’s always possible!

## **[Bing Rewards for the AI Age](https://dataleverage.substack.com/p/bing-rewards-for-the-ai-age) (Mar 29, 2023)**

### Summary:

This post describes a proposal for giving people credits for their data contributions that can be used to query expensive generative AI systems. A key idea: if we set up a credit system well, we might be able to simultaneously account for the incentives faced by generative AI operators, online platforms that host and facilitate the creation of data, and individual people. A real win-win-win!

### How the Key Points Hold Up

This post has been shaken a bit by the waves of news. The costs matter here (even for back-of-the-napkin examples) and we’ve seen big changes in API costs. We also still don’t know exactly how the operational costs of generative AI systems are changing, which could have a big impact on the viability.

Additionally, I started writing this piece after seeing news about Microsoft limiting Bing conversation lengths to inhibit “bad” behavior. It seems this may no longer be an issue, either.

On the other hand, [discussions](https://twitter.com/random_walker/status/1648322180558606338?s=20) about the environmental impacts of AI are heating up, which may actually strengthen the case for a credit based system.

It’s very promising to see the StackOverflow CEO making [statements](https://stackoverflow.blog/2023/04/17/community-is-the-future-of-ai/) like “If AI models are powerful because they were trained on open source or publicly available code, we want to craft models that reward the users who contribute and keep the knowledge base we all rely on open and growing, ensuring we remain the top destination for knowledge on new technologies in the future.” I believe this suggests this kind of idea is quite plausible.

### What’s Next

The main thing I’ll be on the look out is any generative AI firms trying something like this out.

I think there’s also room here to use agent-based modeling to understand the strengths and weaknesses of this kind of system.

If you happen to work on a platform for online communities, and want to implement something like this, please do let me know!

## Upcoming Topics

As you may have already guessed from this very recap, I’m convinced one of the most important policy goals for mitigating the negative impacts of ML and AI is to create standards and transparency around data opt-in mechanisms, or much better versions of data opt-out (I do think these can co-exist).

I also think that once we see a slew of new ways for individuals and groups to engage in data decision-making, via opt-in forms, opt-out forms, and new licenses, we’re really going to see a need for the AI field to engage seriously with collective action and governance research. This won’t just be because it’s the right thing to do, but because with a paradigm of data agency, gaining a new mandate from the public will become a core part of building capable AI systems.

Thanks for reading Data Leverage! Subscribe for free to receive new posts and support my work.
