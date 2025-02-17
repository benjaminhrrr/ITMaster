import random

# Constantes con nombres y apellidos
MASCULINOS = [
    "Carlos",
    "José",
    "Pedro",
    "Manuel",
    "Juan",
    "Miguel",
    "Alberto",
    "Francisco",
    "Diego",
    "Antonio",
    "Eduardo",
    "Sergio",
    "Fernando",
    "Javier",
    "Ricardo",
    "Andrés",
    "Oscar",
    "Daniel",
    "Alejandro",
    "Mario",
    "Gustavo",
    "Enrique",
    "Alfredo",
    "Mauricio",
    "Martín",
    "Luis",
    "Raúl",
    "Gabriel",
    "Felipe",
    "Samuel",
    "Vicente",
    "Cristian",
    "Hugo",
    "Adrián",
    "Ignacio",
    "Arturo",
    "Pablo",
    "Rafael",
    "Salvador",
    "Julio",
    "Isaac",
    "Leonardo",
    "Ángel",
    "Santiago",
    "Víctor",
    "Elías",
    "Gonzalo",
    "Erik",
    "Ramón",
    "Alex",
]

FEMENINOS = [
    "María",
    "Ana",
    "Sofía",
    "Laura",
    "Carmen",
    "Isabel",
    "Marta",
    "Elena",
    "Patricia",
    "Sara",
    "Rosa",
    "Cristina",
    "Susana",
    "Lucía",
    "Paula",
    "Natalia",
    "Clara",
    "Beatriz",
    "Andrea",
    "Esther",
    "Verónica",
    "Julieta",
    "Vanesa",
    "Marina",
    "Lorena",
    "Silvia",
    "Julia",
    "Cecilia",
    "Teresa",
    "Luisa",
    "Rocío",
    "Yolanda",
    "Victoria",
    "Mercedes",
    "Irene",
    "Leticia",
    "Raquel",
    "Adriana",
    "Mónica",
    "Sonia",
    "Inés",
    "Daniela",
    "Miriam",
    "Virginia",
    "Pilar",
    "Gabriela",
    "Alejandra",
    "Violeta",
    "Olga",
    "Mar",
]

APELLIDOS = [
    "González",
    "Rodríguez",
    "Pérez",
    "Martínez",
    "García",
    "López",
    "Hernández",
    "Sánchez",
    "Ramírez",
    "Torres",
    "Flores",
    "Vásquez",
    "Castillo",
    "Ortiz",
    "Gutiérrez",
    "Mendoza",
    "Ruiz",
    "Alvarez",
    "Cruz",
    "Espinoza",
    "Reyes",
    "Morales",
    "Guzmán",
    "Vargas",
    "Medina",
    "Ramos",
    "Romero",
    "Suárez",
    "Navarro",
    "Jiménez",
]

# Lista de artículos de almacén (Código, Nombre, Precio, Categoría)
ARTICULOS_ALMACEN = [
    ("2001", "Leche", 1.20, "ref"),
    #   0       1       2     3
    ("2002", "Huevos", 2.50, "ref"),
    ("2003", "Pan", 1.00, "alm"),
    ("2004", "Mermelada", 2.00, "alm"),
    ("2005", "Aceite", 3.50, "alm"),
    ("2006", "Sal", 0.50, "alm"),
    ("2007", "Azúcar", 1.20, "alm"),
    ("2008", "Café", 4.00, "alm"),
    ("2009", "Te", 3.00, "alm"),
    ("2010", "Yogur", 1.00, "ref"),
    ("2011", "Queso", 2.50, "ref"),
    ("2012", "Arroz", 1.00, "alm"),
    ("2013", "Pasta", 1.50, "alm"),
    ("2014", "Jabón", 0.90, "lim"),
    ("2015", "Detergente", 2.00, "lim"),
    ("2016", "Shampoo", 3.50, "per"),
    ("2017", "Desodorante", 2.50, "per"),
    ("2018", "Papel Higiénico", 1.00, "lim"),
    ("2019", "Servilletas", 1.50, "lim"),
    ("2020", "Zumo de Naranja", 2.00, "ref"),
    ("2101", "Soda", 1.50, "ref"),
    ("2102", "Agua Mineral", 0.80, "ref"),
    ("2103", "Cerveza", 1.50, "ref"),
    ("2104", "Vino", 8.00, "alm"),
    ("2105", "Lata de Atún", 1.20, "alm"),
    ("2106", "Mayonesa", 2.50, "alm"),
    ("2107", "Mostaza", 1.50, "alm"),
    ("2108", "Vinagre", 1.00, "alm"),
    ("2109", "Patatas Fritas", 2.00, "alm"),
    ("2110", "Tortillas de Maíz", 2.00, "alm"),
    ("2111", "Ajo en Polvo", 0.80, "alm"),
    ("2112", "Canela", 0.50, "alm"),
    ("2113", "Champú para Bebés", 4.50, "per"),
    ("2114", "Crema Hidratante", 5.00, "per"),
    ("2115", "Limpiador de Suelos", 3.00, "lim"),
    ("2116", "Blanqueador", 2.50, "lim"),
    ("2117", "Colonia", 10.00, "per"),
    ("2118", "Cepillo de Dientes", 1.00, "per"),
    ("2119", "Pasta de Dientes", 1.50, "per"),
    ("2120", "Enjuague Bucal", 3.00, "per"),
]

