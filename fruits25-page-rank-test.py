
import testingtools
import crawler
import searchdata
import search
output = open('fruits25-page-rank-failed.txt', 'w')
success_output = open('fruits25-page-rank-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html')
#Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html
expected = 0.03159579999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html
expected = 0.03892039999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html
expected = 0.0414408
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html
expected = 0.05466807999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html
expected = 0.04810359999999998
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html
expected = 0.03692783999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html
expected = 0.04550911999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html
expected = 0.021270039999999987
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html
expected = 0.01904219999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html
expected = 0.03686656
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html
expected = 0.048347039999999994
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html
expected = 0.05083659999999998
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html
expected = 0.03690907999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html
expected = 0.04654291999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html
expected = 0.04630903999999998
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html
expected = 0.033533439999999984
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html
expected = 0.028174759999999986
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html
expected = 0.028309039999999987
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html
expected = 0.03434247999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html
expected = 0.051393999999999995
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html
expected = 0.04014835999999998
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html
expected = 0.05204075999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html
expected = 0.051696559999999975
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html
expected = 0.033838480000000004
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html
expected = 0.043232999999999994
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
