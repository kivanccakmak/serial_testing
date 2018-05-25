# serial\_testing

## installation
- chmod 777 install.sh
- sudo ./install.sh

## add new test
- cd src
- cp -r template newtest
- edit config.ini (suite=['template.test', 'newtest.test'])
- edit CONFIG\_PATH in newtest/test.py (CONFIG\_PATH=os.path.abspath('newtest/config.ini')

## run all tests
- close all minicom connections
- cd src
- sudo python main.py
