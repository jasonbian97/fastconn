import pathlib
from setuptools import setup
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
  name="fastCfeat",
  version="0.0.1",
  description="",
  long_description=README,
  long_description_content_type="text/markdown",
  author="",
  author_email="",
  license="MIT",
  packages=["fastCfeat"],
  zip_safe=False
)