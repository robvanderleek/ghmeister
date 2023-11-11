# Workflow

**Description:** Build and run tests.

**File:** [java-maven-test.yml](https://github.com/robvanderleek/repo-meister/blob/main/.github/workflows/java-maven-test.yml)

## Input parameters

None

## Output paramters

None

## Example

```yaml
name: "main"

on:
  push
    branches: [main]
  pull_request
    branches: [main]

jobs:
  test:
    uses: robvanderleek/repo-meister/.github/workflows/java-maven-test.yml@main
```

## Repositories using this workflow

- [robvanderleek/JLifx](https://github.com/robvanderleek/JLifx/blob/main/.github/workflows/main.yml)
