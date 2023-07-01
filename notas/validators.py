from django.core.exceptions import ValidationError

def validate_sem(value):
    if value !='1':
        if value!='2':
            raise ValidationError("No es una opcion permitida")

def validate_sem_len(value):
    if not len(value)<2:
       raise ValidationError('La longitud debe ser de un digito')

def validate_anio_len(value):
    if not len(value)<5:
       raise ValidationError('La longitud debe ser igual o menor de cuatro digitos')
    
