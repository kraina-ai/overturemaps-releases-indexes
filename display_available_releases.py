import json
from pathlib import Path
from subprocess import call

# This is the release with bbox with proper naming convention
MINIMAL_SUPPORTED_RELEASE_VERSION = "2024-04-16-beta.0"

if __name__ == "__main__":
    call(["python", "overturemaps_data/utils/fetch-releases-from-s3.py"])
    releases = json.loads(Path("releases.json").read_text())["releases"]
    releases = [
        release
        for release in releases
        if not (Path("release_indexes") / release).exists()
        and release >= MINIMAL_SUPPORTED_RELEASE_VERSION
    ]
    print(f"{releases=}")
