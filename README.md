# sbt_dep_search
A maven search tool for sbt dependency

# Usage

```
sbt_dep_search
masakiR-2:sbt_dep_search masakir$ sbt_dep_serach.py 
usage: sbt_dep_search.py [query]
masakiR-2:sbt_dep_search masakir$ 
```

```
sbt_dep_search junit | less

#0      libraryDependencies += "com.fitbur.testify.junit" % "junit" % "0.1.3"
{
  "a": "junit",
  "ec": [
    ".pom"
  ],
  "g": "com.fitbur.testify.junit",
  "id": "com.fitbur.testify.junit:junit",
  "latestVersion": "0.1.3",
  "p": "pom",
  "repositoryId": "central",
  "text": [
    "com.fitbur.testify.junit",
    "junit",
    ".pom"
  ],
  "timestamp": 1455810137000,
  "versionCount": 13
}
#1      libraryDependencies += "org.typelevel" % "junit" % "2.11.7"
{
  "a": "junit",
  "ec": [
    "-javadoc.jar",
    "-sources.jar",
    ".jar",
    ".pom"
  ],
  "g": "org.typelevel",
  "id": "org.typelevel:junit",
  "latestVersion": "2.11.7",
  "p": "jar",
  "repositoryId": "central",
  "text": [
    "org.typelevel",
    "junit",
    "-javadoc.jar",
    "-sources.jar",
    ".jar",
:
```

```
sbt_dep_search.py junit | grep ^#3

masakiR-2:sbt_dep_search masakir$ sbt_dep_serach.py junit | grep ^#3
#3	libraryDependencies += "junit" % "junit" % "4.12"
```

```
sbt_dep_serach.py junit | grep ^#3 | cut -f2 >>./build.sbt
```
