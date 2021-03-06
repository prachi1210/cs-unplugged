# Divide and conquer

## Key questions

Imagine 31 numbers have been organised in ascending order in a list by a computer program.
Now the program has to find a number in the list, but it can only look at one number at a time.
Is it easier to find the number now, than if they were in a random order?

### Potential answers could include:

-   The information is organised in a way that makes it more efficient to find.
    By guessing one number and checking it, you can use logical thinking to eliminate the numbers below or above the number guessed because you know the numbers are in order.
-   If they are in random order you can't use a strategy to find them quickly.

## Lesson starter

We have 31 different numbers, one on each card.
You can’t see them but this time they are in order from the lowest number to the highest number.
The numbers range from 0 to 1000.
Can you find number **302**

{panel type="teaching" title="Teaching observations"}

You can adapt the range to suit what your students are working on in their mathematics lessons.
This lesson focuses on sorted lists and we are using a range of numbers from 0 - 999.
This activity works best if the numbers **aren’t** sequential because, for example, if there are 50 cards in the range 1 to 50 and they are sequential and you ask a student to find the number 10 they will probably just look at the 10th card straight away!
You can generate different sets of cards with various ranges of numbers [here]('resources:resource' 'searching-cards').
It's best if the numbers aren't spread evenly so that it's very hard to guess where a particular value might be.

{panel end}

## Lesson activities

Set up a line of cards, with the animal facing upwards.

1.  Have a payment system ready such as tokens for your classroom, counters, sweets, or marbles.

The game is even better if you have some real stakes - for example: I have 10 marbles each is worth 2 minutes of game time.
For every token you use to find the number I’m thinking of, you will lose a marble.

Let’s see how many guesses it takes to find the number: 302

Who would like the first guess? (Choose a student).
Which animal should I turn over? Tell us why you chose that guess.
(They should be selecting the card that is exactly half way.
If they didn’t, check with the class if they agree with the choice or could they add to the student’s thinking to select the middle card.
If they decide not to, that's fine; they will learn the hard way if they use a less efficient approach.)

Turn over the chosen card to show the number under it.
If it's the correct one, you can stop, otherwise _remove that card and all other cards that the number can’t be_ (which will either be all cards to the right or all cards to the left of the chosen one) and take away one token from your pile.
Repeat this process until a student chooses the card with your number on it; if they use all ten tokens then the teacher "wins".

How many guesses did it take to find the number?

With each guess, how many cards were eliminated from being a possibility?
(Answer: half the cards could be eliminated with each guess if you picked the middle card. )

Did the students win because they guessed within 10  guesses or did you win because it took them longer?

Repeat this game until the students have won 3 times or you have won 3 times.

{panel type="teaching" title="Teaching observations"}

The number of guesses required can be anything from 1 (if you are lucky the first time), to 5 (if you have chosen the middle number each time).
Of course, they may use more than 5 guesses if they use a poor strategy. Most of the time they will need close to 5 guesses.
This also means that students will always have tokens left if they use a good strategy, since the maximum number of guesses to find the number is 5.

{panel end}

## Applying what we have just learnt

If any data is organised in order and a binary search is applied, then you can eliminate a lot of data quickly - cutting the number of items in half each time.
As a slightly different example, if we were trying to guess a number between 1 and 1,000,000, then asking if the number is over 500,000 would eliminate 500,000 options in one question, the second question eliminates 250,000, the third question 125,000, and so on.
So in 3 questions you have eliminated 875,000 numbers.
With just 20 questions you can find the one number between 1 and 1,000,000.
It's the same searching for objects that are sorted in descending order - each value that is checked halves the number of possible locations.
Dividing problems in half makes them very small very quickly.

This general process is called "divide and conquer" - you break the problem into (two) parts, and deal with each part separately, in turn break them into two parts.
Very soon you end up with very easy tasks, such as dealing with just one item.
It's a great strategy for reducing any big task or challenge to achievable goals!

## Divide and conquer programming challenges

## Lesson reflection

What is the algorithm for a binary search? Here is a possible answer:

-   Ask to see the middle card
-   Repeat until the correct number is found:     
-   Is the number greater than the number I want to find?
    *   If yes, then keep the cards above that number,
    *   Else, keep the cards below that number
