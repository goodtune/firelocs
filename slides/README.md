## Viewing Slides

See the [output directory](output/index.html)

## Building Slides

Slides are build using pandoc (https://pandoc.org). Install pandoc with
your regular package manager.

Build slides (from the directory containing this README) with:

    pandoc -t slidy --standalone -o ../docs/index.html ncss_2020.txt

*(see the pandoc manpage for other slide formats e.g. slidy, dzslides,
revealjs)*
