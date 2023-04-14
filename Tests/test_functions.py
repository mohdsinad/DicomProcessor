import os
import pytest
import numpy as np
import pandas as pd
from DicomProcessor.functions import DicomProcessor

@pytest.fixture
def dicom_processor():
    input_dir = 'data\\input'
    dp = DicomProcessor(input_dir)
    return dp

def test_load_images(dicom_processor):
    files = dicom_processor.load_images()
    assert len(files) > 0
    assert all(file.endswith(".dcm") for file in files)

def test_extract_metadata(dicom_processor):
    dicom_processor.load_images()
    metadata_df = dicom_processor.extract_metadata()
    assert isinstance(metadata_df, pd.DataFrame)
    assert not metadata_df.empty

def test_extract_image(dicom_processor):
    dicom_processor.load_images()
    images = dicom_processor.extract_image()
    assert len(images) > 0
    assert all(isinstance(image, np.ndarray) for image in images)

def test_convert_to_jpg(dicom_processor):
    input_dir = 'data\\input'
    output_dir = 'data\\output'
    patient_id = '075'
    dicom_processor.convert_to_jpg(input_dir, output_dir, patient_id)
    assert os.path.exists(os.path.join(output_dir, f"{patient_id}_0.jpg"))

def test_get_patient_data(dicom_processor):
    input_dir = 'data\\input'
    patient_data = dicom_processor.get_patient_data(input_dir)
    assert isinstance(patient_data, dict)
    assert len(patient_data.keys()) > 0
    for patient_id, data in patient_data.items():
        assert isinstance(data['metadata'], list)
        assert not len(data['metadata']) == 0
        assert len(data['image']) > 0
        assert all(isinstance(image, np.ndarray) for image in data['image'])