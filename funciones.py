import sympy as sp

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
