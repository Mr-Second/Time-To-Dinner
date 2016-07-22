install:
	pip install -r Crawler/requirements.txt

num = `ls *.jpg | wc -l`
test:
	cd Crawler;python3 Crawler_of_restaurant.py test.json;python3 test.py

clean:
	rm -f Crawler/gomaji.json Crawler/venv
	rm -f Crawler/*.jpg