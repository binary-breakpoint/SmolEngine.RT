import gdown

url = 'https://drive.google.com/uc?id=1dZYsqVcZj53h_k4a-9DSe59bHuQdeS6d'
output = 'SmolEngineSDK-2021.1.0.exe'
print("SmolEngineSDK-2021.1.0")
print("Download will start in a few seconds...")
gdown.download(url, output, quiet=False)
print("Installation...")