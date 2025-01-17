import sys

from overturemaestro.advanced_functions.wide_form import (
    _generate_wide_form_all_column_names_release_index,
)
from overturemaestro.cache import _get_local_wide_form_release_cache_directory

if __name__ == "__main__":
    release_version = sys.argv[1]
    is_generated = _generate_wide_form_all_column_names_release_index(
        release=release_version,
        ignore_cache=True,
        index_location_path=_get_local_wide_form_release_cache_directory(
            release_version
        ),
        verbosity_mode="verbose",
    )
    if not is_generated:
        sys.exit(1)
