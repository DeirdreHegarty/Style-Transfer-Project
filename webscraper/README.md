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

#### CREATING PROJECT

---

`scrapy startproject webscraper`

