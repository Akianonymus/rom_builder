# Copyright (C) 2019 baalajimaestro
# Licensed under the GNU GPL v3.0 License
# you may not use this file except in compliance with the License.
#
## Python backend to workaround for unofficial builds
## This would just clone all deps from the dependencies even when its an unofficial build

import json
import os
import subprocess


deps = json.loads(open("device/"+os.environ.get("oem")+"/"+os.environ.get("device")+"/"+os.environ.get("rom_vendor_name")+".dependencies").read())


for i in deps:
    repo = i["repository"]
    path = i["target_path"]
    branch = i["branch"]
    remote = i["remote"]
    clone_cmd = "git clone https://"
    if remote == "github":
        clone_cmd += "github"
    elif remote == "gitlab":
        clone_cmd += "gitlab"
    else:
        raise Exception("Remote Derped!!")
    clone_cmd += ".com/"
    clone_cmd += repo
    clone_cmd += " -b "
    clone_cmd += branch
    clone_cmd += " "
    clone_cmd += path
    clone_cmd += " --depth=1"
    print("Cloning Repository "+repo)
    clone = subprocess.run(clone_cmd.split(" "), stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(clone.stdout.decode().strip(),clone.stderr.decode().strip())
