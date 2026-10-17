# Technical context

- Static HTML, CSS, and browser JavaScript, published with GitHub Pages.
- Python 3 standard-library scripts generate the Neovim presentation and site ZIP.
- Canonical HTML pages are the source for their generated `*_nvim.html` counterparts.
- CV downloads live in `assets/docs/`; the industry CV source lives in `latex/`.
- The industry CV uses pdfLaTeX with standard TeX Live packages and Latin Modern
  fonts. GNU Make builds it locally; Poppler supports PDF inspection.

See [the repository guide](../README.md) and [CV build instructions](../latex/README.md).
