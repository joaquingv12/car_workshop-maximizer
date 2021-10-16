class Electricidad:
    # SI TODAVIA NO EXISTE EL PRECIO(POR EJEMPLO ES UN DIA QUE TODAVIA NO HA PASADO) EL PRECIO = PRECIO_ESIMADO_MANANA DEL DIA ANTERIOR
    def __init__(self,datos):
        self.precio = datos['precio']
        self.fecha = datos['fecha']
        self.precio_estimado_manana = datos['precio_estimado_manana']
        self.porcentaje_de_subida_o_bajada = datos['porcentaje_de_subida_o_bajada']
        self.dia_semana_actual = datos['dia_semana_actual']
        self.subida_precio = datos['subida_precio']
        
    
    def precio(self):
        return self.precio
    def fecha(self):
        return self.fecha
    def precio_estimado_manana(self):
        return self.precio_estimado_manana
    def porcentaje_de_subida_o_bajada(self):
        return self.porcentaje_de_subida_o_bajada
    def dia_semana_actual(self):
        return self.dia_semana_actual
    def subida_precio(self):
        return self.subida_precio
    
