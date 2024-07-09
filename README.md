# GH Meister

GitHub management made easy.

<div align="center">
  <img src="docs/assets/gh-meister-logo.png" width="384"/>
</div>

# Introduction

# Quickstart

## Installation

To install GH Meister in an isolated Python environment using
[pipx](https://pipx.pypa.io/stable/) run:

```shell
pipx install ghmeister
```

# Development

## Release to PyPi

1. Create a distribution build:
    ```shell
    poetry build
    ```

2. Publish to PyPi:
    ```shell
    poetry publish
    ```

## Local installation using pipx

To install the `main` branch locally run:

```shell
pipx install git+https://github.com/robvanderleek/ghmeister.git
```

Or to install another branch locally run:

```shell
pip install git+https://github.com/robvanderleek/ghmeister.git@issue-123
```

## Building the binary distribution

Generate a self-contained binary:

```shell
poetry run poe bundle
```

Then run the executable `dist/ghmeister/ghmeister`.

# Feedback, suggestions and bug reports

If you have suggestions for how GH Meister could be improved, or want to
report a bug, [open an
issue](https://github.com/robvanderleek/ghmeister/issues)! All and any
contributions are appreciated.

To show your project uses GH Meister place this badge in the README markdown:

[![GH Meister](https://img.shields.io/badge/GH%20Meister-green.svg)](https://github.com/robvanderleek/ghmeister)

```
[![GH Meister](https://img.shields.io/badge/GH%20Meister-green.svg)](https://github.com/robvanderleek/ghmeister)
```

# License

[MIT](LICENSE) © 2023 Rob van der Leek <robvanderleek@gmail.com>
(https://twitter.com/robvanderleek)
