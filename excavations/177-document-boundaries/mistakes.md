# Mistakes — Excavation 177

## Tempting idea

Join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width.

## Evidence that breaks it

A ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document.

## Requirement carried forward

Mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended.

The wrong idea remains because its failure exposes information the successful design must preserve.
