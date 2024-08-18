import json
from pathlib import Path
from subprocess import call

if __name__ == "__main__":
    call(["python", "overturemaps_data/utils/fetch-releases-from-s3.py"])
    releases = json.loads(Path("releases.json").read_text())["releases"]
    releases = [
        release
        for release in releases
        if not (Path("release_indexes") / release).exists()
        and not release.startswith("2023")
    ]
    print(f"{releases=}")
