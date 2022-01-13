import scipy.stats as stats
import math
import os

limpiar = lambda: os.system('cls')

def MenuPrincipal():
    limpiar()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t\t\t===============Calculadora Estadistica==================")
    print("\t\t\t\t\t\t\t[1]. Distribución Binomial")
    print("\t\t\t\t\t\t\t[2]. Distribucion Normal")
    print("\t\t\t\t\t\t\t[3]. Distribución de Poisson")
    print("\t\t\t\t\t\t\t[4]. Muestreo")
    print("\t\t\t\t\t\t\t[5]. Estimación")
    print("\t\t\t\t\t\t\t[6]. Prueba de hipotesis")
    print("\t\t\t\t\t\t\t[7]. SALIR")
    print("\t\t\t\t\t\t\t=========================================================")
    print()
    op = int(input("\t\t\t\t\t\t\tIngrese una opcion------>: "))
    if op==1: DistribucionBinomial()
    elif op==2: DistribucionNormal()
    elif op==3: DistribucionPoisson()
    elif op==4: MuestreoAleatorio()
    elif op==5: Estimacion()
    #elif op==6: Hipotesis()
    elif op==7: exit()


def DistribucionBinomial():
    limpiar()
    while True:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print(f"\t\t\t\t\t\t\t===============Distribución binomial==================")
        print(f"\t\t\t\t\t\t\t[1]. Aplicaciones")
        print(f"\t\t\t\t\t\t\t[2]. Media de una distribución binomial")
        print(f"\t\t\t\t\t\t\t[3]. Desviación estandar de una distribucón binomial")
        print(f"\t\t\t\t\t\t\t[4]. Menu principal")
        print("\t\t\t\t\t\t\t=========================================================")
        print()
        opc = int(input("\t\t\t\t\t\t\tIngrese una opcion -->: "))

        if  opc == 1:
            limpiar()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print(f"\t\t\t\t\t\t\t\t\tAplicaciones")
            print()
            p = float(input("\t\t\t\t\t\t\tProbabilidad de que el evento ocurra -->: "))
            n = int(input("\t\t\t\t\t\t\tNúmero total de experimentos -->: "))
            x = int(input("\t\t\t\t\t\t\tExitos deseados -->: "))
            factorial = math.factorial(n)/(math.factorial(x)*math.factorial(n-x))
            probabilidad =  p**x *(1-p)**(n-x)

            print(f"\t\t\t\t\t\t\tLa probablilidad es de: {factorial*probabilidad:.4f}")
            print()
            input("\t\t\t\t\t\t\tPrecione entrer para volver al menu principal")
            DistribucionBinomial()

        if opc == 2:
            limpiar()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print(f"\t\t\t\t\t\t\t\tMedia de una distribución binomial")
            print()
            nEn = int(input("\t\t\t\t\t\t\tNúmero de ensayos -->: "))
            p = float(input("\t\t\t\t\t\t\tProbabilidad de tener éxito -->: "))
            res = nEn * p
            print (f"\t\t\t\t\t\t\tMedia de la distribucón binomial es igual a -->: {res:.2f}")
            print()
            print()
            input("\t\t\t\t\t\t\tPrecione entrer para volver al menu principal")
            DistribucionBinomial()
        if opc == 3:
            limpiar()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print(f"\t\t\t\t\t\t\t\tDesviación estandar de una distribucón binomial")
            nEn = int(input("\t\t\t\t\t\t\tNúmero de ensayos -->: "))
            p = float(input("\t\t\t\t\t\t\tProbabilidad de tener éxito -->: "))
            res = nEn*p*(1-p)
            r = math.sqrt(res)
            print(f"\t\t\t\t\t\t\tLa desviación estándar es de -->: {r:.3f}")
            print()
            print()
            input("\t\t\t\t\t\t\t\tPrecione entrer para volver al menu principal")
            DistribucionBinomial()
        if opc == 4:
            MenuPrincipal()


