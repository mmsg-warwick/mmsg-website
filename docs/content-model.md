# Content model

Where the content of each page comes from. Pages are Markdown files in [content/](../content/); lists of similar items (publications, software, positions) are data files in [data/](../data/) that templates in [layouts/](../layouts/) turn into pages.

| Page          | Text                                                                     | Generated from                                                                    | Template                                                                    | Guide                                             |
| ------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------- |
| Home          | [content/_index.md](../content/_index.md) (`description` = tagline)      | Latest 5 publications (the three section cards are written in the template)     | [layouts/index.html](../layouts/index.html)                                 | —                                                 |
| Research      | [content/research/_index.md](../content/research/_index.md)              | Theme folders in `content/research/`                                              | [layouts/research/](../layouts/research/), [layouts/_shortcodes/](../layouts/_shortcodes/) | [editing-research.md](editing-research.md)        |
| Theme pages   | `content/research/<theme>/index.md`                                      | `highlights` DOIs → publications; `themes` in software                            | [layouts/research/single.html](../layouts/research/single.html)             | [editing-research.md](editing-research.md)        |
| Team          | [content/team/_index.md](../content/team/_index.md)                      | Person folders in `content/team/`                                                 | [layouts/team/](../layouts/team/)                                           | [adding-people.md](adding-people.md)              |
| Publications  | [content/publications/_index.md](../content/publications/_index.md)      | [data/publications.json](../data/publications.json) (from Zotero)                 | [layouts/publications/list.html](../layouts/publications/list.html)         | [adding-publications.md](adding-publications.md)  |
| Software      | [content/software/_index.md](../content/software/_index.md)              | [data/software.yaml](../data/software.yaml)                                       | [layouts/software/list.html](../layouts/software/list.html)                 | [adding-software.md](adding-software.md)          |
| Opportunities | [content/opportunities.md](../content/opportunities.md)                  | [data/opportunities.yaml](../data/opportunities.yaml)                             | [layouts/opportunities.html](../layouts/opportunities.html)                 | [adding-opportunities.md](adding-opportunities.md) |
| News          | [content/news/_index.md](../content/news/_index.md)                      | —                                                                                 | Blowfish default                                                            | Not in use (hidden from the menu)                 |

## Navigation menu

The menu at the top of every page is set in [hugo.toml](../hugo.toml) under `[[menus.main]]`; `weight` sets the order. The News entry is commented out there.

## Footer and logos

The footer, including the Warwick and Faraday Institution logos, is in [layouts/partials/footer.html](../layouts/partials/footer.html); the logo files are in [static/img/logos/](../static/img/logos/), with light and dark versions.

## Front matter

Every Markdown page starts with a block of settings between `---` lines (the *front matter*), followed by the page text. Fields common to all pages:

| Field     | Meaning                                                    |
| --------- | ---------------------------------------------------------- |
| `title`   | Page title                                                 |
| `draft`   | If `true`, the page is only shown with `hugo server -D`    |
| `weight`  | Ordering within a list (lower first)                       |

Settings that apply to a whole section (e.g. hiding the date and reading time on all team pages) are set once under `cascade:` in that section's `_index.md`.
