# Workflow

**File:** [nodejs-npm.yml](https://github.com/robvanderleek/repo-meister/blob/main/.github/workflows/nodejs-npm.yml)

**Description:** Build and run tests.

## Input parameters

| Name         | Description    | Required | Type   | Default |
| ------------ | -------------- | -------- | ------ | ------- |
| node-version | NodeJS version | false    | string | 18.x    |

## Output parameters

None

## Usage example

```yaml
name: main

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  ci:
    uses: repo-meister/nodejs-npm/.github/workflows/nodejs-npm.yml@main
```

## Repositories using this workflow
