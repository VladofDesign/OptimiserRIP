from cx_Freeze import setup, Executable

setup(
    name = "MonSuperProgramme",
    version = "0.1",
    description = "N'affiche qu'une petite phrase",
    executables = [Executable("main.py")]
)