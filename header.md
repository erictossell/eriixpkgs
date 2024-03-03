## Eriixpkgs

[![Flake Update](https://github.com/erictossell/eriixpkgs/actions/workflows/update.yml/badge.svg)](https://github.com/erictossell/eriixpkgs/actions/workflows/update.yml)
[![Flake Check](https://github.com/erictossell/eriixpkgs/actions/workflows/check.yml/badge.svg)](https://github.com/erictossell/eriixpkgs/actions/workflows/check.yml)
[![Readme Update](https://github.com/erictossell/eriixpkgs/actions/workflows/readme.yml/badge.svg?branch=main)](https://github.com/erictossell/eriixpkgs/actions/workflows/readme.yml)

My collection of Nix packages. Home-rolled, custom built.

### Packages
- [x] [ebolg](https://github.com/erictossell/ebolg)
- [x] [eriixvim](https://github.com/erictossell/eriixvim)
- [x] [go-time](https://github.com/erictossell/go-time)
- [x] [homepage-nix](https://github.com/erictossell/homepage-nix)
- [x] [readme-py](https://github.com/erictossell/readme-py)
- [x] [russh](https://github.com/erictossell/russh)

### Flake Templates

Create a new directory:
```nix
nix flake new -t github:erictossell/eriixpkgs#go project-name
nix flake new -t github:erictossell/eriixpkgs#python project-name
nix flake new -t github:erictossell/eriixpkgs#rust project-name
```

Use in an existing directory:
```nix
nix flake init -t github:erictossell/eriixpkgs#go
nix flake init -t github:erictossell/eriixpkgs#python
nix flake init -t github:erictossell/eriixpkgs#rust
```

