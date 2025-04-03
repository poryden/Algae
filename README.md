# Algae
 
### Work in progress. Check back later for a release.

Algae is a tool used to compare a list of words to controlled vocabulary databases. It was created to speed up the process of verifying the quality of metadata.

This tool takes input in the form of a list of words in a .txt file and compares each of them to select databases, also stored in .txt files. It creates an output file sorting every term by whether it was found in any databases or not, and if so, which ones it was found in. Two databases are included, both from the Library of Congress -- the [Name Authority File](https://id.loc.gov/authorities/names.html) and the [Subject Headings](https://id.loc.gov/authorities/subjects.html)). There is functionality to support NASA's thesaurus and a Master spreadsheet of terms by an organization, but the user must add these manually.

As the project progresses, this page will go further in depth on the specifics of Algae and how to use it.

Made by Lily "Bingo" Marvin ([lmm0060@uah.edu](mailto:lmm0060@uah.edu) or [poryden.art@gmail.com](mailto:poryden.art@gmail.com)) for use in the UAH Salmon Library Archives, but use is not restricted. Project begun 3/30/25. Made in Python.
