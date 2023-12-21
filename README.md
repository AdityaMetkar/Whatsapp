# WhatsApp Clone - Chatbot Powered with AI 🤖

This Project was created with Frontend Languages and REST API in combination with Python Backend Framework (Flask) and Natural Language Processing Library (ChatterBot).
> Originally This was created for my College Competition but it can be tailored to fit the required use cases.
<br>


https://github.com/AdityaMetkar/WhatsappClone/assets/133694021/c9a4202a-b1b6-491f-be76-ba6d1fcb1da6

## Files
> bot.py- The Flask app with the nlp logic written <br>
> frontend.html - The frontend for offline chatting<br>
> Sample Training - Demo file of how to train the chatbot<br>

## Usage
The first step is common
1) `pip install` the `requirements.txt` file to install the prerequisite modules

Then there are two ways to implement this Module -

#### CASE-1) Directly running the modules without explicit training

2) Run the Flask backend server by running the `bot.py` file.<br>
   > Optional: You check out the code to change the hyperparameters like Confidence, Adapters, Preprocessors, etc in the constructor of `Compile Class` 
3) Now open your frontend.html file locally or by using a live server extension.

We are set! 👍

#### CASE-2) Training the Chatbot on your data before usage

The difference in this method is that we will be providing the chatbot with our dataset.<br>
This will create a new db.sqlite file which will be used to predict responses.

2) Delete the current `db.sqlite` file. Normally the Chatbot will use the original trained file in CASE-1 but we don't want this.
3) Now comes the training phase. I have provided the `Sample Training` file to guide you. It only requires the input database, the rest will be handled automatically.
    >Note- Create your database in the specified format for better results.
4) Once the database is ready run the `Sample Training` file, this will create a new `db.sqlite` based on your input data. 
5) Great! you have created your dataset and this will be used for predicting responses.
<br> Now just follow the steps mentioned in CASE-1.

We are set! 👍

## Learn More
You can learn more in the [Chatterbot Modules](https://chatterbot.readthedocs.io/en/stable/).
