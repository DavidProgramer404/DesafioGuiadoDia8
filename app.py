"""
MEMBRESIA
- GRATIS
- BASICA
- FAMILIAR
- SIN CONEXION 
- PRO

MEMBRASIA
- CORREO ELECTRONICO
- NUMERO DE TARJETA

CADA MEMBRASIA DEBE PERMIITR CAMBIAR ENTRE ELLAS
TIPOS DE MEMBRESIAS:
1-BASICA
2-FAMILIAR
3-SIN CONEXION (SOLO ACCESO AL SERVICIO)
4-PRO

"""


from membrasia import Membresia,Gratis,Basica,Familiar,SinConexion,Pro

m = Gratis("Correo@test.gratis.com","123456")
print(type(m))
b = m.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
s = f.cambiar_suscripcion(3)
print(type(s))
p = s.cambiar_suscripcion(4)
print(type(p))
