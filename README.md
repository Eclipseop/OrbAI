# OrbAI

This is a small AI project to detect what orb in on the board in the mobile game Puzzle & Dragons

![](https://i.imgur.com/OHwyfBX.jpg)

In reality, there are probably 100x easier ways of acomplishing this, but hey, AI is cool. The most simple was of doing this was by color, but it seems that the colors shift a bit, and some orbs, such as jammers/darks/posions/mortal-posions, have a pretty similar colorset. 

This project uses the basic 'feed image data and you're all set' method. The only slight difference is changing the classifier to [K-Nearest Neighbor](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761?gi=31d1469aee71), which improved the overal accuracy from 90%ish (except one training session, where it was 60%) to a constant 100%.
