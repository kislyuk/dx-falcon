#!/usr/bin/env python

import os, sys, subprocess
import dxpy

@dxpy.entry_point('main')
def main(reads, length_cutoff, preassembly_length_cutoff, config_file=None):
    reads = [dxpy.DXFile(item) for item in reads]

    with open("input.fofn", "w") as fofn:
        for i, f in enumerate(reads):
            dxpy.download_dxfile(f.get_id(), f.name)
            fofn.write(f.name + "\n")

    if config_file:
        dxpy.download_dxfile(dxpy.DXFile(config_file).get_id(), "falcon.cfg")
            
    subprocess.check_call(["fc_run.py", "falcon.cfg"])

    raise dxpy.AppInternalError("WIP")

    assembly = dxpy.upload_local_file("assembly")

    output = {}
    output["assembly"] = dxpy.dxlink(assembly)

    return output

@dxpy.entry_point('run_script')
def run_script(script_file):
    print "run_script invoked with", script_file

dxpy.run()
