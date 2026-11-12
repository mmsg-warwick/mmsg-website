# Team members

Each person has their own folder in [content/team/](../content/team/), containing an `index.md` file and a photo. The Team page is built from these folders automatically: there is no list to update by hand.

```text
content/team/
├── ferran-brosa-planella/
│   ├── index.md
│   └── photo.jpg
└── kawa-manmi/
    ├── index.md
    └── user.png
```

## Adding a team member

1. **Copy the template.** Copy [content/team/example-member/](../content/team/example-member/) to a new folder named after the person, in lower case with hyphens, e.g. `content/team/jane-smith/`. The folder name becomes the page address (`/team/jane-smith/`).
2. **Add a photo.** Put the photo in the same folder (e.g. `photo.jpg`) and delete `user.png`, or keep `user.png` as a placeholder until a photo is available. Use a square image of at least 400 × 400 pixels with the face centred: it is cropped to a circle. Keep the file under about 500 KB.
3. **Fill in `index.md`** (see the fields below) and delete the `draft: true` line.
4. **Preview** with `hugo server` and open the Team page.
5. **Open a pull request** (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

New members can do this themselves; the lead reviews the pull request.

### Front matter fields

The part between the `---` lines at the top of `index.md` is the front matter:

```yaml
---
title: "Jane Smith"          # Full name, as displayed
name: "Jane"                 # First name
surname: "Smith"             # Surname, used to sort people within each group
role: "PhD Student"          # Job title, shown under the name
status: "student"            # Which group the person appears in (see below)
photo: "photo.jpg"           # File name of the photo in this folder

# Profiles: give the username or ID only, not the full URL. Leave "" or delete
# a line if it does not apply; its icon is then not shown.
email: "jane.smith@warwick.ac.uk"   # full address
github: "janesmith"                 # github.com/janesmith
orcid: "0000-0002-1825-0097"        # orcid.org/0000-0002-1825-0097
scholar: "AbCdEfGAAAAJ"             # the user= value in your Google Scholar profile URL
linkedin: "janesmith"               # linkedin.com/in/janesmith
---

Jane is a PhD student working on ...
```

`status` must be one of:

| `status`     | Section on the Team page | Shown as     |
| ------------ | ------------------------ | ------------ |
| `lead`       | Lead                     | Photo card   |
| `researcher` | Researchers              | Photo card   |
| `student`    | Students                 | Photo card   |
| `affiliate`  | Affiliates               | Photo card   |
| `former`     | Former Members           | Name and role only, in a compact list |

Any other value means the person does not appear on the Team page. Within each section people are sorted by `surname`.

The template also has a `bio` field. It is not shown anywhere on the site, so it can be left out.

### Biography

Everything below the second `---` is the biography, shown on the person's own page. It is written in Markdown, so links (`[text](https://...)`), paragraphs and headings work. Write it in the first or third person, as the person prefers, but keep it consistent within a page. A few short paragraphs is enough: current role and research, then previous positions and education.

## When someone leaves

Keep their folder, so that their page and links to it keep working, and edit `index.md`:

1. Change `status` to `"former"`.
2. Update `role` to what they did in the group, e.g. `"PhD Student (2023–2027)"`, since it is shown next to their name in the Former Members list.
3. Optionally, add a line to the biography saying where they went next.

To remove a person from the site completely (e.g. at their request), delete their folder.

## Updating your own details

Edit the fields in your `index.md` or replace your photo (keeping `photo:` in sync with the file name), and open a pull request.
