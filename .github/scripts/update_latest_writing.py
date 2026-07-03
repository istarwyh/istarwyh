#!/usr/bin/env python3
"""Update the latest technical writing section in README.md."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request
from urllib.request import urlopen


INDEX_URL = "https://xiaohui.cool/agent/search-index.json"
README = Path("README.md")
START = "<!-- LATEST-WRITING:START -->"
END = "<!-- LATEST-WRITING:END -->"
MAX_ITEMS = 5

TECH_PATHS = (
    "/program/llm/",
    "/program/practices/",
    "/program/bot/",
    "/program/full-stream/",
)


def parse_date(value: str | None) -> datetime:
    if not value:
        return datetime.min.replace(tzinfo=timezone.utc)
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return datetime.min.replace(tzinfo=timezone.utc)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def page_date(page: dict) -> datetime:
    dates = page.get("dates", {})
    return max(
        parse_date(dates.get("modified")),
        parse_date(dates.get("default")),
        parse_date(dates.get("published")),
        parse_date(dates.get("created")),
    )


def is_technical_page(page: dict) -> bool:
    url = page.get("url", "")
    if "/en/" in url:
        return False
    return any(path in url for path in TECH_PATHS)


def latest_items() -> list[str]:
    request = Request(
        INDEX_URL,
        headers={
            "Accept": "application/json",
            "User-Agent": "istarwyh-profile-readme-updater/1.0",
        },
    )
    with urlopen(request, timeout=30) as response:
        data = json.load(response)

    pages = [page for page in data.get("pages", []) if is_technical_page(page)]
    pages.sort(key=page_date, reverse=True)

    lines = []
    seen_urls = set()
    for page in pages:
        title = page.get("title", "").strip()
        url = page.get("url", "").strip()
        if not title or not url or url in seen_urls:
            continue
        seen_urls.add(url)
        lines.append(f"- [{title}]({url})")
        if len(lines) == MAX_ITEMS:
            break
    return lines


def replace_section(readme: str, lines: list[str]) -> str:
    if START not in readme or END not in readme:
        raise RuntimeError("README.md is missing latest writing markers")
    before, rest = readme.split(START, 1)
    _, after = rest.split(END, 1)
    body = "\n" + "\n".join(lines) + "\n"
    return before + START + body + END + after


def main() -> None:
    readme = README.read_text(encoding="utf-8")
    updated = replace_section(readme, latest_items())
    README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