# Lista de artículos de librería (Código, Nombre, Precio)
ATICULOS_LIBRERIA = [
    ("1001", "Cuaderno Espiral", 3.50),
    ("1002", "Lápiz HB", 0.40),
    ("1003", "Borrador", 0.25),
    ("1004", "Regla 30 cm", 1.00),
    ("1005", "Tijeras", 2.00),
    ("1006", "Cinta Adhesiva", 1.50),
    ("1007", "Lapicero Azul", 0.75),
    ("1008", "Lapicero Negro", 0.75),
    ("1009", "Lapicero Rojo", 0.75),
    ("1010", "Marcadores", 4.00),
    ("1011", "Corrector Líquido", 1.80),
    ("1012", "Calculadora", 12.00),
    ("1013", "Papel A4 (Resma)", 5.00),
    ("1014", "Clip", 0.05),
    ("1015", "Saca Grapas", 1.50),
    ("1016", "Grapadora", 6.00),
    ("1017", "Carpeta 3 Anillos", 4.00),
    ("1018", "Compás", 3.50),
    ("1019", "Separadores", 2.00),
    ("1020", "Post-its", 1.50),
    ("1021", "Papelógrafo", 15.00),
    ("1022", "Pegamento en Barra", 0.90),
    ("1023", "Cartulina", 0.50),
    ("1024", "Láminas para Carpeta", 0.10),
    ("1025", "Portaminas", 2.00),
    ("1026", "Repuesto para Portaminas", 1.00),
    ("1027", "Cutter", 2.50),
    ("1028", "Grapas", 0.50),
    ("1029", "Lápices de Colores (Caja)", 5.00),
    ("1030", "Resaltador", 1.20),
    ("1031", "Papel Milimetrado", 1.00),
    ("1032", "Cuaderno Universitario", 5.00),
    ("1033", "Portafolio", 7.00),
    ("1034", "Libreta", 1.50),
    ("1035", "Caja de Archivo", 3.00),
    ("1036", "Bolígrafo Multicolor", 2.50),
    ("1037", "Folder", 0.25),
    ("1038", "Sobres", 0.10),
    ("1039", "Recambio de Bolígrafo", 1.00),
    ("1040", "Cinta Métrica", 2.00),
    ("1041", "Escuadra", 1.50),
    ("1042", "Papel para Acuarela", 2.50),
    ("1043", "Mochila", 25.00),
    ("1044", "Rotuladores", 3.00),
    ("1045", "Plumas", 1.00),
    ("1046", "Pincel", 1.50),
    ("1047", "Témperas", 4.00),
    ("1048", "Cuaderno Dibujo", 4.50),
    ("1049", "Set Geometría", 3.00),
    ("1050", "Calculadora Científica", 20.00),
]


