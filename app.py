from flask import Flask, render_template, request
import json

app = Flask(__name__)

# List of fragrances
fragrances = [
    "Chanel No. 5",
    "Dior Sauvage",
    "Bleu de Chanel",
    "Yves Saint Laurent La Nuit De L'Homme",
    "Creed Aventus",
    "Jo Malone English Pear & Freesia",
    "Paco Rabanne 1 Million",
    "Tom Ford Black Orchid",
    "Giorgio Armani Acqua di Gio",
    "Guerlain Shalimar",
    "Lancôme La Vie Est Belle",
    "Versace Eros",
    "Dolce & Gabbana Light Blue",
    "Calvin Klein CK One",
    "Jean Paul Gaultier Le Male",
    "Bvlgari Man in Black",
    "Marc Jacobs Daisy",
    "Hugo Boss Bottled",
    "Estée Lauder Pleasures",
    "Chanel Coco Mademoiselle",
    "Dior J'adore",
    "Tom Ford Tobacco Vanille",
    "Armani Code",
    "Christian Dior Homme Intense",
    "Viktor & Rolf Flowerbomb",
    "Prada L'Homme",
    "Le Labo Santal 33",
    "Paco Rabanne Invictus",
    "Ralph Lauren Polo Blue",
    "Givenchy Gentleman",
    "Chanel Bleu de Chanel",
    "Maison Francis Kurkdjian Baccarat Rouge 540",
    "Gucci Guilty",
    "Narciso Rodriguez For Her",
    "Thierry Mugler Alien",
    "Yves Saint Laurent Black Opium",
    "Chloé Signature",
    "Issey Miyake L'Eau d'Issey",
    "Christian Dior Fahrenheit",
    "Acqua di Parma Colonia",
    "Jo Malone Lime Basil & Mandarin",
    "Byredo Gypsy Water",
    "Hermes Terre d'Hermes",
    "Burberry Brit",
    "Davidoff Cool Water",
    "Tom Ford Oud Wood",
    "Creed Silver Mountain Water",
    "Diptyque Philosykos",
    "Mugler Angel",
    "Kilian Black Phantom"
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
