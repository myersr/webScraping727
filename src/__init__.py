from multiprocessing import Pool
import newspaper
import time
from newspaper import Article, news_pool, Source

#nltk.download('punkt')
#print newspaper.popular_urls()

#print "Size of new cnn articles"
#cnn_paper = Source('http://cnn.com', fetch_images=False, memoize_articles=False, number_threads=20)
#cnn_paper.build()
#print cnn_paper.size()
#sina_paper = newspaper.build('http://www.lemonde.fr/', language='fr')
#paperPool = [cnn_paper]
#news_pool.set(paperPool, threads_per_source=6) # (3*2) = 6 threads total this comment is for entering an array of three builds with source =2
#news_pool.join()


def loopI(x,y):
  for i in range(x,y):
     #print cnn_paper.articles[i].url
     print i
     first_article = Article(url=cnn_paper.articles[i].url, language='en')
     first_article.download()
     #time.sleep(1)
     first_article.parse()
     #print first_article.text[0:30]
     first_article.nlp()
     if "russia" in first_article.keywords:
         print "Article Title" + first_article.title
         print "Article URL" + first_article.url
         print "Keywords"
         print first_article.keywords
  return "Done"

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:
         cnn_paper = Source('http://cnn.com', fetch_images=False, memoize_articles=False)
         cnn_paper.build()
         print cnn_paper.size()
         pool.map(loopI, range(10), range(11,20))


#for category in cnn_paper.category_urls():
#     print(category)
