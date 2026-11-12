# Opportunities

Open positions are listed in [data/opportunities.yaml](../data/opportunities.yaml) and shown on the [Opportunities page](https://www.brosaplanella.xyz/opportunities/), under the section for their category. The surrounding text (what each kind of position involves, how to get in touch) is in [content/opportunities.md](../content/opportunities.md).

## Adding a position

Add an entry to [data/opportunities.yaml](../data/opportunities.yaml). If the file contains only `[]` (no positions), replace that line with the entry:

```yaml
- title: "Funded PhD studentship in battery modelling"
  category: phd
  url: "https://warwick.ac.uk/..."
  deadline: "2027-01-15"
  description: "Fully funded 3.5-year studentship developing reduced-order models for lithium-ion batteries."
```

| Field         | Required | Description                                                     |
| ------------- | -------- | --------------------------------------------------------------- |
| `title`       | Yes      | Name of the position.                                           |
| `category`    | Yes      | One of `undergraduate`, `phd`, `postdoc`.                       |
| `url`         | Yes      | Link to the full advert, usually hosted by the university.      |
| `deadline`    | No       | Closing date as `YYYY-MM-DD`, in quotes. Positions in each category are sorted by deadline. |
| `description` | No       | One or two sentences summarising the position.                  |

Preview with `hugo server` and open a pull request (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

## Closing a position

A position whose deadline has passed is hidden automatically, but only when the site is next built, which happens whenever anything is merged into `main`. If nothing is merged after the deadline, the position stays visible. To be sure, delete the entry once the position closes (and put back `[]` if it was the last one).

Positions without a deadline are never hidden automatically: delete them when filled.
