# Invention Exercises

Do not use these as recall questions. Each set makes an earlier idea fail before asking for the mathematical repair. Short tests appear first; building tasks appear last.

## 000 — Observations

1. Observe the same mug from two positions. List what changes and what survives.
2. Design a world in which yesterday can never help tomorrow. Explain why learning fails there.
3. Write a tiny classifier that stores exact observations only. Break it with a harmless change in lighting or position.

## 001 — Features

1. Decide whether an animal will reach camp soon. Choose three useful measurements and two irrelevant details.
2. Make a one-feature tiger rule fail once with a zebra and once with a three-legged tiger.
3. Change the decision to “can it hide in grass?” Explain why the feature set must change too.

## 002 — Vectors

1. Encode an animal using `[weight, speed, age]`, then deliberately read it as `[age, weight, speed]`. What survived and what was destroyed?
2. Plot four objects using two features. Which meaning belongs to an axis, and where is that agreement stored?
3. Extend the vector with a binary feature. Explain why its numeric scale creates a later problem.

## 003 — Distance

1. Find two nonzero signed differences that sum to zero.
2. Starting only from “cancellation is forbidden,” invent two repairs besides squaring. Compare their behavior.
3. Implement Euclidean distance, then rescale one feature by 1,000. Diagnose the changed nearest neighbor.

## 004 — Change

1. Give three different starts for which `[5, -2]` is the same instruction.
2. Construct two opposite changes whose sum is zero, but whose journey was not empty.
3. Write a function that recovers the instruction from a start and destination, then applies it elsewhere.

## 005 — Matrices

1. Show why a lookup table cannot store every possible two-dimensional input.
2. Invent a transformation where each output must depend on both inputs.
3. Implement it first as verbal rules, then coefficients, then a matrix-vector product.

## 006 — Meaning

1. Infer the role of a made-up word from three sentences without defining it.
2. Break the rule “nearby words have similar meaning” using an opposite pair that shares contexts.
3. Design five context observations that distinguish two meanings of “bank.”

## 007 — Embeddings

1. Explain why arbitrary word IDs contain identity but no usable relationship.
2. Place four words by hand in a two-dimensional usage space; state what each direction means.
3. Use one point for “bank” and show the conflicting pressures from river and money contexts.

## 008 — Attention

1. Resolve “The trophy did not fit in the suitcase because it was too large.” Then replace “large” with “small.”
2. Break the strategies “always use the closest noun” and “average every word equally.”
3. Write the retrieval procedure in words without using query, key, value, dot product, or softmax.

## 009 — Softmax

1. Compare winner-take-all on scores `[15, 14.9, 14.8]` and `[15, 0, -10]`.
2. Break division-by-total with negative scores and squaring with a strong negative score.
3. Implement stable softmax by subtracting the maximum. Explain why this does not change relative weights.

## 010 — Query, Key, Value

1. Map a library request to query, catalog entry, and returned content.
2. Construct two objects that are dissimilar but relevant.
3. Hand-compute feature-wise products and their sum for one query against three keys, then mix three values.

## 011 — Multi-head attention

1. Find two relationships in “The keys to the cabinet near the stairs are missing.”
2. Force both relationships through one distribution and describe the compromise.
3. Build two tiny heads with deliberately different projection matrices and inspect their weights.

## 012 — Feed-forward networks

1. Multiply two linear transformations and show that one matrix can replace them.
2. Find two inputs for which a ReLU gate opens different intermediate paths.
3. Instrument the plain-Python FFN to print its candidate features before and after gating.

## 013 — Residual connections

1. Compare the effort required to learn “copy everything” with the effort required to output zero.
2. Apply five small corrections to a state and trace what remains from the start.
3. Remove the residual from the executable block and compare its output on a zero transformation.

## 014 — Layer normalization

1. Predict the normalized patterns of `[1,2,3]` and `[100,200,300]` before calculating.
2. Find the case that makes division by spread impossible and justify epsilon.
3. Verify mean near zero and variance near one for several token vectors.

## 015 — Learning

1. Separate loss, derivative, gradient, and backpropagation using an archery example.
2. Estimate a derivative by nudging one parameter forward and backward.
3. Train a single scalar with the included gradient-descent example; try a step size that is too large.

## 016 — Emergence

1. Give one case where memorization passes and one novel recombination where it fails.
2. Propose a hidden cause that compresses five visible observations.
3. State the strongest claim the footprint analogy supports—and one claim it does not support.
