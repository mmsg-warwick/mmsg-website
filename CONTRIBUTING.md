# Contributing

All changes are submitted through a pull request: nothing is committed directly to `main`. The guides in [docs/](docs/) explain how to make the most common changes; see the table in the [README](README.md#common-tasks).

## Making a change

1. **Create a branch** from an up-to-date `main`:

   ```bash
   git checkout main
   git pull
   git checkout -b add-jane-smith
   ```

   If you do not have write access to the repository, fork it on GitHub first and work in your fork.

2. **Make the change** and preview it locally with `hugo server` (see [Running the site locally](README.md#running-the-site-locally)).

   For a small text change you can also edit the file directly on GitHub (pencil icon) and choose *Create a new branch… and start a pull request*, then check the result in the deploy preview instead.

3. **Commit and push**:

   ```bash
   git add content/team/jane-smith
   git commit -m "Add Jane Smith to the team page"
   git push -u origin add-jane-smith
   ```

4. **Open a pull request** on GitHub against `main`.

5. **Check the deploy preview.** Netlify builds the site for every pull request and adds a *deploy preview* link to the pull request checks. Open it and check the pages you changed, including on a phone-sized window and in dark mode.

6. **Wait for the checks** (Netlify build, link check, pre-commit.ci) to pass and for a review. Once merged, the live site updates within a couple of minutes.

## Guidelines

- One topic per pull request (e.g. adding one person, or one software tool), with a title that says what it does.
- Keep commits focused.
- Use British English in the site text.
- Describe the group's work plainly and specifically; avoid marketing language.
- Keep images reasonably small (photos under about 500 KB) and only add images you have the right to use.
- If the link check fails on a link you did not touch, an external page has probably moved: fix it in a separate pull request or mention it in yours.
