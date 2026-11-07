"""Update data/publications.json from a Zotero collection.

Fetches the top-level items of one Zotero collection as CSL-JSON through the
Zotero web API and writes them to data/publications.json, sorted newest first.
Uses only the Python standard library.

Configuration (environment variables):
  ZOTERO_LIBRARY_TYPE    "user" or "group" (default: "user")
  ZOTERO_LIBRARY_ID      Numeric user or group ID
  ZOTERO_COLLECTION_KEY  Collection key, e.g. "ABCD1234"
  ZOTERO_API_KEY         Read-only API key (only needed if the library is private)

PDF and software links go in each item's Extra field as lines such as
"PDF: https://..." and "Software: https://..."; Zotero exports them as the
CSL "note" field, which the Publications page reads.
"""

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.zotero.org"
PAGE_SIZE = 100
OUTPUT = Path(__file__).resolve().parent.parent / "data" / "publications.json"


def fetch_items(library_type, library_id, collection_key, api_key):
    headers = {"Zotero-API-Version": "3"}
    if api_key:
        headers["Zotero-API-Key"] = api_key

    items = []
    start = 0
    while True:
        url = (
            f"{API}/{library_type}s/{library_id}/collections/{collection_key}"
            f"/items/top?format=csljson&limit={PAGE_SIZE}&start={start}"
        )
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                total = int(response.headers.get("Total-Results", "0"))
                page = json.load(response)["items"]
        except urllib.error.HTTPError as error:
            if error.code == 403:
                sys.exit(
                    "Zotero returned 403 Forbidden: the library is not public. "
                    "Set ZOTERO_API_KEY to a key with read access."
                )
            if error.code == 404:
                sys.exit(
                    "Zotero returned 404 Not Found: check ZOTERO_LIBRARY_TYPE, "
                    "ZOTERO_LIBRARY_ID and ZOTERO_COLLECTION_KEY."
                )
            raise
        items.extend(page)
        start += PAGE_SIZE
        if not page or start >= total:
            return items


def sort_key(item):
    parts = (item.get("issued", {}).get("date-parts") or [[0]])[0]
    year, month, day = (list(map(int, parts)) + [0, 0, 0])[:3]
    return (-year, -month, -day, item.get("title", "").lower())


def main():
    library_type = os.environ.get("ZOTERO_LIBRARY_TYPE") or "user"
    library_id = os.environ.get("ZOTERO_LIBRARY_ID")
    collection_key = os.environ.get("ZOTERO_COLLECTION_KEY")
    api_key = os.environ.get("ZOTERO_API_KEY") or None

    if library_type not in ("user", "group"):
        sys.exit('ZOTERO_LIBRARY_TYPE must be "user" or "group".')
    if not library_id or not collection_key:
        sys.exit("Set ZOTERO_LIBRARY_ID and ZOTERO_COLLECTION_KEY.")

    items = fetch_items(library_type, library_id, collection_key, api_key)

    # Guard against wiping the publications list if something goes wrong.
    if not items:
        sys.exit("The Zotero collection returned no items; not updating the file.")

    items.sort(key=sort_key)
    OUTPUT.write_text(
        json.dumps(items, indent="\t", ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Wrote {len(items)} publications to data/publications.json")


if __name__ == "__main__":
    main()
