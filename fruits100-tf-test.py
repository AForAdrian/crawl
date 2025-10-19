
import testingtools
import crawler
import searchdata
import search
output = open('fruits100-tf-failed.txt', 'w')
success_output = open('fruits100-tf-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits100/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits100/N-0.html')
#Test #0 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word apricot
expected = 0.05555555555555555
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word coconut
expected = 0.2222222222222222
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word banana
expected = 0.027777777777777776
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word apple
expected = 0.027777777777777776
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word papaya
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word kiwi
expected = 0.1111111111111111
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word fig
expected = 0.16666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word cherry
expected = 0.027777777777777776
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word strawberry
expected = 0.05555555555555555
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word lime
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-15.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word apricot
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word coconut
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word banana
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word apple
expected = 0.05714285714285714
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word papaya
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word kiwi
expected = 0.05714285714285714
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word fig
expected = 0.08571428571428572
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word cherry
expected = 0.04285714285714286
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word strawberry
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word lime
expected = 0.08571428571428572
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-98.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word apricot
expected = 0.08771929824561403
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word coconut
expected = 0.07017543859649122
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word banana
expected = 0.14035087719298245
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word apple
expected = 0.03508771929824561
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word papaya
expected = 0.08771929824561403
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word kiwi
expected = 0.07017543859649122
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word fig
expected = 0.07017543859649122
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word cherry
expected = 0.12280701754385964
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word strawberry
expected = 0.017543859649122806
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word lime
expected = 0.08771929824561403
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-60.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word apricot
expected = 0.038461538461538464
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word coconut
expected = 0.057692307692307696
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word banana
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word apple
expected = 0.17307692307692307
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word papaya
expected = 0.11538461538461539
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word kiwi
expected = 0.019230769230769232
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word fig
expected = 0.057692307692307696
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word cherry
expected = 0.057692307692307696
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word strawberry
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word lime
expected = 0.057692307692307696
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-9.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word apricot
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word coconut
expected = 0.17391304347826086
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word banana
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word apple
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word papaya
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word kiwi
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word fig
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word cherry
expected = 0.13043478260869565
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word strawberry
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word lime
expected = 0.13043478260869565
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-16.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word apricot
expected = 0.047619047619047616
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word coconut
expected = 0.047619047619047616
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word banana
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word apple
expected = 0.09523809523809523
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word papaya
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word kiwi
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word fig
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word cherry
expected = 0.11904761904761904
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word strawberry
expected = 0.09523809523809523
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word lime
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word apricot
expected = 0.08163265306122448
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word coconut
expected = 0.16326530612244897
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word banana
expected = 0.061224489795918366
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word apple
expected = 0.04081632653061224
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word papaya
expected = 0.061224489795918366
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word kiwi
expected = 0.1836734693877551
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word fig
expected = 0.02040816326530612
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word cherry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word strawberry
expected = 0.10204081632653061
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word lime
expected = 0.08163265306122448
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word apricot
expected = 0.13333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word coconut
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word banana
expected = 0.12
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word apple
expected = 0.10666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word papaya
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word kiwi
expected = 0.08
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word fig
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word cherry
expected = 0.05333333333333334
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word strawberry
expected = 0.13333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word lime
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word apricot
expected = 0.0196078431372549
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word coconut
expected = 0.09803921568627451
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word banana
expected = 0.0392156862745098
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word apple
expected = 0.058823529411764705
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word papaya
expected = 0.11764705882352941
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word kiwi
expected = 0.09803921568627451
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word fig
expected = 0.0392156862745098
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word cherry
expected = 0.0392156862745098
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word strawberry
expected = 0.0196078431372549
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word lime
expected = 0.11764705882352941
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word apricot
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word coconut
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word banana
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word apple
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word kiwi
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word fig
expected = 0.2
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word cherry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word strawberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word lime
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
