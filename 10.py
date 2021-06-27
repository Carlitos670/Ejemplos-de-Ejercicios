#EJEMPLO 10
tv,v1,v2,v3,tr,c,sb=0,0,0,0,0,0,0
    sb=int(print("ingrese sueldo base : "))
    v1=int(print("valor de venta 1: "))
    v2=int(print("valor de venta 2: "))
    v3=int(print("valor de venta 3 : "))
    tv=v1+v2+v3
    c=tv*0.1
    tr=sb+c
    print("cantidad total a resivir",tr)