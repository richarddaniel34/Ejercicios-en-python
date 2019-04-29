print ("TU PESO EN OTROS PLANETAS")
""" Peso en Mercurio es: G=3.7 m/seg2
    Peso en Venus es: G=8.87 m/seg2
    Peso en Tierra es: G=9.8 m/seg2
    Peso en Marte es: G=3.7 m/seg2
    Peso en Jupiter es: G=24.8 m/seg2
    Peso en Saturno es: G=10.44 m/seg2
    Peso en Urano es: G=8.87 m/seg2
    Peso en Neptuno es: G=11.15 m/seg2
    Peso en pluton es: G=0.62 m/seg2 OJO (Aunque pluton no sea considerado un planeta)
    seg2 = segundo al cuadrado"""

#-----------------DECLARACION DE VARIABLES--------------------
pesoUsuario=int(input(" ¿Cual es tu Peso? "))
planeta=int(input("Elige tu planeta: \n 1. Mercurio\n 2. Venus\n 3. Tierra\n 4. Marte\n 5. Jupiter\n 6. Saturno\n 7. Urano\n 8. Neptuno\n 9. Pluton \n "))
gravedadMercurio=float(3.7)
gravedadVenus=float(8.87)
gravedadTierra=float(9.8)
gravedadMarte=float(3.7)
gravedadjupiter=float(24.8)
gravedadSaturno=float(10.44)
gravedadUrano=float(8.87)
gravedadNeptuno=float(11.15)
gravedadPluton=float(0.62)
pesoFinal=int()
nombrePlaneta=("")
#------------------------------------------------------------

#------------------------CONDICIONES-------------------------
if (planeta==1):
    pesoFinal=pesoUsuario*gravedadMercurio//gravedadTierra
    nombrePlaneta=("Mercurio")

elif (planeta==2):
    pesoFinal=pesoUsuario*gravedadVenus//gravedadTierra
    nombrePlaneta=("Venus")

elif (planeta==3):
    pesoFinal=pesoUsuario
    nombrePlaneta=("Tierra")

elif (planeta==4):
    pesoFinal=pesoUsuario*gravedadMarte//gravedadTierra
    nombrePlaneta=("Marte")

elif (planeta==5):
    pesoFinal=pesoUsuario*gravedadjupiter//gravedadTierra
    nombrePlaneta=("Jupiter")

elif (planeta==6):
    pesoFinal=pesoUsuario*gravedadSaturno//gravedadTierra
    nombrePlaneta=("Saturno")

elif (planeta==7):
    pesoFinal=pesoUsuario*gravedadUrano//gravedadTierra
    nombrePlaneta=("Urano")

elif (planeta==8):
    pesoFinal=pesoUsuario*gravedadNeptuno//gravedadTierra
    nombrePlaneta=("Neptuno")

elif (planeta==9):
    pesoFinal=pesoUsuario*gravedadPluton//gravedadTierra
    nombrePlaneta=("Pluton")
#-------------------------------------------------------------

print ("Tu peso en ", nombrePlaneta," es ", pesoFinal, " kilos ")
