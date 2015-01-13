#!/usr/bin/env python

import os
import dxpy

@dxpy.entry_point('main')
def main(reads, length_cutoff, preassembly_length_cutoff, config_file=None):
    reads = [dxpy.DXFile(item) for item in reads]

    for i, f in enumerate(reads):
        dxpy.download_dxfile(f.get_id(), "reads-" + str(i))

    if config_file:
        dxpy.download_dxfile(dxpy.DXFile(config_file).get_id(), "falcon.cfg")

    subprocess.check_call(["fc_run.py", "falcon.cfg"])

    raise dxpy.AppInternalError("WIP")

    assembly = dxpy.upload_local_file("assembly")

    output = {}
    output["assembly"] = dxpy.dxlink(assembly)

    return output

dxpy.run()
