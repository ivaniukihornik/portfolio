In this portfolio I created, described and automated tests for https://accounts.ukr.net/login - using _python+pytest+selenium+allure+docker_.

To view test repository send me your email to https://t.me/igor_telgram in order I'll give you invite link.

**To launch tests and view test results perform the following steps:**
1. Make sure that **python 3**, **git**, **pip** and **allure** installed in your system
2. Open terminal in any desired directory and clone repo using ```git clone git@github.com:ivaniukihornik/portfolio.git``` command
3. Move to repo directory
4. Install required packages from _requirements.txt_ using ```pip install -r requirements.txt```
5. Launch tests using ```pytest``` command. After all tests are finished you`ll see message like this:

```===================================== 105 passed, 4 skipped in 1627.68s (0:27:07) =====================================```

6. To serve allure report use command ```allure serve allure-results```. Report must be opened in a new tab of browser after generating. If not - open generated link manually.


Install docker
