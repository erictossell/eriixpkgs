{
  description = "A simple Go package";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils}:
    utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        {
          formatter = pkgs.nixpkgs-fmt;

          packages = {
            default = (import ./default.nix { inherit pkgs; });
          };
          devShells = {
            default = (import ./shell.nix { inherit pkgs; });             
          };
        }) // {
      templates = {
        default = {
          path = ./.;
          description = "A template for a Go project";
        };
      };

    };
}
