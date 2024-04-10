import glob
import json
import os
import random

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import rasterio
import requests
from rasterio import features


def df_to_nested_dict(df):
    """Convert a dataframe to a nested dict. Taken from here:
    https://stackoverflow.com/a/19900276/505698
    """
    d = {}
    for row in df.values:
        here = d
        for elem in row[:-2]:
            if elem not in here:
                here[elem] = {}
            here = here[elem]
        here[row[-2]] = row[-1]

    return d


def class_definition_from_df_deprecated(
    df, name, out_fold=None, version=1, org="NIVA", desc="", colour_dict=None
):
    """NOTE: This function is deprecated, but it's kept here for backwards-compatibility with
    early versions of the class hierarchy (< v1.0). For versions 1.0 and up, use the new
    'class_definition_from_df' function instead.

    Create a hierarchical class definition file for ArcGIS Pro from
    an Excel table. Assumes the table has three levels (columns A to C),
    each more detailed than the last. The fourth column (D) should
    contain class descriptions for the most detailed level (level 3). For
    example:
    |    **A**    |      **B**      |      **C**      |                      **D**                     |
    |:-----------:|:---------------:|:---------------:|:----------------------------------------------:|
    | **Level_1** |   **Level_2**   |   **Level_3**   |                 **Level3_Desc**                |
    |:-----------:|:---------------:|:---------------:|:----------------------------------------------:|
    |    ALGAE    |       RED       |      PALPA      |             Palmaria palmata (søl)             |
    |    ALGAE    |       RED       |      VERLA      | Vertebrata lanosa (grisetangdokke/trøffeltang) |
    |    ALGAE    |       TURF      |       TURF      |             Unspecified turf (lurv)            |
    |    MAERL    |      MAERL      |      MAERL      |     Unspecified maerl (rugl, Lithothamnion)    |
    |    URCHIN   |      URCHIN     |      ECHES      |       Echinus esculentus (rød kråkebolle)      |
    |  BEACHCAST  | BEACHCAST_BROWN | BEACHCAST_BROWN |      Unspecified, dried seaweed (Tangvoll)     |
    |  BEACHCAST  | BEACHCAST_ANGIO | BEACHCAST_ANGIO |    Unspecified, dried seagass (sjøgressvoll)   |
    |    ANGIO    |      ANGIO      |      ZOSMA      |            Zostera marina (ålegras)            |
    A two digit code between 10 and 99 will be assigned sequentially to
    each class in each level. For example, level 1 classes are numbered
    10, 11, 12...; level 2 classes within level 1 class 10 are
    numbered 1010, 1011, 1012...; level 3 classes within level 2 class
    12 are numbered 101210, 101211, 101212...
    Args
        df:          Dataframe defining class hierarchy. See example above
        name:        Str. Name of class definition file to create
        out_fold:    Str or None. Default None. Folder in which to save output
                     file
        version:     Int. Default. ArcGIS Pro schema version
        org:         Str. Default ''. Name of organisation responsible for
                     class file
        desc:        Str. Default ''. High level description  for class file
        colour_dict: Dict or None. Default None. Nested dict in form
                     {0: {}, 1: {}, 2: {}} where 0, 1, 2 are the level
                     indexes for levels 1, 2 and 3, and the nested dicts
                     map class labels to Hex colour codes
    Returns
        None. A class definition file named '{name}.ecs' is saved to the folder specified (or
        to the  working directory, if 'out_fold' is None).
    """
    assert df.shape[1] == 4, "'df' must have four columns."
    assert pd.isna(df).sum().sum() == 0, "'df' contains missing values."

    # Top-level data structure for .ecs file
    data = {
        "version": version,
        "name": name,
        "organization": org,
        "description": desc,
        "classDefs": [],
    }

    # Build hierarchy for classes. If colour_dict is provided, use the colour
    # specified. If no colour is specified for a class, preferentially use the
    # colour for the parent class (if defined), and then the grandparent. If no
    # colour is defined at any level, choose a random hex colour
    r = lambda: random.randint(0, 255)
    class_data = df_to_nested_dict(df)
    for idx1, (lev1, lev2_dict) in enumerate(class_data.items()):
        lev1_id = str(idx1 + 10)

        if colour_dict:
            col1 = colour_dict[0].get(lev1, None)
            if col1 is None:
                col1 = "#%02X%02X%02X" % (r(), r(), r())
        else:
            col1 = "#%02X%02X%02X" % (r(), r(), r())

        lev1_dict = {
            "classVal": int(lev1_id),
            "alias": lev1_id,
            "name": lev1,
            "color": col1,
            "description": "",
            "subclasses": [],
        }
        data["classDefs"].append(lev1_dict)

        for idx2, (lev2, lev3_dict) in enumerate(lev2_dict.items()):
            lev2_id = lev1_id + str(idx2 + 10)

            if colour_dict:
                col2 = colour_dict[1].get(lev2, None)
                if col2 is None:
                    col2 = colour_dict[0].get(lev2, None)
                    if col2 is None:
                        col2 = "#%02X%02X%02X" % (r(), r(), r())
            else:
                col2 = "#%02X%02X%02X" % (r(), r(), r())

            lev2_dict = {
                "classVal": int(lev2_id),
                "alias": lev2_id,
                "name": lev2,
                "color": col2,
                "description": "",
                "subclasses": [],
            }
            lev1_dict["subclasses"].append(lev2_dict)

            for idx3, (lev3, lev3_desc) in enumerate(lev3_dict.items()):
                lev3_id = lev2_id + str(idx3 + 10)

                if colour_dict:
                    col3 = colour_dict[2].get(lev3, None)
                    if col3 is None:
                        col3 = colour_dict[1].get(lev3, None)
                        if col3 is None:
                            col3 = colour_dict[0].get(lev3, None)
                            if col3 is None:
                                col3 = "#%02X%02X%02X" % (r(), r(), r())
                else:
                    col3 = "#%02X%02X%02X" % (r(), r(), r())

                lev3_dict = {
                    "classVal": int(lev3_id),
                    "alias": lev3_id,
                    "name": lev3,
                    "color": col3,
                    "description": lev3_desc,
                    "subclasses": [],
                }
                lev2_dict["subclasses"].append(lev3_dict)

    if out_fold:
        fpath = os.path.join(out_fold, f"{name}.ecs")
    else:
        fpath = f"{name}.ecs"
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def class_definition_from_df(df, name, out_fold=None, version=1, org="NIVA", desc=""):
    """Create a hierarchical class definition file for ArcGIS Pro from an Excel table.
    Assumes the table has three levels, each more detailed than the last. The expected
    format in Excel is:

    |     **A**     |     **B**     |     **C**     |                      **D**                     |     **E**    |     **F**    |     **G**    |
    |:-------------:|:-------------:|:-------------:|:----------------------------------------------:|:------------:|:------------:|:------------:|
    | **lev1_name** | **lev2_name** | **lev3_name** |                  **lev3_desc**                 | **lev1_hex** | **lev2_hex** | **lev3_hex** |
    |     ALGAE     |      RED      |     VERLA     | Vertebrata lanosa (grisetangdokke/trøffeltang) |    #996633   |    #CF4D50   |    #47223E   |
    |     ALGAE     |      TURF     |      TURF     |             Unspecified turf (lurv)            |    #996633   |    #779A7F   |    #779A7F   |
    |     ANGIO     |     ANGIO     |     ZOSMA     |            Zostera marina (ålegras)            |    #A7FD67   |    #A7FD67   |    #A7FD67   |
    |     MAERL     |     MAERL     |     MAERL     |            Maerl (løstliggende rugl)           |    #CAA2A9   |    #CAA2A9   |    #CAA2A9   |
    |     URCHIN    |     URCHIN    |     ECHES     |       Echinus esculentus (rød kråkebolle)      |    #868509   |    #868509   |    #ED7D31   |
    |     URCHIN    |     URCHIN    |     GRAAC     |   Gracilechinus acutus (langpiggsjøpiggsvin)   |    #868509   |    #868509   |    #C98C58   |
    |    STARFISH   |    STARFISH   |     OPHNI     |     Ophiocomina nigra (svart slangestjerne)    |    #80258F   |    #80258F   |    #80258F   |
    |    STARFISH   |    STARFISH   |     ASTRU     |       Asterias rubens (vanlig korstroll)       |    #80258F   |    #80258F   |    #BE4BD1   |

    A two digit code between 10 and 99 will be assigned sequentially to each class in
    each level. For example, level 1 classes are numbered 10, 11, 12...; level 2
    classes within level 1 class 10 are numbered 1010, 1011, 1012...; level 3
    classes within level 2 class 12 are numbered 101210, 101211, 101212...

    Args
        df:          Dataframe defining class hierarchy. See example above.
        name:        Str. Name of class definition file to create.
        out_fold:    Str or None. Default None. Folder in which to save output file.
        version:     Int. Default 1. ArcGIS Pro schema version.
        org:         Str. Default ''. Name of organisation responsible for class file.
        desc:        Str. Default ''. High level description for class file.

    Returns
        None. A class definition file named '{name}.ecs' is saved to the folder
        specified (or to the  working directory if 'out_fold' is None).
    """
    # Validate input
    req_cols = (
        "lev1_name",
        "lev2_name",
        "lev3_name",
        "lev3_desc",
        "lev1_hex",
        "lev2_hex",
        "lev3_hex",
    )
    if tuple(df.columns) != req_cols:
        raise KeyError(f"'df' must have columns: {req_cols}.")
    if pd.isna(df).sum().sum() > 0:
        raise ValueError("'df' contains missing values.")

    # Create id columns
    df = df.sort_values(by=["lev1_name", "lev2_name", "lev3_name"])
    df["lev1_id"] = df["lev1_name"].astype("category").cat.codes + 10
    df["lev2_id"] = (
        df.groupby("lev1_name")["lev2_name"].transform(
            lambda x: x.astype("category").cat.codes
        )
        + 10
    )
    df["lev3_id"] = (
        df.groupby(["lev1_name", "lev2_name"])["lev3_name"].transform(
            lambda x: x.astype("category").cat.codes
        )
        + 10
    )

    # Format ids
    df["lev1_id"] = df["lev1_id"].apply(lambda x: str(x).zfill(2))
    df["lev2_id"] = df["lev1_id"] + df["lev2_id"].apply(lambda x: str(x).zfill(2))
    df["lev3_id"] = df["lev2_id"] + df["lev3_id"].apply(lambda x: str(x).zfill(2))

    # Top-level data structure for .ecs file
    data = {
        "version": version,
        "name": name,
        "organization": org,
        "description": desc,
        "classDefs": [],
    }

    for lev1, lev1_group in df.groupby("lev1_id"):
        lev1_dict = {
            "classVal": lev1,
            "alias": str(lev1),
            "name": lev1_group["lev1_name"].iloc[0],
            "color": lev1_group["lev1_hex"].iloc[0],
            "description": "",
            "subclasses": [],
        }
        for lev2, lev2_group in lev1_group.groupby("lev2_id"):
            lev2_dict = {
                "classVal": lev2,
                "alias": str(lev2),
                "name": lev2_group["lev2_name"].iloc[0],
                "color": lev2_group["lev2_hex"].iloc[0],
                "description": "",
                "subclasses": [],
            }
            for _, row in lev2_group.iterrows():
                lev3_dict = {
                    "classVal": row["lev3_id"],
                    "alias": str(row["lev3_id"]),
                    "name": row["lev3_name"],
                    "color": row["lev3_hex"],
                    "description": row["lev3_desc"],
                    "subclasses": [],
                }
                lev2_dict["subclasses"].append(lev3_dict)
            lev1_dict["subclasses"].append(lev2_dict)
        data["classDefs"].append(lev1_dict)

    if out_fold:
        fpath = os.path.join(out_fold, f"{name}.ecs")
    else:
        fpath = f"{name}.ecs"
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_class_codes(url):
    """Build a dataframe of class labels from an ArcGIS Pro class definition file (.ecs). hosted
    on GitHub. Assumes a hierarchical class definition file originally created from Excel using
    'class_definition_from_df'. Returns a dataframe with the codes, names and colours for each
    level in the .ecs file.

    Args
        url: Str. Raw URL of class definition file (.ecs) on GitHub created using
            'class_definition_from_df'

    Returns
        Dataframe.

    Raises
        ValueError if URL does not end in '.ecs'.
    """
    if not url.endswith(".ecs"):
        raise ValueError("'url' must be a '.ecs' file.")

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to read URL: {response.status_code}")
    data = json.loads(response.text)

    class_dict = {
        "code": [],
        "name": [],
        "desc": [],
        "colour": [],
    }

    def process_subclasses(subclasses):
        for subclass in subclasses:
            class_dict["code"].append(subclass["alias"])
            class_dict["name"].append(subclass["name"])
            class_dict["desc"].append(subclass["description"])
            class_dict["colour"].append(subclass["color"])
            if "subclasses" in subclass:
                process_subclasses(subclass["subclasses"])

    # Recursively process levels in the ECS file
    process_subclasses(data["classDefs"])

    df = pd.DataFrame(class_dict)

    return df


