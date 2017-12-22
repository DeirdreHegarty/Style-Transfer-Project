#### GETTING STARTED

---

```bash

 sudo easy_install pip
 pip install scrapy --user
 pip install pillow --user
 pip install -U Twisted[tls] --user

```

**Next - getting `scrapy` command to work:**

```bash

 vim ~/.bash_profile 
 
 # then change the path variable to start looking here
 # Note: this is mac specific

 export PATH=/$HOME/Library/Python/2.7/bin:$PATH

```

Then run `source ~/.bash_profile` 

---

#### USING SCRAPY SHELL

---

scrapy shell
fetch("https://www.reddit.com/r/gameofthrones/")
print response.text

# extract first element with class = "score unvoted"
response.css(".score.unvoted").extract_first()

# extract image urls
response.css("img::attr(data-img)").extract()

# extract the title in the img tag
response.css("img::attr(title)").extract()

---

#### CREATING PROJECT

---

`scrapy startproject webscraper`

* edit settings.py
