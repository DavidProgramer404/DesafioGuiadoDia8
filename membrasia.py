from abc import ABC, abstractmethod


class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self):
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)    
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)            
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)          
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)


class Gratis(Membresia):
    costo = 0
    dispositivos = 1

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)

    # MEMBRESIA = 0
    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia < 1 or nueva_membresia >4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

class Basica(Membresia):
    costo = 3000
    dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)

        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7
        elif isinstance(self, Pro):
            self.__dias_regalo = 15



    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 2 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

class Familiar(Basica):
    costo = 5000
    dispositivos = 5
    dias_regalo = 7

    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia < 3 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
        
    def modificar_control_parental(self):
        pass
class SinConexion(Basica):
    costo = 3500
    dispositivos = 2

    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia not in [1,2,4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
        

    def incrementar_cantidad_maxima_offline(self):
        pass
        
class Pro(Familiar, SinConexion):
    costo = 7000
    dispositivos = 6
    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self