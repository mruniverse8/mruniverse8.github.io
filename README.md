# Ronaldo Franco Jaldin — Portfolio

Static personal website for <https://mruniverse8.github.io/>.

- `index.html`: the default reading presentation.
- `index_nvim.html`: the light Neovim-inspired presentation.
- Both presentations include Experience, Research, Projects, Teaching, and Competitive Programming.
- Downloadable industry and academic CVs are under `assets/docs/`.

## GitHub Pages

In **Settings → Pages**, select **Deploy from a branch**, then **main** and **/ (root)**.
The files are ready to serve; no dependency installation or build is needed.
`.nojekyll` tells GitHub Pages to publish the static files directly.

## Local preview

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open <http://localhost:8000>.

The site uses relative internal links and falls back to system fonts when Google Fonts
is unavailable. The original content and generation scripts are maintained separately;
this repository contains the public website files only.
