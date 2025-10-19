
import testingtools
import crawler
import searchdata
import search
output = open('tinyfruits-tfidf-failed.txt', 'w')
success_output = open('tinyfruits-tfidf-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html')
#Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word kiwi
expected = 0.10363769827780657
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word blueberry
expected = 0.10363769827780657
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word kiwi
expected = 0.03872609348667805
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word pear
expected = 0.04525008888053903
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word cherry
expected = 0.031595073081303486
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word lime
expected = 0.03872609348667805
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word blueberry
expected = 0.019766560368774045
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word fig
expected = 0.04525008888053903
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apple
expected = 0.07447019235682993
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word coconut
expected = 0.05694192097566775
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word kiwi
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word pear
expected = 0.06445710476952095
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word lime
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word blueberry
expected = 0.054703631988055924
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word fig
expected = 0.06445710476952095
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word coconut
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word cherry
expected = 0.06459482428200948
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apple
expected = 0.07758727832568058
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word coconut
expected = 0.0404119177187868
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word kiwi
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word pear
expected = 0.18271404725510207
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word lime
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word blueberry
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word fig
expected = 0.18271404725510207
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apple
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word pear
expected = 0.06445710476952095
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word cherry
expected = 0.1656555612092295
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word lime
expected = 0.014291714269269087
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word blueberry
expected = 0.054703631988055924
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word fig
expected = 0.06445710476952095
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apple
expected = 0.054703631988055924
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word coconut
expected = 0.014291714269269087
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word cherry
expected = 0.0991299889868547
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apple
expected = 0.06201786293142292
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word coconut
expected = 0.11672149491947882
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word kiwi
expected = 0.02997453317184664
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word lime
expected = 0.10978936524490102
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word blueberry
expected = 0.02997453317184664
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apple
expected = 0.02997453317184664
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word kiwi
expected = 0.02266030222847964
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word cherry
expected = 0.10375537569198201
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word lime
expected = 0.044266247441115764
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word blueberry
expected = 0.08467816515990254
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word fig
expected = 0.14859721830091777
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word coconut
expected = 0.02266030222847964
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word kiwi
expected = 0.012385909108380427
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word pear
expected = 0.13476451852905313
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word cherry
expected = 0.05787647829766945
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word lime
expected = 0.02445006963027565
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apple
expected = 0.06979767743420133
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word coconut
expected = 0.02445006963027565
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
