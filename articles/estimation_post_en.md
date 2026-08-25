How wrong can a software estimate be?

The classic cone of uncertainty (Boehm 1981, McConnell 2006) — the honest spread of an estimate against the eventual actual:

- Concept: ×0.25 – ×4
- Business case / RFP / presale: ×0.5 – ×2
- Requirements complete: ×0.67 – ×1.5
- UI design complete: ×0.8 – ×1.25
- Detailed design complete: ~×0.9 – ×1.1

Being off by 2× at RFP stage is not "a bad team" — it is the physics of the stage. And it is exactly the stage where fixed-price contracts usually get signed.

Three things the cone won't tell you:

1. It does not narrow by itself (Little, 2006). Narrowing is bought with questions, prototypes and re-estimation — with work, not with time.
2. The error is asymmetric: average overrun is +30–40% (Moløkken & Jørgensen), and about one project in six is a black swan at ~+200% (Flyvbjerg & Budzier). The right tail is longer.
3. Part of the "error" isn't error at all — it's scope drift: you built a different project than the one you estimated. An estimate without its assumption list is an estimate of nobody knows what.

Operating rules:

- an early estimate is a range, not a point;
- P50 is not a promise: half of all projects exceed the median, by definition;
- make the corridor asymmetric: P90 farther from the center than P10;
- an honest 80% interval must miss about 1 time in 5 — one that never misses is uselessly wide;
- size the tail reserve from similar-project statistics, not "+20% for risks" on top of a WBS;
- keep assumptions and open questions next to the number.

Cheat card in the image.

References:

- Boehm B. Software Engineering Economics. Prentice-Hall, 1981.
- McConnell S. Software Estimation: Demystifying the Black Art. Microsoft Press, 2006.
- Little T. Schedule Estimation and Uncertainty Surrounding the Cone of Uncertainty. IEEE Software 23(3), 2006.
- Moløkken K., Jørgensen M. A Review of Surveys on Software Effort Estimation. ISESE, 2003.
- Flyvbjerg B., Budzier A. Why Your IT Project May Be Riskier Than You Think. Harvard Business Review, September 2011.
