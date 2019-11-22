# OrbAI

This is a small AI project to detect what orb in on the board in the mobile game Puzzle & Dragons

![](https://i.imgur.com/OHwyfBX.jpg)

In reality, there are probably 100x easier ways of accomplishing this, but hey, AI is cool. The most simple way of doing this was by color, but it seems that the colors shift a bit, and some orbs, such as jammers/darks/poisons/mortal-poisons, have a pretty similar colorset.

This project uses the basic 'feed image data and you're all set' method. The only slight difference is changing the classifier to [K-Nearest Neighbor](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761?gi=31d1469aee71) rather than just using the generic decision tree classifier, which improved the overall accuracy from 90%ish (except one training session, where it was 60%) to a constant 100%.
