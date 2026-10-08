'''
Kennya Mendez 
Problema 2

El programa debe calcular:
Total de horas semanales dedicadas a estas actividades.
Porcentaje del tiempo correspondiente a actividades académicas.
Utilice para calcular el porcentaje académico:
Porcentaje académico = (horas académicas ÷ total de horas) × 100

'''
horasDeClases = int(input('Cuantas horas exactas a la semana va a clases? ')) 

horasDeEstudioYTareas = int(input('Cuantas exactas horas a la semana dedica a estudiar y hacer tareas? ' )) 

horasDeTrabajoRemunerado = int(input('Cuantas horas exactas a la semana trabaja remuneradamente? ')) 

horasEnTraslados = int(input('Cuantas horas exactas a la semana dura trasladandose de un lugar a otro? '))

horasEnResponsabilidadesFamiliares = int(input('Cuantas horas exactas a la semana dedica a responsabilidades familiares? ')) 

totalHorasSemanales = horasDeClases + horasDeEstudioYTareas + horasDeTrabajoRemunerado + horasEnTraslados + horasEnResponsabilidadesFamiliares
print('El total de horas exactas semanales dedicadas a todas las actibvidades del estudiante es de: ', totalHorasSemanales)

horasAcadémicas = horasDeClases + horasDeEstudioYTareas 
print('El total de horas exactas academicas del estudiante es de: ', horasAcadémicas)

porcentajeAcadémico = (horasAcadémicas / totalHorasSemanales) * 100
print('El porcentaje total de horas semanales dedicadas las actividades academicas de estudiante es de: %', porcentajeAcadémico)

