"""Unit tests for ML_Used_Cars_Valuation_Model."""
import pytest
from unittest.mock import patch, MagicMock
import pipeline


def test_load_dataset_missing():
    with pytest.raises(FileNotFoundError):
        pipeline.load_dataset("non_existent_data_file_99.csv")


def test_cli_parsing():
    with patch("pipeline.train_and_evaluate") as mock_train:
        with patch("sys.argv", ["pipeline.py", "--data", "used_cars_powerful.csv"]):
            pipeline.main()
            assert mock_train.called
