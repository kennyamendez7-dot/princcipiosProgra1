# Data

traditionalVersion = 25000
deluxeVersion = 35000
colectionistVersion = 50000
discountAmountArticles= 10
discountStudent = 5 

versionType = input('Que tipo de version esta comprando el cliente? ')

versionValue = 0

# Condiciones

if versionType == 'traditional':
    versionValue = traditionalVersion
elif versionType == 'deluxe':
    versionValue = deluxeVersion
else:
    versionValue = colectionistVersion
    
amountOfArticles = int(input('Cuántos videojuegos esta comprando? '))

subtotal = amountOfArticles * versionValue
discountAmount = 0

if amountOfArticles >= 3:
    print('Por la cantidad de videojuegos que estas comprando recibes un 10 porciento de descuento')
    discountAmount = (subtotal * discountAmountArticles)/100

subtotal2 = subtotal - discountAmount

student= input('El cliente es estudiante? ')
discountAmountStudent = 0 
if student == 'si':
    print('Por ser estudiante recibes un descuento de 5 porciento el total de la compra')
    discountAmountStudent = (subtotal2 * discountStudent)/100

#

total = subtotal2 - discountAmountStudent
print('Total a pagar es: ', total)

