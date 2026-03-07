#!/usr/bin/env python3
"""
Notion -> Hugo sync script.

Pulls blog posts from a Notion database and standalone pages from Notion,
converts them to Hugo-compatible markdown with front matter, downloads images,
and writes them to the content directory.

Environment variables:
  NOTION_TOKEN        - Notion integration token
  NOTION_BLOG_DB_ID   - Data source ID for blog posts database
  NOTION_PAGES        - JSON mapping of content paths to Notion page IDs
                        e.g. {"about": "page-id", "stack": "page-id"}
"""

import json
import os
import re
import sys
import hashlib
import urllib.parse
from datetime import datetime
from pathlib import Path

import requests
from notion_client import Client

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")
BLOG_DB_ID = os.environ.get("NOTION_BLOG_DB_ID", "")
PAGES_JSON = os.environ.get("NOTION_PAGES", "{}")


def get_client():
    if not NOTION_TOKEN:
        print("ERROR: NOTION_TOKEN not set")
        sys.exit(1)
    return Client(auth=NOTION_TOKEN)


# ── Rich text to markdown ──


def rich_text_to_md(rich_texts):
    """Convert Notion rich_text array to markdown string."""
    parts = []
    for rt in rich_texts:
        text = rt.get("plain_text", "")
        annotations = rt.get("annotations", {})
        href = rt.get("href")

        if annotations.get("code"):
            text = f"`{text}`"
        if annotations.get("bold"):
            text = f"**{text}**"
        if annotations.get("italic"):
            text = f"*{text}*"
        if annotations.get("strikethrough"):
            text = f"~~{text}~~"
        if annotations.get("underline"):
            text = f"<u>{text}</u>"
        if href:
            text = f"[{text}]({href})"

        parts.append(text)
    return "".join(parts)


# ── Block to markdown ──


def download_image(url, page_dir):
    """Download an image and return the local filename."""
    try:
        parsed = urllib.parse.urlparse(url)
        # Create a stable filename from the URL hash
        url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
        ext = Path(parsed.path).suffix or ".png"
        if ext not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"):
            ext = ".png"
        filename = f"img-{url_hash}{ext}"

        filepath = page_dir / filename
        if filepath.exists():
            return filename

        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        filepath.write_bytes(resp.content)
        return filename
    except Exception as e:
        print(f"  WARNING: Failed to download image {url}: {e}")
        return None


def download_file(url, page_dir, original_name="file"):
    """Download a file (PDF, etc.) and return the local filename."""
    try:
        parsed = urllib.parse.urlparse(url)
        ext = Path(parsed.path).suffix or ""
        # Use original name if possible, otherwise hash
        safe_name = re.sub(r'[^\w\-.]', '_', original_name)
        if not safe_name.endswith(ext):
            safe_name += ext
        filepath = page_dir / safe_name
        if filepath.exists():
            return safe_name

        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        filepath.write_bytes(resp.content)
        return safe_name
    except Exception as e:
        print(f"  WARNING: Failed to download file {url}: {e}")
        return None


