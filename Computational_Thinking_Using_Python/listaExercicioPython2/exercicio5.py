dias_uteis = int(input("dias uteis: "))
horas_trab = float(input("horas trabalhadas: "))
sal_hora = float(input("salario hora: "))

jornada_padrao = dias_uteis * 8
 #8 horas da jornada diaria de trabalho
if jornada_padrao < horas_trab:
    #tenho hora extra para calcular
    hora_extra = horas_trab - jornada_padrao
    valor_extra = hora_extra * sal_hora * 1.5 #50% do valor da hora como hora extra
    salario_total = jornada_padrao * sal_hora * valor_extra
    print("valor hora extra foi de ", valor_extra)
else:
    salario_total = horas_trab * sal_hora
    print("salario total ", salario_total)