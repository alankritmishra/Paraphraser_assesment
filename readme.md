# Paraphraser Assessment Tool for practicing paraphrasing

This is an AI-assisted writing aid application that will examine the content, format, structure, and similarity of a user's input paragraph. It will then provide an analytical review of how effectively the text has been paraphrased. When a user submits their own rewritten paragraph, our analysis tool compares it to the supplied English paragraph and generates an analytical report. The tool will also produce a system-generated paraphrase of the provided text for the user's reference.
 
The following metrics are included in the analysis report: similarity index, word count, word frequency, and direct phrase detection.
### Similarity Index:
It compares the similarity of the user's provided paragraph to the original one. It is divided into two sections: If the user has made a better paraphrase, the lexical similarity bar should fall in percentage (made structural changes and substituted synonyms). If the user retains the semantic meaning of the paragraph after paraphrasing, the contextual similarity bar should increase in percentage.
### Word Count: 
This measure will monitor how many words the user has used and if it is the same length as the original paragraph.
### Word frequency: 
This metric measures how frequently a specific word appears in the user input paragraph.
### Direct Phrase: 
This measure recognizes directly copied or quoted phrases from the provided paragraph in the user's input text.
 
<!--Link to the paraphraser: https://wat-frontend.vercel.app/.-->

## Structure of the project
It is a backend project which utilizes open-source pre-trained hugging face NLP-based models and wraps it in REST API developed on flask and WSGI. There are three components of the project,

- first is the API to serve paragraphs for practicing paraphrasing.
- Second is the API which would generate paraphrases using per-trained models. (needs improvement)
- third is the API that would provide analysis for the user's generated paragraph.

## How to install this project using a Dockerised container

The easiest way to see how this works it works on any machine is, to run it on docker.

1. clone this project
2. Build the docker image - `docker build -t writing-assist-proj .`
3. Run the docker image - `docker run 8000:8000 getting-started`
4. Voila! You can checkout the APIs from the 8000 port.

## Find a bug?

If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. (or you also use this feedback form: https://forms.gle/8WTMca13RckCgWdk7). If you would like to submit a PR with a fix, reference the issue you created!

## Call for collaboration

This project is still under ongoing development. The optimization for time on paraphrase generation is not completed yet. We are open for opensource contributions and collaborations.
