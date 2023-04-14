import os
import pydicom
import numpy as np
import pandas as pd
from PIL import Image

class DicomProcessor:
    def __init__(self, input_dir, patient_id=None):
        if patient_id is None:
            self.dir = input_dir
        else:
            self.dir = os.path.join(input_dir, patient_id)
        self.patient_files = None
        self.patient_metadatas = None
        self.patient_images = None

    def load_images(self):
        self.patient_files = []
        for root, dirs, files in os.walk(self.dir):
            for file in files:
                if file.endswith(".dcm"):
                    file_path = os.path.join(root, file)
                    self.patient_files.append(file_path)
        return self.patient_files

    def extract_metadata(self):
        self.patient_metadatas = []
        for file in self.patient_files:
            metadata = {}
            ds = pydicom.dcmread(file, stop_before_pixels=True)
            for elem in ds:
                metadata[elem.name] = str(elem.value)
            self.patient_metadatas.append(metadata)
        return pd.DataFrame(self.patient_metadatas)

    def extract_image(self):
        self.patient_images = []
        for file in self.patient_files:
            ds = pydicom.dcmread(file)
            image = ds.pixel_array  # returns PixelData in the form of numpy arrays
            self.patient_images.append(image)
        return self.patient_images

    def convert_to_jpg(self, input_dir, output_dir, patient_id=None):
        if patient_id is None:
            self.dir = input_dir
            self.load_images()
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            for patient_file in self.patient_files:
                ds = pydicom.dcmread(patient_file)
                image = ds.pixel_array
                patient_id = ds.PatientID
                image = Image.fromarray(np.uint16(image)).convert('RGB')
                i = 0
                file_name = f"{patient_id}_{i}.jpg"  # create a unique file name for each image based on patient ID and counter variable
                while os.path.exists(os.path.join(output_dir, file_name)): # check if file already exists, increment counter if it does
                    i += 1
                    file_name = f"{patient_id}_{i}.jpg"
                image.save(os.path.join(output_dir, file_name))
        else:
            self.dir = os.path.join(input_dir, patient_id)
            self.load_images()
            images = self.extract_image()
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            for i, image in enumerate(images):
                image = Image.fromarray(np.uint16(image)).convert('RGB')
                image.save(os.path.join(output_dir, f"{patient_id}_{i}.jpg"))

    def get_patient_data(self, input_dir, patient_id=None):
        if patient_id is None:
            self.dir = input_dir
            self.load_images()
            self.extract_metadata()
            self.extract_image()
            data = {}
            for file in self.patient_files:
                ds = pydicom.dcmread(file, stop_before_pixels=True)
                patient_id = ds.PatientID
                data[patient_id] = {'metadata': self.patient_metadatas, 'image': self.patient_images}
        else:
            self.dir = os.path.join(input_dir, patient_id)
            self.load_images()
            self.extract_metadata()
            self.extract_image()
            data = {patient_id: {'metadata': self.patient_metadatas, 'image': self.patient_images}}
        return data