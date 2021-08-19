# lol-champion-classification

This program is for Classifying Lol-Champions into similar group.\
The basic approach is Louvian method.


### Slides
[ppt link](https://docs.google.com/presentation/d/1jS67YccVQp_itos1OTokRept5MZ2m9oB/edit?usp=sharing&ouid=116551932655872811856&rtpof=true&sd=true, "Google Slides")


### How to Run
    $ python data/dataCrawl.py
    $ python data/dataRemoveDup.py
    $ python classifier/model2.py

### Files
- ```python classifier/model2.py``` : Implements on Model-2
- ```data/dataCrawl.py``` : Web scraping on [fow](https://fow.kr, "link")
- ```data/dataRemoveDup.py``` : Remove the duplicated games
