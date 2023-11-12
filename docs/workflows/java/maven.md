# Workflow

**File:** [java-maven.yml](https://github.com/robvanderleek/repo-meister/blob/main/.github/workflows/java-maven.yml)

**Description:** Build and run tests.

## Input parameters

| Name         | Description | Required | Type   | Default |
| ------------ | ----------- | -------- | ------ | ------- |
| java-version | JDK version | false    | string | 17      |

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
  build:
    uses: robvanderleek/repo-meister/.github/workflows/java-maven.yml@main
```

## Repositories using this workflow

- [robvanderleek/JLifx](https://github.com/robvanderleek/JLifx/blob/main/.github/workflows/main.yml)
