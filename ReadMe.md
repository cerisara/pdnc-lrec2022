# The Project Dialogism Novel Corpus

This repository contains data associated with the LREC 2022 paper [The Project Dialogism Novel Corpus:
A Dataset for Quotation Attribution in Literary Texts]().

## Data Description
The PDN Corpus contains annotations for speaker, addressees, referring expression, and pronominal mentions for all quotations in 22 novels. The list of novels can be found in the file `ListOfNovels.txt`.

In the `data` folder, for each novel, there are three files:
- `text.txt`: The text of the novel
- `quotations.csv`: This is a CSV file where each row contains, for a quotation:
    - The text of the quotation
    - The corresponding character-byte spans from the novel text
    - The name of the speaker
    - The names of the addressees
    - Texts of the mentions annotated within the quotation
    - Character-byte spans of the mentions from the novel text
    - The entities referred to by the above mentions
    - The type of the quotation (implicit, anaphoric, or explict)
    - The referring expression associated with the quotation, if any

- `charDict.pkl`: Each character-entity in a novel is assigned a unique ID. This pickle file is a dictionary with the following key-value pairs:
    - id2names: The list of names (aliases) associated with each ID
    - name2id: A reverse-mapping of each character alias to the corresponding ID
    - id2parent: The *main* character name associated with each ID

## Helper File
The IPython notebook `load_data.ipynb` shows how to load and read the data files for a novel. 

## Authors
Please contact the authors of the paper with any queries:
- [Krishnapriya Vishnubhotla](https://priya22.github.io/) (University of Toronto)
- [Adam Hammond](https://www.adamhammond.com/) (University of Toronto)
- [Graeme Hirst](https://www.cs.toronto.edu/~gh/) (University of Toronto)

Contact: vkpriya@cs.toronto.edu, adam.hammond@utoronto.ca, gh@cs.toronto.edu
