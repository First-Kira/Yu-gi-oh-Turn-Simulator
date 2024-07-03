class Deck
  attr_accessor :cards

  def initialize
    @cards = []
    add_cards("Judgment Dragon", 3)
    add_cards("Solar Recharge", 3)
    add_cards("Charge of the Light Brigade", 1)
    add_cards("Lightsworn Sanctuary", 1)
    add_cards("Realm of Light", 1)
    add_cards("Gragonith", 2)
    add_cards("Lumina, Lightsworn Summoner", 3)
    add_cards("Lumina, Twilightsworn Shaman", 3)
    add_cards("Minerva, Lightsworn Maiden", 3)
    add_cards("Lyla, Lightsworn Sorceress", 3)
    add_cards("Wulf, Lightsworn Beast", 3)
    add_cards("Ehren, Lightsworn Monk", 3)
    add_cards("Raiden, Hand of the Lightsworn", 3)
    add_cards("Felis, Lightsworn Archer", 3)
    add_cards("Electromagnetic Turtle", 1)
    add_cards("Starliege Seyfert", 2)
    add_cards("Twilight Eraser", 3)
    add_cards("Breakthrough Skill", 3)
    add_cards("Galaxy Cyclone", 3)
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
end

# Initialize and shuffle the deck
deck = Deck.new
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
