# sbt_dep_search
A maven search tool for sbt dependency

# Usage

```
sbt_dep_search

sbt_dep_search junit | less

sbt_dep_search.py junit | grep ^#3

sbt_dep_search.py junit | grep ^#3 | cut >> ./build.sbt
```
