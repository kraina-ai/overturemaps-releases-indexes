import sys

from overturemaestro.release_index import generate_release_index

if __name__ == "__main__":
    release_version = sys.argv[1]
    print(release_version)
    generate_release_index(release=release_version)