def merge_shapefiles(shp_fold):
    """Merges all shapefiles in 'shp_fold' by stacking and then dissolving
    on the 'Classcode' field. 'shp_fold' should contain ONLY annotation
    shapefiles for a single area of interest generated by ArcGIS Pro.
    Args
        shp_fold: Str. Path to folder containing shapefiles
    Returns
        Geodataframe.
    """
    search_path = os.path.join(shp_fold, "*.shp")
    flist = glob.glob(search_path)
    gdf_list = [gpd.read_file(fpath) for fpath in flist]
    gdf = pd.concat(gdf_list, ignore_index=True)
    gdf = gdf.dissolve(by="Classcode").reset_index()

    return gdf


def split_every_n(class_str, n=2):
    """Split a string every n characters and return the part from the start
    to the split.
    """
    return [class_str[0 : i + n] for i in range(0, len(class_str), n)]


def rebuild_class_hierarchy(gdf, class_def_path):
    """ArcGIS Pro merges hierarchical annotation and only stores a single
    class label in a field named 'Classcode'. The function
    'class_definition_from_df' embeds a hierarchical code that can be used
    afterwards to rebuild the hierarchy afterwards.
    Args
        gdf:            Geodataframe. Merged annotation from ArcGIS Pro
        class_def_path: Str. Path to class definition file (.ecs) created
                        using 'class_definition_from_df'
    Returns
        Geodataframe. Copy of 'gdf' with new columns added and unnecessary
        ones removed.
    """
    gdf = gdf.copy()

    # Pad the class code with '--' for cases where detailed levels are missing
    gdf["Classcode"] = gdf["Classcode"].str.ljust(6, "-")

    # Create columns for hierarchical codes
    gdf["lev1_code"], gdf["lev2_code"], gdf["lev3_code"] = zip(
        *gdf["Classcode"].apply(split_every_n)
    )

    # Read class definitions
    df = get_class_codes(class_def_path)

    # Join
    for level in range(1, 4):
        cols = ["code", "name"]
        if level == 3:
            cols.append("desc")
        lev_df = df[cols].copy()
        lev_df.rename(
            {
                "code": f"lev{level}_code",
                "name": f"lev{level}_name",
                "desc": f"lev{level}_desc",
            },
            inplace=True,
            axis="columns",
        )
        gdf = gdf.merge(lev_df, how="left", on=f"lev{level}_code")

    # Dissolve
    gdf = gdf.dissolve(by=["subarea_id", "lev3_code"]).reset_index()

    # Tidy
    cols = [
        "subarea_id",
        "lev1_code",
        "lev2_code",
        "lev3_code",
        "lev1_name",
        "lev2_name",
        "lev3_name",
        "lev3_desc",
        "RED",
        "GREEN",
        "BLUE",
        "geometry",
    ]
    gdf = gdf[cols]
    gdf.columns = [col.lower() for col in cols]

    return gdf


