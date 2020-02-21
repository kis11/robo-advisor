# roboadvisor
 
 Hi, welcome to the roboadvisor project. 

 The roboadvisor is a tool you can use to check the performance of your favorite stocks, and let you know whether our team thinks it's a good idea to purchase said stock for investment purposes. 

 Our methodology is as follows:
 
 Buy if the stock is trading below 95 percent of its most recent high. In other words, Buy if Last Closing Price < (0.95 * Recent High Price)
 
 Do not buy if the stock is trading above 95 percent of its most recent high. This might indicate that the stock is overvalued or priced correctly, leaving no room for additional upside. In other words, Do Not Buy if Last Closing Price > (0.95 * Recent High Price)

To use our app:

Step One: Navigate to the robo-advisor folder. If you have a Mac and put it on your Desktop, you can navigate by doing this:

```sh
cd ~/Desktop/robo-advisor
```

Once you are navigated to the folder, we need to create an environment. We will call it stocks-env. To create it, install the necessary packages from the requirements.txt file by doing the following:

``sh
pip install -r requirements.txt
```

Then, to access the application, type:

```sh
python roboadvisor.py
```




