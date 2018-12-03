Zhajinhua(Chinese Card Game) in Python
====

Group Name and Section
-------

Tools of Pynalitics

Section 2

Description
-------

This repository contains the Zhajinhua game, which is made in Python.

“Zhajinhua” is a two-player card game, which is widely spread throughout the China. Each player has three cards each round. Player will win if his/ her three cards are 'Bigger' than the other players'. The game needs to test the player's courage and wisdom.

# Rules of Zhajinhua
The number of participants in the game is two, using a total of 52 cards that red joker and black joker have been removed.

At first, player has 1000 dollar principal, and the initial bet is one dollar. Each round, player would compete with computer. When the game starts, player could see his or her three cards, but couldn't know computer's cards. Then player has right to bet again. After clicking 'Affirm' button, player could see computer's card and check who wins the game. If player wins game, the bet number would be added to principal, otherwise, bet would be subtracted from principla

#### Combinations of cards:

1. Bomb: Three cards with the same point. Example: A-A-A, 2-2-2

2. Straight: Three cards of consecutive rank. Example: 3-4-5

3. Straight flush: straight with same suit. Example: Spades 3-Spades 4-Spades 5

4. Pair: two matching cards of equal rank carrying one card. Example: 2-2-5

5. Single: Three cards do not form any type of combinations mentioned above. Example: 3-6-10

6. Flush： Three cards with the same suit. Example: Spades 3-Spades 8-Spades J


#### Rank of the combination:

1. Bomb > Straight flush > Flush > Straight > Pair > Single

2. Bomb: AAA > KKK >...> 333 > 222

3. Straight flush: AKQ > KQJ > ...> 234

4. Flush: Compare the largest card among three cards. For example, if one player has "3-6-10", the other has "3-6-13". The second player wins because 13 is larger than 10. If the largest card between two players are the same, compare the second largest card, otherwise compare the smallest card.

5. Straight: AKQ > KQJ > ...> 234

6. Pair: AA > KK > ... > 33 > 22. If the number of pairs are the same, compare the remaining card. For example, 3-3-2 is smaller than 3-3-4.

7. Single: A>K>Q>J>10>...>2 (11 represents 'J', 12 represents 'Q', 13 represents 'K', 14 represents 'A') The compare rules are the same as flush.

8. If the number and combinations of cards are totally the same between two players, player wins.



Installation Requirements
-------
1. Python 3.6+

2. All classes needed and GUI Zelle's graphics.py are included in this repository(put all files in the same directory)


Run Instructions
-------
1. Clone this repository:

'git@github.com:sl4430/Tools-of-Pynalitics.git'


2. Start the game with the command：

'python zhajinhua.py'

3. Click 'Deal' button to shuffle cards, then choose the amount you want to bet (the initial bet fee is 1$), and click 'Affirm' button to turn over computer's cards and settle your account. 

Reference
-------
graphics.py: It is written by John Zelle for use with the book "Python Programming: An Introduction to Computer Science" (Franklin, Beedle & Associates).

LICENSE: Zelle's graphics is open-source software released under the terms of the
GPL (http://www.gnu.org/licenses/gpl.html).
