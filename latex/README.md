# Industry CV

## Task CV-1 and scope

The existing industry CV had no editable source in this repository. Its root-level
copy and `assets/docs/ronaldo-franco-industry-cv.pdf` were byte-identical when read
on 2026-10-16. Docker already appeared in the Huawei experience and skills;
Kubernetes did not appear.

Reconstruct that CV in `ronaldo-franco-industry-cv.tex`, preserving its content,
links, section order, serif typography, and one-page A4 format. Add only:

- "Work with Docker and Kubernetes in development workflows." under the current
  freelance role.
- Kubernetes beside Docker in the Software skills row.

Follow-up requirement: use "Machine Learning Engineer" as the headline and
"Machine learning engineer" in the opening description, replacing "Software
Engineer" / "Software engineer". Remove the redundant "Machine Learning"
headline suffix. Keep all experience, skills, and links intact.

Assumption: the user's statement that they work with these tools applies to the
current freelance role. This wording does not assert cluster administration,
scale, certifications, or a measured result. The academic CV and website prose
are outside this task. The supplied root-level PDF remains the original reference.

Use the existing PDF download path so website links keep working. A single `.tex`
file and a small Makefile suffice; a custom class or new build system would add
maintenance without a demonstrated need. Font metrics may differ slightly from
the original XeTeX output; readable content and layout take priority over pixel
identity.

## Acceptance criteria

- **AC-1:** Preserve all original CV text, dates, metrics, and five hyperlink
  targets, apart from whitespace/typographic encoding, the two additions above,
  and the requested headline/opening-description replacements.
- **AC-2:** Include the modest Docker/Kubernetes experience line and skills entry
  without adding other claims.
- **AC-3:** Build a single A4 PDF with selectable text, embedded fonts, no clipped
  or overlapping content, and no LaTeX errors or overfull boxes.
- **AC-4:** Provide a repeatable build in `latex/` and update the industry CV at
  the existing website download path. Preserve the academic and root-level PDFs.

## Build

Requires GNU Make and pdfLaTeX, with `geometry`, `fontenc`, `inputenc`, `lmodern`,
and `hyperref` (standard TeX Live packages). No external fonts, network access, or
shell escape are needed.

From the repository root:

```sh
make -C latex
```

The result is `latex/build/ronaldo-franco-industry-cv.pdf`. After reviewing it,
copy it to the existing website download path with:

```sh
make -C latex install
```

`make -C latex clean` removes only intermediate build files. Failed LaTeX builds
stop before installation; the existing website PDF remains available. Build output
is ignored by Git. The `.tex` source can also be compiled directly with pdfLaTeX
or uploaded to Overleaf using pdfLaTeX.

## Verification (2026-10-16)

- **AC-1 / AC-2 passed:** Poppler text extraction, with Unicode ligatures and
  whitespace normalized, matched the entire original after removing exactly the
  new bullet and Kubernetes skill. All five hyperlink targets matched.
- **AC-3 passed:** `make -C latex` compiled successfully with pdfLaTeX. `pdfinfo`
  reported one A4 page (595.276 x 841.89 pt). All 437 extracted words stayed at
  least 35 pt inside page edges; the final text ended at 792.26 pt. `pdffonts`
  confirmed embedded fonts and Unicode mapping. The final compilation log had no
  warnings, underfull boxes, or overfull boxes. The rendered page was visually
  inspected for spacing, alignment, clipping, and overlap.
- **AC-4 passed:** `make -C latex install` updated the existing website PDF;
  `cmp` confirmed it matched the reviewed build. A second `make -C latex` needed
  no work. A simulated compiler failure in an isolated temporary directory
  stopped installation and preserved the previous download. The original root
  PDF retained its initial SHA-256, and the academic PDF matched its Git version.
- `git diff --check` passed. These checks were completed before committing or
  deploying the changes.

These results describe the initial reconstruction. The follow-up headline and
opening-description update was also built and verified on 2026-10-16: extracted
text differed from the previous website PDF only in those two requested places;
all five links and the Docker/Kubernetes wording were preserved. The result is
one A4 page with 436 words within the same margins, no compilation warnings or
box errors, and a visually inspected layout. Installation succeeded, and `cmp`
confirmed the website PDF matches the reviewed build. All acceptance criteria
are met; no checks are pending.

The editable reconstruction
uses pdfLaTeX rather than the original PDF's XeTeX engine, so small typographic
differences are expected.
