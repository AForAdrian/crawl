
import testingtools
import crawler
import searchdata
import search
output = open('fruits100-tfidf-failed.txt', 'w')
success_output = open('fruits100-tfidf-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits100/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits100/N-0.html')
#Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word blueberry
expected = 0.016408749406293496
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word pear
expected = 0.019108291712746816
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word apple
expected = 0.0034441784212371866
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word banana
expected = 0.011899567121688234
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word papaya
expected = 0.013672255472918936
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word kiwi
expected = 0.03338004736718889
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word fig
expected = 0.01391574809872745
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word apricot
expected = 0.012467384480233495
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word coconut
expected = 0.006332656363867811
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word strawberry
expected = 0.00415473275475362
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-83.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word blueberry
expected = 0.0129812936829857
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word pear
expected = 0.012130021028700788
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word apple
expected = 0.009175237170851593
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word banana
expected = 0.014747938254775389
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word papaya
expected = 0.01491512773429266
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word kiwi
expected = 0.006140831045233077
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word fig
expected = 0.03496471553112925
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word apricot
expected = 0.007408249865065477
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word coconut
expected = 0.014547048318117687
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word strawberry
expected = 0.0095440356557343
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-30.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word blueberry
expected = 0.027539012789949368
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word apple
expected = 0.01946469897141909
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word apricot
expected = 0.012668609841606046
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word coconut
expected = 0.012668609841606046
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word strawberry
expected = 0.016119203702658718
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word blueberry
expected = 0.0064284760750430185
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word pear
expected = 0.038891088994260165
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word apple
expected = 0.004543676006111188
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word banana
expected = 0.012594490938962961
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word papaya
expected = 0.027827129308207264
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word fig
expected = 0.012336148836996486
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word apricot
expected = 0.024066262394699924
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word coconut
expected = 0.024066262394699924
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-90.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word blueberry
expected = 0.009748310569005204
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word pear
expected = 0.015653809937296027
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word apple
expected = 0.01946469897141909
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word papaya
expected = 0.011200524453185806
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word coconut
expected = 0.04640201150327193
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word strawberry
expected = 0.0083116286818328
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word blueberry
expected = 0.007951645846267752
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word pear
expected = 0.006468379873395911
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word apple
expected = 0.008323195362853909
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word banana
expected = 0.007951645846267752
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word papaya
expected = 0.017815412291833893
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word kiwi
expected = 0.030743609774909714
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word fig
expected = 0.02259760085390477
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word apricot
expected = 0.01033371865944495
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word coconut
expected = 0.029499693563023788
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word strawberry
expected = 0.006779751959662912
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-88.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word blueberry
expected = 0.017210868921581416
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word pear
expected = 0.016175984241006944
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word apple
expected = 0.005384011643935776
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word banana
expected = 0.017210868921581416
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word papaya
expected = 0.008752168461359549
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word kiwi
expected = 0.016175984241006944
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word fig
expected = 0.014617672758881251
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word apricot
expected = 0.019323325872188088
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word coconut
expected = 0.016231997057100822
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word strawberry
expected = 0.01064949777363427
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-76.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word blueberry
expected = 0.01395265644540866
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word pear
expected = 0.025946073733079663
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word apple
expected = 0.00338949966364151
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word banana
expected = 0.01171489123488961
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word papaya
expected = 0.0027768255508694192
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word kiwi
expected = 0.01516430448276819
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word fig
expected = 0.018121884786702167
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word apricot
expected = 0.01813245069590456
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word coconut
expected = 0.009275520286339597
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word strawberry
expected = 0.011896348467614769
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word blueberry
expected = 0.020169434673609647
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word pear
expected = 0.03238802197452078
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word apple
expected = 0.009712171773907811
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word banana
expected = 0.003554196665101593
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word kiwi
expected = 0.027281520302248508
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word fig
expected = 0.01999798031485275
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word apricot
expected = 0.00913166148706163
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word coconut
expected = 0.02207890206789756
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word strawberry
expected = 0.008885284623590783
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word blueberry
expected = 0.014869017530995532
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word pear
expected = 0.03134028872377518
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word apple
expected = 0.003619338873772866
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word papaya
expected = 0.01157414762102591
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word kiwi
expected = 0.04561204437821727
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word apricot
expected = 0.006654716030582054
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word coconut
expected = 0.019323325872188088
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word strawberry
expected = 0.016640603386452426
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-69.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
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


#Test #112 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
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


#Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
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


#Test #116 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
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
