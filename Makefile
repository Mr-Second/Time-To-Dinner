install:
	pip install -r Crawler/requirements.txt

test:
	python3 Crawler/Crawler_of_restaurant.py gomaji.json
	python3 Crawler/test.py

clean:
	rm -rf Crawler/*.json Crawler/venv
	rm *.json