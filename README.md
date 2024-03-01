## Eriixpkgs

[![Flake Update](https://github.com/erictossell/eriixpkgs/actions/workflows/update.yml/badge.svg)](https://github.com/erictossell/eriixpkgs/actions/workflows/update.yml)
[![Flake Check](https://github.com/erictossell/eriixpkgs/actions/workflows/check.yml/badge.svg)](https://github.com/erictossell/eriixpkgs/actions/workflows/check.yml)
[![Readme Update](https://github.com/erictossell/eriixpkgs/actions/workflows/readme.yml/badge.svg?branch=main)](https://github.com/erictossell/eriixpkgs/actions/workflows/readme.yml)

My collection of Nix packages. Home-rolled, custom built.


### Directory Structure

- [templates/](templates/)
  - [go/](templates/go/)
  - [python/](templates/python/)
    - [app/](templates/python/app/)
  - [rust/](templates/rust/)
    - [src/](templates/rust/src/)

### Flake Info

```nix
Resolved URL:  git+file:///home/runner/work/eriixpkgs/eriixpkgs?shallow=1
Locked URL:    git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=8897d61de77a67dce4f3a01cd3cf1f2118cf087e&shallow=1
Description:   Eriixpkgs is a collection of my personal Nix packages and NixOS modules
Path:          /nix/store/03yhymsqx1js7c5z1jczg2y2i0fn0wnd-source
Revision:      8897d61de77a67dce4f3a01cd3cf1f2118cf087e
Last modified: 2024-03-01 00:18:06
Inputs:
├───eriixvim: github:erictossell/eriixvim/5e01fc92f65aa61e4402d67b4de782d11a262207
│   ├───flake-parts: github:hercules-ci/flake-parts/b253292d9c0a5ead9bc98c4e9a26c6312e27d69f
│   │   └───nixpkgs-lib: github:NixOS/nixpkgs/97b17f32362e475016f942bbdfda4a4a72a8a652?dir=lib
│   ├───nixpkgs: github:nixos/nixpkgs/f9d39fb9aff0efee4a3d5f4a6d7c17701d38a1d8
│   └───nixvim: github:nix-community/nixvim/183eac72a9f0ae0032239510d89dbc474b180d33
│       ├───flake-parts: github:hercules-ci/flake-parts/b253292d9c0a5ead9bc98c4e9a26c6312e27d69f
│       │   └───nixpkgs-lib follows input 'eriixvim/nixvim/nixpkgs'
│       ├───home-manager: github:nix-community/home-manager/5b9156fa9a8b8beba917b8f9adbfd27bf63e16af
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───nix-darwin: github:lnl7/nix-darwin/bdbae6ecff8fcc322bf6b9053c0b984912378af7
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───nixpkgs: github:NixOS/nixpkgs/f8e2ebd66d097614d51a56a755450d4ae1632df1
│       └───pre-commit-hooks: github:cachix/pre-commit-hooks.nix/0db2e67ee49910adfa13010e7f012149660af7f0
│           ├───flake-compat: github:edolstra/flake-compat/0f9255e01c2351cc7d116c072cb317785dd33b33
│           ├───flake-utils: github:numtide/flake-utils/4022d587cbbfd70fe950c1e2083a02621806a725
│           │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
│           ├───gitignore: github:hercules-ci/gitignore.nix/43e1aa1308018f37118e34d3a9cb4f5e75dc11d5
│           │   └───nixpkgs follows input 'eriixvim/nixvim/pre-commit-hooks/nixpkgs'
│           ├───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│           └───nixpkgs-stable follows input 'eriixvim/nixvim/nixpkgs'
├───flake-utils: github:numtide/flake-utils/d465f4819400de7c8d874d50b982301f28a84605
│   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
├───go-time: github:erictossell/go-time/d2e5a8c286fde94478e16a597bc78b6954e3b9a8
│   └───nixpkgs: github:NixOS/nixpkgs/c3e128f3c0ecc1fb04aef9f72b3dcc2f6cecf370
├───homepage-nix: github:erictossell/homepage-nix/7895b342647955e8572363bbbfb331d15255dd48
│   ├───naersk: github:nix-community/naersk/aeb58d5e8faead8980a807c840232697982d47b9
│   │   └───nixpkgs: github:NixOS/nixpkgs/e5d1c87f5813afde2dda384ac807c57a105721cc
│   ├───nixpkgs: github:NixOS/nixpkgs/e5d1c87f5813afde2dda384ac807c57a105721cc
│   └───utils: github:numtide/flake-utils/1ef2e671c3b0c19053962c07dbda38332dcebf26
│       └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
├───nixpkgs: github:NixOS/nixpkgs/9099616b93301d5cf84274b184a3a5ec69e94e08
├───readme-py: github:erictossell/readme-py/b04ef6299281dc2cf15f889135c16ea6a7aaaa4b
│   ├───flake-utils: github:numtide/flake-utils/1ef2e671c3b0c19053962c07dbda38332dcebf26
│   │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
│   ├───nixpkgs: github:NixOS/nixpkgs/cbc4211f0afffe6dfd2478a62615dd5175a13f9a
│   └───poetry2nix: github:nix-community/poetry2nix/3c92540611f42d3fb2d0d084a6c694cd6544b609
│       ├───flake-utils: github:numtide/flake-utils/1ef2e671c3b0c19053962c07dbda38332dcebf26
│       │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
│       ├───nix-github-actions: github:nix-community/nix-github-actions/5163432afc817cf8bd1f031418d1869e4c9d5547
│       │   └───nixpkgs follows input 'readme-py/poetry2nix/nixpkgs'
│       ├───nixpkgs follows input 'readme-py/nixpkgs'
│       ├───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
│       └───treefmt-nix: github:numtide/treefmt-nix/e504621290a1fd896631ddbc5e9c16f4366c9f65
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
git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=8897d61de77a67dce4f3a01cd3cf1f2118cf087e&shallow=1
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
