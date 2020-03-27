import os
clear=lambda: os.system("clear")
class mercado():
  def __init__(self):
    self.productos={}
    self.cantidad=0
    self.pago=0
    self.vueltas=0
    self.subtotal=0
    self.total=0
    self.cambioexacto=0
    self.compra={}
    self.nombreUser = ""
    self.descripcion = "" 
    self.valor = ""


  def __del__(self):
    pass

  def imprimir(self):
      print("Listado completo de productos:")
      for codigo in self.productos:
          print(codigo,self.productos[codigo])

  def consulta(self,f):
    with open(f, 'r') as lector:
      if f:
        for linea in lector:
          valores = linea.split(",")
          self.nombre = valores[0]
          self.cantidad = int(valores[1])
          i = None
          for x in self.productos:
            if self.nombre == x:
              self.subtotal =self.productos[self.nombre]*self.cantidad
              self.total+=self.subtotal
              self.compra.update({self.nombre:(self.cantidad,self.subtotal)})
              i=1
          if not i:
            print("El valor ingresado no existe")
        print("Total a pagar: ",self.total)
    """
    ciclo='s'
    while ciclo=="s":
      self.nombre =input("Ingrese el producto que desea llevar: ")
      i = None
      for x in self.productos:
        if self.nombre == x:
          print(self.nombre," ",self.productos[self.nombre])
          print("Ingrese la cantidad de %s desea llevar: "%(self.nombre))
          self.cantidad =int(input(" ")) 
          self.subtotal =self.productos[self.nombre]*self.cantidad
          ciclo=input("Desea comprar otro producto[s/n]?")
          self.total+=self.subtotal
          print("Su carrito lleva un valor de: ",self.total)
          i=1
          self.compra.update({self.nombre:(self.cantidad,self.subtotal)})
      if not i:
        print("El valor ingresado no existe")
    """

  def archivo(self, f):
    
    with open(f, 'r') as lector:
      if f:
        for linea in lector:
          linea = linea[:-1] 
          self.productos.update({linea.split(",")[0] : int(linea.split(",")[1])})

  def devolver(self):
    demoni = [100000,50000,20000,10000,5000,2000,1000,500,200,100,50]
    self.pago=int(input("Ingrese el valor del pago: "))
    if self.pago >= self.total:
      self.vueltas = self.pago-self.total 
    print ('sus vueltas son: ',self.vueltas)
    self.cambioexacto=self.vueltas
    for a in demoni:
      billete = self.vueltas // a  
      self.vueltas = self.vueltas % a 
      if a >= 1000 and billete> 0 :
        print ('son: ',billete,' billetes de ',a)
      if a < 1000 and billete> 0 :
        print ('son: ',billete,' monedas de ',a)  

  def datos_cliente(self):
    self.nombreUser=input("Ingrese su nombre %s : "%(self.nombreUser))   

  def tickete(self):
    pausa=input("presione Enter para generar su factura")
    clear()
    print("Su mercado del dia de hoy ",self.nombreUser)
    print(" ")
    print("Detalle de productos:")
    print("Nombre \t \tCantidad \t \tPrecioU \t \tValor")
    #print (self.compra)
    for y in self.compra:
      print("%s \t \t%s \t \t%s \t \t%s "%(y,self.compra[y][0],self.productos[y],self.compra[y][1]))
      #print(y,self.cantidad,self.compra[y])
      #print(self.productos[y],self.cantidad,self.subtotal)
    print("Total de la compra ",self.total)
    print("El valor de su pago ",self.pago)
    print("Su cambio ",self.cambioexacto)
    print ("")
    print ("El total de su compra es : ",self.total)
 
  

#nombre_producto,valor_unitari,unidades, valor_unitario * unidades 

a= mercado()
archivo = './file.txt'
archivo2 = './compras.txt'
a.archivo(archivo)
a.imprimir()
a.consulta(archivo2)
a.devolver()
a.datos_cliente()
a.tickete()