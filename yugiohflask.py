from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        message = "Hello World"
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Yu-Gi-Oh! Random Hand</title>
            <style>
                .card {
                    display: inline-block;
                    margin: 10px;
                    text-align: center;
                }
                .card img {
                    width: 100px;
                    height: 150px;
                }
            </style>
        </head>
        <body>
            <h1>{{ message }}</h1>
            <form method="post">
                <button type="submit">Click me!</button>
            </form>
            <h1>Random Yu-Gi-Oh! Hand</h1>
            <button onclick="getRandomCards()">Get Random Cards</button>
            <div id="card-container"></div>

            <script>
                const deck = [
                    {name: "Destiny HERO - Plasma", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/0/00/DestinyHEROPlasma-SGX1-EN-C-1E.png/revision/latest?cb=20220410014702", count: 3},
                    {name: "Destiny HERO - Dogma", imageUrl: "https://ms.yugipedia.com//9/90/DestinyHERODogma-SGX1-EN-C-1E.png?download", count: 3},
                    {name: "Dark Drill", imageUrl: "https://ms.yugipedia.com//e/ec/DestinyHERODrawhand-MP20-EN-C-1E.png", count: 3},
                    {name: "Destiny HERO - Drawhand", imageUrl: "https://ms.yugipedia.com//e/ec/DestinyHERODrawhand-MP20-EN-C-1E.png", count: 3},
                    {name: "Break the Destiny", imageUrl: "https://ms.yugipedia.com//thumb/c/cd/BreaktheDestiny-BODE-EN-C-1E.png/450px-BreaktheDestiny-BODE-EN-C-1E.png", count: 2},
                    {name: "D - Tactics", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/d/d7/DTactics-DANE-EN-R-1E.png/revision/latest?cb=20190503164804", count: 2},
                    {name: "Polymerization", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/7/73/Polymerization-SBC1-EN-C-1E.png/revision/latest?cb=20230918234835", count: 3},
                    {name: "Destiny HERO - Dasher", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/5/53/DestinyHERODasher-SGX1-EN-C-1E.png/revision/latest?cb=20220410014951", count: 3},
                    {name: "Destiny HERO - Diamond Dude", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/b/bf/DestinyHERODiamondDude-SGX1-EN-C-1E.png/revision/latest?cb=20220410014839", count: 3},
                    {name: "Destiny Fusion", imageUrl: "https://ms.yugipedia.com//d/dc/FusionDestiny-BLC1-EN-C-1E.png", count: 2},
                    {name: "Future Fusion", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/b/b7/FutureFusion-SGX1-EN-C-1E.png/revision/latest?cb=20220419174251", count: 2},
                    {name: "Necro Fusion", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/e/eb/NecroFusion-SDAZ-EN-C-1E.png/revision/latest/scale-to-width-down/300?cb=20220506020833", count: 2},
                    {name: "Raigeki", imageUrl: "https://ms.yugipedia.com//1/1d/Raigeki-LOB-EN-SR-UE-25thAnniversaryEdition.png", count: 2},
                    {name: "Lightning Storm", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/6/61/LightningStorm-MAMA-EN-UR-1E.png/revision/latest?cb=20221203232338", count: 1},
                    {name: "Monster Reborn", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/4/40/MonsterReborn-EGO1-EN-C-1E.png/revision/latest?cb=20210920164521", count: 1},
                    {name: "Destiny HERO - Disk Commander", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/e/e0/DestinyHERODiskCommander-LEHD-EN-UR-1E.png/revision/latest?cb=20181012170703", count: 1},
                    {name: "Destiny Draw", imageUrl: "https://ms.yugipedia.com//2/29/DestinyDraw-LEHD-EN-C-1E.png", count: 3},
                    {name: "Destiny HERO - Malicious", imageUrl: "https://ms.yugipedia.com//thumb/b/b3/DestinyHEROMalicious-BLC1-EN-UR-1E.png/450px-DestinyHEROMalicious-BLC1-EN-UR-1E.png", count: 2},
                    {name: "Destiny HERO - Dreamer", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/e/ef/DestinyHERODreamer-LEHD-EN-C-1E.png/revision/latest?cb=20181012170856", count: 2},
                    {name: "Destiny HERO - Dark Angel", imageUrl: "https://static.wikia.nocookie.net/yugioh/images/e/ea/DestinyHERODarkAngel-SGX1-EN-C-1E.png/revision/latest?cb=20220410015314", count: 2}
                ];

                function getRandomCards() {
                    let allCards = [];
                    deck.forEach(card => {
                        for (let i = 0; i < card.count; i++) {
                            allCards.push(card);
                        }
                    });
                    
                    const shuffled = allCards.sort(() => 0.5 - Math.random());
                    const selectedCards = shuffled.slice(0, 5);
                    
                    const cardContainer = document.getElementById('card-container');
                    cardContainer.innerHTML = '';
                    selectedCards.forEach(card => {
                        const cardElement = document.createElement('div');
                        cardElement.className = 'card';
                        cardElement.innerHTML = `
                            <img src="${card.imageUrl}" alt="${card.name}">
                            <p>${card.name}</p>
                        `;
                        cardContainer.appendChild(cardElement);
                    });
                }
            </script>
        </body>
        </html>
    ''', message=message)

if __name__ == '__main__':
    app.run(debug=True)