def blocks_to_markdown(notion, block_id, page_dir, depth=0):
    """Recursively convert Notion blocks to markdown."""
    lines = []
    blocks = []

    # Paginate through all blocks
    cursor = None
    while True:
        kwargs = {"block_id": block_id, "page_size": 100}
        if cursor:
            kwargs["start_cursor"] = cursor
        resp = notion.blocks.children.list(**kwargs)
        blocks.extend(resp["results"])
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")

    numbered_counter = 0

    for block in blocks:
        btype = block["type"]
        bdata = block.get(btype, {})

        # Reset numbered list counter when we leave a numbered list
        if btype != "numbered_list_item":
            numbered_counter = 0

        if btype == "paragraph":
            text = rich_text_to_md(bdata.get("rich_text", []))
            lines.append(text)
            lines.append("")

        elif btype in ("heading_1", "heading_2", "heading_3"):
            level = int(btype[-1])
            text = rich_text_to_md(bdata.get("rich_text", []))
            lines.append(f"{'#' * level} {text}")
            lines.append("")

        elif btype == "bulleted_list_item":
            text = rich_text_to_md(bdata.get("rich_text", []))
            indent = "  " * depth
            lines.append(f"{indent}- {text}")
            if block.get("has_children"):
                child_md = blocks_to_markdown(notion, block["id"], page_dir, depth + 1)
                lines.append(child_md)

        elif btype == "numbered_list_item":
            numbered_counter += 1
            text = rich_text_to_md(bdata.get("rich_text", []))
            indent = "  " * depth
            lines.append(f"{indent}{numbered_counter}. {text}")
            if block.get("has_children"):
                child_md = blocks_to_markdown(notion, block["id"], page_dir, depth + 1)
                lines.append(child_md)

        elif btype == "to_do":
            text = rich_text_to_md(bdata.get("rich_text", []))
            checked = "x" if bdata.get("checked") else " "
            lines.append(f"- [{checked}] {text}")

        elif btype == "toggle":
            text = rich_text_to_md(bdata.get("rich_text", []))
            lines.append(f"**{text}**")
            lines.append("")
            if block.get("has_children"):
                child_md = blocks_to_markdown(notion, block["id"], page_dir, depth)
                lines.append(child_md)

        elif btype == "code":
            text = rich_text_to_md(bdata.get("rich_text", []))
            lang = bdata.get("language", "")
            lines.append(f"```{lang}")
            lines.append(text)
            lines.append("```")
            lines.append("")

        elif btype == "quote":
            text = rich_text_to_md(bdata.get("rich_text", []))
            for line in text.split("\n"):
                lines.append(f"> {line}")
            lines.append("")

        elif btype == "callout":
            icon = bdata.get("icon") or {}
            emoji = icon.get("emoji", "") if icon.get("type") == "emoji" else ""
            text = rich_text_to_md(bdata.get("rich_text", []))
            # Special pill rendering for tagged callouts
            if emoji == "🤖" and text.strip().lower().startswith("ai generated"):
                lines.append('<span class="pill pill-ai">🤖 AI Generated</span>')
            else:
                lines.append(f"> {emoji} {text}")
            lines.append("")

        elif btype == "divider":
            lines.append("---")
            lines.append("")

        elif btype == "image":
            img_data = bdata
            img_type = img_data.get("type", "")
            caption = rich_text_to_md(img_data.get("caption", []))

            url = ""
            if img_type == "file":
                url = img_data.get("file", {}).get("url", "")
            elif img_type == "external":
                url = img_data.get("external", {}).get("url", "")

            if url:
                local_name = download_image(url, page_dir)
                if local_name:
                    if caption:
                        lines.append(f"![{caption}]({local_name})")
                    else:
                        lines.append(f"![]({local_name})")
                else:
                    lines.append(f"![{caption}]({url})")
            lines.append("")

        elif btype == "video":
            vid_type = bdata.get("type", "")
            url = ""
            if vid_type == "external":
                url = bdata.get("external", {}).get("url", "")
            elif vid_type == "file":
                url = bdata.get("file", {}).get("url", "")

            # Detect YouTube
            yt_match = re.search(
                r'(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)', url
            )
            if yt_match:
                lines.append(f'{{{{< youtube {yt_match.group(1)} >}}}}')
            else:
                lines.append(f"[Video]({url})")
            lines.append("")

        elif btype == "embed":
            url = bdata.get("url", "")
            # YouTube embed
            yt_match = re.search(
                r'(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)', url
            )
            if yt_match:
                lines.append(f'{{{{< youtube {yt_match.group(1)} >}}}}')
            else:
                # Generic embed as iframe
                lines.append(
                    f'<iframe src="{url}" width="100%" height="400" '
                    f'frameborder="0" loading="lazy"></iframe>'
                )
            lines.append("")

        elif btype == "bookmark":
            url = bdata.get("url", "")
            caption = rich_text_to_md(bdata.get("caption", []))
            if caption:
                lines.append(f"[{caption}]({url})")
            else:
                lines.append(f"[{url}]({url})")
            lines.append("")

        elif btype == "file" or btype == "pdf":
            file_data = bdata
            file_type = file_data.get("type", "")
            url = ""
            name = file_data.get("name", "file")
            if file_type == "file":
                url = file_data.get("file", {}).get("url", "")
            elif file_type == "external":
                url = file_data.get("external", {}).get("url", "")
            caption = rich_text_to_md(file_data.get("caption", []))

            if url:
                local_name = download_file(url, page_dir, name)
                if local_name and local_name.endswith(".pdf"):
                    lines.append(f'{{{{< embed-pdf url="{local_name}" >}}}}')
                elif local_name:
                    lines.append(f"[{caption or local_name}]({local_name})")
                else:
                    lines.append(f"[{caption or name}]({url})")
            lines.append("")

        elif btype == "table":
            if block.get("has_children"):
                table_rows = []
                row_cursor = None
                while True:
                    kwargs = {"block_id": block["id"], "page_size": 100}
                    if row_cursor:
                        kwargs["start_cursor"] = row_cursor
                    row_resp = notion.blocks.children.list(**kwargs)
                    table_rows.extend(row_resp["results"])
                    if not row_resp.get("has_more"):
                        break
                    row_cursor = row_resp.get("next_cursor")

                for i, row in enumerate(table_rows):
                    cells = row.get("table_row", {}).get("cells", [])
                    row_text = " | ".join(
                        rich_text_to_md(cell) for cell in cells
                    )
                    lines.append(f"| {row_text} |")
                    if i == 0:
                        sep = " | ".join("---" for _ in cells)
                        lines.append(f"| {sep} |")
                lines.append("")

        elif btype == "column_list":
            if block.get("has_children"):
                child_md = blocks_to_markdown(
                    notion, block["id"], page_dir, depth
                )
                lines.append(child_md)

        elif btype == "column":
            if block.get("has_children"):
                child_md = blocks_to_markdown(
                    notion, block["id"], page_dir, depth
                )
                lines.append(child_md)

        elif btype == "child_page":
            title = bdata.get("title", "")
            lines.append(f"**{title}**")
            lines.append("")

        elif btype == "child_database":
            title = bdata.get("title", "")
            lines.append(f"*Database: {title}*")
            lines.append("")

        else:
            # Unknown block type — skip with a comment
            lines.append(f"<!-- unsupported block: {btype} -->")
            lines.append("")

    return "\n".join(lines)


