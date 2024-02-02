{
  description = "A flake wrapping packages and modules";

  inputs = {
    eriixvim.url = "github:erictossell/eriixvim";
    go-time.url = "github:erictossell/go-time";
    russh.url = "github:erictossell/russh";
    homepage-nix.url = "github:erictossell/homepage-nix";
    nixpkgs.url = "nixpkgs/nixos-unstable"; 
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, eriixvim, nixpkgs, flake-utils, go-time, russh, homepage-nix, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in {
        packages = {
	  eriixvim = eriixvim.packages.${system}.default;
          go-time = go-time.packages.${system}.default;
          russh = russh.packages.${system}.default;
          homepage-nix = homepage-nix.packages.${system}.homepage-nix;
        };
        nixosModules = {
          homepage-nix = homepage-nix.nixosModules.${system}.homepage-nix;
        };
      }
    );
}

