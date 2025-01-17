import sys

from overturemaestro.cache import _get_local_release_cache_directory
from overturemaestro.release_index import _generate_release_index

if __name__ == "__main__":
    release_version = sys.argv[1]
    theme_type_tuple = sys.argv[2]
    theme_value, type_value = theme_type_tuple.split("|")
    is_generated = _generate_release_index(
        release=release_version,
        theme=theme_value,
        type=type_value,
        index_location_path=_get_local_release_cache_directory(release_version),
        verbosity_mode="verbose",
    )
    if not is_generated:
        sys.exit(1)
