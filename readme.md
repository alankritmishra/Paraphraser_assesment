# Writing Assistant Tool (WAT) for practicing paraphrasing

It is a backend project which utilizes open-source pre-trained hugging face NLP-based models and wraps it in REST API developed on flask and WSGI. There are three components of the project,

- first is the API to serve paragraphs for practicing paraphrasing.
- Second is the API which would generate paraphrases using per-trained models.
- third is the API that would provide analysis for the user's generated paragraph.

## How to install this project using a Dockerised container

The easiest way to see how this works it works on any machine is, to run it on docker.

1. clone this project
2. Build the docker image - `docker build -t writing-assist-proj .`
3. Run the docker image - `docker run 8000:8000 getting-started`
4. Voila! You can checkout the APIs from the 8000 port.

## Find a bug?

If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to submit a PR with a fix, reference the issue you created!

## Known issues (Work in progress)

This project is still under ongoing development. The optimization for time on paraphrase generation is not completed yet. This is coming soon
