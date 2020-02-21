# roboadvisor
 
 Hi, welcome to the roboadvisor project. 

 The roboadvisor is a tool you can use to check the performance of your favorite stocks, and let you know whether our team thinks it's a good idea to purchase said stock for investment purposes. 

 Our methodology is as follows:
 
 Buy if the stock is trading below 95 percent of its most recent high. In other words, Buy if Last Closing Price < (0.95 * Recent High Price)
 
 Do not buy if the stock is trading above 95 percent of its most recent high. This might indicate that the stock is overvalued or priced correctly, leaving no room for additional upside. In other words, Do Not Buy if Last Closing Price > (0.95 * Recent High Price)

To use our app:

Step One: Recreate the necessary environment with the provided .yml file on the GitHub repository. We call it stocks-env. 

```sh
conda env create -n stocks-env -f /path/to/environment.yml
```


