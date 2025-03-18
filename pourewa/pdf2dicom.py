import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian
import sys

def pdf_to_dicom(pdfFilePath, templateDicomFilePath, dicomOutFilePath):
    with open(pdfFilePath, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    meta = FileMetaDataset()
    meta.MediaStorageSOPClassUID = "1.2.840.10008.5.1.4.1.1.104.1"  # Encapsulated PDF Storage
    meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
    meta.TransferSyntaxUID = ExplicitVRLittleEndian

    ds = Dataset()
    ds.file_meta = meta
    ds.SOPClassUID = meta.MediaStorageSOPClassUID
    ds.SOPInstanceUID = meta.MediaStorageSOPInstanceUID
    ds.Modality = "OT"  # Other
    ds.PatientName = "Test^Patient"
    ds.PatientID = "123456"
    ds.EncapsulatedDocument = pdf_bytes
    ds.MIMETypeOfEncapsulatedDocument = "application/pdf"

    ds.is_little_endian = True
    ds.is_implicit_VR = False

    ds.save_as(dicom_path, write_like_original=False)
    print(f"Saved {dicom_path}")
