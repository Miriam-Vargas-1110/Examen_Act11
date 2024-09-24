print("clase de tienda de moda asiatica")
print("Miriam Vargas Carrillo 1110")
# crear clase clientes

class Clientes1110:

    idcliente = 0
    nombres = ""
    apellido = ""
    direccion = ""
    numero = 0
    ciudad = ""
    correo = ""

    def mostrardatos (self):
        print(f"idcliente, Nombres, Apellidos, Direccion, Numero, Ciudad, Correo.")

    def lista_idclientes1110 (self):
        clien = ["0143","3742","4843","3953","1854"]
        print("clien")
        for clien in clien:
            print(clien)

    def tupla_nombres1110 (self):
        nomb = ("Alondra","karen","sofia","Matias","Felix")
        print(nomb)
        for nomb in nomb:
            print(nomb)

    def diccionario_apellidos_numero():
        apelli = {
        "Hernandes" : "6561992393",
        "Ramirez" : "6563497654",
        "Moras" : "6566878873",
        "Corona" : "6569378726",
        "Sandoval" : "6561063874"
        }
        for x,y in apelli.items():
            print(x,y)


    def altas (self,n):
        print(f"{n} el cliente esta activo")

    def bajas (self,n):
        print(f"{n} el cliente esta dado de baja")

#crear objetos
cliente=Clientes1110()

#llamar atributos y usar objetos
cliente.idcliente=3742
print(f"id del cliente: {cliente.idcliente}")
cliente.nombres="Felix"
print(f"nombres del cliente: {cliente.nombres}")
cliente.apellido="Hernandez"
print(f"apellido del cliente: {cliente.apellido}")
cliente.direccion="calle flores"
print(f"direccion del cliente: {cliente.direccion}")
cliente.numero="6561992393"
print(f"numero del cliente: {cliente.numero}")
cliente.ciudad="Corea"
print(f"ciudad del cliente: {cliente.ciudad}")
cliente.correo="felixdestraykids@gmail.com"
print(f"correo del cliente: {cliente.correo}")

#funciones
cliente.mostrardatos()
print("\n")
cliente.lista_idclientes1110()
print("\n")
cliente.tupla_nombres1110()
print("\n")
cliente.diccionario_apellidos_numero()