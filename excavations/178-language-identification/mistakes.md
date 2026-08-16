# Mistakes — Excavation 178

## Tempting idea

Keep documents containing mostly familiar latin characters and discard the rest.

## Evidence that breaks it

Spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language.

## Requirement carried forward

Use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label.

The wrong idea remains because its failure exposes information the successful design must preserve.
