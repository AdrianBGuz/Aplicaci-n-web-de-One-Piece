from flask import Flask, render_template

app = Flask(__name__)

# Lista de arcos de One Piece
one_piece_arcs = [
   {"name": "East Blue", "description": "El arco de East Blue es donde comienza la aventura de Luffy y donde recluta a sus primeros compañeros, como Zoro, Nami, Usopp y Sanji."},

   {"name": "Baratie", "description": "En el arco de Baratie, Luffy y su tripulación se encuentran con Sanji, un talentoso cocinero, en un restaurante flotante. También luchan contra el pirata Don Krieg."},

   {"name": "Arlong Park", "description": "En el arco de Arlong Park, los Sombrero de Paja enfrentan al hombre-pez Arlong, quien tiene esclavizada a la aldea de Nami. Este arco destaca por la emotiva historia de Nami."},

   {"name": "Loguetown", "description": "En el arco de Loguetown, la tripulación visita la ciudad donde nació y murió Gol D. Roger, el Rey de los Piratas. Aquí, Luffy tiene un encuentro cercano con el Capitán Smoker."},

   {"name": "Reverse Mountain", "description": "El arco de Reverse Mountain marca la entrada de los Sombrero de Paja al Grand Line, cruzando la peligrosa montaña y conociendo a Laboon, la ballena gigante."},

   {"name": "Whisky Peak", "description": "En Whisky Peak, la tripulación llega a una isla que parece ser amigable, pero resulta ser un nido de cazadores de recompensas. Zoro muestra su habilidad en combate."},

   {"name": "Little Garden", "description": "El arco de Little Garden lleva a los Sombrero de Paja a una isla prehistórica, donde se encuentran con dos gigantes guerreros y luchan contra agentes de Baroque Works."},

   {"name": "Drum Island", "description": "En el arco de Drum Island, la tripulación busca un doctor para Nami, quien está enferma. Aquí, se encuentran con Tony Tony Chopper y luchan contra el cruel rey Wapol."},

   {"name": "Arabasta", "description": "En el arco de Arabasta, los Sombrero de Paja ayudan a la princesa Vivi a salvar su reino de la organización Baroque Works y su líder, Crocodile."},

   {"name": "Jaya", "description": "El arco de Jaya lleva a la tripulación a una isla gobernada por piratas. Aquí, conocen a Bellamy y descubren pistas sobre la legendaria isla del cielo, Skypiea."},

   {"name": "Skypiea", "description": "El arco de Skypiea lleva a los Sombrero de Paja a una isla en el cielo, donde descubren una antigua civilización y luchan contra el dios Enel."},

   {"name": "Water 7", "description": "En Water 7, la tripulación busca reparar el Going Merry y se enfrenta a CP9, una organización secreta del Gobierno Mundial."},

   {"name": "Enies Lobby", "description": "El arco de Enies Lobby es donde los Sombrero de Paja rescatan a Robin y declaran la guerra al Gobierno Mundial."},

   {"name": "Post-Enies Lobby", "description": "Tras los eventos de Enies Lobby, la tripulación celebra su victoria y se preparan para nuevos desafíos. Aquí, obtienen su nuevo barco, el Thousand Sunny."},

   {"name": "Thriller Bark", "description": "En Thriller Bark, los Sombrero de Paja se enfrentan al Shichibukai Gecko Moria en una isla que es en realidad un enorme barco pirata."},

   {"name": "Sabaody Archipelago", "description": "En el arco de Sabaody Archipelago, la tripulación se enfrenta a los Dragones Celestiales y conoce a Rayleigh, el antiguo primer oficial del Rey de los Piratas."},
 
   {"name": "Amazon Lily", "description": "El arco de Amazon Lily sigue a Luffy en una isla habitada únicamente por mujeres guerreras. Aquí, conoce a Boa Hancock, una Shichibukai que se enamora de él."},

   {"name": "Impel Down", "description": "En el arco de Impel Down, Luffy se infiltra en la prisión más segura del mundo para rescatar a su hermano Ace, enfrentándose a varios peligrosos enemigos en el proceso."},

   {"name": "Marineford", "description": "El arco de Marineford es una gran guerra donde Luffy y una alianza de piratas luchan contra la Marina para rescatar a Ace, quien está condenado a ser ejecutado."},

   {"name": "Post-Marineford", "description": "Tras la batalla de Marineford, Luffy y sus amigos se recuperan y se preparan para los desafíos que vienen, marcando el comienzo de la nueva era de piratas."},

   {"name": "Return to Sabaody", "description": "Después de dos años de entrenamiento, la tripulación de los Sombrero de Paja se reúne en Sabaody Archipelago y se preparan para adentrarse en el Nuevo Mundo."},

   {"name": "Fishman Island", "description": "En Fishman Island, la tripulación llega a una isla submarina y se enfrenta a Hody Jones, un hombre-pez rebelde, mientras intentan proteger el reino de la princesa Shirahoshi."},

   {"name": "Punk Hazard", "description": "El arco de Punk Hazard lleva a los Sombrero de Paja a una isla dividida entre fuego y hielo, donde se enfrentan a Caesar Clown, un científico loco."},

   {"name": "Dressrosa", "description": "En Dressrosa, la tripulación se enfrenta al Shichibukai Donquixote Doflamingo, quien gobierna la isla con mano de hierro, mientras liberan a los habitantes oprimidos."},

   {"name": "Zou", "description": "El arco de Zou sigue a los Sombrero de Paja mientras visitan un enorme elefante gigante que lleva una ciudad en su espalda. Aquí, se alían con los Minks para luchar contra Kaido."},

   {"name": "Whole Cake Island", "description": "En Whole Cake Island, la tripulación intenta rescatar a Sanji de un matrimonio arreglado y se enfrenta a Big Mom, una de los Cuatro Emperadores."},

   {"name": "Reverie", "description": "El arco de Reverie sigue a los líderes del mundo mientras se reúnen para discutir importantes asuntos globales, revelando secretos y preparando el escenario para futuras tramas."},

   {"name": "Wano Country", "description": "El arco de Wano Country lleva a los Sombrero de Paja a un país aislado inspirado en el Japón feudal, donde luchan contra el Emperador Kaido y sus seguidores para liberar la nación."},
]

@app.route('/')
def index():
    return render_template('index.html', arcs=one_piece_arcs)

if __name__ == '__main__':
    app.run(debug=True)