"""
python3 setup.py bdist_appimage
./dist/AppImageTestApp-1.0.0-x86_64.AppImage
"""

from cx_Freeze import setup, Executable


setup(
    name="AppImageTestApp",
    version="1.0.0",
    description="Of all applications, this is definitely one.",
    options={"build_exe": {}},
    executables=[Executable("main.py", base="gui")],
)
