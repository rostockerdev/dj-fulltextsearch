## Basic and Full-text Search with Django and Postgres

## Objectives
- [x] Set up basic search functionality in Django app with the Q object
- [x] Add full-text search to a Django app
- [x] Sort full-text search results by relevance using stemming, ranking and weighting

## Stemming -
- Semming is the process of reducing words to their word stem, base or root form. 
Example: the word 'drives', 'drove' and 'driven' will be recorded under the single concept
word 'drive'.

## Project Setup and Overview
Clone down from the [dj-fulltestsearch](https://github.com/rostockerdev/dj-fulltextsearch.git)

```
$ git clone https://github.com/rostockerdev/dj-fulltextsearch.git --branch main --single-branch
$ cd dj-fulltextsearch
```