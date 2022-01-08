from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="stream-delay",
    description="Stream a file or stdin one line at a time with a delay",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/stream-delay",
    project_urls={
        "Issues": "https://github.com/simonw/stream-delay/issues",
        "CI": "https://github.com/simonw/stream-delay/actions",
        "Changelog": "https://github.com/simonw/stream-delay/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    py_modules=["stream_delay"],
    entry_points="""
        [console_scripts]
        stream-delay=stream_delay:main
    """,
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
)
