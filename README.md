# Tilesizer

## Background

Tilesizer measures the average size of a tile in a set of files, weighted by weights. It is designed for tiles and accesses but could work with any type of files where you want a weighted average of size.

## Install

For local development

```sh
python3 -m venv venv
. venv/bin/activate
pip install --editable .
```

## Usage

Give tilesizer a list of files on stdin, relative to the path you give it. The list of files is in the format
`path weight`, e.g. `0/0/0 838360`.

```sh
cat access_list | tilesizer /location/of/tiles
```

Tilesizer can read from [anything PyFilesystem supports](https://www.pyfilesystem.org/page/index-of-filesystems/)

```sh
cat access_list | tilesizer s3://mybucket
```

OpenStreetMap provides statistics in the required form

```sh
curl -s 'https://planet.openstreetmap.org/tile_logs/tiles-2020-01-01.txt.xz' \
  | tilesizer /location/of/tiles
```

Use grep to filter the access list

```sh
xzgrep '^10/' tiles-2020-01-01.txt.xz | tilesizer /location/of/tiles
```

## Contributing

All code should be formatted according to flake8. Check this with `flake8 tilekiln tests`

## License

This repository is licensed under the ISC license contained in [LICENSE](LICENSE)
