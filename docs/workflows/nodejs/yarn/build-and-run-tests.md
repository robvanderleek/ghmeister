# Workflow

**Description:** Build and run tests.

**File:** [nodejs-yarn-test.yml](https://github.com/robvanderleek/repo-meister/blob/main/.github/workflows/nodejs-yarn-test.yml)

## Input parameters

None

## Output paramters

None

## Example

```yaml
name: "main"

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    uses: robvanderleek/repo-meister/.github/workflows/nodejs-yarn-test.yml@main
```

## Repositories using this workflow

- [robvanderleek/mudslide](https://github.com/robvanderleek/mudslide/blob/main/.github/workflows/main.yml)
