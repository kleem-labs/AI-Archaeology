# Mistakes — 046

## First idea

Count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

## Counterexample

Use the held-out sentence “the tiger sleeps.” Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token.

## Repair

Score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.
