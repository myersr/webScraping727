#from multiprocessing import Pool
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
     time.sleep(5)
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
     cnn_paper = Source('http://cnn.com', fetch_images=False)#, memoize_articles=False) 
#memorize turns off caching which we will need, testing not so much. 
     #pool takes in an array, we build first
     cnn_paper.build()
     sourceArray = [cnn_paper]
     news_pool.set(sourceArray, threads_per_source=3)
     news_pool.join()
     print cnn_paper.size()

     print cnn_paper[3]


#for category in cnn_paper.category_urls():
#     print(category)
