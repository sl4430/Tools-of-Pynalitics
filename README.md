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

At first, player has 1000 dollar principal, and the initial bet is one dollar. Each round, player would compete with computer. When the game starts, player could see his or her three cards, but couldn't know computer's cards. Then player has right to bet again. After clicking 'Affirm' button, player could see computer's card and check who wins the game. If player wins game, the bet number would be added to principal. 

#### Combinations of cards:

1. Bomb: Three cards with the same point. Example: A-A-A, 2-2-2

2. Straight: Three cards of consecutive rank. Example: 3-4-5

3. Straight flush: straight with same suit. Example: Spades 3-Spades 4-Spades 5

4. Pair: two matching cards of equal rank. Example: 2-2-5

5. Single: Three cards do not form any type of combinations mentioned above. Example: 3-6-10

6. Flush： Three cards with the same suit. Example: Spades 3-Spades 8-Spades J


#### Rank of the cards:

1. Bomb > Straight flush > Flush > Straight > Pair > Single

2. Bomb: AAA > KKK >...> 333 > 222

3. Straight flush: AKQ > KQJ > ...> 234

4. Flush: Compare the largest card among three cards. For example, if one player has "3-6-10", another player has "3-6-13". The second player wins the game because 13 is larger than 10.

5. Straight: AKQ > KQJ > ...> 234

6. Pair: AA > KK > ... > 333 > 222

7. Single: Compare the largest card among three cards



Requirements
-------

Run Instructions
-------
Clone this repository:

'git@github.com:sl4430/Tools-of-Pynalitics.git'


Start the game with the command：
