## Web scraping project for csce 727 at the University of South Carolina



### Requirements and Installation
Most packages will be installed via `requirements.txt`. Newspaper requires some additional system packages and installation is covered [here](http://newspaper.readthedocs.io/en/latest/user_guide/install.html)  
It is a good idea to install everythin within a virtual evironment. [virtualenv](https://virtualenv.pypa.io/en/stable/) is easy to use.  
After installing the needed packages with apt and activating your virtual environment run `pip install -r requirements.txt` 


*Note for newspaper*  
You must install nltk package punkt to use nlp. Below I create a shared directory but you can use the default which in inside home. I hate the clutter. If you use share you must either run python as sudo or chown the directory to yourself. 
[nltk Documentation](https://media.readthedocs.org/pdf/nltk/latest/nltk.pdf)
```
(env)~$ mkdir /usr/share/nltk_data
(env)~$ python
>>>> import nltk
>>>> nltk.download()
---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> c
Local Machine:
  - Data directory: /home/roy/nltk_data

---------------------------------------------------------------------------
    s) Show Config   u) Set Server URL   d) Set Data Dir   m) Main Menu
---------------------------------------------------------------------------
Config> d
  New Directory> /usr/share/nltk_data

---------------------------------------------------------------------------
    s) Show Config   u) Set Server URL   d) Set Data Dir   m) Main Menu
---------------------------------------------------------------------------
Config> s

Data Server:
  - URL: <http://nltk.github.com/nltk_data/>
  - 3 Package Collections Available
  - 107 Individual Packages Available

Local Machine:
  - Data directory: /usr/share/nltk_data

---------------------------------------------------------------------------
    s) Show Config   u) Set Server URL   d) Set Data Dir   m) Main Menu
---------------------------------------------------------------------------
Config> m

---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> d

Download which package (l=list; x=cancel)?
  Identifier> punkt
```

