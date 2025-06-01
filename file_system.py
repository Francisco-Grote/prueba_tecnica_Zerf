'''
Se pide modelar un file system similar al de Linux. El file system debe poder
ejecutar los siguientes comandos:
● cd(dirName): recibe por parámetro una ruta y posiciona al usuario en la
misma. Además, si el parámetro es “..”, se debe volver hacia la ruta anterior.
● touch(fileName): recibe el nombre del archivo a crear y lo crea en el
directorio en donde el usuario se encuentra
● ls(): lista los archivos y carpetas del directorio en donde el usuario se
encuentra
● mkdir(dirName): recibe por parámetro el nombre de una carpeta y la crea
● pwd(): imprime por pantalla el nombre de la ruta en donde el usuario se
# encuentra

El ejercicio debe resolverse como máximo en 2 horas. Puede utilizarse cualquier
lenguaje de programación y paradigma. Puede realizarse en pseudo código.
No se pueden utilizar las funciones propias del filesystem para hacerlo, ni
tampoco se deben crear realmente los archivos y directorios.
Cualquier definición tomada más allá de lo que dice el enunciado debe dejarse
por escrito
'''

# Simulación de un sistema de archivos en memoria similar a Linux

class Directorio:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre
        self.subdirectorios = {}  # Diccionario para almacenar subdirectorios
        self.archivos = set()     # Conjunto para almacenar nombres de archivos

class SistemaDeArchivos:
    def __init__(self):
        self.raiz = Directorio("/")
        self.actual = self.raiz

    def crear_directorio(self, nombre_directorio):
        """Crea un nuevo subdirectorio en el directorio actual."""
        if nombre_directorio in self.actual.subdirectorios:
            print(f"Error: El directorio '{nombre_directorio}' ya existe en '{self.actual.nombre}'.")
        else:
            nuevo_directorio = Directorio(nombre_directorio, self.actual)
            self.actual.subdirectorios[nombre_directorio] = nuevo_directorio
            print(f"Directorio '{nombre_directorio}' creado exitosamente en '{self.actual.nombre}'.")

    def crear_archivo(self, nombre_archivo):
        """Crea un nuevo archivo en el directorio actual."""
        if nombre_archivo in self.actual.archivos:
            print(f"Error: El archivo '{nombre_archivo}' ya existe en '{self.actual.nombre}'.")
        else:
            self.actual.archivos.add(nombre_archivo)
            print(f"Archivo '{nombre_archivo}' creado exitosamente en '{self.actual.nombre}'.")

    def listar_contenido(self):
        """Lista el contenido del directorio actual."""
        print(f"Contenido de '{self.actual.nombre}':")
        for nombre in sorted(self.actual.subdirectorios):
            print(f"  [D] {nombre}")
        for nombre in sorted(self.actual.archivos):
            print(f"  [A] {nombre}")

    def cambiar_directorio(self, nombre_directorio):
        """Cambia al directorio especificado."""
        if nombre_directorio == "..":
            if self.actual.padre:
                self.actual = self.actual.padre
                print(f"Cambiado al directorio padre: '{self.actual.nombre}'.")
            else:
                print("Error: Ya estás en el directorio raíz.")
        elif nombre_directorio in self.actual.subdirectorios:
            self.actual = self.actual.subdirectorios[nombre_directorio]
            print(f"Cambiado al directorio: '{self.actual.nombre}'.")
        else:
            print(f"Error: El directorio '{nombre_directorio}' no existe en '{self.actual.nombre}'.")

    def mostrar_ruta_actual(self):
        """Muestra la ruta completa del directorio actual."""
        ruta = []
        actual = self.actual
        while actual is not None:
            ruta.append(actual.nombre)
            actual = actual.padre
        ruta.reverse()
        print("Ruta actual:", "/".join(ruta))

# Prueba manual del sistema de archivos en memoria
fs = SistemaDeArchivos()
fs.crear_directorio("documentos")
fs.cambiar_directorio("documentos")
fs.crear_archivo("cv.pdf")
fs.crear_archivo("proyecto.docx")
fs.crear_directorio("fotos")
fs.listar_contenido()  
fs.cambiar_directorio("..")
fs.mostrar_ruta_actual() 
