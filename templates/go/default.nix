{ pkgs, lib ? pkgs.lib }:
pkgs.buildGoModule {
  pname = "go-flake"; 
  version = "0.1.0"; # Replace with your desired version
  src = ./.;
  vendorHash = null;
}

