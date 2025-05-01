## Data and Compute Pooling

Presently, it is not very common that private AI labs coordinate to share compute infrastructure, run shared training runs, or otherwise take advantage of situations in which they might be running very similar experiments or processes.

In theory, there is great potential for pooling in the AI space, because model training involves different organisations doing the same thing in parallel, especially in pre-training.

Before the generative AI era, there was an implicit form of information pooling between companies in the form of replicable research publications and data sharing (in part, probably made possible because these companies had market power, which allowed them to invest in innovation). A lightweight version of this now exists in the form of model weight sharing, though outside a few select organisations, model weight releases are rarely accompanied by truly replicable papers or implementation details. (Another side note: as generative AI becomes attached to flagship products like search, and sold as a primary product, it makes sense that firms have started to crack down on sharing; in the past, replicable and open research papers from private tech companies were primarily in the realm of core research. Google did not publish papers about to build a copy of Google from scratch).

Why is this the case? In short, market pressure. More specifically, under current incentive systems, AI labs are competing on model quality to obtain individual subscriptions, API users, and enterprise customers. If Anthropic were to share model checkpoints with OpenAI, or give OpenAI employees direct access to their compute while during downtime, that might help OpenAI take some paying Claude customers.

Note, however, that the current set of practices actually preclude us from testing an open research question: perhaps, if OpenAI and Anthropic joined forces to build a new "base layer model", and then iterated on top of that new layer, they could make even more money.

To put numbers on this, let's say right now that open models score 93/100 on a scale we're making up for this example.

Perhaps OpenAI and Anthropic's flagship offerings are around a 95-96. So OpenAI releases a 95.5, gets some users, Anthropic releases a 95.6, then OpenAI releases a 95.65, and so on.

But, in an alternate world where OpenAI and Anthropic pool all compute and experiments for 6-months, perhaps they emerge with a new base layer model that's a 98, and now compute on fine-tuning, UX, etc.

Perhaps the jump to a 98 increases the number of consumers who will pay for AI so much that both companies are better off.

In practice, some versions of this might raise flags for anti-trust behavior (especially if this was e.g. Google and Microsoft instead of OpenAI and Anthropic).

But a public AI consortium can basically do exactly this!

The specific action I'm advocating for here is sharing various mid-training checkpoints (and "final" model weights), in addition to sharing access to compute (though if the checkpoint pooling works well, this would effectively reduce the need for even running compute for some participants).

### Tricky considerations (getting bullet pointy now)

One tricky consideration here is that by sharing model checkpoints, you are kind of sharing data too. Maybe privacy concerns

Another obvious concern is basic commons / collective action problems. How to make sure nobody is free-riding? How to fairly make sure participants bearing the brunt of costs (e.g., have the physical data centers in their country, are actually paying the power bill) feel they're being trated fairly.

Go to classic work on Ostrom, Kollock (Mancur Olson, Oliver and Marwell, etc.)

- Ideally they do the hard work of making a plane, but then stand the benefit when the "Singapore Airlines" of AI actually use that plane
