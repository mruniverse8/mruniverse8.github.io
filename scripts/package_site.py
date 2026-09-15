"""Create a static-site ZIP using an explicit list of publishable files."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from build_nvim import build

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "index.html",
    "experience.html",
    "research.html",
    "projects.html",
    "teaching.html",
    "competitive-programming.html",
    "index_small.html",
    "index_nvim.html",
    "experience_nvim.html",
    "research_nvim.html",
    "projects_nvim.html",
    "teaching_nvim.html",
    "competitive-programming_nvim.html",
    "404.html",
    "robots.txt",
    ".nojekyll",
    "assets/css/small.css",
    "assets/css/nvim.css",
    "assets/js/nvim-theme.js",
    "assets/images/favicon.svg",
    "assets/docs/ronaldo-franco-industry-cv.pdf",
    "assets/docs/ronaldo-franco-academic-cv.pdf",
)


def main():
    build()
    missing = [name for name in FILES if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit(f"Missing site files: {', '.join(missing)}")
    destination = ROOT / "dist" / "portfolio.zip"
    destination.parent.mkdir(exist_ok=True)
    with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
        for name in FILES:
            archive.write(ROOT / name, name)
    print(f"Packaged {len(FILES)} files: {destination}")


if __name__ == "__main__":
    main()
