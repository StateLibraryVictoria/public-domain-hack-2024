# Public Domain Hack 2024

This is the repository for the State Library Victoria's Code Club and Collection Curation and Engagement joint hack event (2024).

Clone the repo to your local environment: `git@github.com:StateLibraryVictoria/public-domain-hack-2024.git`

## Branching strategy

For the duration of the two week hack sprint, there are likely to be different participants contributing to this repository. To help avoid confusion it is recommended that each participant or team creates a feature branch for their project. The branch name should be descriptive and distinct from any of the other existing branch names e.g. `robo-copyright-curator`.

Sample git command `git checkout -b"name-of-new-branch"`

**Please try to avoid committing directly to the `main` branch.**

## Repository structure

[datasets](./datasets/): the location for any datasets that are created for the hack event.

[hack-projects](./hack-projects/): folder where files for each project can be stored. An example/template sub-directory ([hack-projects/example/](./hack-projects/example/)) has been created that can be copied and renamed.

## Credential management

**Important please take note!**

Please ensure that credentials, such as API keys and passwords are not committed to the repository and use `.env` (or equivalent) files to store the relevant values. If you're unsure how to manage this securely contact one of the hack day organisers, who will do their best to help!
