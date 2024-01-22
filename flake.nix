{
  description = "A flake wrapping packages and modules";

  inputs = {
    go-time.url = "github:erictossell/go-time";
    russh.url = "github:erictossell/russh";
    homepage-nix.url = "github:erictossell/homepage-nix";
    nixpkgs.url = "nixpkgs/nixos-21.05";  # Adjust this to your NixOS version
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, go-time, russh, homepage-nix, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in {
        packages = {
          goTime = go-time.packages.${system}.default;
          russh = russh.packages.${system}.default;
          homepage = homepage-nix.packages.${system}.default;
        };
        nixosModules = [
          homepage-nix.nixosModules.default
        ];
      }
    );
}

