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


### Directory Structure

- [templates/](templates/)
  - [go/](templates/go/)
  - [python/](templates/python/)
    - [app/](templates/python/app/)
  - [rust/](templates/rust/)
    - [src/](templates/rust/src/)
  - [simple/](templates/simple/)

### Flake Info

```nix
Resolved URL:  git+file:///home/runner/work/eriixpkgs/eriixpkgs?shallow=1
Locked URL:    git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=520b4930c17cfcc8b6b215c8491f8b2114a8b975&shallow=1
Description:   Eriixpkgs is a collection of my personal Nix packages and NixOS modules
Path:          /nix/store/qw1ciqfzhm56zxz8plfvgk9a25dlzi4m-source
Revision:      520b4930c17cfcc8b6b215c8491f8b2114a8b975
Revisions:     1
Last modified: 2024-07-07 00:21:42
Inputs:
├───eriixvim: github:erictossell/eriixvim/def3d45fa7848c1bce05a70fa919311df14943de (2024-07-05 05:02:57)
│   ├───flake-parts: github:hercules-ci/flake-parts/9227223f6d922fee3c7b190b2cc238a99527bbb7 (2024-07-03 08:15:18)
│   │   └───nixpkgs-lib: https://github.com/NixOS/nixpkgs/archive/5daf0514482af3f97abaefc78a6606365c9108e2.tar.gz?narHash=sha256-Fm2rDDs86sHy0/1jxTOKB1118Q0O3Uc7EC0iXvXKpbI%3D (2024-07-01 23:35:45)
│   ├───nixpkgs: github:nixos/nixpkgs/9f4128e00b0ae8ec65918efeba59db998750ead6 (2024-07-03 18:27:49)
│   └───nixvim: github:nix-community/nixvim/92e9f5466dcfd51e8e2e7627e992c1c9d5fc6fd6 (2024-07-04 21:00:56)
│       ├───devshell: github:numtide/devshell/1ebbe68d57457c8cae98145410b164b5477761f4 (2024-06-03 10:02:49)
│       │   ├───flake-utils: github:numtide/flake-utils/4022d587cbbfd70fe950c1e2083a02621806a725 (2023-12-04 08:58:27)
│       │   │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───flake-compat: https://api.flakehub.com/f/pinned/edolstra/flake-compat/1.0.1/018afb31-abd1-7bff-a5e4-cff7e18efb7a/source.tar.gz?narHash=sha256-kvjfFW7WAETZlt09AgDn1MrtKzP7t90Vf7vypd3OL1U%3D (2023-10-04 13:37:54)
│       ├───flake-parts: github:hercules-ci/flake-parts/4e3583423212f9303aa1a6337f8dffb415920e4f (2024-07-01 23:44:14)
│       │   └───nixpkgs-lib follows input 'eriixvim/nixvim/nixpkgs'
│       ├───git-hooks: github:cachix/git-hooks.nix/0ff4381bbb8f7a52ca4a851660fc7a437a4c6e07 (2024-06-24 20:12:25)
│       │   ├───flake-compat: github:edolstra/flake-compat/0f9255e01c2351cc7d116c072cb317785dd33b33 (2023-10-04 13:37:54)
│       │   ├───gitignore: github:hercules-ci/gitignore.nix/637db329424fd7e46cf4185293b9cc8c88c95394 (2024-02-28 02:28:52)
│       │   │   └───nixpkgs follows input 'eriixvim/nixvim/git-hooks/nixpkgs'
│       │   ├───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       │   └───nixpkgs-stable follows input 'eriixvim/nixvim/nixpkgs'
│       ├───home-manager: github:nix-community/home-manager/59ce796b2563e19821361abbe2067c3bb4143a7d (2024-07-01 09:50:39)
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───nix-darwin: github:lnl7/nix-darwin/ec12b88104d6c117871fad55e931addac4626756 (2024-07-01 14:50:23)
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───nixpkgs: github:NixOS/nixpkgs/00d80d13810dbfea8ab4ed1009b09100cca86ba8 (2024-07-01 15:47:52)
│       └───treefmt-nix: github:numtide/treefmt-nix/bdb6355009562d8f9313d9460c0d3860f525bc6c (2024-07-02 02:35:53)
│           └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
├───flake-utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
│   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
├───go-time: github:erictossell/go-time/22b1066f50a0b7c7361b1bdbc915b0cbf83536cd (2024-06-29 15:27:48)
│   └───nixpkgs: github:NixOS/nixpkgs/b2852eb9365c6de48ffb0dc2c9562591f652242a (2024-06-27 16:44:53)
├───homepage-nix: github:erictossell/homepage-nix/540adeb9f307826c9bdd1b047a8b4467160709a4 (2024-07-05 04:49:49)
│   ├───naersk: github:nix-community/naersk/941ce6dc38762a7cfb90b5add223d584feed299b (2024-06-18 16:21:15)
│   │   └───nixpkgs: path:/nix/store/dk2rpyb6ndvfbf19bkb2plcz5y3k8i5v-source?lastModified=0&narHash=sha256-rwz8NJZV%2B387rnWpTYcXaRNvzUSnnF9aHONoJIYmiUQ%3D (1970-01-01 00:00:00)
│   ├───nixpkgs: github:NixOS/nixpkgs/1afc5440469f94e7ed26e8648820971b102afdc3 (2024-07-04 10:07:58)
│   └───utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
│       └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
├───nixpkgs: github:NixOS/nixpkgs/9f4128e00b0ae8ec65918efeba59db998750ead6 (2024-07-03 18:27:49)
├───readme-py: github:erictossell/readme-py/fb10275a3e38114828f1b4b01c5d861b55ed9c91 (2024-07-07 00:12:51)
│   ├───flake-utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
│   │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│   ├───nixpkgs: github:NixOS/nixpkgs/9f4128e00b0ae8ec65918efeba59db998750ead6 (2024-07-03 18:27:49)
│   └───poetry2nix: github:nix-community/poetry2nix/42262f382c68afab1113ebd1911d0c93822d756e (2024-07-01 16:21:24)
│       ├───flake-utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
│       │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│       ├───nix-github-actions: github:nix-community/nix-github-actions/5163432afc817cf8bd1f031418d1869e4c9d5547 (2023-12-29 15:30:25)
│       │   └───nixpkgs follows input 'readme-py/poetry2nix/nixpkgs'
│       ├───nixpkgs follows input 'readme-py/nixpkgs'
│       ├───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│       └───treefmt-nix: github:numtide/treefmt-nix/8df5ff62195d4e67e2264df0b7f5e8c9995fd0bd (2024-06-30 12:03:42)
│           └───nixpkgs follows input 'readme-py/poetry2nix/nixpkgs'
└───russh: github:erictossell/russh/45da95e1260fe25cd7145a23e4111d84b5b8ef7f (2024-07-05 04:45:21)
    ├───naersk: github:nix-community/naersk/941ce6dc38762a7cfb90b5add223d584feed299b (2024-06-18 16:21:15)
    │   └───nixpkgs: path:/nix/store/dk2rpyb6ndvfbf19bkb2plcz5y3k8i5v-source?lastModified=0&narHash=sha256-rwz8NJZV%2B387rnWpTYcXaRNvzUSnnF9aHONoJIYmiUQ%3D (1970-01-01 00:00:00)
    ├───nixpkgs: github:NixOS/nixpkgs/1afc5440469f94e7ed26e8648820971b102afdc3 (2024-07-04 10:07:58)
    └───utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
        └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)

```

### Flake Outputs

```nix
git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=520b4930c17cfcc8b6b215c8491f8b2114a8b975&shallow=1
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
    ├───rust: template: A template for a Rust flake
    └───simple: template: A simple template for a flake

```

---

👤 [**erictossell**](https://github.com/erictossell)
