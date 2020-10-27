# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0]

### Added

- `create_shell_parent_env()` method to hooks to setup `parent_env` kwarg.

### Changed

- Renamed `tk-config-default2`'s `AppLaunch` class to `RezAppLaunch`.
- Slimmed down `env/*` configuration yaml files
- Cleaned up links in README


## [0.2.0]

### Added

- Substitute `{version}` in package request ([GitHub #4])
- Links in `CHANGELOG.md`
- CI for [black formatting][black]

### Changed

- [Black formatted][black] ([GitHub #5])


## [0.1.0]

### Added

- `rez_app_launch.py` hooks per `tk-config-default*` configurations.
- `tk-config-default*/env/**` example configurations folders.
- GitHub CI workflow to test patching/installing against
  official Shotgun `tk-config-default*`


[black]: https://black.readthedocs.io/en/stable/
[GitHub #5]: https://github.com/nerdvegas/rez-shotgun/pull/5
[GitHub #4]: https://github.com/nerdvegas/rez-shotgun/issues/4
[0.3.0]: https://github.com/nerdvegas/rez-shotgun/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/nerdvegas/rez-shotgun/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/nerdvegas/rez-shotgun/releases/tag/0.1.0
