from flask import Flask, render_template, request
import json

app = Flask(__name__)

# List of fragrances
fragrances = [
    "Acqua di Parma Colonia",
    "Armani Code",
    "Baccarat Rouge 540",
    "Black Orchid by Tom Ford",
    "Bleu de Chanel",
    "Boss Bottled by Hugo Boss",
    "Brit by Burberry",
    "Bvlgari Man in Black",
    "Byredo Gypsy Water",
    "Calvin Klein CK One",
    "Chanel Coco Mademoiselle",
    "Chanel No. 5",
    "Chloé Signature",
    "Christian Dior Fahrenheit",
    "Christian Dior Homme Intense",
    "Cool Water by Davidoff",
    "Creed Aventus",
    "Creed Silver Mountain Water",
    "Daisy by Marc Jacobs",
    "Diptyque Philosykos",
    "Dior J'adore",
    "Dior Sauvage",
    "Dolce & Gabbana Light Blue",
    "English Pear & Freesia by Jo Malone",
    "Eros by Versace",
    "Estée Lauder Pleasures",
    "Flowerbomb by Viktor & Rolf",
    "Gentleman by Givenchy",
    "Giorgio Armani Acqua di Gio",
    "Gucci Guilty",
    "Guerlain Shalimar",
    "Hermes Terre d'Hermes",
    "Invictus by Paco Rabanne",
    "Issey Miyake L'Eau d'Issey",
    "Jean Paul Gaultier Le Male",
    "Jasmine Sambac & Marigold by Jo Malone",
    "Jo Malone Lime Basil & Mandarin",
    "Jovan Musk",
    "Kilian Black Phantom",
    "La Vie Est Belle by Lancôme",
    "Lancome Tresor",
    "Le Labo Santal 33",
    "Light Blue by Dolce & Gabbana",
    "Lime Basil & Mandarin by Jo Malone",
    "Marc Jacobs Decadence",
    "Michael Kors by Michael Kors",
    "Mugler Angel",
    "Narciso Rodriguez For Her",
    "Narciso Rodriguez Pure Musc",
    "Nina by Nina Ricci",
    "Noir by Tom Ford",
    "Obsession by Calvin Klein",
    "Olympea by Paco Rabanne",
    "Opium by Yves Saint Laurent",
    "Oud Wood by Tom Ford",
    "Paco Rabanne 1 Million",
    "Paco Rabanne Lady Million",
    "Philosykos by Diptyque",
    "Pleasures by Estée Lauder",
    "Polo Blue by Ralph Lauren",
    "Prada L'Homme",
    "Ralph by Ralph Lauren",
    "Santal 33 by Le Labo",
    "Shalimar by Guerlain",
    "Si by Giorgio Armani",
    "Silver Mountain Water by Creed",
    "Tom Ford Black Orchid",
    "Tom Ford Oud Wood",
    "Tom Ford Tobacco Vanille",
    "Tommy by Tommy Hilfiger",
    "Tresor by Lancôme",
    "Valentino Uomo",
    "Van Cleef & Arpels Midnight in Paris",
    "Vanilla Fields by Coty",
    "Versace Bright Crystal",
    "Versace Eros",
    "Versace Pour Homme",
    "Vetiver by Guerlain",
    "Viktor & Rolf Spicebomb",
    "Y by Yves Saint Laurent",
    "Yves Saint Laurent Black Opium",
    "Yves Saint Laurent La Nuit De L'Homme",
    "Yves Saint Laurent Opium",
]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_rating = {fragrance: request.form.get(f'rating_{fragrance}') for fragrance in fragrances}

        try:
            with open('ratings.json', 'r') as file:
                ratings = json.load(file)
        except FileNotFoundError:
            ratings = []

        ratings.append(new_rating)

        with open('ratings.json', 'w') as file:
            json.dump(ratings, file)

        return "Thank you for your submission!"
    return render_template('index.html', fragrances=fragrances)

if __name__ == '__main__':
    app.run(debug=True)
