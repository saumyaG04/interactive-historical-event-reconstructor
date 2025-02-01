from pathlib import Path

env_path = Path(r"C:\Users\saumy\OneDrive\Documents\Python Projects\portfolio\interactive historical event reconstructor\test\.env")

# Read the file manually
with open(env_path, "r") as file:
    content = file.read()
    
print("Contents of .env file:")
print(content)