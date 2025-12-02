'''

Dadas dos listas (contable vs. banco), detectar montos coincidentes con 
tolerancia y señalar diferencias.

'''

# Tenemos dos listas, una contable y otra de banco
contable = [100.0, 250.5, 300.0, 99.99, 68]
banco     = [100.01, 250.5, 299.99, 50.0, 88]

# Aceptamos una tolerancia del 5%
tolerancia = 0.05

# Vamos a separar en dos listas, las que coinciden y las faltantes
coinciden = []
faltantes = []

for c in contable:
    # Creamos el ciclo para ir buscando por cada monto coincidente
    match = None
    
    for b in banco:
    # Hacemos lo mismo en la cuenta de banco

        if abs(c - b) <= tolerancia:

            '''
            
            Utilizamos la función abs, para utilizar el valor absoluto entre el 
            monto que tenemos en contable con el que estamos trabajando en este 
            ciclo por la parte del banco, y si la tolerancia es mayor o igual
            al valor absoluto, entonces entra al loop.

            '''

            # El match se realiza con el monto que hay en el banco
            match = b
            break
        
    if match:
        # Si hay match, entonces se unen los montos que coinciden a la lista
        coinciden.append((c, match))

    else:
        # Por el contrario, entonces se une el monto no coincidente
        faltantes.append(c)

print("Coincidencias:", coinciden)
print("Faltantes:", faltantes)
