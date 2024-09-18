from unittest.mock import patch

from pandas import DataFrame

from src.get_data_from_csv_or_xlsx_files import get_data_from_csv, get_data_from_xlsx


@patch("pandas.read_csv")
def test_get_data_from_csv(mock_read_csv):
    mock_read_csv.return_value = DataFrame({"key": ["value"]})
    assert get_data_from_csv("test_file") == [{"key": "value"}]


@patch("pandas.read_excel")
def test_get_data_from_xlsx(mock_read_excel):
    mock_read_excel.return_value = DataFrame({"key": ["value"]})
    assert get_data_from_xlsx("test_file") == [{"key": "value"}]
