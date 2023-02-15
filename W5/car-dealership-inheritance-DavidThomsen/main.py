from vehicle_types import Car, Motorcycle, Truck

A=Car(10000,"Honda", "CRV", 2020,35)
print (A.miles)
print(A.purchase_price())
print(A.sale_price())
print(A)

B = Truck(10000,"MAC", "Truck", 2020, 20)
print (B.miles)
print(B.purchase_price())
print(B.sale_price())
print(B)

C = Motorcycle(10000,"Harley Davidson", "Chopper", 2020, 20)
print (C.miles)
print(C.purchase_price())
print(C.sale_price())
print(C)