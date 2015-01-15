#!/usr/bin/env python

import os, sys, subprocess, shutil, time
import dxpy

os.mkdir("falcon")
wd = os.path.join(os.getcwd(), "falcon")
subprocess.check_call(["chmod", "a+rwx", "falcon"])
os.umask(0)

@dxpy.entry_point('main')
def main(reads, length_cutoff, preassembly_length_cutoff, config_file=None):
    subprocess.check_call(["ssh-keygen", "-t", "rsa", "-N", "", "-f", "id_rsa"])
    with open("id_rsa.pub") as pubkey, open(".ssh/authorized_keys", "ab") as authorized_keys:
        authorized_keys.write(pubkey.read())

    dxpy.upload_local_file("id_rsa")

    reads = [dxpy.DXFile(item) for item in reads]

    with open(os.path.join(wd, "input.fofn"), "w") as fofn:
        for i, f in enumerate(reads):
            dxpy.download_dxfile(f.get_id(), os.path.join(wd, f.name))
            fofn.write(os.path.join(wd, f.name) + "\n")

    if config_file:
        dxpy.download_dxfile(dxpy.DXFile(config_file).get_id(), os.path.join(wd, "falcon.cfg"))

    shutil.copy("falcon.cfg", wd)
    subprocess.check_call(["fc_run.py", "falcon.cfg"], cwd=wd)

    assembly = dxpy.upload_local_file("assembly")

    output = {}
    output["assembly"] = dxpy.dxlink(assembly)

    return output

@dxpy.entry_point('run_script')
def run_script(script_file, origin_job_addr):
    dxpy.download_dxfile(dxpy.search.find_one_data_object(name="id_rsa")["id"], "id_rsa")
    subprocess.check_call(["chmod", "go-rwx", "id_rsa"])
    dxpy.download_dxfile(dxpy.DXFile(script_file).get_id(), "run.sh")
    time.sleep(1)
    subprocess.check_call(["sshfs", "-o", "StrictHostKeyChecking=no", "-o", "IdentityFile=/home/dnanexus/id_rsa", "dnanexus@{}:{}".format(origin_job_addr, wd), wd])
    subprocess.check_call("set -ex; source ../run.sh", shell=True, executable="/bin/bash", cwd=wd)

dxpy.run()
