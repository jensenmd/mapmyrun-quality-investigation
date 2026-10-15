# Portfolio visual system: investigation variant

The portfolio card retains the shared 1200 x 630 canvas, dark background, Arial typography, top accent bar, divider, badges, footer, and generous spacing used by the technical projects. Investigation work uses teal / blue / amber accents and an evidence-oriented illustration instead of numbered implementation stages.

Color reinforces explicit labels: teal marks the reported resilience result, amber marks the workout-integrity question, and blue marks synthesis or an unknown processing boundary. Color alone never communicates status. The accent bar stays at the top across project types.

Supporting figures use the same palette and typography on a 1600 x 900 canvas, with more room for explanations. They are illustrations of the assessment, not original test screenshots or verified system diagrams. The Outside emblem and brand styling are not used. Outside remains named in the origin and product-context text.

## Editable sources and regeneration

The three root SVG files are the editable graphic sources. Root PNGs are their rendered outputs. The PDF text sources are `docs/brief.md` and `docs/assessment.md`. The original filenames remain stable so existing repository links keep working.

Install the optional publishing dependencies with `python -m pip install -r assets/requirements.txt`, then run `python assets/build_publication.py` from the repository root. CairoSVG also needs native Cairo; on Windows, Cairo DLLs may need to be available on PATH. Fonts can differ across systems; the PDFs use the standard Helvetica family.

The builder generates three PNGs and two PDFs. It does not execute field tests or validate their observations. Review the rendered graphics and every PDF page after edits. The publication date is explicitly October 15, 2026; update it deliberately for future revisions.

Do not remove the substantive investigation diagrams merely because they differ in layout from the portfolio card. Their job is to explain the evidence, not duplicate the thumbnail.
