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
  - [ansible/](templates/ansible/)
  - [go/](templates/go/)
  - [python/](templates/python/)
    - [app/](templates/python/app/)
  - [rust/](templates/rust/)
    - [src/](templates/rust/src/)
  - [simple/](templates/simple/)
  - [terraform/](templates/terraform/)

### Flake Info

```nix
Resolved URL:  git+file:///home/runner/work/eriixpkgs/eriixpkgs?shallow=1
Locked URL:    git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=8f9af665a69b0663dc72a4b1a759034e79f5a6b5&shallow=1
Description:   Eriixpkgs is a collection of my personal Nix packages and NixOS modules
Path:          /nix/store/9rpszmnw6c9rrf72yhz3mg105k5w7hj2-source
Revision:      8f9af665a69b0663dc72a4b1a759034e79f5a6b5
Revisions:     1
Last modified: 2025-01-19 00:24:51
Inputs:
├───eriixvim: github:erictossell/eriixvim/4c8a5ccc13c162f45ecdfa44b4327001eb1b496c (2024-12-29 23:12:00)
│   ├───flake-parts: github:hercules-ci/flake-parts/205b12d8b7cd4802fbcb8e8ef6a0f1408781a4f9 (2024-12-04 11:43:21)
│   │   └───nixpkgs-lib: https://github.com/NixOS/nixpkgs/archive/5487e69da40cbd611ab2cadee0b4637225f7cfae.tar.gz?narHash=sha256-1qRH7uAUsyQI7R1Uwl4T%2BXvdNv778H0Nb5njNrqvylY%3D (2024-12-01 23:35:40)
│   ├───nixpkgs: github:nixos/nixpkgs/634fd46801442d760e09493a794c4f15db2d0cbb (2024-12-27 09:21:16)
│   └───nixvim: github:nix-community/nixvim/f4b0b81ef9eb4e37e75f32caf1f02d5501594811 (2024-12-28 09:37:50)
│       ├───devshell: github:numtide/devshell/dd6b80932022cea34a019e2bb32f6fa9e494dfef (2024-10-07 19:51:55)
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───flake-compat: https://api.flakehub.com/f/pinned/edolstra/flake-compat/1.0.1/018afb31-abd1-7bff-a5e4-cff7e18efb7a/source.tar.gz?narHash=sha256-kvjfFW7WAETZlt09AgDn1MrtKzP7t90Vf7vypd3OL1U%3D (2023-10-04 13:37:54)
│       ├───flake-parts: github:hercules-ci/flake-parts/205b12d8b7cd4802fbcb8e8ef6a0f1408781a4f9 (2024-12-04 11:43:21)
│       │   └───nixpkgs-lib follows input 'eriixvim/nixvim/nixpkgs'
│       ├───git-hooks: github:cachix/git-hooks.nix/f0f0dc4920a903c3e08f5bdb9246bb572fcae498 (2024-12-21 16:13:23)
│       │   ├───flake-compat follows input 'eriixvim/nixvim/flake-compat'
│       │   ├───gitignore: github:hercules-ci/gitignore.nix/637db329424fd7e46cf4185293b9cc8c88c95394 (2024-02-28 02:28:52)
│       │   │   └───nixpkgs follows input 'eriixvim/nixvim/git-hooks/nixpkgs'
│       │   ├───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       │   └───nixpkgs-stable follows input 'eriixvim/nixvim/nixpkgs'
│       ├───home-manager: github:nix-community/home-manager/cb27edb5221d2f2920a03155f8becc502cf60e35 (2024-12-22 10:13:25)
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───nix-darwin: github:lnl7/nix-darwin/a35b08d09efda83625bef267eb24347b446c80b8 (2024-12-07 11:27:23)
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───nixpkgs: github:NixOS/nixpkgs/d70bd19e0a38ad4790d3913bf08fcbfc9eeca507 (2024-12-19 23:01:11)
│       ├───nuschtosSearch: github:NuschtOS/search/3051be7f403bff1d1d380e4612f0c70675b44fc9 (2024-12-09 19:42:28)
│       │   ├───flake-utils: github:numtide/flake-utils/11707dc2f618dd54ca8739b309ec4fc024de578b (2024-11-13 21:27:16)
│       │   │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│       │   ├───ixx: github:NuschtOS/ixx/9fd01aad037f345350eab2cd45e1946cc66da4eb (2024-10-26 15:53:28)
│       │   │   ├───flake-utils follows input 'eriixvim/nixvim/nuschtosSearch/flake-utils'
│       │   │   └───nixpkgs follows input 'eriixvim/nixvim/nuschtosSearch/nixpkgs'
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       └───treefmt-nix: github:numtide/treefmt-nix/65712f5af67234dad91a5a4baee986a8b62dbf8f (2024-12-20 14:21:19)
│           └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
├───flake-utils: github:numtide/flake-utils/11707dc2f618dd54ca8739b309ec4fc024de578b (2024-11-13 21:27:16)
│   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
├───go-time: github:erictossell/go-time/f6fde276a99e8f19ed1e3d5b0f4946383eb4bc35 (2024-07-14 13:24:29)
│   └───nixpkgs: github:NixOS/nixpkgs/7e7c39ea35c5cdd002cd4588b03a3fb9ece6fad9 (2024-07-12 07:14:11)
├───homepage-nix: github:erictossell/homepage-nix/540adeb9f307826c9bdd1b047a8b4467160709a4 (2024-07-05 04:49:49)
│   ├───naersk: github:nix-community/naersk/941ce6dc38762a7cfb90b5add223d584feed299b (2024-06-18 16:21:15)
│   │   └───nixpkgs: path:/nix/store/dk2rpyb6ndvfbf19bkb2plcz5y3k8i5v-source?lastModified=0&narHash=sha256-rwz8NJZV%2B387rnWpTYcXaRNvzUSnnF9aHONoJIYmiUQ%3D (1970-01-01 00:00:00)
│   ├───nixpkgs: github:NixOS/nixpkgs/1afc5440469f94e7ed26e8648820971b102afdc3 (2024-07-04 10:07:58)
│   └───utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
│       └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
├───nixpkgs: github:NixOS/nixpkgs/5df43628fdf08d642be8ba5b3625a6c70731c19c (2025-01-16 21:27:11)
├───readme-py: github:erictossell/readme-py/fc15ffb48fd604110907a2375090f21d924272ef (2025-01-19 00:14:43)
│   ├───flake-utils: github:numtide/flake-utils/11707dc2f618dd54ca8739b309ec4fc024de578b (2024-11-13 21:27:16)
│   │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│   ├───nixpkgs: github:NixOS/nixpkgs/5df43628fdf08d642be8ba5b3625a6c70731c19c (2025-01-16 21:27:11)
│   └───poetry2nix: github:nix-community/poetry2nix/75d0515332b7ca269f6d7abfd2c44c47a7cbca7b (2025-01-14 19:51:49)
│       ├───flake-utils: github:numtide/flake-utils/c1dfcf08411b08f6b8615f7d8971a2bfa81d5e8a (2024-09-17 08:14:13)
│       │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│       ├───nix-github-actions: github:nix-community/nix-github-actions/e04df33f62cdcf93d73e9a04142464753a16db67 (2024-10-24 04:09:24)
│       │   └───nixpkgs follows input 'readme-py/poetry2nix/nixpkgs'
│       ├───nixpkgs follows input 'readme-py/nixpkgs'
│       ├───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│       └───treefmt-nix: github:numtide/treefmt-nix/9ef337e492a5555d8e17a51c911ff1f02635be15 (2024-10-28 13:05:26)
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
git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=8f9af665a69b0663dc72a4b1a759034e79f5a6b5&shallow=1
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
│   │   ├───readme-py: package 'python3.12-readme-py-0.1.0'
│   │   └───russh: package 'russh-0.1.92'
│   ├───aarch64-linux
│   │   ├───eriixvim: package 'nixvim'
│   │   ├───go-time: package 'go-time-0.1.58'
│   │   ├───homepage-nix: package 'homepage-nix-0.2.0'
│   │   ├───readme-py: package 'python3.12-readme-py-0.1.0'
│   │   └───russh: package 'russh-0.1.92'
│   ├───x86_64-darwin
│   │   ├───eriixvim: package 'nixvim'
│   │   ├───go-time: package 'go-time-0.1.58'
│   │   ├───homepage-nix: package 'homepage-nix-0.2.0'
│   │   ├───readme-py: package 'python3.12-readme-py-0.1.0'
│   │   └───russh: package 'russh-0.1.92'
│   └───x86_64-linux
│       ├───eriixvim: package 'nixvim'
│       ├───go-time: package 'go-time-0.1.58'
│       ├───homepage-nix: package 'homepage-nix-0.2.0'
│       ├───readme-py: package 'python3.12-readme-py-0.1.0'
│       └───russh: package 'russh-0.1.92'
└───templates
    ├───go: template: A template for a Go flake
    ├───python: template: A template for a Python flake
    ├───rust: template: A template for a Rust flake
    └───simple: template: A simple template for a flake

```

---

👤 [**erictossell**](https://github.com/erictossell)
