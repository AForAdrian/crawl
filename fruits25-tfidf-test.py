
import testingtools
import crawler
import searchdata
import search
output = open('fruits25-tfidf-failed.txt', 'w')
success_output = open('fruits25-tfidf-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html')
#Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word pear
expected = 0.01041698392067085
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apple
expected = 0.00738613147022325
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word kiwi
expected = 0.00738613147022325
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word blueberry
expected = 0.003616104585169806
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word fig
expected = 0.021277374851608032
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apricot
expected = 0.007084571195508225
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word banana
expected = 0.020743103707281035
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word coconut
expected = 0.017815412291833893
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word pear
expected = 0.008722075193882767
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word apple
expected = 0.021997491629348293
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word kiwi
expected = 0.013530061368747843
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word blueberry
expected = 0.0044729081462969965
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word apricot
expected = 0.0044729081462969965
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word banana
expected = 0.023150979092818654
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word coconut
expected = 0.015100641268186226
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word pear
expected = 0.007392976736066969
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apple
expected = 0.012183801272907425
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word kiwi
expected = 0.009217098356891351
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word blueberry
expected = 0.007392976736066969
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word fig
expected = 0.01796926681825092
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apricot
expected = 0.005964949287103142
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word banana
expected = 0.034862481993596706
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word coconut
expected = 0.013356426642475827
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word pear
expected = 0.003332412725162628
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word apple
expected = 0.013356426642475827
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word kiwi
expected = 0.013356426642475827
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word blueberry
expected = 0.0016825427660007034
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word fig
expected = 0.0068066721858765855
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word apricot
expected = 0.008098089771498661
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word coconut
expected = 0.015552001456108683
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word pear
expected = 0.005151009376339124
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word apple
expected = 0.02044099783798403
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word kiwi
expected = 0.005340356569797789
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word blueberry
expected = 0.005151009376339124
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word fig
expected = 0.015552001456108683
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word apricot
expected = 0.01680838953287179
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word banana
expected = 0.025768679616493564
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word coconut
expected = 0.008607444705009883
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word pear
expected = 0.0042140355055771865
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word apple
expected = 0.011384270255879295
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word kiwi
expected = 0.014117364448464627
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word blueberry
expected = 0.006911583759158722
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word fig
expected = 0.014117364448464627
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word apricot
expected = 0.009526117220462484
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word banana
expected = 0.015503515981597573
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word coconut
expected = 0.010112446315772362
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word pear
expected = 0.011132899274232564
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apple
expected = 0.01654088102298361
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word kiwi
expected = 0.013356426642475827
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word blueberry
expected = 0.008098089771498661
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word fig
expected = 0.01654088102298361
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apricot
expected = 0.004950854670969278
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word banana
expected = 0.018878015874743782
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word coconut
expected = 0.021571607012108827
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word pear
expected = 0.00832496743137005
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apple
expected = 0.017004293566508805
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word kiwi
expected = 0.005030725989125216
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word blueberry
expected = 0.00832496743137005
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word fig
expected = 0.009919722371000582
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apricot
expected = 0.003668150916437207
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word banana
expected = 0.020090174755817453
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word coconut
expected = 0.006675742044297133
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word pear
expected = 0.007946500733719867
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word apple
expected = 0.016231250442311055
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word kiwi
expected = 0.009919722371000582
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word blueberry
expected = 0.01380852374156493
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word fig
expected = 0.013104176751508352
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word apricot
expected = 0.004856500821031621
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word apple
expected = 0.02172179992016925
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word blueberry
expected = 0.010634565686534009
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word fig
expected = 0.011200524453185806
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word apricot
expected = 0.005483556310194886
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
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


#Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
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
