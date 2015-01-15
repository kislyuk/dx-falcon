#!/bin/bash

# E. coli
#dx build -f --run $(for i in $(dx ls "Falcon Test:/data/*.fasta" --brief); do echo "-i reads=$i"; done) --debug-on AppInternalError --yes --watch

# A. thaliana
echo dx build -f --run -i config_file="Falcon Test:/fc_run_arab.cfg" $(for i in $(dx ls "Falcon Test:/data/a.thaliana/*.fasta" --brief); do echo "-i reads=$i"; done) --debug-on AppInternalError --yes --watch
