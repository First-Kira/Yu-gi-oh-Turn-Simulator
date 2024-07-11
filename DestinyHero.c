#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Define a structure for a card
typedef struct {
    char *name;
    char *imageUrl;
} Card;

// Function to shuffle an array using Fisher-Yates algorithm
void shuffle(Card *array, size_t n) {
    if (n > 1) {
        size_t i;
        for (i = 0; i < n - 1; i++) {
            size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
            Card temp = array[j];
            array[j] = array[i];
            array[i] = temp;
        }
    }
}

int main() {
    srand(time(NULL));  // Seed the random number generator

    // Define an array of cards
    Card deck[] = {
        {"Destiny HERO - Plasma", "https://example.com/card1.png"},
        {"Destiny HERO - Dogma", "https://example.com/card2.png"},
        {"Destiny HERO - Dark Angel", "https://example.com/card3.png"},
        {"Destiny HERO - Drawhand", "https://example.com/card4.png"},
        {"Destiny HERO - Diamond Dude", "https://example.com/card5.png"},
        {"Destiny HERO - Dasher", "https://example.com/card6.png"},
        {"Destiny HERO - Disk Commander", "https://example.com/card7.png"},
        {"Destiny HERO - Dreamer", "https://example.com/card8.png"},
        {"Destiny HERO - Malicious", "https://example.com/card9.png"},
        {"Destiny HERO - Destiny Draw", "https://example.com/card10.png"},
        {"Destiny HERO - Destiny Fusion", "https://example.com/card11.png"},
        {"Destiny HERO - D-Tactics", "https://example.com/card12.png"},
        {"Destiny HERO - Dark Drill", "https://example.com/card13.png"},
        {"Break the Destiny", "https://example.com/card14.png"},
        {"Future Fusion", "https://example.com/card15.png"},
        {"Necro Fusion", "https://example.com/card16.png"},
        {"Polymerization", "https://example.com/card17.png"},
        {"Raigeki", "https://example.com/card18.png"},
        {"Lightning Storm", "https://example.com/card19.png"},
        {"Monster Reborn", "https://example.com/card20.png"}
    };
    size_t deck_size = sizeof(deck) / sizeof(deck[0]);

    // Shuffle the deck
    shuffle(deck, deck_size);

    // Print out a random selection of cards
    int num_cards = 5;
    for (int i = 0; i < num_cards; i++) {
        printf("Card Name: %s\n", deck[i].name);
        printf("Image URL: %s\n", deck[i].imageUrl);
        printf("\n");
    }

    return 0;
}
