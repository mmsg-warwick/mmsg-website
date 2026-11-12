# Software

The [Software page](https://www.brosaplanella.xyz/software/) lists the tools the group develops or contributes to. Each tool is one entry in [data/software.yaml](../data/software.yaml), and tools are shown in the order they appear in that file. The introduction above the list is in [content/software/_index.md](../content/software/_index.md).

## Adding a tool

1. **Add the logo (optional).** Put a square logo in [static/img/software/](../static/img/software/), named after the tool in lower case, e.g. `static/img/software/mytool.svg`. SVG is best; otherwise use a PNG of at least 128 × 128 pixels with a transparent background. If the logo is hard to see on a dark background, add a second version for dark mode (e.g. `mytool-dark.svg`). Without a logo a generic code icon is shown.
2. **Add an entry** to [data/software.yaml](../data/software.yaml), in the position where it should appear:

   ```yaml
   - name: "MyTool"
     themes: ["thermal-energy-storage"]
     tagline: "One line saying what the tool is"
     description: "Two or three sentences on what it does, who it is for, and how the group is involved (e.g. we lead its development, or members contribute to it)."
     logo: "img/software/mytool.svg"
     logo_dark: "img/software/mytool-dark.svg"
     links:
       website: "https://mytool.org"
       github: "https://github.com/mmsg-warwick/MyTool"
       docs: "https://mytool.readthedocs.io"
       paper: "https://doi.org/10.21105/joss.00000"
   ```

3. **Preview** with `hugo server` and check the Software page in both light and dark mode (with the site's light/dark toggle), and the research theme pages it is tagged with.
4. **Open a pull request** (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

## Fields

| Field         | Required | Description                                                                                                                                                         |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | Yes      | Name of the tool. Also used for the link anchor, e.g. `/software/#mytool`, so changing it breaks existing links to the tool.                                        |
| `tagline`     | Yes      | One line saying what the tool is.                                                                                                                                   |
| `description` | Yes      | Two or three sentences. Markdown is allowed (e.g. `[link](https://...)`, `*italics*`).                                                                              |
| `logo`        | No       | Path to the logo **relative to `static/`**, i.e. starting with `img/`, not `static/img/` or `/img/`.                                                                |
| `logo_dark`   | No       | Version of the logo for dark mode, if `logo` does not work on a dark background.                                                                                     |
| `links`       | No       | Any of `website`, `github`, `docs`, `paper`, as full URLs. Each becomes a button, always in that order. Leave out the ones that do not apply. Other keys are ignored. |
| `themes`      | No       | Research themes the tool is listed under, given as folder names in [content/research/](../content/research/), e.g. `electrochemical-energy-storage`, `thermal-energy-storage`. |

## Tips

- YAML is sensitive to indentation: use two spaces, never tabs, and keep each entry starting with `- name:` at the left margin. Put text in double quotes; if the text itself contains a double quote, write it as `\"`.
- The tool links to the research themes only through `themes`. A theme folder name that does not exist is ignored without warning, so check the theme page in the preview.
- To link a specific paper to its software, use the `Software:` line in Zotero instead (see [adding-publications.md](adding-publications.md#adding-pdf-and-software-links)).

## Removing a tool

Delete its entry from [data/software.yaml](../data/software.yaml) and, if no longer used, its logo from `static/img/software/`.
