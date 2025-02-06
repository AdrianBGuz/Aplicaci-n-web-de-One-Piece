from flask import Flask, render_template

app = Flask(__name__)

# Lista de arcos de One Piece
arcos_one_piece = [
    "Arco de East Blue",
    "Arco de Baratie",
    "Arco de Arlong Park",
    "Arco de Loguetown",
    "Arco de Reverse Mountain",
    "Arco de Whisky Peak",
    "Arco de Little Garden",
    "Arco de Drum Island",
    "Arco de Arabasta",
    "Arco de Jaya",
    "Arco de Skypiea",
    "Arco de Water 7",
    "Arco de Enies Lobby",
    "Arco de Post-Enies Lobby",
    "Arco de Thriller Bark",
    "Arco de Sabaody Archipelago",
    "Arco de Amazon Lily",
    "Arco de Impel Down",
    "Arco de Marineford",
    "Arco de Post-Marineford",
    "Arco de Return to Sabaody",
    "Arco de Fishman Island",
    "Arco de Punk Hazard",
    "Arco de Dressrosa",
    "Arco de Zou",
    "Arco de Whole Cake Island",
    "Arco de Reverie",
    "Arco de Wano Country"
]

@app.route('/')
def index():
    return render_template('index.html', arcos=arcos_one_piece)

if __name__ == '__main__':
    app.run(debug=True)