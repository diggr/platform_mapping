# DIGGR PLATFORM MAPPING

The diggr platform mapping provides a mapping, reference and grouping for platform strings of various video game databases. It is meant to ease mapping and matching of releases, local releases or games in general which are to be found in these databases.

This is meant as a first step towards unification of platform identification.

The list is not exhaustive.

Everything is provided as is and comes without any warranty.

## Access

The data can be accessed in two forms: Either by cloning this repository and using the provided platform mapping files.
Or by using the github pages, which are served from the _dist_ subdirectory as a static REST API.<https://diggr.github.io/platform_mapping>

Using the static REST API version is preferable, as it always serves to up-to-date version,
while using a cloned git repository can result in usage of an out-of-date version, e.g. if you 
forget to pull the latest updates before using it. 

## Data

The vocabulary of platform names from each source were retrieved at different time.
Last Updates:

- [ESRB](http://esrb.org/) 2017-08
- [GameFAQs](http://gamefaqs.com/) 2017-11
- [MediaArt](http://mediaarts-db.bunka.go.jp/gm) 2017-10
- [Mobygames](http://mobygames.com/) 2017-10
- [OGDB](http://ogdb.eu/) 2017-09
- [PEGI](http://pegi.info/) 2017-09
- [USK](http://usk.de/) 2017-08

In some data sources there are platform groups (like "Game Archives") which includes individual platforms.
A mapping is located at _platform_groups.tsv_ in the tabular_data folder.

The file _diggr_vocab.tsv_ contains the whole standarized vocabulary we used for internal mappings. It also contains links to the [GAMECIP](https://gamemetadata.soe.ucsc.edu/platform) Platform Vocabulary.

## Metadata

JSON-exports contain information about the author, license and copyright information, a version and a date element.

### version

The version number describes the general structure of the JSON-export. Major changes to the overall structure of the file result in a increase of the minor or major version number. Please refer to CHANGELOG to learn more about the changes, which were made. If you use the data in your application an fetch updates from this repository on a regular basis, please check for changes in the version number.

### date

The date section in the JSON-exports indicates the time the data was exported. Updates to the data result in new _date_.

## Contribution

Feel free to inform us about mistakes or ideas to provide better access to those mappings: <team@diggr.link>

## License

* __Software:__ GPLv3
* __Data:__ Creative Commons CC0 1.0 Universal

## Copyright

2018, Universitätsbibliothek Leipzig

## Authors

* Tracy Hoffmann, <hoffmannt@ub.uni-leipzig.de>
* Peter Mühleder, <muehleder@ub.uni-leipzig.de>
* Florian Rämisch, <raemisch@ub.uni-leipzig.de>

## Links

* Universitätsbibliothek Leipzig: <http://ub.uni-leipzig.de>
* diggr: <http://diggr.link>
