## Eriixpkgs

My collection of Nix packages. Home-rolled, custom built.

### Pkgs

- [eriixvim](https://github.com/erictossell/eriixvim)
- [go-time](https://github.com/erictossell/go-time)
- [homepage-nix](https://github.com/erictossell/homepage-nix)
- [russh](https://github.com/erictossell/russh)

#### Nix Flake Show

```bash
git+file:///eriixpkgs
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
