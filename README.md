# Software Engineer Assignment

## Approach : 

* I wasn't familer with  *Scarpy* so I learned it from YouTube and documentations. 
* Here I have made 3 spiders. 
    * spider1.py for clothes 
    * spider2.py for shoes
    * spider_all.py for both
* I have also stored the scraped data into three seperate json files for later use.

* Here I have used mongodb compass.

* I couldn't find any product on discounted price. If you could show me how to see sale price then it can also be added properly changing just a few lines of code. 


## Document Structure 

```
cliff.ai
│
|---- cliff
│   |
|   |---- __pycache__ 
|   |       |---
|   |
|   |---- spiders
|   |   |---- __pycache__
|   |   |   |---
|   |   |
|   |   |---- __init__.py
|   |   |---- spider_all.py
|   |   |---- spider1.py
|   |   |---- spider2.py
|   |
|   |---- __init__.py
|   |---- items.py
|   |---- middlewares.py
|   |---- pipelines.py
|   |---- settings.py
│
|---- data
|   |---- clothes_and_shoes.json
|   |---- clothes.json
|   |---- shoes.json
|
|---- query
|   |---- query.js
|
|---- results
│    │---- part2-question answers.pdf
│    │---- Screenshot1.jpg
│    │---- Screenshot2.jpg
│    │---- Screenshot3.jpg
│      
│   
|---- commands.txt
|---- README.md
|---- scrapy.cfg

```