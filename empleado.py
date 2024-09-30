from abc import ABC, abstractmethod

# Excepción personalizada para salarios menores al mínimo
class SalarioInvalidoException(Exception):
    pass

# Clase abstracta Empleado
class Empleado_O24(ABC):
    def __init__(self, RFC, apellidos, nombres):
        self.RFC = RFC
        self.apellidos = apellidos
        self.nombres = nombres

    @abstractmethod
    def calcular_ingresos(self):
        pass

    @abstractmethod
    def calcular_sueldo_neto(self):
        pass

    def mostrar_informacion(self):
        return f"RFC: {self.RFC}, Apellidos: {self.apellidos}, Nombres: {self.nombres}"

# Clase hija EmpleadoVendedor
class EmpleadoVendedor_O24(Empleado_O24):
    def __init__(self, RFC, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(RFC, apellidos, nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision
        self.ingresos = self.calcular_ingresos()

    # Calcula ingresos basados en monto vendido y tasa de comisión
    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision

    # Calcula la bonificación según las reglas
    def calcular_bonificacion(self):
        if self.monto_vendido < 1000:
            return 0
        elif 1000 <= self.monto_vendido <= 5000:
            return 0.05 * self.ingresos
        else:
            return 0.10 * self.ingresos

    # Calcula el descuento según las reglas
    def calcular_descuento(self):
        if self.ingresos < 1000:
            return 0.11 * self.ingresos
        else:
            return 0.15 * self.ingresos

    # Calcula el sueldo neto
    def calcular_sueldo_neto(self):
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento()
        return self.ingresos + bonificacion - descuento

# Clase hija EmpleadoPermanente
class EmpleadoPermanente_O24(Empleado_O24):
    def __init__(self, RFC, apellidos, nombres, sueldo_base, seguro_social):
        super().__init__(RFC, apellidos, nombres)
        if sueldo_base < 150:
            raise SalarioInvalidoException("El sueldo base no puede ser menor a 150.")
        self.sueldo_base = sueldo_base
        self.seguro_social = seguro_social
        self.ingresos = self.sueldo_base

    # Retorna el sueldo base
    def calcular_ingresos(self):
        return self.sueldo_base

    # Calcula el descuento por afiliación del seguro social
    def calcular_descuento(self):
        return 0.11 * self.sueldo_base

    # Permite calcular el sueldo neto
    def calcular_sueldo_neto(self):
        descuento = self.calcular_descuento()
        return self.ingresos - descuento

# este codigo es para los ejemplos
empleados = [
    EmpleadoVendedor_O24("RFC633", "Ortiz", "Oscar", 3000, 0.10),
    EmpleadoPermanente_O24("RFC978", "López", "Juan", 2000, "SS12345")
]

for empleado in empleados:
    print(empleado.mostrar_informacion())
    print(f"Sueldo neto: {empleado.calcular_sueldo_neto()}")
