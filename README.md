## Eriixpkgs

[![Flake Update](https://github.com/erictossell/eriixpkgs/actions/workflows/update.yml/badge.svg)](https://github.com/erictossell/eriixpkgs/actions/workflows/update.yml)
[![Flake Check](https://github.com/erictossell/eriixpkgs/actions/workflows/check.yml/badge.svg)](https://github.com/erictossell/eriixpkgs/actions/workflows/check.yml)

My collection of Nix packages. Home-rolled, custom built.

## Nix Flake Show

```nix
git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=6dccc51fd0d966cf3d0761eb373036a0d015c677&shallow=1
├───nixosModules
│   ├───aarch64-darwin: NixOS module
│   ├───aarch64-linux: NixOS module
│   ├───x86_64-darwin: NixOS module
│   └───x86_64-linux: NixOS module
└───packages
    ├───aarch64-darwin
    │   ├───eriixvim: package 'nixvim'
    │   ├───go-time: package 'go-time-0.1.58'
    │   ├───homepage: package 'homepage-nix-0.2.0'
    │   └───russh: package 'russh-0.1.92'
    ├───aarch64-linux
    │   ├───eriixvim: package 'nixvim'
    │   ├───go-time: package 'go-time-0.1.58'
    │   ├───homepage: package 'homepage-nix-0.2.0'
    │   └───russh: package 'russh-0.1.92'
    ├───x86_64-darwin
    │   ├───eriixvim: package 'nixvim'
    │   ├───go-time: package 'go-time-0.1.58'
    │   ├───homepage: package 'homepage-nix-0.2.0'
    │   └───russh: package 'russh-0.1.92'
    └───x86_64-linux
        ├───eriixvim: package 'nixvim'
        ├───go-time: package 'go-time-0.1.58'
        ├───homepage: package 'homepage-nix-0.2.0'
        └───russh: package 'russh-0.1.92'

```
