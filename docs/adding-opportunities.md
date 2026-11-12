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

A position whose deadline has passed is hidden automatically when the site is rebuilt, which happens every day (see the Scheduled Rebuild workflow in the [README](../README.md#automation)) and whenever anything is merged into `main`. It is still good practice to delete the entry once the position is filled (and put back `[]` if it was the last one).

Positions without a deadline are never hidden automatically: delete them when filled.
