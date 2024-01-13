import sympy as sp
from sympy import init_printing
init_printing() 

# calcular integral con a = 2
def calcularIntegral(a):
    pi = sp.pi
    t= sp.symbols('t')
    dx_dt = sp.diff(a*sp.cos(t), t)
    dy_dt = sp.diff(a*sp.sin(t), t)
    dz_dt = sp.diff(4-(a/2)*(sp.cos(t)+sp.sin(t)), t)
    expr = sp.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2)
    return sp.integrate(expr,(t,0,2*pi))

def calcularTraza(a, n):
    #declaracion de variables 'symbols'
    pi = sp.pi
    t= sp.symbols('t')
    #parametrizacion de la curva
    expr_x = a * sp.cos(t)
    expr_y = a * sp.sin(t)
    expr_z = 4 - (a/2)*(sp.cos(t)+sp.sin(t))
    #derivadas con respecto a "t"
    dx_dt = sp.diff(expr_x, t)
    dy_dt = sp.diff(expr_y, t)
    dz_dt = sp.diff(expr_z, t)
    #expresion longitud de arco
    expr = sp.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2)
    resultado = 0
    #incremento
    inter = (2*pi)/n
    t_i = 0
    #punto derecho
    for i in range(1,n+1):
        resultado += expr.subs(t, t_i + (inter*i))
        t_i += inter
    longAprox = resultado*inter
    return longAprox.evalf()



def trazaConSum(a,n):
    #declaracion de variables 'symbols'
    pi = sp.pi.evalf()
    t, i= sp.symbols('t i',integer=True)
    #parametrizacion de la curva
    x = a * sp.cos(t)
    y = a * sp.sin(t)
    z = 4 - (a/2)*(sp.cos(t)+sp.sin(t))
    #derivadas con respecto a "t"
    dx_dt = sp.diff(x, t)
    dy_dt = sp.diff(y, t)
    dz_dt = sp.diff(z, t)
    #expresion longitud de arco
    expr = sp.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2)
    delta_t = 2*pi/n
    #definiendo variables Sum riemann
    t_i = i*delta_t
    f = expr.subs(t,t_i)
    #Suma de rieman
    """
    n
    ---
    \      f(t_i)*delta_t
    /
    ---
    i=1
    """
    sumt = sp.Sum(f,(i,1,n))
    return (sumt.evalf()*delta_t) 

a = 100
n = 1000
#resultado = calcularTraza(a, n)
#print(f"Resultado de la traza: {resultado}")
resultado2 = trazaConSum(a,n)
print(resultado2)