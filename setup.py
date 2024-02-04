from cx_Freeze import setup, Executable

setup(
    name="ProyectoCV",
    version="1.0",
    description="Descripción de MiScript",
    author="Diaz,Martin,Munizaga,Sanchez",
    executables=[Executable("grafica.py", icon="iconoCV.ico")]
)
