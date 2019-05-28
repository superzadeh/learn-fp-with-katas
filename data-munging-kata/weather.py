import pandas as pd


def load_file(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name, sep=r"\s*", index_col=None)
    # Filter out summary rows
    return df[df.Dy != "mo"]


def convert_temperature_values(column: pd.DataFrame) -> pd.DataFrame:
    return pd.to_numeric(column.apply(lambda value: value.replace("*", "")))


def compute_temperature_spead(
    temperature_max: pd.DataFrame, temperature_min: pd.DataFrame
) -> pd.DataFrame:
    return temperature_max - temperature_min


def get_smallest_temperature_spread(data: pd.DataFrame) -> int:
    data["temperature_spread"] = compute_temperature_spead(
        convert_temperature_values(data["MxT"]), convert_temperature_values(data["MnT"])
    )
    lowest_spread_row_index = data["temperature_spread"].idxmin()
    return data.iloc[lowest_spread_row_index].Dy
