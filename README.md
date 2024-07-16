### Description
In this portfolio I created, described and automated tests for https://accounts.ukr.net/login using [_qase.io_](https://qase.io/) as test management system and _python+pytest+selenium+allure+docker_ as test automation framework.

### Test and defects repository
To view test repository and detected bugs send your email to [my telegram](https://t.me/ivaniuk_qa) to get invite to **qase.io**.

### Launching tests in system
**To launch tests and view test results in your system environment perform the following steps:**
1. Make sure that **python 3**, **git**, **pip** and **allure** installed in your system
2. Open terminal in any desired directory and clone repo using ```git clone git@github.com:ivaniukihornik/portfolio.git``` command
3. Move to root repo directory
4. Create and activate virtual environment. Install required packages from _requirements.txt_ using ```pip install -r requirements.txt```
5. Launch tests using ```pytest``` command. After all tests are finished you`ll see message like this:

```===================================== 105 passed, 4 skipped in 1627.68s (0:27:07) =====================================```

6. To serve allure report use command ```allure serve allure-results```. Report must be opened in a new tab of browser after generating. If not - open generated link manually.

### Launching tests in Docker
**To launch tests in docker container perform the following steps:**
1. Make sure that **docker** installed and launched with appropriate permissions
2. Open terminal in any desired directory and clone repo using ```git clone git@github.com:ivaniukihornik/portfolio.git``` command
3. Move to root repo directory
4. Make sure that ```--headless``` mode is set to webdriver in ```/UkrNet/tests/conftest.py``` file. To do it add argument ```is_headless=True``` when initializing ```driver``` object in ```create_driver``` fixture:

```driver = DriverFactory.create_driver(driver_id=conf.browser_id, is_headless=True)```

5. Build docker image using ```docker build -t <image_name>:<tag> .``` command. After successfully building you'll see messages:

```Successfully built <build hash>```

```Successfully tagged <image_name>:<tag>```

6. Run docker container using ```docker run --privileged -it <image_name>:<tag>``` command. After successfully starting your user'll be **tester**. E.g.: ```tester@9e02e5a09033:/project$```
7. Launch tests in container using ```pytest``` command. After all tests are finished you`ll see message like this:

```===================================== 105 passed, 4 skipped in 1627.68s (0:27:07) =====================================```
