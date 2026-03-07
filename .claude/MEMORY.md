# wan0net.github.io Project Memory

## Architecture
- Hugo static site deployed to GitHub Pages via `.github/workflows/hugo.yaml`
- Custom theme (no external dependencies) — replaced Congo theme in March 2026
- Design system matches link42 platform (Geist fonts, CSS custom properties, light/dark theme)
- Logo: `assets/img/header.png` (geometric shapes — circles, hexagons, triangles)

## Content Structure
- `content/about/index.md` — bio + presentations with embedded PDFs, YouTube, podcasts
- `content/stack/index.md` — tech gear list
- `content/posts/` — blog posts as page bundles (each in dated folder with images)
- Blog posts use `layout: "post"`, static pages use `layout: "page"`

## Notion Sync
- `_scripts/notion_sync.py` — pulls from Notion API, converts to Hugo markdown
- `.github/workflows/notion-sync.yml` — runs every 6 hours or manual trigger
- Requires GitHub secrets: `NOTION_TOKEN`, `NOTION_BLOG_DB_ID`, `NOTION_PAGES`, `PAT_TOKEN`
- PAT_TOKEN needed so pushes trigger the Hugo deploy workflow

## Key Config
- `config/_default/params.toml` — author data with social links
- `config/_default/module.toml` — no external modules
- Markup: goldmark with unsafe HTML enabled, code highlighting without classes
