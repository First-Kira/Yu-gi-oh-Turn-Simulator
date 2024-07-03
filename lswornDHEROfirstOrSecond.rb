class Deck
  attr_accessor :cards

  def initialize(cards = [])
    @cards = cards
  end

  def add_cards(name, count)
    count.times { @cards << name }
  end

  def shuffle
    @cards.shuffle!
  end

  def draw(num)
    @cards.shift(num)
  end

  def card_count
    @cards.size
  end
end

def create_lightsworn_deck
  deck = Deck.new
  deck.add_cards("Judgment Dragon", 3)
  deck.add_cards("Solar Recharge", 3)
  deck.add_cards("Charge of the Light Brigade", 1)
  deck.add_cards("Lightsworn Sanctuary", 1)
  deck.add_cards("Realm of Light", 1)
  deck.add_cards("Gragonith", 2)
  deck.add_cards("Lumina, Lightsworn Summoner", 3)
  deck.add_cards("Lumina, Twilightsworn Shaman", 3)
  deck.add_cards("Minerva, Lightsworn Maiden", 3)
  deck.add_cards("Lyla, Lightsworn Sorceress", 3)
  deck.add_cards("Wulf, Lightsworn Beast", 3)
  deck.add_cards("Ehren, Lightsworn Monk", 3)
  deck.add_cards("Raiden, Hand of the Lightsworn", 3)
  deck.add_cards("Felis, Lightsworn Archer", 3)
  deck.add_cards("Electromagnetic Turtle", 1)
  deck.add_cards("Starliege Seyfert", 2)
  deck.add_cards("Twilight Eraser", 3)
  deck.add_cards("Breakthrough Skill", 3)
  deck.add_cards("Galaxy Cyclone", 3)
  deck
end

def create_destiny_hero_deck
  deck = Deck.new
  deck.add_cards("Destiny HERO - Plasma", 3)
  deck.add_cards("Destiny HERO - Dogma", 3)
  deck.add_cards("Dark Drill", 3)
  deck.add_cards("Destiny HERO - Drawhand", 3)
  deck.add_cards("Break the Destiny", 2)
  deck.add_cards("D - Tactics", 2)
  deck.add_cards("Polymerization", 3)
  deck.add_cards("Destiny HERO - Dasher", 3)
  deck.add_cards("Destiny HERO - Diamond Dude", 3)
  deck.add_cards("Destiny Fusion", 2)
  deck.add_cards("Future Fusion", 2)
  deck.add_cards("Necro Fusion", 2)
  deck.add_cards("Raigeki", 2)
  deck.add_cards("Harpie's Feather Duster", 1)
  deck.add_cards("Monster Reborn", 1)
  deck.add_cards("Destiny HERO - Disk Commander", 1)
  deck.add_cards("Destiny Draw", 3)
  deck.add_cards("Destiny HERO - Malicious", 2)
  deck.add_cards("Destiny HERO - Dreamer", 2)
  deck.add_cards("Destiny HERO - Dark Angel", 2)
  deck
end

def draw_hand(deck)
  # Initialize and shuffle the deck
  deck.shuffle

  # Ask if going first or second
  puts "Are you going first or second? (enter 'first' or 'second')"
  choice = gets.chomp.downcase

  # Draw cards based on choice
  if choice == 'first'
    hand = deck.draw(5)
    puts "You are going first. Your starting hand is:"
  else
    hand = deck.draw(6)
    puts "You are going second. Your starting hand is:"
  end

  hand.each { |card| puts card }
end

# Create and draw hands for both decks
lightsworn_deck = create_lightsworn_deck
destiny_hero_deck = create_destiny_hero_deck

puts "Choose your deck: (enter 'lightsworn' or 'destiny')"
deck_choice = gets.chomp.downcase

if deck_choice == 'lightsworn'
  draw_hand(lightsworn_deck)
else
  draw_hand(destiny_hero_deck)
end
