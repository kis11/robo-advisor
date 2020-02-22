# roboadvisor
 
 Hi, welcome to the roboadvisor project. 

 The roboadvisor is a tool you can use to check the performance of your favorite stocks, and let you know whether our team thinks it's a good idea to purchase said stock for investment purposes. 

 ### Our methodology
 
 Buy if the stock is trading below 95 percent of its most recent high. In other words, Buy if Last Closing Price < (0.95 * Recent High Price)
 
 Do not buy if the stock is trading above 95 percent of its most recent high. This might indicate that the stock is overvalued or priced correctly, leaving no room for additional upside. In other words, Do Not Buy if Last Closing Price > (0.95 * Recent High Price)

#### To use our app...

Access the Github Repository: https://github.com/kis11/robo-advisor

Fork, then clone the repository, which contains the data files you'll need to perform the exercise.

Step One: Navigate to the robo-advisor folder on your terminal. If you have a Mac and put it on your Desktop, you can navigate by doing this:

```sh
cd ~/Desktop/robo-advisor
```

Step 2: Once you are navigated to the folder, we need to create an environment. We will call it stock-env. To create stock-env, do the following: 

```sh
conda create -n stock-env python=3.7 #first time only
conda activate stock-env
```


Step 3: Now we need to install the necessary packages from the requirements.txt file by doing the following:

```sh
pip install -r requirements.txt
```

Step 4: Get an API Key from AlphaVantage. You can do so here: https://www.alphavantage.co/. Sign up and put your API key on your clipboard. Then create a .env file in your roboadvisor folder on your Desktop. In your text editor, navigate to your .env file, and within the file, set the following variable:

```sh
ALPHAVANTAGE_API_KEY="abc123"
```

Where abc123 is your provided AlphaVantage key. 

Step 4: Then, to access the application, type:

```sh
~/desktop/robo-advisor/app
python roboadvisor.py
```

You should then get a prompt to enter a ticker. If your ticker is valid, the process will go through and you will be able to get a recommendation. In the event that you type an invalid response (i.e. a ticker that is not on an exchange), the system will prompt you to try again. 


