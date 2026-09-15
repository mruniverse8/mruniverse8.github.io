# Ronaldo Franco Jaldin — Portfolio

A static portfolio with two presentations:

- **[Reading view](https://mruniverse8.github.io/)** — the default, minimal design.
- **[Neovim view](https://mruniverse8.github.io/index_nvim.html)** — Gruvbox Light and Dark,
  monospace typography, file explorer, document tabs, and status line.

Both presentations share the same content. The top bar includes a Dark mode toggle; the bottom bar
also links back to the reading view. The toggle remembers your choice between pages
and visits; without JavaScript, the Neovim view remains readable in its default light theme.

## Repository map

```text
index.html                       Home and contact links
experience.html                  Professional experience
research.html                    Publication and thesis
projects.html                    Five ML projects and PetsADHD
teaching.html                    Courses, mentorship, community
competitive-programming.html     Contest results and training
*_nvim.html                      Generated Neovim versions
index_small.html                 Compatibility redirect to Home
404.html                         Missing-page response
assets/
  css/small.css                  Reading theme
  css/nvim.css                   Gruvbox light/dark themes
  js/nvim-theme.js               Theme switching and saved preference
  docs/                          Downloadable CV PDFs
  images/favicon.svg             Site icon
scripts/
  build_nvim.py                  Generate alternate pages
  package_site.py                Create dist/portfolio.zip
```

`robots.txt` allows indexing. `.nojekyll` tells GitHub Pages to serve the static files
directly. `dist/`, Python caches, and editor backup files are ignored by Git.

## Edit content

1. Edit the six canonical HTML pages listed above. Update their shared navigation together
   when adding or renaming a page.
2. Regenerate the Neovim versions using Python 3 (standard library only):

   ```sh
   python3 scripts/build_nvim.py
   ```

3. Preview locally:

   ```sh
   python3 -m http.server 8000 --bind 127.0.0.1
   ```

4. Check both presentations, mobile widths, links, and CV links (PDFs open in new tabs). Commit the source
   pages and regenerated `*_nvim.html` files together, then push to `main`.

The `_nvim.html` files are generated: edit their canonical counterparts instead.
Theme-specific layout and colors live in the two CSS files. The terminal view uses
Menlo, then JetBrains Mono and system monospace fallbacks; the reading view uses
Newsreader and IBM Plex. External font loading is optional.

## GitHub Pages

Publishing source: **Settings → Pages → Deploy from a branch → main → / (root)**.
Pushing to `main` starts GitHub's Pages build and deployment. No package installation,
JavaScript bundler, or custom workflow is needed. Review deployments in the repository's
**Actions** tab.

## Static-site ZIP

```sh
python3 scripts/package_site.py
```

This regenerates the Neovim pages and packages only the deployable HTML, stylesheets,
theme script, favicon, CV PDFs, `robots.txt`, and `.nojekyll` into `dist/portfolio.zip`.
The archive excludes scripts, documentation, and Git history.

CV source files and the recovered ML repositories are maintained outside this public
website repository. [PetsADHD](https://github.com/mruniverse8/PetsADHD) is linked from
Home and Projects as a separate project.
