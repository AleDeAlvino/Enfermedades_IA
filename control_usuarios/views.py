from django.shortcuts import render
from decimal import Decimal

# Create your views here.
def index_view(request):
    return render(request, 'Index.html')

def preguntas_view(request):


    enfermedades={
        'RG':{'valores':[1.0, 0.8, 0.5, 0.6, 0.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              'sintomas':['sensacion de ardor', 'dolor de pecho', 'dificultad para tragar', 'nudo en la garganta', 'regurgitacion'],
              'descripcion': 'El reflujo gastroesofágico (RGE) se presenta cuando el contenido del estómago se devuelve al esófago. La enfermedad por reflujo gastroesofágico (ERGE) es una afección más grave y duradera en la que, con el tiempo, el reflujo gastroesofágico causa síntomas repetidos o complicaciones.',
              'tratamiento': 'El tratamiento consiste en antiácidos y cuidado personal. El alivio que proporcionan los cambios en el estilo de vida y los medicamentos de venta libre suelen ser temporales. Cuidado personal: Elevar cabeza de la cama, Modificación dietética y Adelgazamiento. Medicamentos: Antiácido, Inhibidor de la bomba de protones y Antidiarreico',
              'promedio': 0.088,
              'nombre': 'Reflujo gastroesofágico'
              },
        'UP':{'valores':[0, 0, 0, 0, 0, 1.0, 0.7, 0.5, 0.8, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              'sintomas':['dolor estomacal', 'intolerancia a las bebidas con gas', 'nauseas', 'acidez de estomago', 'hinchazon'],
              'descripcion': 'Las úlceras pépticas son llagas abiertas que aparecen en el revestimiento interno del estómago y la parte superior del intestino delgado.',
              'tratamiento': 'Medicamentos antibióticos para eliminar el helicobácter pylori. Medicamentos que bloquean la producción de ácido y promueven la recuperación. Medicamentos para reducir la producción de ácido. Antiácidos que neutralizan el ácido estomacal.',
              'promedio': 0.008,
              'nombre': 'Úlcera péptica'
              },
        'EC':{'valores':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.9, 0.6, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              'sintomas':['dolor abdominal', 'diarrea', 'irritabilidad', 'decaimiento animico'],
              'descripcion': 'La enfermedad celíaca es un trastorno digestivo que afecta al intestino delgado. Las personas con esta enfermedad no pueden comer gluten, una proteína que se encuentra en el trigo, la cebada y el centeno. La enfermedad puede causar problemas digestivos a largo plazo e impedir la obtención de nutrientes necesarios.',
              'tratamiento': 'El tratamiento consiste en cambios en la dieta. El tratamiento principal consiste en una dieta estricta libre de gluten que pueda controlar los síntomas y promover la curación del intestino. Medicamentos: Suplemento dietético y Vitamina',
              'promedio': 0.059,
              'nombre': 'Enfermedad celíaca'
              },
        'IL':{'valores':[0, 0, 0, 0, 0, 0.5, 0, 0.4, 0, 0.4, 0.7, 1.0, 0, 0, 1.0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              'sintomas':['diarrea', 'gases', 'hinchazon', 'nauseas', 'vomito', 'dolor abominal'],
              'descripcion': 'La intolerancia a la lactosa es causada por la malabsorción de lactosa, una afección en la que el intestino delgado no puede digerir o descomponer toda la lactosa que una persona come o bebe. No todas las personas con malabsorción de lactosa tienen síntomas después de consumir lactosa.',
              'tratamiento': 'El tratamiento consiste en cambios en la dieta. El tratamiento se basa en evitar los productos lácteos, consumir productos libres de lactosa o tomar suplementos de lactasa. Cuidado personal. Evitar la lactosa. Medicamentos: Suplemento dietético',
              'promedio': 0.102,
              'nombre': 'Intolerancia a la lactosa'
              },
        'CH':{'valores':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0.8, 0.8, 0.4, 0.5, 0.1, 0.2, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              'sintomas':['fatiga', 'perdida de apetito', 'adelgazamiento involuntario', 'picazon en la piel', 'hematomas', 'confusion', 'dificultad para hablar', 'hinchazon en las piernas'],
              'descripcion': 'La cirrosis es una condición médica en la que el hígado está cicatrizado y permanentemente dañado. El tejido cicatricial reemplaza el tejido sano del hígado y evita que funcione normalmente.',
              'tratamiento': 'El tratamiento varía. Los tratamientos se especializan en la causa subyacente. En los casos avanzados, puede ser necesario hacer un trasplante de hígado. Cuidado personal: Dieta baja en sodio y Evitar el alcohol. Medicamentos: Diurético, Reductor de amoniaco, Beta bloqueador, Hormona sintética, Antibiótico y Antiviral. Procedimiento médico: Ligadura con banda elástica, Endoscopía terapéutica y Derivación portosistémica intrahepática transyugular',
              'promedio': 0.090,
              'nombre': 'Cirrosis hepática'
              },
        'ECR':{'valores':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.8, 0.7, 0, 0, 0, 0, 1.0, 0.8, 0, 0, 0, 0, 0, 0, 0.3, 0.2, 0.5, 0, 0, 0, 0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'sintomas':['dolor abdominal', 'diarrea', 'llagas en la boca', 'perdida de apetito', 'desnutricion', 'sangre en las heces', 'debilidad', 'fatiga'],
               'descripcion': 'La enfermedad de Crohn es una enfermedad crónica que causa inflamación e irritación en el tubo digestivo. La enfermedad de Crohn afecta con más frecuencia al intestino delgado y el comienzo del intestino grueso. Sin embargo, la enfermedad puede afectar cualquier parte del tubo digestivo, desde la boca hasta el ano.',
               'tratamiento': 'El tratamiento consiste en medicamentos antiinflamatorios. La enfermedad de Crohn no tiene cura. Algunos medicamentos, como los esteroides y los inmunosupresores, se usan para lentificar el progreso de la enfermedad.',
               'promedio': 0.123,
               'nombre': 'Enfermedad de Crohn'
              },
        'CU':{'valores':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.9, 0.9, 0, 0, 0, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0.4, 0, 0, 0, 0.4, 0.6, 0.2, 0, 0, 0, 0, 0, 0, 0, 0],
              'sintomas':['diarrea', 'sangre en las heces', 'pus en las heces', 'dolor rectal', 'estreñimiento', 'dolor abdominal', 'fiebre', 'fatiga'],
              'descripcion': 'Inflamación crónica del colon que produce úlceras en su revestimiento. Esta afección se caracteriza por dolor abdominal, calambres y descargas intestinales poco compactas de pus, sangre y moco.',
              'tratamiento': 'El tratamiento consiste en medicamentos antiinflamatorios. El tratamiento incluye medicamentos y cirugía. Medicamentos: Antiinflamatorio no esteroideo, Antibiótico, Antiinflamatorio, Inmunosupresor, Esteroide, Analgésico y Suplemento dietético',
              'promedio': 0.107,
              'nombre': 'Colitis ulcerosa'
              },
        'SIC':{'valores':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 0, 0, 0, 0, 0.4, 0, 0.2, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0.5, 0.6, 0, 0, 0, 0, 0.6, 0, 0, 0, 0, 0, 0, 0],
               'sintomas':['diarrea', 'fatiga', 'heces olor fetido', 'deshidratacion', 'adelgazamiento involuntario', 'grasa en las heces'],
               'descripcion': 'El síndrome de intestino corto es una afección en la que el organismo no puede absorber suficientes nutrientes de los alimentos que ingieres, debido a que tu intestino delgado es más corto. El intestino delgado es donde el organismo absorbe, durante la digestión, la mayoría de los nutrientes que ingieres.',
               'tratamiento': 'El tratamiento del síndrome del intestino corto puede incluir: Terapia nutricional médica. Las personas con síndrome de intestino delgado deberán seguir una dieta especial y tomar suplementos nutricionales. Solucion: Cirugia',
               'promedio': 0.079,
               'nombre': 'Síndrome del intestino corto'
              },
        'HR':{'valores':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 1.0, 1.0, 0, 0, 0, 0, 0],
              'sintomas':['dolor al toser', 'dolor al inclinarse', 'dolor al levantar objetos pesados'],
              'descripcion': 'Abultamiento de un órgano interno a través de un área débil o la ruptura de un músculo u otro tejido que lo mantiene en su lugar. La mayoría de las hernias se presentan en el abdomen.',
              'tratamiento': 'El tratamiento consiste en cuidados de apoyo. El tratamiento incluye chequeos médicos para control. Si es necesario, una cirugía puede volver el tejido a su ubicación normal y cerrar la apertura.',
              'promedio': 0.071,
              'nombre': 'Hernia'
              },
        'AP':{'valores':[0, 0, 0, 0, 0, 0, 0, 0.6, 0, 0.5, 0, 0.8, 0, 0, 0, 0.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.9, 0, 0, 0, 0, 1.0, 0, 0, 0],
              'sintomas':['dolor abdominal lado derecho', 'fiebre', 'nauseas', 'vomito', 'hinchazon', 'diarrea'],
              'descripcion': 'La apendicitis es la inflamación del apéndice, un tubo cerrado de tejido que se encuentra unido al intestino largo en la parte inferior derecha del abdomen. La inflamación puede ocurrir cuando el apéndice se infecta o bloquea con heces, con objetos foráneos o con un tumor.',
              'tratamiento': 'El tratamiento consiste en cirugía. La apendicitis suele tratarse con cirugía y antibióticos. Si no se trata, el apéndice puede reventarse y causar un absceso o una infección sistémica (sepsis). Cirugía: Apendicectomía, Laparotomía y Laparoscopia. Medicamentos: Antibiótico y Penicilina',
              'promedio': 0.109,
              'nombre': 'Apendicitis'
              },
        'HE':{'valores':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0, 0.6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 1.0, 1.0],
              'sintomas':['bulto cerca del ano', 'hinchazon', 'dolor anal', 'sangre en las heces', 'irritabilidad cerca del ano'],
              'descripcion': 'Las hemorroides, también llamadas almorranas, son venas hinchadas en el ano y la parte inferior del recto, similares a las venas varicosas. Las hemorroides pueden desarrollarse dentro del recto (hemorroides internas) o debajo de la piel alrededor del ano',
              'tratamiento': 'El tratamiento consiste en cambios en la dieta y laxantes. Una dieta alta en fibras puede resultar efectiva, junto con laxantes. En algunos casos, puede ser necesario hacer un procedimiento médico para quitar la hemorroide y brindar alivio. Cuidado personal. Dieta alta en fibra, Compresa fría, Compresa fría, Hamamelis y Óxido de zinc. Medicamentos: Esteroide, Anestésico local y Suplemento dietético',
              'promedio': 0.119,
              'nombre': 'Hemorroides'
              }
        }
        
    if request.method == 'POST':
      
        pe1= request.POST['respuesta1']
        pr1= request.POST['progress1']
        print(pe1)
        print(pr1)
        pe2= request.POST['respuesta2']
        pr2= request.POST['progress2']
        print(pe2)
        print(pr2)
        pe3= request.POST['respuesta3']
        pr3= request.POST['progress3']
        print(pe3)
        print(pr3)
        pe4= request.POST['respuesta4']
        pr4= request.POST['progress4']
        print(pe4)
        print(pr4)
        pe5= request.POST['respuesta5']
        pr5= request.POST['progress5']
        print(pe5)
        print(pr5)
        pe6= request.POST['respuesta6']
        pr6= request.POST['progress6']
        print(pe6)
        print(pr6)
        pe7= request.POST['respuesta7']
        pr7= request.POST['progress7']
        print(pe7)
        print(pr7)
        pe8= request.POST['respuesta8']
        pr8= request.POST['progress8']
        print(pe8)
        print(pr8)
        pe9= request.POST['respuesta9']
        pr9= request.POST['progress9']
        print(pe9)
        print(pr9)
        pe10= request.POST['respuesta10']
        pr10= request.POST['progress10']
        print(pe10)
        print(pr10)
        pe11= request.POST['respuesta11']
        pr11= request.POST['progress11']
        print(pe11)
        print(pr11)
        pe12= request.POST['respuesta12']
        pr12= request.POST['progress12']
        print(pe12)
        print(pr12)
        pe13= request.POST['respuesta13']
        pr13= request.POST['progress13']
        print(pe13)
        print(pr13)
        pe14= request.POST['respuesta14']
        pr14= request.POST['progress14']
        print(pe14)
        print(pr14)
        pe15= request.POST['respuesta15']
        pr15= request.POST['progress15']
        print(pe15)
        print(pr15)
        pe16= request.POST['respuesta16']
        pr16= request.POST['progress16']
        print(pe16)
        print(pr16)
        pe17= request.POST['respuesta17']
        pr17= request.POST['progress17']
        print(pe17)
        print(pr17)
        pe18= request.POST['respuesta18']
        pr18= request.POST['progress18']
        print(pe18)
        print(pr18)
        pe19= request.POST['respuesta19']
        pr19= request.POST['progress19']
        print(pe19)
        print(pr19)
        pe20= request.POST['respuesta20']
        pr20= request.POST['progress20']
        print(pe20)
        print(pr20)
        pe21= request.POST['respuesta21']
        pr21= request.POST['progress21']
        print(pe21)
        print(pr21)
        pe22= request.POST['respuesta22']
        pr22= request.POST['progress22']
        print(pe22)
        print(pr22)
        pe23= request.POST['respuesta23']
        pr23= request.POST['progress23']
        print(pe23)
        print(pr23)
        pe24= request.POST['respuesta24']
        pr24= request.POST['progress24']
        print(pe24)
        print(pr24)
        pe25= request.POST['respuesta25']
        pr25= request.POST['progress25']
        print(pe25)
        print(pr25)
        pe26= request.POST['respuesta26']
        pr26= request.POST['progress26']
        print(pe26)
        print(pr26)
        pe27= request.POST['respuesta27']
        pr27= request.POST['progress27']
        print(pe27)
        print(pr27)
        pe28= request.POST['respuesta28']
        pr28= request.POST['progress28']
        print(pe28)
        print(pr28)
        pe29= request.POST['respuesta29']
        pr29= request.POST['progress29']
        print(pe29)
        print(pr29)
        pe30= request.POST['respuesta30']
        pr30= request.POST['progress30']
        print(pe30)
        print(pr30)
        pe31= request.POST['respuesta31']
        pr31= request.POST['progress31']
        print(pe31)
        print(pr31)
        pe32= request.POST['respuesta32']
        pr32= request.POST['progress32']
        print(pe32)
        print(pr32)
        pe33= request.POST['respuesta33']
        pr33= request.POST['progress33']
        print(pe33)
        print(pr33)
        pe34= request.POST['respuesta34']
        pr34= request.POST['progress34']
        print(pe34)
        print(pr34)
        pe35= request.POST['respuesta35']
        pr35= request.POST['progress35']
        print(pe35)
        print(pr35)
        pe36= request.POST['respuesta36']
        pr36= request.POST['progress36']
        print(pe36)
        print(pr36)
        pe37= request.POST['respuesta37']
        pr37= request.POST['progress37']
        print(pe37)
        print(pr37)
        pe38= request.POST['respuesta38']
        pr38= request.POST['progress38']
        print(pe38)
        print(pr38)
        pe39= request.POST['respuesta39']
        pr39= request.POST['progress39']
        print(pe39)
        print(pr39)
        pe40= request.POST['respuesta40']
        pr40= request.POST['progress40']
        print(pe40)
        print(pr40)
        pe41= request.POST['respuesta41']
        pr41= request.POST['progress41']
        print(pe41)
        print(pr41)
        pe42= request.POST['respuesta42']
        pr42= request.POST['progress42']
        print(pe42)
        print(pr42)
        pr1 = Decimal(pr1)
        pr2 = Decimal(pr2)
        pr3 = Decimal(pr3)
        pr4 = Decimal(pr4)
        pr5 = Decimal(pr5)
        pr6 = Decimal(pr6)
        pr7 = Decimal(pr7)
        pr8 = Decimal(pr8)
        pr9 = Decimal(pr9)
        pr10 = Decimal(pr10)
        pr11 = Decimal(pr11)
        pr12 = Decimal(pr12)
        pr13 = Decimal(pr13)
        pr14 = Decimal(pr14)
        pr15 = Decimal(pr15)
        pr16 = Decimal(pr16)
        pr17 = Decimal(pr17)
        pr18 = Decimal(pr18)
        pr19 = Decimal(pr19)
        pr20 = Decimal(pr20)
        pr21 = Decimal(pr21)
        pr22 = Decimal(pr22)
        pr23 = Decimal(pr23)
        pr24 = Decimal(pr24)
        pr25 = Decimal(pr25)
        pr26 = Decimal(pr26)
        pr27 = Decimal(pr27)
        pr28 = Decimal(pr28)
        pr29 = Decimal(pr29)
        pr30 = Decimal(pr30)
        pr31 = Decimal(pr31)
        pr32 = Decimal(pr32)
        pr33 = Decimal(pr33)
        pr34 = Decimal(pr34)
        pr35 = Decimal(pr35)
        pr36 = Decimal(pr36)
        pr37 = Decimal(pr37)
        pr38 = Decimal(pr38)
        pr39 = Decimal(pr39)
        pr40 = Decimal(pr40)
        pr41 = Decimal(pr41)
        pr42 = Decimal(pr42)
        
        prom = (pr1+pr2+pr3+pr4+pr5+pr6+pr7+pr8+pr9+pr10+pr11+pr12+pr13+pr14+pr15+pr16+pr17+pr18+pr19+pr20+pr21+pr22+pr23+pr24+pr25+pr26+pr27+pr28+pr29+pr30+pr31+pr32+pr33+pr34+pr35+pr36+pr37+pr38+pr39+pr40+pr41+pr42)/42
        prom = round(prom, 3)
        sint = [pe1, pe2, pe3, pe4, pe5, pe6, pe7, pe8, pe9, pe10, pe11, pe12, pe13, pe14, pe15, pe16, pe17, pe18, pe19, pe20, pe21, pe22, pe23, pe24, pe25, pe26, pe27, pe28, pe29, pe30, pe31, pe32, pe33, pe34, pe35, pe36, pe37, pe38, pe39, pe40, pe41, pe42 ]
      #   print(sint)
        print(prom)
        
        cont = 0
        composicion = {}
        for en in enfermedades:
              for s in sint:
                    for sin in enfermedades[en]['sintomas']:
                          if(s==sin):
                                print("s= ",s, "y sin =", sin)
                                cont = cont + 1
              print(en, '=', cont)
              composicion[en]=cont
              cont=0

        print(composicion)

    
        maximos = {}
        value = 0
        for key in composicion:
            if(composicion[key]>value):
                maximos = {}
                value = composicion[key]
                maximos[key] = composicion[key]

            elif(composicion[key] == value):
                maximos[key] = composicion[key]
        print(maximos)

        # if(len(maximos)>1):
        #     for key in maximos:
                
        #         pass

        closestKey = ""
        minDif = 10000000
        if(len(maximos)>1):
            for key in maximos:
                dif = abs(enfermedades[key]["promedio"] - float(prom))
                if(dif < minDif):
                    closestKey = key
                    minDif = dif
            
        elif(len(maximos)==1):
            closestKey = list(maximos.keys())[0]

        print(closestKey)
        print(prom)
        print(enfermedades[closestKey]["promedio"])
        print(minDif)
        return render (request, 'resultado.html',{'nombre': enfermedades[closestKey]["nombre"], 'sintomas': enfermedades[closestKey]["sintomas"], 'descripcion': enfermedades[closestKey]["descripcion"], 'tratamiento': enfermedades[closestKey]["tratamiento"]})

        



    return render(request, 'preguntas.html')

def resultado_view(request):

    return render(request, 'resultado.html')