import sys

from overturemaestro.release_index import generate_release_index

if __name__ == "__main__":
    release_version = sys.argv[1]
    print(release_version)
    is_generated = generate_release_index(release=release_version)
    if not is_generated:
        sys.exit(1)