TEXTO = """
El muerto
Que un hombre del suburbio de Buenos Aires, que un triste compadrito sin más 
virtud que la infatuación del coraje, se interne en los desiertos ecuestres de la 
frontera del Brasil y llegue a capitán de contrabandistas, parece de antemano 
imposible. A quienes lo entienden así, quiero contarles el destino de Benjamin 
Otálora, de quien acaso no perdura un recuerdo en el barrio de Balvanera y que 
murió en su ley, de un balazo, en los confines de Río Grande do Sul. Ignoro los 
detalles de su aventura; cuando me sean revelados, he de rectificar y ampliar estas 
páginas. Por ahora, este resumen puede ser útil. 
Benjamín Otálora cuenta, hacia 1891, diecinueve años. Es un mocetón de frente 
mezquina, de sinceros ojos claros, de reciedumbre vasca; una puñalada feliz le ha 
revelado que es un hombre valiente; no lo inquieta la muerte de su contrario, 
tampoco la inmediata necesidad de huir de la República. El caudillo de la parroquia 
le da una carta para un tal Azevedo Bandeira, del Uruguay. Otálora se embarca, la 
travesía es tormentosa y crujiente; al otro día, vaga por las calles de Montevideo, 
con inconfesada y tal vez ignorada tristeza. No da con Azevedo Bandeira; hacia la 
medianoche, en un almacén del Paso del Molino, asiste a un altercado entre unos 
troperos. Un cuchillo relumbra; Otálora no sabe de qué lado está la razón, pero lo 
atrae el puro sabor del peligro, como a otros la baraja o la música. Para, en el 
entrevero, una puñalada baja que un peón le tira a un hombre de galera oscura y de 
poncho. Éste, después, resulta ser Azevedo Bandeira. (Otálora, al saberlo, rompe la 
carta, porque prefiere debérselo todo a sí mismo. 
Azevedo Bandeira da, aunque fornido, la injustificable impresión de ser 
contrahecho; en su rostro, siempre demasiado cercano, están el judío, el negro y el 
indio; en su empaque, el mono y el tigre; la cicatriz que le atraviesa la cara es un 
adorno más, como el negro bigote cerdoso. 
Proyección o error del alcohol, el altercado cesa con la misma rapidez con que se 
produjo. Otálora bebe con los troperos y luego los acompaña a una farra y luego a 
un caserón en la Ciudad Vieja, ya con el sol bien alto. En el último patio, que es de 
tierra, los hombres tienden su recado para dormir. Oscuramente, Otálora compara 
esa noche con la anterior; ahora ya pisa tierra firme, entre amigos. Lo inquieta 
algún remordimiento, eso sí, de no extrañar a Buenos Aires. Duerme hasta la 
oración, cuando lo despierta el paisano que agredió, borracho, a Bandeira. (Otálora 
recuerda que ese hombre ha compartido con los otros la noche de tumulto y de 
júbilo y que Bandeira lo sentó a su derecha y lo obligó a seguir bebiendo.) El 
hombre le dice que el patrón lo manda buscar. En una suerte de escritorio que da al 
zaguán (Otálora nunca ha visto un zaguán con puertas laterales) está esperándolo 
Azevedo Bandeira, con una clara y desdeñosa mujer de pelo colorado. Bandeira lo 
pondera, le ofrece una copa de caña, le repite que le está pareciendo un hombre 
animoso, le propone ir al Norte con los demás a traer una tropa. Otálora acepta; 
hacia la madrugada están en camino, rumbo a Tacuarembó. 
Empieza entonces para Otálora una vida distinta, una vida de vastos amaneceres y 
de jornadas que tienen el olor del caballo. Esa vida es nueva para él, y a veces 
atroz, pero ya está en su sangre, porque lo mismo que los hombres de otras 
naciones veneran y presienten el mar, así nosotros (también el hombre que entreteje 
estos símbolos) ansiamos la llanura inagotable que resuena bajo los cascos. Otálora 
se ha criado en los barrios del carrero y del cuarteador; antes de un año se hace 
gaucho. Aprende a jinetear, a entropillar la hacienda, a carnear, a manejar el lazo 
que sujeta y las boleadoras que tumban, a resistir el sueño, las tormentas, las 
heladas y el sol, a arrear con el silbido y el grito. Sólo una vez, durante ese tiempo 
de aprendizaje, ve a Azevedo Bandeira, pero lo tiene muy presente, porque ser 
hombre de Bandeira es ser considerado y temido, y porque, ante cualquier 
hombrada, los gauchos dicen que Bandeira lo hace mejor. Alguien opina que 
Bandeira nació del otro lado del Cuareim, en Rio Grande do Sul; eso, que debería 
rebajarlo, oscuramente lo enriquece de selvas populosas, de ciénagas, de 
inextricable y casi infinitas distancias. Gradualmente, Otálora entiende que los 
negocios de Bandeira son múltiples y que el principal es el contrabando. Ser 
tropero es ser un sirviente; Otálora se propone ascender a contrabandista. Dos de 
los compañeros, una noche, cruzarán la frontera para volver con unas partidas de 
caña; Otálora provoca a uno de ellos, lo hiere y toma su lugar. Lo mueve la 
ambición y también una oscura fidelidad. Que el hombre (piensa) acabe por 
entender que yo valgo más que todos sus orientales juntos. 
Otro año pasa antes que Otálora regrese a Montevideo. Recorren las orillas, la 
ciudad (que a Otálora le parece muy grande); llegan a casa del patrón; los hombres 
tienden los recados en el último patio. Pasan los días y Otálora no ha visto a 
Bandeira. Dicen, con temor, que está enfermo; un moreno suele subir a su 
dormitorio con la caldera y con el mate. Una tarde, le encomiendan a Otálora esa 
tarea. Éste se siente vagamente humillado, pero satisfecho también. 
El dormitorio es desmantelado y oscuro. Hay un balcón que mira al poniente, hay 
una larga mesa con un resplandeciente desorden de taleros, de arreadores, de cintos, 
de armas de fuego y de armas blancas, hay un remoto espejo que tiene la luna 
empañada. Bandeira yace boca arriba; sueña y se queja; una vehemencia de sol 
último lo define. El vasto lecho blanco parece disminuirlo y oscurecerlo; Otálora 
nota las canas, la fatiga, la flojedad, las grietas de los años. Lo subleva que los esté 
mandando ese viejo. Piensa que un golpe bastaría para dar cuenta de él. En eso, ve 
en el espejo que alguien ha entrado. Es la mujer de pelo rojo; está a medio vestir y 
descalza y lo observa con fría curiosidad. Bandeira se incorpora; mientras habla de 
cosas de la campaña y despacha mate tras mate, sus dedos juegan con las trenzas de 
la mujer. Al fin, le da licencia a Otálora para irse. 
Días después, les llega la orden de ir al Norte. Arriban a una estancia perdida, que 
está como en cualquier lugar de la interminable llanura. Ni árboles ni un arroyo la 
alegran, el primer sol y el último la golpean. Hay corrales de piedra para la 
hacienda, que es guampuda y menesterosa. "El Suspiro" se llama ese pobre 
establecimiento. Otálora oye en rueda de peones que Bandeira no tardará en llegar 
de Montevideo. Pregunta por qué; alguien aclara que hay un forastero agauchado 
que está queriendo mandar demasiado. Otálora comprende que es una broma, pero 
le halaga que esa broma ya sea posible. Averigua, después, que Bandeira se ha 
enemistado con uno de los jefes políticos y que éste le ha retirado su apoyo. Le 
gusta esa noticia. 
Llegan cajones de armas largas; llegan una jarra y una palangana de plata para el 
aposento de la mujer; llegan cortinas de intrincado damasco; llega de las cuchillas, 
una mañana, un jinete sombrío, de barba cerrada y de poncho. Se llama Ulpiano 
Suárez y es el capanga o guardaespaldas de Azevedo Bandeira. Habla muy poco y 
de una manera abrasilerada. Otálora no sabe si atribuir su reserva a hostilidad, a 
desdén o a mera barbarie. Sabe, eso si, que para el plan que está maquinando tiene 
que ganar su amistad. Entra después en el destino de Benjamin Otálora un colorado 
cabos negros que trae del sur Azevedo Bandeira y que luce apero chapeado y 
carona con bordes de piel de tigre. Ese caballo liberal es un símbolo de la autoridad 
del patrón y por eso lo codicia el muchacho, que llega también a desear, con deseo 
rencoroso, a la mujer de pelo resplandeciente. La mujer, el apero y el colorado son 
atributos o adjetivos de un hombre que él aspira a destruir. 
Aquí la historia se complica y se ahonda. Azevedo Bandeira es diestro en el arte de 
la intimidación progresiva, en la satánica maniobra de humillar al interlocutor 
gradualmente, combinando veras y burlas; Otálora resuelve aplicar ese método 
ambiguo a la dura tarea que se propone. Resuelve suplantar, lentamente, a Azevedo 
Bandeira. Logra, en jornadas de peligro común, la amistad de Suárez. Le confía su 
plan; Suárez le promete su ayuda. Muchas cosas van aconteciendo después, de las 
que sé unas pocas. Otálora no obedece a Bandeira; da en olvidar, en corregir, en 
invertir sus órdenes. El universo parece conspirar con él y apresura los hechos. Un 
mediodía, ocurre en campos de Tacuarembó un tiroteo con gente riograndense; 
Otálora usurpa el lugar de Bandeira y manda a los orientales. Le atraviesa el 
hombro una bala, pero esa tarde Otálora regresa al "Suspiro" en el colorado del jefe 
y esa tarde unas gotas de su sangre manchan la piel de tigre y esa noche duerme 
con la mujer de pelo reluciente. Otras versiones cambian el orden de estos hechos y 
niegan que hayan ocurrido en un solo día. 
Bandeira, sin embargo, siempre es nominalmente el jefe. Da órdenes que no se 
ejecutan; Benjamín Otálora no lo toca, por una mezcla de rutina y de lástima. 
La última escena de la historia corresponde a la agitación de la última noche de 
1894. Esa noche, los hombres del "Suspiro" comen cordero recién carneado y 
beben un alcohol pendenciero. Alguien infinitamente rasguea una trabajosa 
milonga. En la cabecera de la mesa, Otálora, borracho, erige exultación sobre 
exultación, júbilo sobre júbilo; esa torre de vértigo es un símbolo de su irresistible 
destino. Bandeira, taciturno entre los que gritan, deja que fluya clamorosa la noche. 
Cuando las doce campanadas resuenan, se levanta como quien recuerda una 
obligación. Se levanta y golpea con suavidad a la puerta de la mujer. Ésta le abre en 
seguida, como si esperara el llamado. Sale a medio vestir y descalza. Con una voz 
que se afemina y se arrastra, el jefe le ordena: 
-Ya que vos y el porteño se quieren tanto, ahora mismo le vas a dar un beso a vista 
de todos. 
Agrega una circunstancia brutal. La mujer quiere resistir, pero dos hombres la han 
tomado del brazo y la echan sobre Otálora. Arrasada en lágrimas, le besa la cara y 
el pecho. Ulpiano Suárez ha empuñado el revólver. Otálora comprende, antes de 
morir, que desde el principio lo han traicionado, que ha sido condenado a muerte, 
que le han permitido el amor, el mando y el triunfo, porque ya lo daban por muerto, 
porque para Bandeira ya estaba muerto. 
Suárez, casi con desdén, hace fuego.
"""


