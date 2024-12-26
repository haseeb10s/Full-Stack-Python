from pathlib import Path

path = Path('ecommerce')  # True
print(path.exists())

path = Path('emails')  
print(path.mkdir())
print(path.rmdir())

# PyPI 