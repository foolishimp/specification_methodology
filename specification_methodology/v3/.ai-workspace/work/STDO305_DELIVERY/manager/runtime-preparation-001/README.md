# STDO manager 3.0.5 runtime setup

The manager wheel is source-matched to the3.0.5 release. Dependency versions
remain independently pinned in constraints-python313.txt. The offline lock
and included wheels select CPython3.13 on macOS arm64, the qualified platform.
They include the exact manager wheel and pip26.2.1. No existing environment is
required beyond an available Python3.13 interpreter and its venv bootstrap.

For the fully locked offline setup, from this extracted directory:

```sh
python3.13 -m venv /absolute/new/manager
/absolute/new/manager/bin/python -m pip install --no-index --find-links wheels --require-hashes --no-deps -r requirements-macos-arm64-cp313.txt
/absolute/new/manager/bin/python -m pip check
```

For another platform with CPython3.13, retain the same dependency versions and
select available binary wheels from PyPI:

```sh
python3.13 -m venv /absolute/new/manager
/absolute/new/manager/bin/python -m pip install --only-binary=:all: --constraint constraints-python313.txt wheels/stdo_toolchain-3.0.5-py3-none-any.whl
/absolute/new/manager/bin/python -m pip check
```

This second path preserves package versions but selects platform-specific
artifacts; it is not the macOS artifact qualification. Record the actual
platform, interpreter, wheels and installation result for a new qualification.
The manager package itself supports Python3.11+, while this exact dependency
selection and recipe target Python3.13.

Use `/absolute/new/manager/bin/stdo --store /absolute/new/store install v3.0.5
--repository https://github.com/foolishimp/specification_methodology.git
--manifest-sha256 EXACT_RELEASE_MANIFEST_SHA256` as one command, selecting the
manifest digest from the separately published exact release asset. Local
prepublication acquisition instead explicitly names the prepared local
repository; it does not establish public acquisition.

The installed method's Getting Started and tooling guides expose all selected
components. Source custody, runtime setup, actual installed qualification,
publication and Product adoption retain their separate evidence.
