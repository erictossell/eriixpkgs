## Eriixpkgs

My collection of Nix packages. Home-rolled, custom built.


`Directory Tree`

    [docs](docs/)/
        [readme.md](docs/readme.md)

## Nix Flake Show

```nix
git+file:///home/eriim/repos/nix/eriixpkgs
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