# ── Sync blog posts from database ──


def sync_blog_posts(notion):
    """Sync all pages from the blog database."""
    if not BLOG_DB_ID:
        print("NOTION_BLOG_DB_ID not set, skipping blog sync")
        return

    print(f"Syncing blog posts from database {BLOG_DB_ID}...")

    # Query all pages in the database via REST API
    pages = []
    cursor = None
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }
    while True:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        resp = requests.post(
            f"https://api.notion.com/v1/databases/{BLOG_DB_ID}/query",
            headers=headers,
            json=body,
        )
        resp.raise_for_status()
        data = resp.json()
        pages.extend(data["results"])
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")

    print(f"  Found {len(pages)} blog posts")

    for page in pages:
        props = page["properties"]
        page_id = page["id"]

        # Extract properties
        title = ""
        title_prop = props.get("Title") or props.get("Name") or props.get("title")
        if title_prop:
            title_items = title_prop.get("title", [])
            title = rich_text_to_md(title_items)

        if not title:
            print(f"  Skipping page {page_id} — no title")
            continue

        # Slug
        slug = ""
        slug_prop = props.get("Slug") or props.get("slug")
        if slug_prop and slug_prop.get("rich_text"):
            slug = rich_text_to_md(slug_prop["rich_text"]).strip()
        if not slug:
            slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

        # Date
        date_str = ""
        date_prop = props.get("Date") or props.get("date")
        if date_prop and date_prop.get("date"):
            date_str = date_prop["date"].get("start", "")
        if not date_str:
            date_str = page.get("created_time", "")[:10]

        # Description
        desc = ""
        desc_prop = props.get("Description") or props.get("description")
        if desc_prop and desc_prop.get("rich_text"):
            desc = rich_text_to_md(desc_prop["rich_text"]).strip()

        # Categories
        categories = []
        cat_prop = props.get("Categories") or props.get("categories") or props.get("Tags") or props.get("tags")
        if cat_prop and cat_prop.get("multi_select"):
            categories = [opt["name"] for opt in cat_prop["multi_select"]]

        # Draft
        draft = False
        draft_prop = props.get("Draft") or props.get("draft")
        if draft_prop and draft_prop.get("type") == "checkbox":
            draft = draft_prop.get("checkbox", False)

        # Cover/preview image — use the Notion page cover
        cover_url = ""
        if page.get("cover"):
            cover = page["cover"]
            if cover.get("type") == "file":
                cover_url = cover.get("file", {}).get("url", "")
            elif cover.get("type") == "external":
                cover_url = cover.get("external", {}).get("url", "")

        print(f"  Syncing: {title} ({slug})")

        # Create content directory (date-prefixed for organization)
        post_dir = CONTENT_DIR / "posts" / f"{date_str}-{slug}"
        post_dir.mkdir(parents=True, exist_ok=True)

        # Download cover image
        cover_filename = ""
        if cover_url:
            cover_filename = download_image(cover_url, post_dir)

        # Convert blocks to markdown
        md_content = blocks_to_markdown(notion, page_id, post_dir)

        # Build front matter
        fm_lines = [
            "---",
            f'title: "{title}"',
            f"date: {date_str}",
        ]
        if desc:
            fm_lines.append(f'description: "{desc}"')
        fm_lines.append(f"draft: {str(draft).lower()}")
        fm_lines.append('layout: "post"')
        if slug:
            fm_lines.append(f'slug: "{slug}"')
        if categories:
            cats = ", ".join(f'"{c}"' for c in categories)
            fm_lines.append(f"categories: [{cats}]")
        if cover_filename:
            fm_lines.append(f"preview: {cover_filename}")
            fm_lines.append(f"feature: {cover_filename}")
        fm_lines.append("---")

        front_matter = "\n".join(fm_lines)
        full_content = f"{front_matter}\n\n{md_content}"

        # Write the file
        index_file = post_dir / "index.md"
        index_file.write_text(full_content, encoding="utf-8")
        print(f"    -> {index_file.relative_to(CONTENT_DIR.parent)}")


