import json
from pathlib import Path
from subprocess import call

from overturemaestro.cache import _get_local_wide_form_release_cache_directory
from overturemaestro.release_index import MINIMAL_SUPPORTED_RELEASE_VERSION

if __name__ == "__main__":
    call(["python", "overturemaps_data/utils/fetch-releases-from-s3.py"])
    releases = json.loads(Path("releases.json").read_text())["releases"]
    releases = [
        release
        for release in releases
        if not (
            _get_local_wide_form_release_cache_directory(release)
            / "release_index_content.json"
        ).exists()
        and release >= MINIMAL_SUPPORTED_RELEASE_VERSION
    ]
    print(f"{releases=}")
