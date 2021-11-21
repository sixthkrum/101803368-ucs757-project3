# Algo trading using multiple platforms and complex indicators

## This project has multiple parts that work in tandem, this includes a Linode server that parses the raw indicators from [TradingView](https://www.tradingview.com/) (a charting service) and passes them on to [TradeTron](https://tradetron.tech/) (a basic algo trading platform) please read on for the step by step explanation

### TradingView

This is a charting service that allows users to make complex indicators using [**pinescript**](https://www.tradingview.com/pine-script-docs/en/v4/index.html) which is an in house scripting language developed by tradingview.

I have been helping develop and debug trading view scripts for a while now with user [sharaau7](https://www.tradingview.com/u/sharaaU7/) (hover over the encircled i in the profile pic to see attribution) and we have developed both [public scripts](https://www.tradingview.com/u/sharaaU7/#published-scripts) and private scripts to monitor and send alerts for various tickers.

**How this works with this project:** We have made a private script that sends alerts to a linode server that tracks the current position we are in and accordingly sends alerts down to tradetron that actually executes orders. 

In the code uploaded in this project, we are using another user's private script to get our alerts so it has some string parsing code but the main purpose of the linode server is to track our current positions and appropriately send alerts over to tradetron. Using this kind of a system also allows easy extensibility down the line. For example, it makes it feasible to use machine learning to make even better decisions with our indicators.

### Linode server

This linode server is setup at webhook-forwarder.valagh.com
I have setup a firewall to only allow incoming requests from tradingview's IP addresses as this is a live project currently being tested using paper trading.

This is a debian server and it uses nginx, uwsgi and flask in the backend. I have uploaded all the server side code barring some configuration files in this repository with the api keys etc. redacted.

TradingView sends over webhook requests to this server that contain an API key that corresponds to the strategy and the ticker that is being tested. The API key is sent over as a url parameter over https as tradingview does not offer editing the http headers of requests. This key is verified by my server and the other arguments are parsed according to the strategy they are for.

Currently we are using a basic strategy that only takes into account a single ticker, previously we have used strategies that use 2 indicators and the signal sent over to tradetron is a function of the current signal received and their history.

After we have parsed the input, we send it over to TradeTron which again involves sending an API key over https along with the parameters that we want the tradetron side of things to take into account.

### TradeTron

This is an algo trading platform that allows for creating basic strategies using an interface similar to the scratch programming language. It allows for making "if then else" sort of command blocks that are chained together using "or" and "and" logical operators that then do some action like take a position.

**Here is the strategy we use on the tradetron side:** nfott is the name of the parameter that we pass onto tradetron from the linode server that makes decisions on what positions to take. These screenshots do not completely show the customizability that tradetron has but it allows for a lot of control when it comes to taking positions and making some basic strategies.

Every strategy can have multiple sets that each necessarily have an entry and exit block along with optional repair blocks. Entry blocks define the conditions for entering a position along with information about how to enter said position. Exit blocks define how to exit the position. All these sets can work independently of each other.

![strategy name](https://github.com/sixthkrum/101803368-ucs757-project3/blob/main/images/1.png)
![strategy name](https://github.com/sixthkrum/101803368-ucs757-project3/blob/main/images/2.png)
![strategy name](https://github.com/sixthkrum/101803368-ucs757-project3/blob/main/images/3.png)
![strategy name](https://github.com/sixthkrum/101803368-ucs757-project3/blob/main/images/4.png)
![strategy name](https://github.com/sixthkrum/101803368-ucs757-project3/blob/main/images/5.png)
![strategy name](https://github.com/sixthkrum/101803368-ucs757-project3/blob/main/images/6.png)
![strategy name](https://github.com/sixthkrum/101803368-ucs757-project3/blob/main/images/7.png)
![strategy name](https://github.com/sixthkrum/101803368-ucs757-project3/blob/main/images/8.png)
![strategy name](https://github.com/sixthkrum/101803368-ucs757-project3/blob/main/images/9.png)

While currently the strategy is being tested using paper trading we plan on getting it live soon after we have some more testing data.



