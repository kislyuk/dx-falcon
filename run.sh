#!/bin/bash

dx build -f --run $(for i in $(dx ls "Falcon Test:/data/*.fasta" --brief); do echo "-i reads=$i"; done) --debug-on AppInternalError --yes --watch
