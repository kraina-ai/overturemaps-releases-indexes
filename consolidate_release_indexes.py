import sys

from overturemaestro.release_index import _consolidate_release_index_files

if __name__ == "__main__":
    release_version = sys.argv[1]
    is_consolidated = _consolidate_release_index_files(
        release=release_version, remove_other_files=True
    )
    if not is_consolidated:
        sys.exit(1)
