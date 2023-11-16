# Repo Meister

A Collection of Reusable GitHub Actions and Workflows.

<div align="center">
  <img src="docs/repo-meister-logo.png" width="384"/>
</div>

# Introduction

This collection of resusable workflows and actions make it easy to setup GitHub Actions for your repository. Find your programming language and build tool below to get started.

## Reasons for using Repo Meister

- Fastest way to setup GitHub Actions for your project
- Use a standard setup, based on best practices from the community
- Automatically have up-to-date actions with sane defaults
- Reduce code duplication in your workflows

# Quickstart

Pre-configured GitHubb Actions and Workflows make it possible to, for example, setup a standard Continuous Integration pipeline in minutes.

For example, if your project used NodeJS and NPM, you need to put the following configuration in a file called `.github/workflows/main.yml` to setup Continunous Integreation for all pushes and pull-requests to your `main` branch:

```yaml
name: main

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  ci:
    uses: repo-meister/ci-nodejs-npm/.github/workflows/ci.yml@main
```

Check the [Actions and Workflows](#actions-and-workflows) section below for a listing of reusable workflows and actions.

> [!NOTE]
> Contributions needed! Please share your reusable workflows by [opening an issue](https://github.com/robvanderleek/repo-meister/issues/new).

# Actions and Workflows

## Continuous Integration

### Java

- [Maven](https://github.com/repo-meister-actions/ci-java-maven#readme)

### NodeJS

- [NPM](https://github.com/repo-meister-actions/ci-nodejs-npm#readme)
- [Yarn](https://github.com/repo-meister-actions/ci-nodejs-yarn#readme)

# Feedback, suggestions and bug reports

Please create an issue here: https://github.com/robvanderleek/repo-mister/issues

# License

[MIT](LICENSE) © 2023 Rob van der Leek <robvanderleek@gmail.com>
(https://twitter.com/robvanderleek)
