# Workflow 

*Description:* Build and run tests.

*File:* [java-maven-test.yml](https://github.com/repo-meister/.github/workflows/java-maven-test.yml)

## Input parameters

None

## Output paramters

None

## Usage example

```yaml
name: main

on: [push, pull_request]

jobs:
  test:
    uses: robvanderleek/repo-meister/.github/workflows/java-maven-test.yml@main
```
