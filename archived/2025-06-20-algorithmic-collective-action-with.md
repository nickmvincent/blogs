---
title: "Algorithmic Collective Action With Two Collectives [crosspost]"
subtitle: ""
date: "2025-06-20"
original_url: "https://dataleverage.substack.com/p/algorithmic-collective-action-with"
content_id: "substack/post/166419096"
authors: ["Nick Vincent"]
published_at: "2025-06-20T18:29:39.666Z"
source_updated_at: "2025-06-20T18:30:05.198Z"
archived_at: "2026-09-25T20:33:47+00:00"
source_body_sha256: "aafe866f0dd1e149d2f51fa32948c9e3c8510a04444f39f3652850dadbb7fe0d"
---

*This post was written by [Aditya Karan], with support from Nick Vincent and [Karrie Karahalios] to accompany a FAccT 2025 [paper]. It was originally published on Jun 19, 2025 via the Crowd Dynamics Lab [blog].*

## Summary

Swifties organizing to promote new versions of songs, artists intentionally adding adversarial watermarks to protect their own work, and people adding positive articles about themselves to make LLMs make positive associations with their name. All of these examples demonstrate how people can change their behavior to get specific outcomes out of ML systems. Algorithmic Collective Action (ACA) encompasses many such situations in which groups of people engage in some coordinated activity to achieve a certain result from a ML model. From [empirical examples], and [prior theoretical work], we see that small collectives really can alter the behavior of ML models (often focusing on a certain subset of the data) by engaging in collective action.

As these large systems are expected to grow, multiple groups may try to engage in collective action. These groups can have different objectives and because of the complexity and often blackbox nature of these models, it’s hard to predict what could happen. If we think of each of these collectives as trying to adjust the underlying model behavior (weights), what happens when multiple collectives try to do the same thing? How should we reason about ACA when multiple collectives are at play?

![][1]

## What we did

Our [paper] (appearing at ACM [FAccT] 2025) explores this design space in several ways. We first introduce a collective action framework, which formalizes the components of collective action. In particular, we note that when multiple collectives engage in the system, the final dataset used to train composes of each of the collective’s data modification + the unperturbed data. This ultimately produces new parameters, which are then used to measure the group’s collective.

![][2]

The main components of collective action are:

1.  **Number of Collective and Objectives**: What are the collectives and what are their objectives?

2.  **Collective Composition**: Who is making up the collective?

3.  **Model Access**: What level of access does the collective have?

4.  **Action Availability**: What actions can the collective take?

5.  **Affected Party**: Who is the target of collective action?

6.  **Measurements**: How does the collective measure its own success? In introducing this framework, we aim to support further exploration into, and consideration of, the factors that go into determining possible outcomes of collective action, especially in the presence of multiple groups.

To illustrate the point, we also designed experiments to understand the success of collective action when two collectives participate vs just one. It turns out just adding one more collective already adds a lot of complexity into collective action scenarios. Consider a scenario where a company uses AI to analyze resumes. This collective, really wanting to get a certain job, works together to plan to slightly modify their resumes to cause an ML model to output particular classification results. We denote the individual classes with letters A/B and unique characters with numbers. For example A100 is targeting class A with a character identified with “100” (actual characters used can be found in the paper) We find that depending on the specific modification strategy, these collectives can either hurt or help each other. For example, below we see the collective’s hurting each other when both are acting.

![][3]

While in other cases, there’s very little impact.

![][4]

Why is this important? It suggests that examining collective action in isolation could obscure the important interaction effects that occur when multiple groups engage. More broadly speaking, it also signals the need to understand what outcomes different groups want out of ML systems, and what changes or strategies they may use to achieve this desired goal. It behooves both platforms and other collectives to understand these dynamics and how they may affect ML systems more broadly.

This framework also opens many other avenues to explore to further understand important considerations in algorithmic collective action. For platform developers, understanding how and why different groups might want different outcomes from ML models can help illustrate a stronger understanding of how data is generated. For organizers, understanding how to avoid conflicts with other groups, and how to optimize the composition could play a key role in success.

We examine some of these implications further in our full paper. We hope that our framework and experiments serve as launching points to explore more deeply the power and limitations of collective action on algorithmic system. The paper, which also dives into other set of experiments looking at heterogeneity and discusses on the role collective action may or should play in data generations and models, can be found [here][paper]!

## Addendum

Exploring the role of heterogeneity in collective effectiveness

We also used the above framework to explore the impact of homogeneity of collective members in the effectiveness of collective action. We find that for a recommender system case, where some groups are trying to promote/demote specific content, group size has more of an impact, but groups that are somewhere in between fully homogenous and fully heterogenous can offer some performance boost.

![][5]

These experiments further demonstrate the need to understand the specific collectives, their goals and composition, to truly understand how algorithmic collective action might come about in practice.

  [Aditya Karan]: https://adityakaran.me/
  [Karrie Karahalios]: http://www.karriekarahalios.com/
  [paper]: https://arxiv.org/abs/2505.00195
  [blog]: https://crowddynamicslab.github.io/collective/action,/machine/learning/2025/06/19/two-collectives/
  [empirical examples]: https://www.the-independent.com/arts-entertainment/music/news/taylor-swift-fearless-fans-b1829051.html
  [prior theoretical work]: https://arxiv.org/abs/2410.12633
  [1]: ../media/algorithmic-collective-action-with/edc6e908bbfbca630908.png
  [FAccT]: https://facctconference.org/
  [2]: ../media/algorithmic-collective-action-with/e62b93bda7725d770c11.png
  [3]: ../media/algorithmic-collective-action-with/b422fefb5e970eef1e75.png
  [4]: ../media/algorithmic-collective-action-with/679f9cc410df51fee568.png
  [5]: ../media/algorithmic-collective-action-with/5f1fd2639860c24a4877.png