def DistribucionNormal():
    limpiar()
    while True:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print(f"\t\t\t\t\t\t\t===============Distribución Normal==================")
        print(f"\t\t\t\t\t\t\t     Aplicaciones")
        print(f"\t\t\t\t\t\t\t[1]. Encontrar < X")
        print(f"\t\t\t\t\t\t\t[2]. Encontrar > X")
        print(f"\t\t\t\t\t\t\t[3]. Encontrar area entre dos puntos")
        print(f"\t\t\t\t\t\t\t[4]. Estandarización de una variable aleatoria normal ")
        print(f"\t\t\t\t\t\t\t[5]. Menu Principal ")
        print("\t\t\t\t\t\t\t=========================================================")
        print()
        opc = int(input("\t\t\t\t\t\t\tIngrese una opcion: "))
        if opc == 1 or opc == 2:
            limpiar()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print(f"\t\t\t\t\t\t\t     Aplicaciones")
            print()
            x = float(input("\t\t\t\t\t\t\tValor de x -->: "))
            media = float(input("\t\t\t\t\t\t\tValor de µ -->: "))
            desviacionS = float(input("\t\t\t\t\t\t\tValor de σ -->: "))
            prob = stats.norm.cdf((x - media)/ desviacionS)
            z = (x - media) / desviacionS
            res = 1 - prob
            limpiar()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("\t\t\t\t\t\t\t====RESULTADOS===")
            print()
            print(f"\t\t\t\t\t\t\tEl valor de Z es --->: {z:.4f}")
            if opc == 1:
                print(f"\t\t\t\t\t\t\tEl resultado es de --->: {prob:.4f} ")
                print()
                input("\t\t\t\t\t\tPrecione entrer para volver al menu anterior")
                DistribucionNormal()
            if opc == 2: 
                limpiar
                print(f"\t\t\t\t\t\t\tEl resultado es de --->: {res * 100:.2f}%")
                print("")
                input("\t\t\t\t\t\tPrecione entrer para volver al menu anterior")
                DistribucionNormal()
        if opc == 3:
            limpiar()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            for i in range(0,2):
                x = float(input("\t\t\t\t\t\t\tValor de x -->: "))
                media = float(input("\t\t\t\t\t\t\tValor de µ -->: "))
                desviacionS = float(input("\t\t\t\t\tValor de σ -->: "))
                z = ((x - media) / desviacionS)
                print()
                print(f"\t\t\t\t\t\t\tEl valor para Z es de --->: {z:.4f}")
            contador = 0
            for i in range(0,2):
                valorTabla = float(input("\t\t\t\t\t\t\tValores obtenidos (Tabla Z)--->"))
                contador = contador + valorTabla
            print()
            print(f"\t\t\t\t\t\t\tSu resultado es de --->: {contador*100:.2f}%")
            print()
            input("\t\t\t\t\t\tPresione entrer para volver al menu anterior")
            DistribucionNormal()
        if opc == 4:
            limpiar()
            print(f"\t\t\t\t\t\t\tEstandarización de una variable aleatoria normal")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            x = float(input("\t\t\t\t\t\t\tValor de x -->: "))
            media = float(input("\t\t\t\t\t\t\tValor de x̄ -->: "))
            desviacionS = float(input("\t\t\t\t\t\t\tValor de σ -->: "))
            estand = (x - media)/desviacionS
            print("\t\t\t\t\t\t\t====RESULTADOS===")
            print(f"\t\t\t\t\t\t\tZ es igual a --->: {estand:.2f}")
            print()
            input("\t\t\t\t\t\t\tPresione entrer para volver al menu anterior")
            DistribucionNormal()
        if opc == 5:
            limpiar()
            MenuPrincipal() 


def DistribucionPoisson():
    limpiar()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t\t\t===============Dstribución de Poisson==================")
    print()
    µ = float(input("\t\t\t\t\t\t\tValor promedio esperado µ:"))
    x = int(input("\t\t\t\t\t\t\tProbabilidad de tener exactamente x ocurrencias:"))
    f = math.e**(-µ) *µ**x
    p = math.factorial(x)     
    print(f"\t\t\t\t\t\t\tLa probablilidad es de: {f/p:.4f}")
    print()
    input("\t\t\t\t\t\t\tPrecione entrer para volver al menu principal")
    MenuPrincipal()
    