# ── Sync standalone pages ──


def sync_pages(notion):
    """Sync standalone Notion pages to Hugo content directories."""
    try:
        pages_map = json.loads(PAGES_JSON)
    except json.JSONDecodeError:
        print("WARNING: NOTION_PAGES is not valid JSON, skipping page sync")
        return

    if not pages_map:
        print("No standalone pages configured, skipping page sync")
        return

    print(f"Syncing {len(pages_map)} standalone pages...")

    for content_path, page_id in pages_map.items():
        print(f"  Syncing page: {content_path} ({page_id})")

        # Get page metadata
        page = notion.pages.retrieve(page_id=page_id)
        props = page.get("properties", {})

        title = content_path
        title_prop = props.get("title") or props.get("Title") or props.get("Name")
        if title_prop:
            title_items = title_prop.get("title", [])
            if title_items:
                title = rich_text_to_md(title_items)

        # Create content directory
        page_dir = CONTENT_DIR / content_path
        page_dir.mkdir(parents=True, exist_ok=True)

        # Convert blocks to markdown
        md_content = blocks_to_markdown(notion, page_id, page_dir)

        # Build front matter
        front_matter = "\n".join([
            "---",
            f'title: "{title}"',
            f"date: {datetime.now().strftime('%Y-%m-%d')}",
            'draft: false',
            'layout: "page"',
            "showAuthor: false",
            "showBreadcrumbs: false",
            "showDate: false",
            "showDateUpdated: false",
            "showTableOfContents: true",
            "showPagination: false",
            "showReadingTime: false",
            "---",
        ])

        full_content = f"{front_matter}\n\n{md_content}"

        index_file = page_dir / "index.md"
        index_file.write_text(full_content, encoding="utf-8")
        print(f"    -> {index_file.relative_to(CONTENT_DIR.parent)}")


# ── Main ──


def main():
    print("=== Notion -> Hugo Sync ===")
    print(f"Content directory: {CONTENT_DIR}")

    notion = get_client()

    sync_blog_posts(notion)
    sync_pages(notion)

    print("\nSync complete!")


if __name__ == "__main__":
    main()
