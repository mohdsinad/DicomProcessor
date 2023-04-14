# DICOM Processor
`DicomProcessor` is a Python library that allows you to process DICOM files. It includes a `DicomProcessor` class for loading DICOM files, extracting metadata, extracting images, and converting DICOM images to JPEG format.

### Installation
To install, open your terminal and navigate to the python package directory, then run the command: `pip install .`

### Usage
The DicomProcessor can be used to do the following:
- Load DICOM images (given the study structure).
- Extract DICOM Tags into a Pandas Dataframe.
- Extract pixel data into a Numpy array.
- Convert and save individual slices to JPG images.
- Retrieve the numpy array data and a dictionary of the metadata.

An example of how to use the `DicomProcessor` class is shown below:

```python
from DicomProcessor import DicomProcessor
processor = DicomProcessor(input_dir='/path/to/dicom/files')
processor.load_images()
metadata = processor.extract_metadata()
images = processor.extract_image()
processor.convert_to_jpg(input_dir='/path/to/dicom/files',output_dir='/path/to/output/files', patient_id=None)
patient_data = processor.get_patient_data(input_dir='/path/to/dicom/files', patient_id=None)
```
Patient IDs can be passed on to `convert_to_jpg` and `get_patient_data` functions to for conversion to JPG or retrieving data for those specific patients.

### Development
If you want to contribute to the package, you can install the development requirements: `pip install -r requirements-dev.txt`

You can also run the tests from the command line from the same directory as the project and test files using `pytest`

### License
`DicomProcessor` is released under the MIT License.