def MuestreoAleatorio():
    limpiar()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print(f"\t\t\t\t\t\t\t===============MUESTREO==================")
    print(f"\t\t\t\t\t\t\t[1]. Error estandar ")
    print(f"\t\t\t\t\t\t\t[2]. Estandarización de la media de la muestra ")
    print(f"\t\t\t\t\t\t\t[3]. Error estándar de la media para poblaciones finitas")
    print(f"\t\t\t\t\t\t\t[4]. Error estándar de la media para poblaciones infinitas")
    print(f"\t\t\t\t\t\t\tAPLICACIONES")
    print(f"\t\t\t\t\t\t\t[5]. Muestras pequeñas")
    print(f"\t\t\t\t\t\t\t[6]. Teorema de limite central P  x̄ <")
    print(f"\t\t\t\t\t\t\t[7]. Teorema de limite central P  x̄ >")
    print(f"\t\t\t\t\t\t\t[8]. Menu principal")
    print("\t\t\t\t\t\t\t=========================================================")
    print()
    opc = int(input("\n\t\t\t\t\t\tIngrese una opcion: "))
    limpiar()
    #Calcular error estandar
    if opc == 1:
        limpiar()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("\t\t\t\t\t\t\t\tError estandar")
        print()
        desviacionS = float(input("\t\t\t\t\t\t\tDesviacón estandar -->: "))
        n = float(input("\t\t\t\t\t\t\tTamaño de la muestra -->: "))
        Error = desviacionS/math.sqrt(n)
        print(f"\t\t\t\t\t\t\tEl error estandar de la media es de -->: {Error:.3f}")
        input("\t\t\t\t\t\t\tPrecione entrer para volver al menu anterior")
        MuestreoAleatorio()
    #Estandarización de la media de la muestra
    if opc == 2:
        limpiar()
        print("\t\t\t\t\t\t\tEstandarización de la media de la muestra")
        print()
        MediaMuestra = float(input("\t\t\t\t\t\t\tMedia de la muestra -->: "))
        MediaPoblacion = float(input("\t\t\t\t\t\t\tMedia de la población -->: "))
        ErrorEstandarMedia = float(input("\t\t\t\t\t\t\tError estandar de la media -->: "))
        z = (MediaMuestra - MediaPoblacion)/ErrorEstandarMedia
        print(f"\t\t\t\t\t\t\tZ es igual a -->:  {z:.2f}")
        input("\t\t\t\t\t\t\tPrecione entrer para volver al menu anterior")
        MuestreoAleatorio()
    #Error estándar de la media para poblaciones finitas
    if opc == 3:
        limpiar()
        ErrorEstandarMedia = float(input("\t\t\t\t\t\t\tDesviación estándar -->: "))
        n = float(input("\t\t\t\t\t\t\tTamaño de la muestra -->: "))
        TamPoblacion = float(input("\t\t\t\t\t\t\tTamaño de la población -->: "))

        MPoblacionFinita = (TamPoblacion-n)/(TamPoblacion-1)
        Raiz = math.sqrt(MPoblacionFinita)
        Error = ErrorEstandarMedia/math.sqrt(n)
        Resultado = Error * Raiz
        print(f"\t\t\t\t\t\t\tError estandar de la media de la población finita igual a -->: {Resultado:.2f}")
        input("\t\t\t\t\t\t\tPrecione entrer para volver al menu anterior")
        MuestreoAleatorio()
    
    #Error estándar de la media para poblaciones infinitas
    if opc == 4:
        limpiar()
        desviacionS = float(input("\t\t\t\t\t\t\tDesviación estandar de la población -->: "))
        n = float(input("\t\t\t\t\t\t\tTamaño de la muestar -->: "))
        ErrorS = desviacionS/math.sqrt(n)
        print(f"\t\t\t\t\t\t\tEl error estándar de la media para poblaciones infinitas es de -->: {ErrorS}")
        input("\t\t\t\t\t\t\tPrecione entrer para volver al menu anterior")
        MuestreoAleatorio()
   
    #Aplicaciones
    if opc == 5:
        #Muestras pequeñas
        limpiar()
        n = int(input("\t\t\t\t\t\t\tTamaño de la muestra (n) --->: "))
        MediaPoblacion = float(input("\t\t\t\t\t\t\tMedia de la población (μ) -->: "))
        desviacionS = float(input("\t\t\t\t\t\t\tDesviación estándar de la población (σ) -->: "))
        ErrorEstandarMedia = desviacionS / math.sqrt(n)
        print("")
        print(f"\t\t\t\t\t\t\tError estandar -->: {ErrorEstandarMedia:.3f}")
        print("")
        x = float(input("\t\t\t\t\t\t\tIngrese x̄ -->: "))
        P = (x - MediaPoblacion) / ErrorEstandarMedia
        print(f"\t\t\t\t\t\t\t z < igual a -->: {P:.2f}")
        print()
        z = 0.5
        Resultado = float(input("\t\t\t\t\t\t\tIngrese su resultado (Tabla Z) -->: "))
        res = z - Resultado
        print()
        print(f"\t\t\t\t\t\t\tEl resultado es de  -->: {res:.4f}")
        print()
        input("\t\t\t\t\t\t\tPrecione entrer para volver al menu anterior")
        MuestreoAleatorio()

         #Teorema de limite central
    if opc == 6 or opc == 7:
        limpiar()
        n = float(input("Tamaño de la muestra (n) -->: "))
        if n < 30:
            print(f"\t\t\t\t\t\t\tEl teorema de limite central solo puede ser usado en muestras grandes!!")
        else:
            MediaPoblacion = float(input(f"Media de la población (μ)-->: "))
            des = float(input("Desviacion estándar (σ)-->: "))
            ErrorS = des/math.sqrt(n)
            print("")
            print(f"Error estandar -->: {ErrorS:.3f}")
            print("")
            if opc == 6:
                x = float(input("Ingrese x̄ -->: "))
                P = (x - MediaPoblacion) / ErrorS
                print(f" z < igual a -->: {P:.2f}")
                print("")
                z = 0.5
                Resultado = float(input("Ingrese su resultado (Tabla Z) -->"))
                res = z - Resultado
                print("")
                print(f"El resultado es -->: {res:.4f}")
                input("Precione entrer para volver al menu anterior")
                MuestreoAleatorio()

            if opc == 7:
                x = float(input("Ingrese x̄ -->: "))
                P = (x - MediaPoblacion) / ErrorS
                print(f" z < igual a -->: {P:.2f}")
                print("")
                z = 0.5
                Resultado = float(input("Ingrese su resultado (Tabla Z) -->"))
                res = z + Resultado
                print("")
                print(f"El resultado es -->: {res:.4f}")
                input("Precione entrer para volver al menu anterior")
                MuestreoAleatorio()
    if opc == 8:
        MenuPrincipal()

         