def annotation_to_raster(gpkg_path, snap_raster_path, level, anno_raster_path):
    """Convert annotation from a SeaBee annotation geopackage to a raster.

    Args
        gpkg_path:        Str. Path to geopackage containing annotation.
        sanp_raster_path: Str. Path to original image mosaic (used as the
                          "snap raster")
        level:            Int. Either 1, 2 or 3. Level in the annotation
                          hierarchy to convert
        anno_raster_path: Str. GeoTiff to be created.

    Returns
        Geodataframe. A new raster is created. Vector annotations for the
        level of interest are returned.
    """
    assert level in (1, 2, 3), "'level' must be 1, 2 or 3."
    assert (
        anno_raster_path[-4:] == ".tif"
    ), "'anno_raster_path' should be a '.tif' file."

    # Open the "snap raster" and get output properties
    dtype_dict = {1: "uint8", 2: "uint16", 3: "uint32"}
    with rasterio.open(snap_raster_path) as src:
        meta = src.meta.copy()
        meta.update(
            compress="lzw", count=1, nodata=0, dtype=dtype_dict[level], driver="GTiff"
        )
        crs = meta["crs"]

    # Reproject annotation to same CRS and get data for the 'level' of interest
    gdf = gpd.read_file(gpkg_path, layer="annotation")
    gdf = gdf.to_crs(crs)
    gdf.dropna(subset=f"lev{level}_name", inplace=True)
    gdf[f"lev{level}_code"] = gdf[f"lev{level}_code"].astype(int)

    # Rasterize
    with rasterio.open(anno_raster_path, "w+", **meta) as dst:
        out_arr = dst.read(1)
        shapes = (
            (geom, value) for geom, value in zip(gdf.geometry, gdf[f"lev{level}_code"])
        )
        burned = features.rasterize(
            shapes=shapes, fill=0, out=out_arr, transform=dst.transform
        )
        dst.write_band(1, burned)

    return gdf