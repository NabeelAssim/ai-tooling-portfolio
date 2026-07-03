# Task 2: LinkedIn Organic Content Strategy Research (B2B SaaS)

This folder documents research into LinkedIn organic content strategy experts relevant to B2B SaaS, completed as part of a portfolio task. The goal was to identify practitioners whose methodology is backed by verifiable outcomes — not just follower count — and build a structured, sourced repository of their content and commentary.

## Structure

- **`linkedin-posts/`** — Collected LinkedIn posts per expert, used to study format, hooks, and content patterns.
- **`youtube-transcripts/`** — Transcripts of videos/podcast appearances per expert, fetched via `get_transcript.py`.
- **`get_transcript.py`** — Script used to pull transcripts from YouTube via the Supadata API, given a video URL, expert name, and title. Organizes output into per-expert folders automatically.
- **`sources.md`** — Full source list with links to each expert's LinkedIn, YouTube, podcasts, newsletter, and website, plus selection rationale.

## Selection Criteria

Experts were chosen for **verifiable, outcome-tied methodology** over audience size — people who document how their LinkedIn strategy produced measurable results (pipeline, revenue, ARR growth, engagement data) rather than general commentary on "how to grow on LinkedIn."

## Experts Researched

| # | Expert | Known For |
|---|--------|-----------|
| 1 | [Lara Acosta](https://www.linkedin.com/in/laraacostar/) | Fastest-growing female B2B LinkedIn creator; documents her own growth system with real metrics |
| 2 | [Richard van der Blom](https://www.linkedin.com/in/richardvanderblom/) | Publishes the annual Algorithm InSights Report — data-driven LinkedIn algorithm research |
| 3 | [Jasmin Alic](https://www.linkedin.com/in/alicjasmin/) | 17 years of LinkedIn content experience; coached Lara Acosta |
| 4 | [Samantha McKenna](https://www.linkedin.com/in/samsalesli/) | Founder of #samsales Consulting; ties content directly to B2B pipeline and revenue |
| 5 | [Chris Orlob](https://www.linkedin.com/in/chrisorlob/) | Former VP Sales at Gong; LinkedIn content tied to enterprise pipeline generation |
| 6 | [Matt Lakajev](https://www.linkedin.com/in/mattlakajev/) | Documents LinkedIn lead generation with conversion data ($3.5M without going viral) |
| 7 | [Josh Braun](https://www.linkedin.com/in/josh-braun/) | Deconstructs outreach failure/success using real response data |
| 8 | [Obaid Durrani](https://www.linkedin.com/in/obaidbot/) | Scaled a content company from $1.7M to $7.2M ARR using LinkedIn organic |
| 9 | [Amanda Natividad](https://www.linkedin.com/in/amandanat/) | Chief Evangelist at SparkToro; creator of the Zero Click Content framework |
| 10 | [Guillaume Moubeche](https://www.linkedin.com/in/guillaume-moubeche-a026541b2/) | CEO of lemlist; uses LinkedIn organic as a primary SaaS growth channel |

Full details — including podcast appearances, publications, newsletters, and individual selection rationale — are in [`sources.md`](./sources.md).

## Process

1. Identified candidate experts through LinkedIn's own algorithm, referrals between practitioners (e.g. Jasmin Alic coaching Lara Acosta), and cross-referencing podcast/media appearances.
2. Verified each expert's claims against public, checkable outcomes (ARR figures, engagement reports, client results) rather than self-reported growth alone.
3. Collected LinkedIn posts per expert into `linkedin-posts/`.
4. Fetched relevant YouTube/podcast video transcripts per expert into `youtube-transcripts/`, using `get_transcript.py`.
5. Documented sourcing and rationale in `sources.md` for traceability.

See the root [`README.md`](../README.md) for Task 1 (AI tooling environment setup).