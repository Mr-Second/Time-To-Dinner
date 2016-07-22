install:
	pip install -r Crawler/requirements.txt

num = `ls *.jpg | wc -l`
test:
	cd Crawler;python3 Crawler_of_restaurant.py test.json;python3 Crawler/test.py
	@echo "last time : num of picture is $(num)"
	@echo $(num) > record# this will output how many jpg file are there.
	@echo "this time is : $(num)"

clean:
	rm -f Crawler/gomaji.json Crawler/venv
	rm -f Crawler/*.jpg