import sys

import pandas as pd
import pyarrow.fs as fs
import pyarrow.parquet as pq

if __name__ == "__main__":
    release_version = sys.argv[1]
    dataset = pq.ParquetDataset(
        f"overturemaps-us-west-2/release/{release_version}/",
        filesystem=fs.S3FileSystem(anonymous=True, region="us-west-2"),
    )
    df = pd.DataFrame(dict(filename=dataset.files))
    df["split_filename"] = df["filename"].str.split("/")
    df["theme"] = df["split_filename"].apply(lambda x: x[3].split("=")[1])
    df["type"] = df["split_filename"].apply(lambda x: x[4].split("=")[1])

    theme_type_pairs = list(
        df[["theme", "type"]]
        .drop_duplicates()
        .reset_index(drop=True)
        .agg("|".join, axis=1)
    )
    print(f"{theme_type_pairs=}")
