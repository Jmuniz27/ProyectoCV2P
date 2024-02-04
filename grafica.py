import tkinter
from tkinter import simpledialog
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from funciones import trazaConSum
# Crear una ventana emergente para solicitar el valor de A
root = tkinter.Tk()
root.withdraw()  # Ocultar la ventana principal

# Solicitar al usuario que ingrese un valor
a = simpledialog.askfloat("Valor de A", "Ingrese el valor de A:")

# Solicitar al usuario que ingrese un valor
n = simpledialog.askinteger("Valor de N", "Cuantos sub-intervalos:")

# Cerrar la ventana emergente
root.destroy()

# Validar que se haya ingresado un valor
if a is not None and n is not None:
    #print(funciones.trazaConSum(a,n))
    valorTraza = trazaConSum(a,n)
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111, projection='3d')

    def grafCilindro(a):
        # Coordenadas esféricas
        theta_ = np.linspace(0, 2*np.pi, 100)
        z_ = np.linspace(-10*a,10*a,100)
        theta, z_cili = np.meshgrid(theta_,z_)
        rho = a  # Radio del cilindro

        # Coordenadas cartesianas
        x_cili = rho * np.cos(theta)
        y_cili = rho * np.sin(theta)

        # Graficar el cilindro
        ax.plot_surface(x_cili,y_cili,z_cili, color='bisque',zorder=0,alpha=0.35)

    def grafPlano(a):
        def z(x,y):
            return (8-x-y)/2
        x_plano = np.linspace(-10*a/2,10*a/2)
        y_plano = np.linspace(-10*a/2,10*a/2)
        x_plano,y_plano = np.meshgrid(x_plano,y_plano)
        z_plano = z(x_plano,y_plano)
        ax.plot_surface(x_plano,y_plano,z_plano,color='pink',zorder=2,alpha=0.85)

    def traza(a):
        t = np.linspace(0,2*np.pi)
        expr_x = a*np.cos(t)
        expr_y = a*np.sin(t)
        expr_z = 4 - (1/2)*(expr_x+expr_y)
        ax.plot(expr_x,expr_y,expr_z,color='black',zorder=1)

    grafCilindro(a)
    grafPlano(a)
    traza(a)
    # Agregar texto dentro de la ventana de Matplotlib
    ax.text2D(0.05, 0.95, f"El valor de la traza es: {valorTraza}", transform=ax.transAxes,ha='center', va='center', fontsize=16, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.6))
    #giro
    def update(num, ax, a):
        ax.view_init(elev=num, azim=num*2)  # Cambiar la elevación y el azimut para rotar en Z

    ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), fargs=(ax, a), interval=50)

    # Configurar el aspecto del gráfico
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Calculo Traza $x^2 + y^2 = {a}^2$ y x+y+2z=8')
    # Ajustar automáticamente la escala de los ejes
    ax.auto_scale_xyz([-a*5, a*5], [-a*5, a*5], [0, a*5])
    # Rotar el gráfico para una mejor visualización inicial
    ax.legend()

    plt.show()