# GitHub Meister

<div align="center">
  <img src="assets/logo.png" width="500"/>
  <p>
    <i>Your GitHub terminal client</i>
  </p>
</div>

---

GitHub Meister is a GitHub terminal client that tries to be a **simple**, yet
**productive** tool for commen GitHub tasks and automations. 

Core features:

* Simple to navigate **menu-driven terminal interface**, based on [InquirerPy](https://github.com/kazhala/InquirerPy)
* Powerful command-line interface to the **full GitHub API**, based on [Typer](https://github.com/tiangolo/typer)
* Fully writen in Python, contributions are welcome!

## Installation

To install the latest version of GitHub Meister in an isolated Python
environment using [pipx](https://pipx.pypa.io/stable/) run:

```shell
pipx install ghmeister
```

Output:

```shell
Installed package ghmeister 0.1.0, installed using Python 3.12.4
These apps are now globally available
  - ghm
done! ✨ 🌟 ✨
```

After which you can run GitHub Meister:

```shell
ghm --version
```

Output:

```shell
GitHub Meister version: 0.1.0
```

<div id="installation.cast" style="z-index: 1; position: relative;"></div>

<script>
  window.onload = function(){
    AsciinemaPlayer.create('/assets/installation.cast', document.getElementById('installation.cast'));
}
</script>
