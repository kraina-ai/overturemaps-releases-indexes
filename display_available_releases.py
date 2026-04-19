from overturemaestro.release_index import MINIMAL_SUPPORTED_RELEASE_VERSION, get_available_release_versions

if __name__ == "__main__":
    releases = get_available_release_versions()
    releases = [
        release
        for release in releases
        if not (
            _get_local_release_cache_directory(release) / "release_index_content.json"
        ).exists()
        and release >= MINIMAL_SUPPORTED_RELEASE_VERSION
    ]
    print(f"{releases=}")
