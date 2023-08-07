"""Module responsible for loading a dataset."""
import json
from typing import Any, Dict, Tuple

import pandas as pd


def process_json_file(
    file_path: str,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Process json file returning the full transactional dataset and it splitted into relational.

    Args:
        file_path: Path to the json file.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]: transacional, nf and itens dataframes.
    """
    content = read_file(file_path)
    content = json.loads(content)
    df_nf = pd.json_normalize(content).drop(columns="ItemList")
    process_data = [
        __generate_object(nf, itens)
        for nf in content
        for itens in nf.get("ItemList", {})
    ]
    df_transactional = pd.json_normalize(process_data)
    df_itens = df_transactional.iloc[:, -4:]
    return df_transactional, df_nf, df_itens


def read_file(file_path: str) -> str:
    """Method responsible for reading files.

    Args:
        file_path (str): Path where the file is.

    Returns:
        str: Content of the file.
    """
    fd = open(file_path, "r")
    content = fd.read()
    fd.close()
    return content


def __generate_object(nf: Dict[str, Any], itens: Dict[str, Any]) -> Dict[str, Any]:
    """Generate dictionary that normalize all data inside nf and itens.

    Args:
        nf (Dict[str, Any]): Nf dictionary.
        itens (Dict[str, Any]): Itens dictionary.

    Returns:
        Dict[str, Any]: Dictionary with all data.
    """
    obj = {
        "CreateDate": nf.get("CreateDate"),
        "EmissionDate": nf.get("EmissionDate"),
        "Discount": nf.get("Discount"),
        "NFeNumber": nf.get("NFeNumber"),
        "NFeID": nf.get("NFeID"),
        "ProductName": itens.get("ProductName"),
        "Value": itens.get("Value"),
        "Quantity": itens.get("Quantity"),
    }
    return obj
