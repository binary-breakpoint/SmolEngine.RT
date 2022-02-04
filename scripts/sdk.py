import gdown

SDK_VERSION = "2022.1.0"
FILE_URL = "https://drive.google.com/uc?id=1wFrE1LR7cZFk0TRPd1GNRsAXV2HS-MJk"
FILE_NAME = "SmolEngineSDK-" + SDK_VERSION
DESTINATION = FILE_NAME + ".exe"

print(FILE_NAME)
print("Download will start in a few seconds...")

gdown.download(FILE_URL, DESTINATION, quiet=False)
print("Installation...")