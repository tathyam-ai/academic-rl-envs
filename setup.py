
##File 2: `setup.py`
from setuptools import setup, find_packages

setup(
    name="tathyam",
    version="0.0.1",
    description="Academic RL environments for AI agent evaluation",
    author="Tathyam AI",
    author_email="abc@dxy",
    url="https://github.com/tathyam-ai/academic-rl-envs",  # ✅ Removed trailing space
    packages=find_packages(),
    install_requires=[
        "gymnasium>=0.29.0",
        "docker>=6.0.0",
        "openai>=1.0.0",
        "pydantic>=2.0.0",
    ],
    python_requires=">=3.8",
)