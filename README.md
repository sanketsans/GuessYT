# GuessYT
Code for the project guessYT. 
Do you know about 'Charades' or the board game 'Dixit'? The project is simple game where based on given hints, one has to identify the target video. 

The videos are sampled from an open source library [scrapetube](https://scrapetube.readthedocs.io/en/latest/) . The clips are searched based on the keywords provided by the user. They are sampled in 4 main categories : 
## Categories : By default, selection is set to "Search" :
- Channel : Youtube channel for the keyword - it has to be same as the official channel name (eg. youtube.com/@Mrwhosetheboss, mr whose the boss wont work for this category).
- Shorts : Same conditions as channels.
- Streams : Same conditions as channels.
- Search : Search the keyword on the youtube Do not require to be exact channel name.

From the keyword, a collection of videos are extracted and randomly a target video is sampled along with 3 other videos for building the option(s) set. The correct option is compared using the videoId comparison. 

## Hints : By default the selection is to "text" :
The title of the video is essentially used to curate the hints. 
1. Text :
   - I use an open source tools [spacy](https://spacy.io/), for the NLP and tokenization of each word.
   - Specifically, from the title text, I extract important words using NLP techniques such as Lemmatization or Stemming. You can also explore other methods such as similar words text retrival using a LLM model.
   - Those "tokenized" words are then presented as individual hints.
2. Images:
   - I create set of natural language prompts for our generative AI models.
   - The prompts are created using the noun chunks from the models and also extracting the entity based information for the text. Refer to the spacy docs to know about entity based features.
   - For the generative AI model, I used [huggingface](https://huggingface.co/) repository to use a diffusion based model, specifically I tried 3 different models.
   - Stabillity AI, RunwayML and CompVis.
   - You can alter the runtime inference steps to speed up the hint generation process.
  

For the backend, I mostly used python as my main language. For the front-end, I used HTML, CSS and JS for the interactions. I also used Flask to connect and exchange the information from backend to front-end. 

To run the project : 

`conda env create -f env.yml`

`conda activate guessyt`

`python app.py`

# PS: You will need a powerful GPU to generate the diffusion model based images faster. Otherwise, it may take a while.  
## Sample Results 

![](https://github.com/sanketsans/GuessYT/blob/main/media/media.gif), ![](https://github.com/sanketsans/GuessYT/blob/main/media/media2.gif), ![](https://github.com/sanketsans/GuessYT/blob/main/media/media3.gif)


## If you liked the project, consider hitting a 🌟


