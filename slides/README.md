## Viewing Slides

See the [output directory](output/index.html)

## Building Slides

Slides are build using pandoc (https://pandoc.org). Install pandoc with your regular package manager.

Build slides (from the directory containing this README) with:
`pandoc -t s5 --self-contained -o ../docs/index.html ncss_2020.md`

_(see the pandoc manpage for other slide formats e.g. slidy, dzslides, revealjs)_