def menu():
 limpiar()
 print ()
 print("\t\t\t\t\t\t\t\t\tEstimaciones puntuales")
 print ("\t\t\t\t\t\t\t\t\t[1]. Ingresar datos")
 print ("\t\t\t\t\t\t\t\t\t[2]. Varianza")
 print ("\t\t\t\t\t\t\t\t\t[3]. Desviación")
 print ("\t\t\t\t\t\t\t\t\t[4]. Media ")
 print ("\t\t\t\t\t\t\t\t\t[5]. Error Estándar de la media de una población finita")
 print ("\t\t\t\t\t\t\t\t\t[6]. Error Estándar de la media de una población infinita")
 print ("\t\t\t\t\t\t\t\t\t[7]. Error estándar de la proporción")
 print ("\t\t\t\t\t\t\t\t\tAplicaciones")
 print ("\t\t\t\t\t\t\t\t\t[8]. Estimaciones de intervalo al rededor de la media")
 print ("\t\t\t\t\t\t\t\t\t[9]. Estimaciones de intervalo al rededor de la media usando un intervalo de confianza")
 print ("\t\t\t\t\t\t\t\t\t[10]. Menu Principal")
 print ("\t\t\t\t\t\t\t\t\t[11]. SALIR")
 
def obtenerDatos():
 limpiar()
 print ("\t\t\t\t\t\t\t\t\tDigite cuantos datos desea ingresar?")
 numeroDatos = int(input("\t\t\t\t\t\t\t\t\t--->: "))
 datos = []
 for i in range(0, numeroDatos):
  print ("\t\t\t\t\t\t\t\t\tValor ", i + 1)
  dato = input("\t\t\t\t\t\t\t\t\t--->")
  datos.append(int(dato))
 return datos

def obtenerPromedio(datos):
 suma = 0
 for dato in datos:
    suma += dato
 return suma / len(datos)

def obtenerVarianza(datos):
 limpiar()
 n = len(datos)
 promedio = obtenerPromedio(datos)
 varianza = 0
 for dato in datos:
  varianza += math.pow((dato - promedio), 2)
 return varianza / (n - 1)

def obtenerDesviacion(varianza, datos):
 limpiar()
 if(varianza == 0):
  varianza = obtenerVarianza(datos)
  return math.sqrt(varianza)
 elif(varianza > 0):
  return math.sqrt(varianza)


def ErrorEstandar():
    limpiar()
    print("\t\t\t\tError Estándar de la Media en una Población Finita")
    print("")
    Np = int(input("Ingrese el total de la población N: "))
    n = int(input("Ingrese el total de muestras n: "))
    sigma = float(input("Ingrese la desviación estándar: "))
    sigmax = (sigma/math.sqrt(n))*(math.sqrt((Np-n)/(Np-1)))
    print("")
    print(f"La Error Estandar es --->: {sigmax:4f}" )
    print("")
    input("Presione entrer para volver al menu principal")

