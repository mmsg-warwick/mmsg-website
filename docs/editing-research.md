# Research

The [Research page](https://www.brosaplanella.xyz/research/) has two parts, both written in [content/research/_index.md](../content/research/_index.md):

- **What we work on**: one card per research theme, generated from the theme folders in [content/research/](../content/research/).
- **How we work**: cards for the methods (mathematical modelling, open-source software), written directly in `_index.md` with the `{{< method >}}` shortcode.

## Editing a research theme

Each theme is a folder with an `index.md` and an image, e.g. [content/research/thermal-energy-storage/](../content/research/thermal-energy-storage/):

```yaml
---
title: "Thermal Energy Storage"
summary: "One sentence, shown on the card on the Research page."
photo: "thermal.png"       # image in this folder, used on the card and the page
weight: 20                 # order of the cards (lower comes first)

highlights:                # "Selected papers" section, in this order
  - doi: "10.1098/rspa.2025.0660"
    note: "Optional sentence shown under the paper."
  - doi: "10.1016/j.ijheatmasstransfer.2024.126533"
---

Two or three paragraphs of overview, in Markdown.
```

The page then shows, in order: the overview, the selected papers, and the software tagged with this theme.

### Selected papers

- Each `doi` must match the DOI of an item in the Zotero collection, i.e. in [data/publications.json](../data/publications.json) (capitalisation does not matter). Write the DOI only, without `https://doi.org/`.
- A DOI that is not found is skipped **without any warning**. After editing, check the theme page in the preview and count the papers. If a paper is missing, add it to Zotero first (see [adding-publications.md](adding-publications.md)).
- Details (title, authors, journal, year) come from Zotero, so they do not need to be repeated here.

### Software

Software is not listed in the theme page itself: tag the tool with the theme's folder name in `themes` in [data/software.yaml](../data/software.yaml) (see [adding-software.md](adding-software.md)).

## Adding a research theme

1. Copy an existing theme folder, e.g. `content/research/thermal-energy-storage/`, to a new folder named after the theme in lower case with hyphens.
2. Replace the image with one for the new theme (landscape, at least 800 × 400 pixels; it is cropped to that ratio on the card) and update `photo`.
3. Edit `title`, `summary`, `weight`, `highlights` and the overview.
4. Tag related tools in [data/software.yaml](../data/software.yaml) with the new folder name.

The card appears on the Research page automatically.

## Hidden pages

[content/research/mathematical-modelling/](../content/research/mathematical-modelling/) and [content/research/scientific-software/](../content/research/scientific-software/) are not built (their front matter contains `build: render: never`), because methods are described under "How we work" instead. They are kept as drafts in case they become themes later; delete the `build:` block to publish one.