"""
return (2>1) ? 10 : 20
"""


def obtener_nombre_completo(sexo: str = "X") -> str:
    # Elegir la lista de nombres según el sexo
    if sexo == "X":
        sexo = "M" if random.randint(0, 1) == 0 else "F"

    nombres = MASCULINOS if sexo == "M" else FEMENINOS

    # Obtener un nombre aleatorio
    nombre = random.choice(nombres)

    # Probabilidad de tener un nombre compuesto (50%)
    if random.random() < 0.5:
        segundo_nombre = random.choice(nombres)
        # Asegurar que el segundo nombre sea diferente al primero
        while segundo_nombre == nombre:
            segundo_nombre = random.choice(nombres)
        nombre = f"{nombre} {segundo_nombre}"

    # Probabilidad de tener un tercer nombre (5%)
    if " " in nombre and random.random() < 0.05:
        tercer_nombre = random.choice(nombres)
        # Asegurar que el tercer nombre sea diferente
        # "Juan Pablo"
        while tercer_nombre in nombre.split():
            tercer_nombre = random.choice(nombres)
        nombre = f"{nombre} {tercer_nombre}"

    # Obtener un apellido aleatorio
    apellido = random.choice(APELLIDOS)

    # Probabilidad de tener un segundo apellido (30%)
    if random.random() < 0.3:
        segundo_apellido = random.choice(APELLIDOS)
        # Asegurar que el segundo apellido sea diferente al primero
        while segundo_apellido == apellido:
            segundo_apellido = random.choice(APELLIDOS)
        apellido = f"{apellido} {segundo_apellido}"

    return f"{nombre} {apellido}"


# Test de la función
if __name__ == "__main__":
    print(obtener_nombre_completo())
    print(obtener_nombre_completo(sexo="F"))
    print(obtener_nombre_completo("M"))
