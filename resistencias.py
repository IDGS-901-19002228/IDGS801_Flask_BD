class Resistencia():
    
    def calcular(self, form):  
        form = form.data
        min = 0
        max = 0
        suma = (int(form['banda1']) * 10 + int(form['banda2'])) * 10 ** int(form['multiplicador'])
          
        if form['tolerancia'] == '1':
            min = suma - (suma * .05)
            max = suma + (suma * .05)
        else:
            min = suma - (suma * .10)
            max = suma + (suma * .10)
        return {'tot': suma, 'min': min, 'max': max}
    
    def setColor(self, color):
        colores = {
            0: "#000000",
            1: "#541204",
            2: "#E80B2C",
            3: "#F48421",
            4: "#F4F21E",
            5: "#0B9E0B",
            6: "#0B3EE8",
            7: "#8B0BE8",
            8: "#808080",
            9: "#FFFFFF"
        }
        color = int(color)
        color = colores.get(color)
        
        return color
    
    
    def setTolerancia(self, color):
        colores = {
            1: "#FFD700",
            2: "#C0C0C0"
        }
        color = int(color)
        color = colores.get(color)        
        
        return color