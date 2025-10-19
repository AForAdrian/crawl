
import testingtools
import crawler
import searchdata
import search
output = open('tinyfruitsA-page-rank-failed.txt', 'w')
success_output = open('tinyfruitsA-page-rank-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html')
#Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html
expected = 0.04337549364213977
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html
expected = 0.11607762994927237
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html
expected = 0.1541643641256654
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html
expected = 0.06099693965376308
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html
expected = 0.05526151568869791
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html
expected = 0.2514639802597616
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html
expected = 0.05566093263355323
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html
expected = 0.0827021363071326
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html
expected = 0.12463607510646232
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html
expected = 0.05566093263355323
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
