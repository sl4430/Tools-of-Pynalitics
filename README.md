Zhajinhua(China Card Game) in Python
====

Group Name and Section
-------

Tools of Pynalitics

Section 2

Description
-------

This repository contains the Zhajinhua game, which is made in Python.

“Zhajinhua” is a two-player card game, which is widely spread throughout the China. Each player has three cards each round. Player will win if his/ her three cards are 'Bigger' than another players'. The game needs to test the player's courage and wisdom.

# Rules of Zhajinhua
The number of participants in the game is two, using a total of 52 cards that have been removed red joker and black joker.

#### Combinations of cards:

1.Bomb: Three cards with the same point. Example: A-A-A, 2-2-2

2.Straight: Three cards of consecutive rank. Example: 3-4-5

3.Straight flush: straight with same suit. Example: Spades 3-Spades 4-Spades 5

4.Pair: two matching cards of equal rank. Example: 2-2-5

5.Single: Three cards do not form any type of combinations mentioned above. Example: 3-6-10

6.Flush： Three cards with the same suit. Example: Spades 3-Spades 8-Spades J


#### Rank of the cards:

1. Bomb > Straight flush > Flush > Straight > Pair > Single

2. Bomb: AAA > KKK >...> 333 > 222

3. Straight flush: AKQ > KQJ > ...> 234

4. Flush:

5. Straight: AKQ > KQJ > ...> 234

6. Pair: AA > KK > ... > 333 > 222

7. Single: Compare the largest card among three cards. For example, if one player has "3-6-10", another player has "3-6-13". The second player win the game.



Requirements
-------

Run Instructions
-------
Clone this repository:

'git@github.com:sl4430/Tools-of-Pynalitics.git'


Start the game with the command：