def ErrorEstandarProporcion():
    limpiar()
    print("\t\t\t\tError Estándar de la Proporción")
    print("")
    P = float(input("Ingrese la proporción verdadera de ocurrencias P: "))
    n = int(input("Ingrese el total de muestras n: "))
    sigmap = math.sqrt((P*(1-P))/n) 
    print("")
    print(f"La Error Estandar de la Proporción es: {sigmap:.4f}" )
    print("")
    input("Presione entrer para volver al menu principal")

#Aplicaciones
def EstimacionIntervalo():
    limpiar
    desviacionS = float(input("Desviacón estandar -->: "))
    n = float(input("Tamaño de la muestra -->: "))
    Error = desviacionS/math.sqrt(n)
    print(f"El error estandar de la media es de -->: {Error:.3f}")
    Media = float(input("Media -->: "))

    intervalo = Media + Error
    intervalo1 = Media - Error
    print(f"Intervalo al rededor de la media -->: ({intervalo1:.3f} , {intervalo:.3f})")  
    input("Precione entrer para volver al menu anterior")

def EstimacionIntervaloConfianza():
    limpiar
    desviacionS = float(input("Desviacón estandar -->: "))
    n = float(input("Tamaño de la muestra -->: "))
    Error = desviacionS/math.sqrt(n)
    print(f"El error estandar de la media es de -->: {Error:.3f}")
    Media = float(input("Media -->: "))
    PorcentajeConfianza = float(input("Nivel de confianza -->: "))
    
    r = PorcentajeConfianza* Error
    
    intervalo = Media + r
    intervalo1 = Media - r
    print(f"Intervalo al rededor de la media -->: ({intervalo1:.3f} , {intervalo:.3f})")  
    input("Precione entrer para volver al menu anterior")

def ErrorEstimado():
    limpiar()
    print("\t\t\t\tError Estándar Estimado de la Media de una Población Infinita")
    print("\t\tBIENVENIDO, ingrese los valores que se le solicitan a continuación")
    print("")
    sigma = float(input("Ingrese la desviación estandar: "))
    n = int(input("Ingrese el total de muestras n: "))
    sigmaxe = sigma/math.sqrt(n) 
    print("")
    print(f"El Error Estandar Estimado de la Media de una Población Infinita es: {sigmaxe:.4f}")
    print("")
    input("Presione entrer para volver al menu principal")

def Estimacion():
 limpiar()
 salir = False
 datos = []
 varianza = 0
 prom = 0
 while not salir:
  opcion = -1
  menu()
  print()
  opcion = int(input("\t\t\t\t\t\t\tIngrese una opcion -->: "))
  if(opcion == 1):
   limpiar()
   datos = obtenerDatos()
   input("\t\t\t\t\t\t\t\t\tEnter para continuar...")
  elif(opcion == 2):
   limpiar()
   varianza = obtenerVarianza(datos)
   print ("\t\t\t\t\t\t\t\t\tVarianza -->: ", varianza)
   input("\t\t\t\t\t\t\t\t\tEnter para continuar...")
  elif(opcion == 3):
   limpiar()
   desviasion = obtenerDesviacion(varianza, datos)
   print ("\t\t\t\t\t\t\t\t\tDesviacion estandar -->: ", desviasion)
   input("\t\t\t\t\t\t\t\t\tEnter para continuar...")
  elif(opcion == 4):
    limpiar()
    prom = obtenerPromedio(datos) 
    print ("\t\t\t\t\t\t\t\t\tMedia de la muestra -->: ", prom)
    input("\t\t\t\t\t\t\t\t\tEnter para continuar...")
  elif(opcion == 5):
    limpiar()
    ErrorEstandar()
  elif(opcion == 6):
   limpiar()
   ErrorEstimado()
  elif(opcion == 7):
    limpiar()
    ErrorEstandarProporcion()
  elif(opcion == 8):
    limpiar()
    EstimacionIntervalo()
  elif(opcion == 9):
    limpiar()
    EstimacionIntervaloConfianza()
  elif(opcion == 10):
    limpiar()
    MenuPrincipal()
  elif(opcion == 11):
    exit()
  else:
    print ("Opcion incorrecta!")

MenuPrincipal()
