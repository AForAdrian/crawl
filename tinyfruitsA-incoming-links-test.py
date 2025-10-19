
import testingtools
import crawler
import searchdata
import search
output = open('tinyfruitsA-incoming-links-failed.txt', 'w')
success_output = open('tinyfruitsA-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html')
#Test #0 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
