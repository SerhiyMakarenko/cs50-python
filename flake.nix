{
    description = "CS50P development shell";

    inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

    outputs = { self, nixpkgs }:
    let
        systems = [ "aarch64-darwin" "x86_64-darwin" "x86_64-linux" "aarch64-linux" ];
        forAllSystems = f:
            nixpkgs.lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});
    in
    {
        devShells = forAllSystems (pkgs:
            let
                python = pkgs.python313;
            in
            {
                default = pkgs.mkShell {
                    venvDir = "./.venv";

                    buildInputs = [
                        python
                        python.pkgs.venvShellHook
                    ];

                    postVenvCreation = ''
                        unset SOURCE_DATE_EPOCH
                        pip install --upgrade pip
                        if [ -f requirements.txt ]; then
                            pip install -r requirements.txt
                        fi
                    '';

                    postShellHook = ''
                        unset SOURCE_DATE_EPOCH
                    '';
                };
            }
        );
    };
}
