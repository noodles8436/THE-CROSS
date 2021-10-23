import zipfile
import gdown
import os


if os.path.isdir('./customDetector') is False:
    print('Creating customDetector Folder...')
    os.mkdir('./customDetector')
    print('Created customDetector Folder!\n')

print('Download Custom Detection Model from Google Drive..')
URL = 'https://drive.google.com/uc?id=1SmJ6W0jZIWy4CwTkghhT6KSJ2B07bJBb'
gdown.download(URL, './customDetector/customDetector.zip', quiet=False)
print('Successfully Downloaded!\n')

print('Extract Downloaded File : customDetector.zip')
zipfile.ZipFile('./customDetector/customDetector.zip').extractall('./customDetector/')
print('Successfully Extracted!\n')

print('Remove customDetector.zip...')
os.remove('./customDetector/customDetector.zip')
print('Successfully Removed!')
