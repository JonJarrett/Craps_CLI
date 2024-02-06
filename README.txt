Craps CLI program


Hello, I'm Jon. I am attempting to become a self-taught Software Developer and this is my first program.
I know this is quite sloppy and there are some bugs I can't replicate or don't know how to fix. I tried to catch
what would be common mistakes, but I'm sure I have missed some.

It is helpful to understand how the game of Craps works to understand what the program is trying to do. I will put a
description for those that don't play craps at the end of the README. I know the code is really sloppy, but it seems
to get the job done. It allows a single player to determine how much money they would like to play with, bet on the
Pass Line or Don't Pass Line and make standard bets on the numbers. I would like to incorporate a GUI, multiple players
and also the ability to make more bets in the future.

I could use some tips on how to make my code more concise, better ways to write it or any bugs that are found so that I
can try to improve the program. I don't know much on how GitHub works for messages/commenting so reddit might be the
easiest way (You probably came from reddit anyway).


/u/WalkingParaDocs






Craps Table: Understanding the Basics
The first thing to learn in Craps 101 is that the game is based around simply betting on the outcome of the roll of two
dice, but there are lots of ways the dice can fall.

There can be as many as eight players at the craps table, and each player can bet on every roll. Each player gets a
chance at rolling the dice (known as the shooter). A player’s first roll at the table is known as the come-out roll.
This initial roll has three possible outcomes:

Natural Numbers
A come-out roll that lands a 7 or 11 is a winner and is known as a natural. Any bets that were placed on the
“pass line” for this roll will win, and any on the “don’t pass line” will lose. Whenever a natural is rolled,
you’ll get another chance at shooting the dice.

Crap Numbers
When players get a 2, 3 or 12 during a come-out roll, any bets placed on the pass line will lose. Bets on the
don’t pass line will win, although the 12 or 2 may be a push depending on the casino’s rules for the craps table.
The upside of shooting craps is that you’ll get another shot at rolling the dice.

Point Numbers
When your initial roll is one of the place numbers (4, 5, 6, 8, 9 or 10), the dealer marks it as a point on the table.
You’ll then have to roll that number before a 7 for any pass bets to win and bets on the don’t pass line to lose, plus
you’ll get to roll again. Rolling a 7 before the point will have the opposite effect.


What Bets Can You Make in Craps?
From the simple pass line bet to those on place numbers 4, 5, 6, 8, 9 or 10 to land, there are various ways to bet on
each roll of the dice. Here’s a breakdown of the different bets available at the craps table:

Pass Line Bet | A bet on the pass line is a bet on the shooter’s roll to win. Bets on the pass line are the simplest to
make — you’re betting on the dice to roll a 7 or 11 on the come-out roll or on the shooter to successfully hit an
established point. If a craps number is rolled, your bet loses.

Don’t Bets | These bets are the opposite of bets on the pass line and come line. Remember these are technically bets
against the shooter. Although some think it is rude, many players build their entire craps strategy on making
Don’t Bets. They aren’t contract bets though and can be taken back at any time.

Place Bet | These bets are on a roll of 4, 5, 6, 8, 9 and 10 before a 7 is rolled. All you have to do is pick one or
more place numbers to bet on and get paid every time each number is rolled. There isn’t even a pass line bet necessary,
unless you are the Shooter.


Gameplay
There are 2 stages of the game, the come-out roll and when a point has been established, the actual game. Once a point
has been established the Shooter may place additional bets on the 4, 5, 6, 8, 9 or 10 and keeps rolling the dice until
they  either roll a 7 or roll the point number. When the point or a 7 was rolled, depending on whether the player bet
on the Pass or Don't Pass Line, they either won or lost their initial bet(Pass or Don't Pass). If a 7 was rolled, all
place bets are lost. At that point the game moves back to the come-out roll and the game starts over again.