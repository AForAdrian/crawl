
import testingtools
import crawler
import searchdata
import search
output = open('fruits50-tfidf-failed.txt', 'w')
success_output = open('fruits50-tfidf-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html')
#Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word apple
expected = 0.0083116286818328
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word coconut
expected = 0.0013787887146004864
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word cherry
expected = 0.010634565686534009
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word banana
expected = 0.008724336160347927
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word blueberry
expected = 0.004222855235043958
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word kiwi
expected = 0.0040077252326171445
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word apricot
expected = 0.004222855235043958
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word lime
expected = 0.048390686107874004
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word papaya
expected = 0.011200524453185806
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word pear
expected = 0.005483556310194886
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apple
expected = 0.0029607176565235346
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word coconut
expected = 0.0028358578623939247
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word cherry
expected = 0.0057301911223788075
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word banana
expected = 0.0179439946327521
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word blueberry
expected = 0.016821991509375966
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word kiwi
expected = 0.0028358578623939247
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apricot
expected = 0.011455150550718891
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word lime
expected = 0.021171037671366244
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word papaya
expected = 0.003989782481904419
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word pear
expected = 0.007557479465357401
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word apple
expected = 0.012274573544126323
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word coconut
expected = 0.003365738894720593
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word cherry
expected = 0.006800879335501042
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word banana
expected = 0.017171661973760285
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word blueberry
expected = 0.012274573544126323
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word kiwi
expected = 0.002713798884545823
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word apricot
expected = 0.0062834679313081634
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word lime
expected = 0.015316114869686972
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word papaya
expected = 0.01389124338138478
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word pear
expected = 0.00414548718952568
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word apple
expected = 0.020649815734778323
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word coconut
expected = 0.001789601498463702
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word cherry
expected = 0.007084571195508225
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word banana
expected = 0.022185212463694468
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word blueberry
expected = 0.005481063179879387
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word kiwi
expected = 0.001789601498463702
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word lime
expected = 0.013360232627711856
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word papaya
expected = 0.021277374851608032
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word pear
expected = 0.01041698392067085
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apple
expected = 0.0095440356557343
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word coconut
expected = 0.00507232104076176
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word cherry
expected = 0.002151143585032254
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word banana
expected = 0.025978512761594803
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word blueberry
expected = 0.0095440356557343
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word kiwi
expected = 0.0021029025948996398
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apricot
expected = 0.0095440356557343
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word lime
expected = 0.05857270573666875
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word papaya
expected = 0.004393852267309213
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word pear
expected = 0.004249167047585765
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word apple
expected = 0.006839777850279317
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word coconut
expected = 0.0036587664801601577
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word cherry
expected = 0.012876533046261858
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word banana
expected = 0.004794155185316261
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word blueberry
expected = 0.004599972769482762
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word kiwi
expected = 0.0015019199543946375
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word apricot
expected = 0.009041293783778537
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word lime
expected = 0.016672134621081573
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word papaya
expected = 0.02079124597791728
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word pear
expected = 0.005964949287103142
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apple
expected = 0.01333454286915998
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word coconut
expected = 0.0036587664801601577
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word cherry
expected = 0.008797399341668202
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word banana
expected = 0.014130846999617188
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word blueberry
expected = 0.009041293783778537
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word kiwi
expected = 0.0036587664801601577
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apricot
expected = 0.01333454286915998
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word lime
expected = 0.02203838639375518
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word papaya
expected = 0.015100641268186226
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word pear
expected = 0.003034809502733903
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apple
expected = 0.0095440356557343
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word coconut
expected = 0.004300752818056708
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word cherry
expected = 0.007501837267470175
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word banana
expected = 0.019717790630373322
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word blueberry
expected = 0.007690974246916072
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word kiwi
expected = 0.004300752818056708
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apricot
expected = 0.011370811617785921
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word lime
expected = 0.03643715364243369
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word papaya
expected = 0.0026496376415987956
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word pear
expected = 0.002574913207315954
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apple
expected = 0.007968657650939693
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word coconut
expected = 0.0017523072269786204
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word cherry
expected = 0.005257282852529639
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word banana
expected = 0.016463090545135076
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word blueberry
expected = 0.0027113747984100554
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word kiwi
expected = 0.00425101976868384
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apricot
expected = 0.017880127353309024
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word lime
expected = 0.025640211026962248
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word papaya
expected = 0.014175050303884235
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word pear
expected = 0.003540747034210253
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word apple
expected = 0.007968657650939693
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word coconut
expected = 0.0008852808739632389
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word cherry
expected = 0.006939825618530336
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word banana
expected = 0.021731944186784428
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word blueberry
expected = 0.007968657650939693
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word kiwi
expected = 0.0026018166922826334
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word apricot
expected = 0.010518949819235976
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word lime
expected = 0.025640211026962248
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word papaya
expected = 0.014175050303884235
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word pear
expected = 0.001788816242191212
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
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


#Test #113 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
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


#Test #116 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
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
