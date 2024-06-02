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
Locked URL:    git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=6d04c4613bb5d6a02e740a335a99f66a21bdac74&shallow=1
Description:   Eriixpkgs is a collection of my personal Nix packages and NixOS modules
Path:          /nix/store/1sana3rzyjz0rjplclkiyy6mx8y8h12p-source
Revision:      6d04c4613bb5d6a02e740a335a99f66a21bdac74
Revisions:     1
Last modified: 2024-06-02 00:20:33
Inputs:
├───eriixvim: github:erictossell/eriixvim/9b5d73b84fa3bd2f9e75bd6c6afc53ea93f480d5 (2024-04-30 21:42:18)
│   ├───flake-parts: github:hercules-ci/flake-parts/9126214d0a59633752a136528f5f3b9aa8565b7d (2024-04-01 23:40:58)
│   │   └───nixpkgs-lib: github:NixOS/nixpkgs/d8fe5e6c92d0d190646fb9f1056741a229980089?dir=lib (2024-03-29 09:07:56)
│   ├───nixpkgs: github:nixos/nixpkgs/58a1abdbae3217ca6b702f03d3b35125d88a2994 (2024-04-27 21:35:43)
│   └───nixvim: github:nix-community/nixvim/2483dff03dd326296278213a8e051d375b56d3df (2024-04-30 16:36:11)
│       ├───devshell: github:numtide/devshell/12e914740a25ea1891ec619bb53cf5e6ca922e40 (2024-04-19 13:19:58)
│       │   ├───flake-utils: github:numtide/flake-utils/4022d587cbbfd70fe950c1e2083a02621806a725 (2023-12-04 08:58:27)
│       │   │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───flake-compat: https://api.flakehub.com/f/pinned/edolstra/flake-compat/1.0.1/018afb31-abd1-7bff-a5e4-cff7e18efb7a/source.tar.gz?narHash=sha256-kvjfFW7WAETZlt09AgDn1MrtKzP7t90Vf7vypd3OL1U%3D (2023-10-04 13:37:54)
│       ├───flake-parts: github:hercules-ci/flake-parts/9126214d0a59633752a136528f5f3b9aa8565b7d (2024-04-01 23:40:58)
│       │   └───nixpkgs-lib follows input 'eriixvim/nixvim/nixpkgs'
│       ├───home-manager: github:nix-community/home-manager/9fe79591c1005ce6f93084ae7f7dab0a2891440d (2024-04-28 22:30:45)
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───nix-darwin: github:lnl7/nix-darwin/230a197063de9287128e2c68a7a4b0cd7d0b50a7 (2024-04-24 08:09:31)
│       │   └───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│       ├───nixpkgs: github:NixOS/nixpkgs/58a1abdbae3217ca6b702f03d3b35125d88a2994 (2024-04-27 21:35:43)
│       └───pre-commit-hooks: github:cachix/pre-commit-hooks.nix/6fb82e44254d6a0ece014ec423cb62d92435336f (2024-04-24 10:34:06)
│           ├───flake-compat: github:edolstra/flake-compat/0f9255e01c2351cc7d116c072cb317785dd33b33 (2023-10-04 13:37:54)
│           ├───flake-utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
│           │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│           ├───gitignore: github:hercules-ci/gitignore.nix/637db329424fd7e46cf4185293b9cc8c88c95394 (2024-02-28 02:28:52)
│           │   └───nixpkgs follows input 'eriixvim/nixvim/pre-commit-hooks/nixpkgs'
│           ├───nixpkgs follows input 'eriixvim/nixvim/nixpkgs'
│           └───nixpkgs-stable follows input 'eriixvim/nixvim/nixpkgs'
├───flake-utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
│   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
├───go-time: github:erictossell/go-time/18e4d069522a1ad1e65223ec95daed4baeae5f71 (2024-04-30 21:46:46)
│   └───nixpkgs: github:NixOS/nixpkgs/58a1abdbae3217ca6b702f03d3b35125d88a2994 (2024-04-27 21:35:43)
├───homepage-nix: github:erictossell/homepage-nix/c6620260812bc35ee7209ab2fa0f4899868b86f1 (2024-03-08 02:17:42)
│   ├───naersk: github:nix-community/naersk/aeb58d5e8faead8980a807c840232697982d47b9 (2023-10-27 15:31:12)
│   │   └───nixpkgs: github:NixOS/nixpkgs/f945939fd679284d736112d3d5410eb867f3b31c (2024-03-07 02:56:54)
│   ├───nixpkgs: github:NixOS/nixpkgs/f945939fd679284d736112d3d5410eb867f3b31c (2024-03-07 02:56:54)
│   └───utils: github:numtide/flake-utils/d465f4819400de7c8d874d50b982301f28a84605 (2024-02-28 13:18:44)
│       └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
├───nixpkgs: github:NixOS/nixpkgs/ad57eef4ef0659193044870c731987a6df5cf56b (2024-05-29 02:06:23)
├───readme-py: github:erictossell/readme-py/5aa386ce95659257d578c9a80d75fefe16ae1b1a (2024-06-02 00:12:29)
│   ├───flake-utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
│   │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│   ├───nixpkgs: github:NixOS/nixpkgs/ad57eef4ef0659193044870c731987a6df5cf56b (2024-05-29 02:06:23)
│   └───poetry2nix: github:nix-community/poetry2nix/11e97e742da5b4e43c27cfe13fca904e82fd4e56 (2024-06-01 13:55:09)
│       ├───flake-utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
│       │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│       ├───nix-github-actions: github:nix-community/nix-github-actions/5163432afc817cf8bd1f031418d1869e4c9d5547 (2023-12-29 15:30:25)
│       │   └───nixpkgs follows input 'readme-py/poetry2nix/nixpkgs'
│       ├───nixpkgs follows input 'readme-py/nixpkgs'
│       ├───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)
│       └───treefmt-nix: github:numtide/treefmt-nix/03b982b77df58d5974c61c6022085bafe780c1cf (2024-05-31 19:02:28)
│           └───nixpkgs follows input 'readme-py/poetry2nix/nixpkgs'
└───russh: github:erictossell/russh/dd53274d43199a67f9d192d88b6f77807363657b (2024-04-30 21:45:16)
    ├───naersk: github:nix-community/naersk/c5037590290c6c7dae2e42e7da1e247e54ed2d49 (2024-04-19 09:58:44)
    │   └───nixpkgs: path:/nix/store/370qy3d3wg9zhbn5a3dcv6k1q1iigfh4-source?lastModified=0&narHash=sha256-Drmja/f5MRHZCskS6mvzFqxEaZMeciScCTFxWVLqWEY%3D (1970-01-01 00:00:00)
    ├───nixpkgs: github:NixOS/nixpkgs/cf8cc1201be8bc71b7cbbbdaf349b22f4f99c7ae (2024-04-28 14:22:29)
    └───utils: github:numtide/flake-utils/b1d9ab70662946ef0850d488da1c9019f3a9752a (2024-03-11 08:33:50)
        └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e (2023-04-09 08:27:08)

```

### Flake Outputs

```nix
git+file:///home/runner/work/eriixpkgs/eriixpkgs?ref=refs/heads/main&rev=6d04c4613bb5d6a02e740a335a99f66a21bdac74&shallow=1
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
