class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        # Garantizamos que no se consuma cantidad negativa de pepinos
        if pepinos <= 0:
            raise ValueError("La cantidad de pepinos debe ser positiva.")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):  
        # Garantizar que el tiempo de espera no sea negativo
        if tiempo_en_horas < 0:
            raise ValueError("El tiempo de espera no puede ser negativo.")
        self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        # El estómago gruñe si ha esperado al menos 1.5 horas y ha comido más de 10 pepinos
        if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
            return True

        # Nueva validación: no debería gruñir si se han comido menos de 5 pepinos
        if self.pepinos_comidos < 5:
            return False # No gruñe si se han comido muy pocos pepinos
        
        return False
        