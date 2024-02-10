## Eriixpkgs

[![Flake Update](https://github.com/erictossell/eriixpkgs/actions/workflows/update.yml/badge.svg)](https://github.com/erictossell/eriixpkgs/actions/workflows/update.yml)
[![Flake Check](https://github.com/erictossell/eriixpkgs/actions/workflows/check.yml/badge.svg)](https://github.com/erictossell/eriixpkgs/actions/workflows/check.yml)
[![Readme Update](https://github.com/erictossell/eriixpkgs/actions/workflows/readme.yml/badge.svg?branch=main)](https://github.com/erictossell/eriixpkgs/actions/workflows/readme.yml)

My collection of Nix packages. Home-rolled, custom built.


### Directory Structure

- [templates/](templates/)
  - [go-flake/](templates/go-flake/)
  - [python-flake/](templates/python-flake/)
    - [app/](templates/python-flake/app/)
  - [rust-flake/](templates/rust-flake/)
    - [src/](templates/rust-flake/src/)

### Flake Info

```nix
Resolved URL:  git+file:///home/runner/work/eriixpkgs/eriixpkgs?shallow=1
Locked URL:    git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=14cc243307aa27135548c514e2516675366c3a48&shallow=1
Description:   Eriixpkgs is a collection of my personal Nix packages and NixOS modules
Path:          /nix/store/lbyjjh8fmkissry6avcn7gwmzwql2gji-source
Revision:      14cc243307aa27135548c514e2516675366c3a48
Last modified: 2024-02-10 00:15:42
Inputs:
├───eriixvim: github:erictossell/eriixvim/8f0699a539a9a3348933997c76a93f91584aa18a
│   ├───flake-parts: github:hercules-ci/flake-parts/b253292d9c0a5ead9bc98c4e9a26c6312e27d69f
│   │   └───nixpkgs-lib: github:NixOS/nixpkgs/97b17f32362e475016f942bbdfda4a4a72a8a652?dir=lib
│   ├───nixpkgs: github:nixos/nixpkgs/f8e2ebd66d097614d51a56a755450d4ae1632df1
│   └───nixvim: github:nix-community/nixvim/ec07263b1693ebbd74080b1e21d9b88ae7b74d18
│       ├───flake-parts: github:hercules-ci/flake-parts/b253292d9c0a5ead9bc98c4e9a26c6312e27d69f
│       │   └───nixpkgs-lib follows input 'eriixvim/nixvim/nixpkgs'
│       ├───home-manager: github:nix-community/home-manager/880d9bc2110f7cae59698f715b8ca42cdc53670c
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───nix-darwin: github:lnl7/nix-darwin/bdbae6ecff8fcc322bf6b9053c0b984912378af7
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───nixpkgs: github:NixOS/nixpkgs/b8b232ae7b8b144397fdb12d20f592e5e7c1a64d
│       └───pre-commit-hooks: github:cachix/pre-commit-hooks.nix/7c54e08a689b53c8a1e5d70169f2ec9e2a68ffaf
│           ├───flake-compat: github:edolstra/flake-compat/0f9255e01c2351cc7d116c072cb317785dd33b33
│           ├───flake-utils: github:numtide/flake-utils/4022d587cbbfd70fe950c1e2083a02621806a725
│           │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
│           ├───gitignore: github:hercules-ci/gitignore.nix/43e1aa1308018f37118e34d3a9cb4f5e75dc11d5
│           │   └───nixpkgs follows input 'eriixvim/nixvim/pre-commit-hooks/nixpkgs'
│           ├───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│           └───nixpkgs-stable follows input 'eriixvim/nixvim/nixpkgs'
├───flake-utils: github:numtide/flake-utils/1ef2e671c3b0c19053962c07dbda38332dcebf26
│   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
├───go-time: github:erictossell/go-time/d2e5a8c286fde94478e16a597bc78b6954e3b9a8
│   └───nixpkgs: github:NixOS/nixpkgs/c3e128f3c0ecc1fb04aef9f72b3dcc2f6cecf370
├───homepage-nix: github:erictossell/homepage-nix/7895b342647955e8572363bbbfb331d15255dd48
│   ├───naersk: github:nix-community/naersk/aeb58d5e8faead8980a807c840232697982d47b9
│   │   └───nixpkgs: github:NixOS/nixpkgs/e5d1c87f5813afde2dda384ac807c57a105721cc
│   ├───nixpkgs: github:NixOS/nixpkgs/e5d1c87f5813afde2dda384ac807c57a105721cc
│   └───utils: github:numtide/flake-utils/1ef2e671c3b0c19053962c07dbda38332dcebf26
│       └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
├───nixpkgs: github:NixOS/nixpkgs/f8e2ebd66d097614d51a56a755450d4ae1632df1
├───readme-py: github:erictossell/readme-py/bb3e80e2a8205d915cfc38ed2b4f2951443b0024
│   ├───flake-utils: github:numtide/flake-utils/1ef2e671c3b0c19053962c07dbda38332dcebf26
│   │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
│   ├───nixpkgs: github:NixOS/nixpkgs/b8b232ae7b8b144397fdb12d20f592e5e7c1a64d
│   └───poetry2nix: github:nix-community/poetry2nix/e0b44e9e2d3aa855d1dd77b06f067cd0e0c3860d
│       ├───flake-utils: github:numtide/flake-utils/ff7b65b44d01cf9ba6a71320833626af21126384
│       │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
│       ├───nix-github-actions: github:nix-community/nix-github-actions/4bb5e752616262457bc7ca5882192a564c0472d2
│       │   └───nixpkgs follows input 'readme-py/poetry2nix/nixpkgs'
│       ├───nixpkgs follows input 'readme-py/nixpkgs'
│       ├───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
│       └───treefmt-nix: github:numtide/treefmt-nix/e82f32aa7f06bbbd56d7b12186d555223dc399d1
│           └───nixpkgs follows input 'readme-py/poetry2nix/nixpkgs'
└───russh: github:erictossell/russh/948dfb643c24c0f029d9917c0fd665b97ade3926
    ├───naersk: github:nix-community/naersk/aeb58d5e8faead8980a807c840232697982d47b9
    │   └───nixpkgs: github:NixOS/nixpkgs/e5d1c87f5813afde2dda384ac807c57a105721cc
    ├───nixpkgs: github:NixOS/nixpkgs/e5d1c87f5813afde2dda384ac807c57a105721cc
    └───utils: github:numtide/flake-utils/1ef2e671c3b0c19053962c07dbda38332dcebf26
        └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e

```

### Flake Outputs

```nix
git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=14cc243307aa27135548c514e2516675366c3a48&shallow=1
├───nixosModules
│   ├───aarch64-darwin: NixOS module
│   ├───aarch64-linux: NixOS module
│   ├───x86_64-darwin: NixOS module
│   └───x86_64-linux: NixOS module
├───packages
│   ├───aarch64-darwin
│   │   ├───eriixvim: package 'nixvim'
│   │   ├───go-time: package 'go-time-0.1.58'
│   │   ├───homepage-nix: package 'homepage-nix-0.2.0'
│   │   ├───readme-py: package 'python3.11-readme-py-0.1.0'
│   │   └───russh: package 'russh-0.1.92'
│   ├───aarch64-linux
│   │   ├───eriixvim: package 'nixvim'
│   │   ├───go-time: package 'go-time-0.1.58'
│   │   ├───homepage-nix: package 'homepage-nix-0.2.0'
│   │   ├───readme-py: package 'python3.11-readme-py-0.1.0'
│   │   └───russh: package 'russh-0.1.92'
│   ├───x86_64-darwin
│   │   ├───eriixvim: package 'nixvim'
│   │   ├───go-time: package 'go-time-0.1.58'
│   │   ├───homepage-nix: package 'homepage-nix-0.2.0'
│   │   ├───readme-py: package 'python3.11-readme-py-0.1.0'
│   │   └───russh: package 'russh-0.1.92'
│   └───x86_64-linux
│       ├───eriixvim: package 'nixvim'
│       ├───go-time: package 'go-time-0.1.58'
│       ├───homepage-nix: package 'homepage-nix-0.2.0'
│       ├───readme-py: package 'python3.11-readme-py-0.1.0'
│       └───russh: package 'russh-0.1.92'
└───templates
    ├───go: template: A template for a Go flake
    ├───python: template: A template for a Python flake
    └───rust: template: A template for a Rust flake

```

---

👤 [**erictossell**](https://github.com/erictossell)
