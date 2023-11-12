# Workflow

**Description:** Build and run tests.

**File:** [nodejs-yarn.yml](https://github.com/robvanderleek/repo-meister/blob/main/.github/workflows/nodejs-yarn.yml)

## Input parameters

| Name         | Description | Required | Type   | Default |
| ------------ | ----------- | -------- | ------ | ------- |
| node-version | JDK version | false    | string | 18.x    |

## Output paramters

None

## Example

```yaml
name: "main"

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  test:
    uses: robvanderleek/repo-meister/.github/workflows/nodejs-yarn.yml@main
```

## Repositories using this workflow

- [robvanderleek/mudslide](https://github.com/robvanderleek/mudslide/blob/main/.github/workflows/main.yml)
