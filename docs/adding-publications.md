# Publications

The publication list is managed in **Zotero**, not in this repository. Once a week a GitHub Action downloads the list from Zotero and opens a pull request; merging that pull request updates the website.

```text
Zotero collection ──(weekly GitHub Action)──▶ data/publications.json ──(pull request, merge)──▶ website
```

Never edit [data/publications.json](../data/publications.json) by hand: the next update overwrites it.

The list feeds three places on the site:

- the [Publications page](https://www.brosaplanella.xyz/publications/) (all items, grouped by year),
- the five most recent items on the home page,
- the "Selected papers" on each research theme page (see [editing-research.md](editing-research.md)).

## Where the list lives

| Setting          | Value                                                                     |
| ---------------- | ------------------------------------------------------------------------- |
| Zotero library   | Group library **mmsg - public** (ID `6615360`), public with closed membership |
| Collection       | Key `VHPUD96K`                                                            |

To edit it you need to be a member of the Zotero group; ask the group lead to add you.

## Adding a publication

1. In Zotero, add the item to the collection (e.g. with the Zotero Connector from the journal page, or *Add Item by Identifier* with the DOI).
2. Check these fields, since they are what the website shows:

   | Zotero field                         | Used for                                                           |
   | ------------------------------------ | ------------------------------------------------------------------ |
   | Title                                | Title, linked to the DOI                                           |
   | Authors                              | Author list (the home page and theme pages show the first four)    |
   | Publication (journal or book title)  | Venue                                                              |
   | Volume, Pages                        | Shown after the venue                                              |
   | Date                                 | Year heading and sort order. **Required**; see troubleshooting      |
   | DOI                                  | Link on the title, and how theme pages find the paper              |
   | Extra                                | Optional PDF and software links (below)                            |

3. Wait for the next weekly run, or run it now (see [Running the update by hand](#running-the-update-by-hand)).
4. Review and merge the pull request (see [Reviewing the pull request](#reviewing-the-pull-request)).

Only items placed directly in the collection are included: items in sub-collections, and child notes and attachments, are ignored.

### Adding PDF and software links

Each publication can show a **PDF** button (e.g. a link to the open-access version or arXiv) and a **Software** button (e.g. a link to the code used in the paper). Add them to the item's **Extra** field in Zotero, one per line, in exactly this format:

```text
PDF: https://arxiv.org/pdf/2401.01234
Software: https://github.com/mmsg-warwick/some-repo
```

- The prefix must be `PDF: ` or `Software: ` (capital letters as shown, then a colon and a space).
- Use a full URL starting with `https://`.
- Other lines in Extra are ignored by the website, so existing content can stay.

## Updating or removing a publication

- **Update**: edit the item in Zotero. The change is picked up by the next run.
- **Remove**: remove the item from the collection (*Remove Item from Collection…*; it does not need to be deleted from the library). If the paper is listed as a selected paper on a research theme page, remove it there too, or it silently disappears from that page.

## Running the update by hand

1. Go to the repository's **Actions** tab on GitHub and select **Update Publications**.
2. Click **Run workflow** (on branch `main`).
3. After a minute, a pull request called **Update publications from Zotero** appears if anything changed. If nothing changed, no pull request is opened.

If there is already an open update pull request, the run updates it rather than opening a new one.

## Reviewing the pull request

The pull request changes only `data/publications.json`. Before merging:

1. Open the **Netlify deploy preview** from the pull request checks and look at the Publications page.
2. Check that new items appear under the right year, with authors, venue and links, and that nothing has disappeared unexpectedly.
3. Merge. The live site updates a minute or two later.

If something looks wrong, fix it in Zotero and run the workflow again; it updates the same pull request.

## Running the script locally

The update is done by [scripts/update_publications.py](../scripts/update_publications.py), which only needs Python 3:

```bash
ZOTERO_LIBRARY_TYPE=group ZOTERO_LIBRARY_ID=6615360 ZOTERO_COLLECTION_KEY=VHPUD96K \
  python3 scripts/update_publications.py
```

Then run `hugo server` to see the result. This is useful for checking a Zotero change before the weekly run, but normally there is no need to commit the result yourself: let the workflow open the pull request.

## Troubleshooting

| Problem                                              | Cause and fix                                                                                                                                                                                                                          |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A publication appears under the year **0**           | The item has no Date in Zotero. Add one.                                                                                                                                                                                               |
| The title is not a link                              | The item has no DOI in Zotero.                                                                                                                                                                                                         |
| PDF or Software button missing                       | Check the Extra field format above (prefix, capitalisation, space after the colon, one link per line).                                                                                                                                 |
| The workflow fails with *403 Forbidden*              | The Zotero library is no longer public. Make it public again, or create a read-only Zotero API key and store it as the repository secret `ZOTERO_API_KEY`.                                                                             |
| The workflow fails with *404* or "no items"          | The library ID or collection key is wrong, or the collection is empty. They are stored as repository variables (**Settings → Secrets and variables → Actions → Variables**): `ZOTERO_LIBRARY_TYPE`, `ZOTERO_LIBRARY_ID`, `ZOTERO_COLLECTION_KEY`. The script refuses to write an empty list, so the site is never wiped. |
| The workflow fails when creating the pull request    | GitHub Actions must be allowed to create pull requests: **Settings → Actions → General → Allow GitHub Actions to create and approve pull requests**, enabled for both the `mmsg-warwick` organisation and the repository.               |
