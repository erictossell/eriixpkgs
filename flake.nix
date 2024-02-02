{
  description = "A flake wrapping packages and modules";

  inputs = {
    eriixvim.url = "github:erictossell/eriixvim";
    go-time.url = "github:erictossell/go-time";
    readme-py.url = "github:erictossell/readme-py";
    russh.url = "github:erictossell/russh";
    homepage-nix.url = "github:erictossell/homepage-nix";
    nixpkgs.url = "nixpkgs/nixos-unstable"; 
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, eriixvim, nixpkgs, flake-utils, go-time, russh, homepage-nix, readme-py, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in {
        packages = {
	  eriixvim = eriixvim.packages.${system}.default;
          go-time = go-time.packages.${system}.default;
	  readme-py = readme-py.packages.${system}.default;
          russh = russh.packages.${system}.default;
          homepage-nix = homepage-nix.packages.${system}.homepage-nix;
        };
        nixosModules = {
          homepage-nix = homepage-nix.nixosModules.${system}.homepage-nix;
        };
      }
    ) // {
      templates = {
        go = {
	  path = ./templates/go-flake;
	  description = "A template for a Go flake";
	};
	rust = {
	  path = ./templates/rust-flake;
	  description = "A template for a Rust flake";
	};
	python = {
	  path = ./templates/python-flake;
	  description = "A template for a Python flake";
	};
      };
    };
}

