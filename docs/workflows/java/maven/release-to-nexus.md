# Workflow

**Description:** Release to Maven Central

**File:** [java-maven-release-to-nexus.yml](https://github.com/robvanderleek/repo-meister/blob/main/.github/workflows/java-maven-release-to-nexus.yml)

## Input parameters

None

## Input secrets

| Name            | Description                         | Type   | Required |
| --------------- | ----------------------------------- | ------ | -------- |
| gpg_private_key | GPG private key used for deployment | string | true     |

## Output paramters

None

## Usage example

```yaml
name: "release"

on:
  push:
    tags:
      - v*

jobs:
  release:
    uses: robvanderleek/repo-meister/.github/workflows/java-maven-release-to-nexus.yml@main
```

## Repositories using this workflow

- [robvanderleek/JLifx](https://github.com/robvanderleek/JLifx/blob/main/.github/workflows/main.yml)
