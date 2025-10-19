
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html')


output = open('tinyfruitsA-all-outgoing-failed.txt', 'w')
success_output = open('tinyfruitsA-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = None
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruitsA-all-incoming-failed.txt', 'w')
success_output = open('tinyfruitsA-all-incoming-passed.txt', 'w')

#Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruitsA-all-pagerank-failed.txt', 'w')
success_output = open('tinyfruitsA-all-pagerank-passed.txt', 'w')

#Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html
expected = 0.11607762994927237
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html
expected = 0.0827021363071326
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html
expected = 0.05526151568869791
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html
expected = 0.06099693965376308
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html
expected = 0.1541643641256654
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html
expected = 0.2514639802597616
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html
expected = 0.04337549364213977
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html
expected = 0.12463607510646232
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html
expected = 0.05566093263355323
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html
expected = 0.05566093263355323
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruitsA-all-idf-failed.txt', 'w')
success_output = open('tinyfruitsA-all-idf-passed.txt', 'w')

#Test #33 checking IDF for word banana
expected = 0.15200309344505006
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking IDF for word pear
expected = 0.15200309344505006
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking IDF for word kiwi
expected = 0.0
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking IDF for word peach
expected = 0.32192809488736235
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking IDF for word apple
expected = 0.0
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking IDF for word papaya
expected = 0.15200309344505006
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking IDF for word apricot
expected = 0.15200309344505006
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking IDF for word fig
expected = 0.0
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking IDF for word coconut
expected = 0.32192809488736235
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking IDF for word cherry
expected = 0.0
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking IDF for word blueberry
expected = 0.0
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking IDF for word strawberry
expected = 0.0
result = searchdata.get_idf('strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking IDF for word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking IDF for word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking IDF for word lime
expected = 0.0
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking IDF for word tomato
expected = 0
result = searchdata.get_idf('tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking IDF for word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking IDF for word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruitsA-all-tf-failed.txt', 'w')
success_output = open('tinyfruitsA-all-tf-passed.txt', 'w')

#Test #47 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word pear
expected = 0.13333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word banana
expected = 0.03333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word lime
expected = 0.03333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word fig
expected = 0.03333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word papaya
expected = 0.03333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word blueberry
expected = 0.03333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word peach
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word kiwi
expected = 0.13333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word apricot
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word cherry
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word pear
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word banana
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word lime
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word papaya
expected = 0.045454545454545456
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word blueberry
expected = 0.045454545454545456
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word kiwi
expected = 0.22727272727272727
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word apricot
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word cherry
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word pear
expected = 0.05
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word banana
expected = 0.2
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word lime
expected = 0.05
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word fig
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word papaya
expected = 0.15
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word blueberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word kiwi
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word apricot
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word cherry
expected = 0.05
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word pear
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word banana
expected = 0.047619047619047616
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word lime
expected = 0.09523809523809523
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word fig
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word blueberry
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word peach
expected = 0.14285714285714285
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word kiwi
expected = 0.07142857142857142
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word apricot
expected = 0.11904761904761904
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word cherry
expected = 0.16666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word lime
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word fig
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word papaya
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word blueberry
expected = 0.13333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word peach
expected = 0.26666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word kiwi
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word apricot
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word cherry
expected = 0.13333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word lime
expected = 0.13333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word fig
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word papaya
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word blueberry
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word peach
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word kiwi
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word apricot
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word cherry
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word pear
expected = 0.13793103448275862
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word banana
expected = 0.10344827586206896
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word lime
expected = 0.10344827586206896
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word fig
expected = 0.034482758620689655
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word papaya
expected = 0.06896551724137931
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word blueberry
expected = 0.10344827586206896
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word peach
expected = 0.1724137931034483
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word kiwi
expected = 0.10344827586206896
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word apricot
expected = 0.06896551724137931
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word cherry
expected = 0.034482758620689655
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word pear
expected = 0.19148936170212766
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word banana
expected = 0.0425531914893617
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word lime
expected = 0.0425531914893617
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word fig
expected = 0.0425531914893617
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word papaya
expected = 0.06382978723404255
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word blueberry
expected = 0.02127659574468085
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word peach
expected = 0.0851063829787234
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word kiwi
expected = 0.0851063829787234
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word apricot
expected = 0.0851063829787234
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word cherry
expected = 0.1276595744680851
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word pear
expected = 0.034482758620689655
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word banana
expected = 0.10344827586206896
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word lime
expected = 0.10344827586206896
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word fig
expected = 0.10344827586206896
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word papaya
expected = 0.20689655172413793
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word blueberry
expected = 0.10344827586206896
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word peach
expected = 0.06896551724137931
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word kiwi
expected = 0.06896551724137931
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word apricot
expected = 0.06896551724137931
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word cherry
expected = 0.06896551724137931
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word pear
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word banana
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word lime
expected = 0.027777777777777776
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word fig
expected = 0.027777777777777776
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word blueberry
expected = 0.05555555555555555
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #152 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #152 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word kiwi
expected = 0.1111111111111111
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word apricot
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word cherry
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruitsA-all-tfidf-failed.txt', 'w')
success_output = open('tinyfruitsA-all-tfidf-passed.txt', 'w')

#Test #168 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word apricot
expected = 0.014152917496331312
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word coconut
expected = 0.02997453317184664
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word peach
expected = 0.02997453317184664
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word papaya
expected = 0.014152917496331312
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word pear
expected = 0.015129730287875636
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word apricot
expected = 0.024665759170377815
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word coconut
expected = 0.032043329759576286
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word banana
expected = 0.010201565384574599
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word peach
expected = 0.06201786293142292
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word peach
expected = 0.10978936524490102
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word papaya
expected = 0.014152917496331312
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word pear
expected = 0.01908108239963235
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word apricot
expected = 0.01908108239963235
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word coconut
expected = 0.0404119177187868
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word banana
expected = 0.01908108239963235
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word papaya
expected = 0.009748009671471615
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word pear
expected = 0.017552894270256875
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word apricot
expected = 0.017552894270256875
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word coconut
expected = 0.04893406628975068
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word banana
expected = 0.017552894270256875
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word pear
expected = 0.027447539927876227
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word apricot
expected = 0.014152917496331312
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word coconut
expected = 0.02997453317184664
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word banana
expected = 0.007190614983939457
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word peach
expected = 0.02997453317184664
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word papaya
expected = 0.007190614983939457
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word pear
expected = 0.007434410572265377
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word apricot
expected = 0.014625025556204782
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word banana
expected = 0.021587328068596676
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word peach
expected = 0.03097441314041437
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word papaya
expected = 0.0412387465741404
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word pear
expected = 0.02833537154185039
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word apricot
expected = 0.014625025556204782
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word banana
expected = 0.021587328068596676
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word peach
expected = 0.07387665353353737
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word papaya
expected = 0.014625025556204782
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word pear
expected = 0.01069939558501044
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word coconut
expected = 0.02266030222847964
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word banana
expected = 0.039982043369217374
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word papaya
expected = 0.030648970641056626
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word pear
expected = 0.03842122461570417
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word apricot
expected = 0.017911511045374046
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word coconut
expected = 0.019354636558164728
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word banana
expected = 0.009138576831497242
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word peach
expected = 0.0379348768285149
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word papaya
expected = 0.013568911534362437
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruitsA-all-search-failed.txt', 'w')
success_output = open('tinyfruitsA-all-search-passed.txt', 'w')

#Test #289 checking search results for 'peach blueberry lime apricot lime coconut lime coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1275480331385189}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.12296028392177383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10024874837946977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0732403660680402}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.06283116128679567}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05814004132687371}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053053955525906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.04823545717329352}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.045616854566753316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.019773031583789864}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1275480331385189}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.12296028392177383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10024874837946977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0732403660680402}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.06283116128679567}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05814004132687371}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053053955525906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.04823545717329352}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.045616854566753316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.019773031583789864}]
result = search.search('peach blueberry lime apricot lime coconut lime coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #289 checking search results for 'peach blueberry lime apricot lime coconut lime coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #289 checking search results for 'peach blueberry lime apricot lime coconut lime coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking search results for 'peach blueberry lime apricot lime coconut lime coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9531632514171042}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9531632514171042}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.8855921907028612}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.8728580201277151}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8636353828319888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.8273509501492154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8195488722237976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.5041169760290205}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.4889777207644459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.4558572116071584}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9531632514171042}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9531632514171042}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.8855921907028612}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.8728580201277151}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8636353828319888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.8273509501492154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8195488722237976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.5041169760290205}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.4889777207644459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.4558572116071584}]
result = search.search('peach blueberry lime apricot lime coconut lime coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #290 checking search results for 'peach blueberry lime apricot lime coconut lime coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #290 checking search results for 'peach blueberry lime apricot lime coconut lime coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking search results for 'apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #291 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #291 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking search results for 'apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #292 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #292 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking search results for 'coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.0}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #293 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #293 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking search results for 'coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #294 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #294 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking search results for 'apple banana lime kiwi fig peach fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.24837746839559066}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14824124454494375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12289097366813805}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.055157624419166246}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.054498447511870725}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.049560945874682176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.039223102025930566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0353108183121039}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.023594666682954832}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.24837746839559066}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14824124454494375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12289097366813805}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.055157624419166246}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.054498447511870725}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.049560945874682176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.039223102025930566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0353108183121039}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.023594666682954832}]
result = search.search('apple banana lime kiwi fig peach fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #295 checking search results for 'apple banana lime kiwi fig peach fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #295 checking search results for 'apple banana lime kiwi fig peach fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking search results for 'apple banana lime kiwi fig peach fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9877258291188163}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.98599842431789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9791148824376374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9615791910516138}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.42696379910876053}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9877258291188163}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.98599842431789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9791148824376374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9615791910516138}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.42696379910876053}]
result = search.search('apple banana lime kiwi fig peach fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #296 checking search results for 'apple banana lime kiwi fig peach fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #296 checking search results for 'apple banana lime kiwi fig peach fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking search results for 'apricot kiwi pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.23956015389944949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14992018898789114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11849947733196663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08270213630713262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053019295461351104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.0523022950817831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.23956015389944949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14992018898789114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11849947733196663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08270213630713262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053019295461351104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.0523022950817831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('apricot kiwi pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #297 checking search results for 'apricot kiwi pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #297 checking search results for 'apricot kiwi pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking search results for 'apricot kiwi pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9724698041480282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9526619027185704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9525405513846941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9507638717822757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.939658978158309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9724698041480282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9526619027185704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9525405513846941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9507638717822757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.939658978158309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('apricot kiwi pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #298 checking search results for 'apricot kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #298 checking search results for 'apricot kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking search results for 'tomato apple apricot strawberry apricot apple coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.16703781183979632}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.15378167042702043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08676807203954558}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.08279093188844809}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07673806582903037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05853002647482448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.0556495912429938}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05340982480674843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05302656157273087}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.16703781183979632}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.15378167042702043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08676807203954558}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.08279093188844809}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07673806582903037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05853002647482448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.0556495912429938}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05340982480674843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05302656157273087}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('tomato apple apricot strawberry apricot apple coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #299 checking search results for 'tomato apple apricot strawberry apricot apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #299 checking search results for 'tomato apple apricot strawberry apricot apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking search results for 'tomato apple apricot strawberry apricot apple coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9997962414565689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9975176254200159}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.9278849284382045}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7475003760626789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.6642613851385265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.6642613851385265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9997962414565689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9975176254200159}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.9278849284382045}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7475003760626789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.6642613851385265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.6642613851385265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('tomato apple apricot strawberry apricot apple coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #300 checking search results for 'tomato apple apricot strawberry apricot apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #300 checking search results for 'tomato apple apricot strawberry apricot apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking search results for 'strawberry peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0}]
result = search.search('strawberry peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #301 checking search results for 'strawberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #301 checking search results for 'strawberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking search results for 'strawberry peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0}]
result = search.search('strawberry peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #302 checking search results for 'strawberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #302 checking search results for 'strawberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking search results for 'papaya coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.139406011900442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.10736601635071817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10225399211004464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07478495476961346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05485564788015886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05411070940723738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.05321509213345997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.018519765553665885}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.139406011900442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.10736601635071817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10225399211004464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07478495476961346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05485564788015886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05411070940723738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.05321509213345997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.018519765553665885}]
result = search.search('papaya coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #303 checking search results for 'papaya coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #303 checking search results for 'papaya coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking search results for 'papaya coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9855323165586175}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9791752675054497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8809104058614148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9855323165586175}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9791752675054497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8809104058614148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}]
result = search.search('papaya coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #304 checking search results for 'papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #304 checking search results for 'papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking search results for 'lime apricot peach kiwi apricot tomato fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.21682916598857185}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14492503304341087}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11959538981968262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05853002647482448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05493583561729113}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05340982480674843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05340982480674843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.036708090956228887}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.03242319780940382}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.21682916598857185}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14492503304341087}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11959538981968262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05853002647482448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05493583561729113}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05340982480674843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05340982480674843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.036708090956228887}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.03242319780940382}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}]
result = search.search('lime apricot peach kiwi apricot tomato fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #305 checking search results for 'lime apricot peach kiwi apricot tomato fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #305 checking search results for 'lime apricot peach kiwi apricot tomato fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking search results for 'lime apricot peach kiwi apricot tomato fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9400683086869338}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.8622672947616113}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.7475003760626789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.6642613851385265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.6642613851385265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9595567713242412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9400683086869338}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.8622672947616113}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.7475003760626789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.6642613851385265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.6642613851385265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}]
result = search.search('lime apricot peach kiwi apricot tomato fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #306 checking search results for 'lime apricot peach kiwi apricot tomato fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #306 checking search results for 'lime apricot peach kiwi apricot tomato fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking search results for 'apple apricot lime peach coconut kiwi strawberry cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.1809140110762248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14763203239517608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.09244478823912784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.07785467697305681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.061054924862578755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.053126920804455226}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.040988446653596834}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.02909247068131442}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.1809140110762248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14763203239517608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.09244478823912784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.07785467697305681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.061054924862578755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.053126920804455226}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.040988446653596834}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.02909247068131442}]
result = search.search('apple apricot lime peach coconut kiwi strawberry cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #307 checking search results for 'apple apricot lime peach coconut kiwi strawberry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #307 checking search results for 'apple apricot lime peach coconut kiwi strawberry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking search results for 'apple apricot lime peach coconut kiwi strawberry cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9576274856544373}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9544741399541253}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.7417177423162824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.7417177423162824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.7382508794674643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.7194430426550201}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.6707121519200594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.6707121519200594}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9576274856544373}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9544741399541253}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.7417177423162824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.7417177423162824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.7382508794674643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.7194430426550201}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.6707121519200594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.6707121519200594}]
result = search.search('apple apricot lime peach coconut kiwi strawberry cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #308 checking search results for 'apple apricot lime peach coconut kiwi strawberry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #308 checking search results for 'apple apricot lime peach coconut kiwi strawberry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking search results for 'coconut kiwi papaya papaya tomato cherry peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.1736714847236279}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.12437094574472263}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.09783686936588243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0909764569707936}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05926626288826875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.051704716047249084}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.051417859947627924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.04951524831606912}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0390579926150745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.028707095421582753}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.1736714847236279}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.12437094574472263}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.09783686936588243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0909764569707936}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05926626288826875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.051704716047249084}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.051417859947627924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.04951524831606912}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0390579926150745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.028707095421582753}]
result = search.search('coconut kiwi papaya papaya tomato cherry peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #309 checking search results for 'coconut kiwi papaya papaya tomato cherry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #309 checking search results for 'coconut kiwi papaya papaya tomato cherry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking search results for 'coconut kiwi papaya papaya tomato cherry peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9716268262749218}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.928922919557419}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9237692851131367}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.8067425079076187}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.7849803460379476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7837552938542219}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.7067846787825736}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.6906415962406455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.6618275208214228}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.5987178871919745}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9716268262749218}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.928922919557419}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9237692851131367}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.8067425079076187}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.7849803460379476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7837552938542219}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.7067846787825736}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.6906415962406455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.6618275208214228}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.5987178871919745}]
result = search.search('coconut kiwi papaya papaya tomato cherry peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #310 checking search results for 'coconut kiwi papaya papaya tomato cherry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #310 checking search results for 'coconut kiwi papaya papaya tomato cherry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking search results for 'cherry apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('cherry apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #311 checking search results for 'cherry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #311 checking search results for 'cherry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking search results for 'cherry apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('cherry apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #312 checking search results for 'cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #312 checking search results for 'cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking search results for 'papaya kiwi apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.25146398025976163}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11251966642309864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.10901066729057013}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05847924140138765}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05513878397143248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.052916715274378516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05257505337519079}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.030671105691671013}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.25146398025976163}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11251966642309864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.10901066729057013}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05847924140138765}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05513878397143248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.052916715274378516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05257505337519079}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.030671105691671013}]
result = search.search('papaya kiwi apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #313 checking search results for 'papaya kiwi apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #313 checking search results for 'papaya kiwi apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking search results for 'papaya kiwi apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9906191176213603}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9513863801955661}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9506976036991436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9027857009055041}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9906191176213603}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9513863801955661}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9506976036991436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9027857009055041}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}]
result = search.search('papaya kiwi apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #314 checking search results for 'papaya kiwi apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #314 checking search results for 'papaya kiwi apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking search results for 'pear pear apricot peach peach apple apricot kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.24472392182849126}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1513858947899242}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12239769299409563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.056097635063359894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05336736400981566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05251204778083987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.04592607036503654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.04558018600366503}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.03607268292463982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.03068777145698505}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.24472392182849126}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1513858947899242}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12239769299409563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.056097635063359894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05336736400981566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05251204778083987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.04592607036503654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.04558018600366503}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.03607268292463982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.03068777145698505}]
result = search.search('pear pear apricot peach peach apple apricot kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #315 checking search results for 'pear pear apricot peach peach apple apricot kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #315 checking search results for 'pear pear apricot peach peach apple apricot kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking search results for 'pear pear apricot peach peach apple apricot kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9820406562830649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9819772270232545}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9731967241419314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9587939239387634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9434273788862969}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9196795016567535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.831637403881781}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.5553190330474652}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.5553190330474652}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.3926698539898191}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9820406562830649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9819772270232545}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9731967241419314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9587939239387634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9434273788862969}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9196795016567535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.831637403881781}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.5553190330474652}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.5553190330474652}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.3926698539898191}]
result = search.search('pear pear apricot peach peach apple apricot kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #316 checking search results for 'pear pear apricot peach peach apple apricot kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #316 checking search results for 'pear pear apricot peach peach apple apricot kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking search results for 'papaya banana strawberry tomato apricot cherry kiwi strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.24687620613865843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.11626746686908132}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11422814900782828}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.09396023811838272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.06752601153019253}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05381010698547991}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.053276719202232176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05261646412827748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.049803792674352386}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0250428529305223}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.24687620613865843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.11626746686908132}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11422814900782828}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.09396023811838272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.06752601153019253}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05381010698547991}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.053276719202232176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05261646412827748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.049803792674352386}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0250428529305223}]
result = search.search('papaya banana strawberry tomato apricot cherry kiwi strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #317 checking search results for 'papaya banana strawberry tomato apricot cherry kiwi strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #317 checking search results for 'papaya banana strawberry tomato apricot cherry kiwi strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking search results for 'papaya banana strawberry tomato apricot cherry kiwi strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9817557404588761}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9667482099112796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9640835677101839}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9453033148883945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9164934703716902}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.816496580927726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.816496580927726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8094603426986295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.7541786166244435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.5773502691896257}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9817557404588761}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9667482099112796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9640835677101839}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9453033148883945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9164934703716902}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.816496580927726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.816496580927726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8094603426986295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.7541786166244435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.5773502691896257}]
result = search.search('papaya banana strawberry tomato apricot cherry kiwi strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #318 checking search results for 'papaya banana strawberry tomato apricot cherry kiwi strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #318 checking search results for 'papaya banana strawberry tomato apricot cherry kiwi strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking search results for 'coconut strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.0}]
result = search.search('coconut strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #319 checking search results for 'coconut strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #319 checking search results for 'coconut strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking search results for 'coconut strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0}]
result = search.search('coconut strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #320 checking search results for 'coconut strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #320 checking search results for 'coconut strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking search results for 'pear papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.23956015389944949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.10901066729057013}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.1045454838859716}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.10236884790781851}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05847924140138765}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05257505337519079}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05021834376977115}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.04804771783025943}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.030671105691671013}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.23956015389944949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.10901066729057013}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.1045454838859716}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.10236884790781851}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05847924140138765}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05257505337519079}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05021834376977115}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.04804771783025943}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.030671105691671013}]
result = search.search('pear papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #321 checking search results for 'pear papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #321 checking search results for 'pear papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking search results for 'pear papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9526619027185704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9513863801955661}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.902218870466766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.9006514341450589}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.8632215731379168}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.821342037771781}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9526619027185704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9513863801955661}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.902218870466766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.9006514341450589}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.8632215731379168}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.821342037771781}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}]
result = search.search('pear papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #322 checking search results for 'pear papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #322 checking search results for 'pear papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking search results for 'peach pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2507591914323017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1510344583182311}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12201181985005512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.055157624419166246}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05317020160427275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05227422974905126}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.049560945874682176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.039223102025930566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0353108183121039}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.023594666682954832}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2507591914323017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1510344583182311}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12201181985005512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.055157624419166246}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05317020160427275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05227422974905126}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.049560945874682176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.039223102025930566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0353108183121039}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.023594666682954832}]
result = search.search('peach pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #323 checking search results for 'peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #323 checking search results for 'peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking search results for 'peach pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9971972573299291}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9796976050516901}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9789446574423528}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9552517194478515}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9391547585665064}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.42696379910876053}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9971972573299291}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9796976050516901}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9789446574423528}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9552517194478515}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9391547585665064}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.42696379910876053}]
result = search.search('peach pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #324 checking search results for 'peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #324 checking search results for 'peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking search results for 'banana pear tomato apricot banana fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.23216835153417303}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.12624873472563838}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12239335767506498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10218549355414595}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0788391041221757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.052680240001910975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.04124794101436677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.04022812105678436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.02604982939921962}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.23216835153417303}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.12624873472563838}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12239335767506498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10218549355414595}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0788391041221757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.052680240001910975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.04124794101436677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.04022812105678436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.02604982939921962}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('banana pear tomato apricot banana fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #325 checking search results for 'banana pear tomato apricot banana fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #325 checking search results for 'banana pear tomato apricot banana fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking search results for 'banana pear tomato apricot banana fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9820058724612305}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9532898138131441}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.9532898138131439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9232668284910777}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8803202959847002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.8189229426764808}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.7410573100872173}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.722735303801472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.4270678094193949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9820058724612305}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9532898138131441}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.9532898138131439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9232668284910777}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8803202959847002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.8189229426764808}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.7410573100872173}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.722735303801472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.4270678094193949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('banana pear tomato apricot banana fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #326 checking search results for 'banana pear tomato apricot banana fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #326 checking search results for 'banana pear tomato apricot banana fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking search results for 'cherry peach apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2439122064294367}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1538624641476771}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.039223102025930566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0353108183121039}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.023594666682954832}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2439122064294367}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1538624641476771}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.039223102025930566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0353108183121039}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.023594666682954832}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}]
result = search.search('cherry peach apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #327 checking search results for 'cherry peach apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #327 checking search results for 'cherry peach apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking search results for 'cherry peach apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9980417006245218}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9699687652182872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9980417006245218}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9699687652182872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}]
result = search.search('cherry peach apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #328 checking search results for 'cherry peach apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #328 checking search results for 'cherry peach apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking search results for 'banana kiwi apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.246941287701648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14239798375759882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12239443935101857}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08270213630713262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05294598787831017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.052916715274378516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.246941287701648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14239798375759882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12239443935101857}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08270213630713262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05294598787831017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.052916715274378516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('banana kiwi apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #329 checking search results for 'banana kiwi apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #329 checking search results for 'banana kiwi apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking search results for 'banana kiwi apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9820145511359454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9820145511359454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9512235130317157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9506976036991436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9236763928239906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9820145511359454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9820145511359454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9512235130317157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9506976036991436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9236763928239906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('banana kiwi apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #330 checking search results for 'banana kiwi apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #330 checking search results for 'banana kiwi apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking search results for 'lime strawberry lime fig peach papaya apple kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2439122064294367}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.139406011900442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11023571572707162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.055395908060030224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.049560945874682176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04126899457584179}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.023594666682954832}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2439122064294367}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.139406011900442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11023571572707162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.055395908060030224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.049560945874682176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04126899457584179}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.023594666682954832}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}]
result = search.search('lime strawberry lime fig peach papaya apple kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #331 checking search results for 'lime strawberry lime fig peach papaya apple kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #331 checking search results for 'lime strawberry lime fig peach papaya apple kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking search results for 'lime strawberry lime fig peach papaya apple kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9952385890608804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9699687652182872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9514357327278576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.8844607440735748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9952385890608804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9699687652182872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9514357327278576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.8844607440735748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}]
result = search.search('lime strawberry lime fig peach papaya apple kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #332 checking search results for 'lime strawberry lime fig peach papaya apple kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #332 checking search results for 'lime strawberry lime fig peach papaya apple kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking search results for 'kiwi apricot peach apricot lime banana cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.21961354100373248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1428463633973532}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11752714329425888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05609408113947876}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.055193212118491874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.0531538671424316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053147404501476134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.03863317877497701}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.03748202988881019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.030574741581980678}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.21961354100373248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1428463633973532}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11752714329425888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05609408113947876}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.055193212118491874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.0531538671424316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053147404501476134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.03863317877497701}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.03748202988881019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.030574741581980678}]
result = search.search('kiwi apricot peach apricot lime banana cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #333 checking search results for 'kiwi apricot peach apricot lime banana cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #333 checking search results for 'kiwi apricot peach apricot lime banana cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking search results for 'kiwi apricot peach apricot lime banana cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9549582557729129}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9548421484665907}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9429624865342471}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9265848447369689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9048521521208293}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.8733399542028736}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.7048851555265524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.6782664105696258}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.6782664105696258}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.33282191230007263}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9549582557729129}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9548421484665907}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9429624865342471}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9265848447369689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9048521521208293}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.8733399542028736}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.7048851555265524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.6782664105696258}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.6782664105696258}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.33282191230007263}]
result = search.search('kiwi apricot peach apricot lime banana cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #334 checking search results for 'kiwi apricot peach apricot lime banana cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #334 checking search results for 'kiwi apricot peach apricot lime banana cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking search results for 'coconut pear peach apple peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.22115958409736156}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541311989586916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.1103423748391648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.05966483496480847}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05704495189453723}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.0503340972644189}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.048490339259169186}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.04231086897544475}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.03720686372762269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.028404863322177114}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.22115958409736156}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541311989586916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.1103423748391648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.05966483496480847}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05704495189453723}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.0503340972644189}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.048490339259169186}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.04231086897544475}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.03720686372762269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.028404863322177114}]
result = search.search('coconut pear peach apple peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #335 checking search results for 'coconut pear peach apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #335 checking search results for 'coconut pear peach apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking search results for 'coconut pear peach apple peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9997848713795702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9352100649367244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9042984887766103}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.8853165084419735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.8794881233841297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8711736754108662}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.8577853668845813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.5140080391965521}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.5140080391965521}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.5116055142555691}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9997848713795702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9352100649367244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9042984887766103}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.8853165084419735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.8794881233841297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8711736754108662}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.8577853668845813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.5140080391965521}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.5140080391965521}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.5116055142555691}]
result = search.search('coconut pear peach apple peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #336 checking search results for 'coconut pear peach apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #336 checking search results for 'coconut pear peach apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking search results for 'strawberry peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0}]
result = search.search('strawberry peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #337 checking search results for 'strawberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #337 checking search results for 'strawberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking search results for 'strawberry peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0}]
result = search.search('strawberry peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #338 checking search results for 'strawberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #338 checking search results for 'strawberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking search results for 'banana tomato strawberry lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.0}]
result = search.search('banana tomato strawberry lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #339 checking search results for 'banana tomato strawberry lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #339 checking search results for 'banana tomato strawberry lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking search results for 'banana tomato strawberry lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0}]
result = search.search('banana tomato strawberry lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #340 checking search results for 'banana tomato strawberry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #340 checking search results for 'banana tomato strawberry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking search results for 'banana apple peach pear coconut kiwi blueberry strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.19104384065322086}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14484734857456402}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.09252978014058363}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.07328450660787199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.06313467755617809}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05515762441916625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05323840892639053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.048866155653835036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.042488489100531365}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.027734921421707318}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.19104384065322086}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14484734857456402}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.09252978014058363}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.07328450660787199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.06313467755617809}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05515762441916625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05323840892639053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.048866155653835036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.042488489100531365}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.027734921421707318}]
result = search.search('banana apple peach pear coconut kiwi blueberry strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #341 checking search results for 'banana apple peach pear coconut kiwi blueberry strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #341 checking search results for 'banana apple peach pear coconut kiwi blueberry strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking search results for 'banana apple peach pear coconut kiwi blueberry strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9564771269085354}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9395644019034989}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9042687179431865}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8779255636183466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.7688621741734296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.7633983881832695}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.7597264644259314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.7423996628708506}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.6394145424724926}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.6313404799865262}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9564771269085354}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9395644019034989}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9042687179431865}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8779255636183466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.7688621741734296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.7633983881832695}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.7597264644259314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.7423996628708506}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.6394145424724926}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.6313404799865262}]
result = search.search('banana apple peach pear coconut kiwi blueberry strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #342 checking search results for 'banana apple peach pear coconut kiwi blueberry strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #342 checking search results for 'banana apple peach pear coconut kiwi blueberry strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking search results for 'papaya banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.246941287701648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.1189527857578065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11507731975022176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.10901066729057013}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05847924140138765}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05463086022133569}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05257505337519079}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.030671105691671013}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.246941287701648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.1189527857578065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11507731975022176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.10901066729057013}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05847924140138765}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05463086022133569}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05257505337519079}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.030671105691671013}]
result = search.search('papaya banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #343 checking search results for 'papaya banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #343 checking search results for 'papaya banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking search results for 'papaya banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.9913824033150249}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9820145511359454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9814937989092084}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9544009281116945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9513863801955661}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.9913824033150249}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9820145511359454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9814937989092084}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9544009281116945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9513863801955661}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}]
result = search.search('papaya banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #344 checking search results for 'papaya banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #344 checking search results for 'papaya banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking search results for 'lime peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0}]
result = search.search('lime peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #345 checking search results for 'lime peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #345 checking search results for 'lime peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking search results for 'lime peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0}]
result = search.search('lime peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #346 checking search results for 'lime peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #346 checking search results for 'lime peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking search results for 'banana apple apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.246941287701648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14239798375759882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12239443935101857}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08270213630713262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05294598787831017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.052916715274378516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.246941287701648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14239798375759882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12239443935101857}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08270213630713262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05294598787831017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.052916715274378516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('banana apple apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #347 checking search results for 'banana apple apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #347 checking search results for 'banana apple apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking search results for 'banana apple apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9820145511359454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9820145511359454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9512235130317157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9506976036991436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9236763928239906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9820145511359454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9820145511359454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9512235130317157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9506976036991436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9236763928239906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('banana apple apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #348 checking search results for 'banana apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #348 checking search results for 'banana apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking search results for 'coconut papaya fig kiwi cherry lime cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.139406011900442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.10736601635071817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10225399211004464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07478495476961346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05485564788015886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05411070940723738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.05321509213345997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.018519765553665885}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.139406011900442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.10736601635071817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10225399211004464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07478495476961346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05485564788015886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05411070940723738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.05321509213345997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.018519765553665885}]
result = search.search('coconut papaya fig kiwi cherry lime cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #349 checking search results for 'coconut papaya fig kiwi cherry lime cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #349 checking search results for 'coconut papaya fig kiwi cherry lime cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking search results for 'coconut papaya fig kiwi cherry lime cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9855323165586175}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9791752675054497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8809104058614148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9855323165586175}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9791752675054497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8809104058614148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}]
result = search.search('coconut papaya fig kiwi cherry lime cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #350 checking search results for 'coconut papaya fig kiwi cherry lime cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #350 checking search results for 'coconut papaya fig kiwi cherry lime cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking search results for 'strawberry cherry kiwi apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('strawberry cherry kiwi apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #351 checking search results for 'strawberry cherry kiwi apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #351 checking search results for 'strawberry cherry kiwi apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking search results for 'strawberry cherry kiwi apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('strawberry cherry kiwi apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #352 checking search results for 'strawberry cherry kiwi apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #352 checking search results for 'strawberry cherry kiwi apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking search results for 'papaya fig peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2439122064294367}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.139406011900442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11023571572707162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.055395908060030224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.049560945874682176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04126899457584179}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.023594666682954832}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2439122064294367}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.139406011900442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11023571572707162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.055395908060030224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.049560945874682176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04126899457584179}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.023594666682954832}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}]
result = search.search('papaya fig peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #353 checking search results for 'papaya fig peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #353 checking search results for 'papaya fig peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking search results for 'papaya fig peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9952385890608804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9699687652182872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9514357327278576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.8844607440735748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9952385890608804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9699687652182872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9514357327278576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.8844607440735748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}]
result = search.search('papaya fig peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #354 checking search results for 'papaya fig peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #354 checking search results for 'papaya fig peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking search results for 'tomato kiwi papaya fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}]
result = search.search('tomato kiwi papaya fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #355 checking search results for 'tomato kiwi papaya fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #355 checking search results for 'tomato kiwi papaya fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking search results for 'tomato kiwi papaya fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}]
result = search.search('tomato kiwi papaya fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #356 checking search results for 'tomato kiwi papaya fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #356 checking search results for 'tomato kiwi papaya fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking search results for 'banana apricot strawberry strawberry cherry coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14912035462749673}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.13713119710597504}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08725293251083052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08211442788696356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.06796796171079425}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.056097635063359894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05466014674724512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05328435221329949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14912035462749673}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.13713119710597504}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08725293251083052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08211442788696356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.06796796171079425}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.056097635063359894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05466014674724512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05328435221329949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('banana apricot strawberry strawberry cherry coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #357 checking search results for 'banana apricot strawberry strawberry cherry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #357 checking search results for 'banana apricot strawberry strawberry cherry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking search results for 'banana apricot strawberry strawberry cherry coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.992893673048705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9820199583629539}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.96728161189017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9573025404389092}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9196795016567535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.751677412340012}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.5453313709753537}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.5453313709753537}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.992893673048705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9820199583629539}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.96728161189017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9573025404389092}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9196795016567535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.751677412340012}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.5453313709753537}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.5453313709753537}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('banana apricot strawberry strawberry cherry coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #358 checking search results for 'banana apricot strawberry strawberry cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #358 checking search results for 'banana apricot strawberry strawberry cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking search results for 'pear coconut lime papaya cherry pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.17776424054488268}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.13960867076797084}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.09654472298315606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07245454956638449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05489233634036229}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.054738343418116106}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.052826842564813445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.052023407493935664}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.047704595548346586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.014483971333688506}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.17776424054488268}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.13960867076797084}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.09654472298315606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07245454956638449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05489233634036229}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.054738343418116106}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.052826842564813445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.052023407493935664}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.047704595548346586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.014483971333688506}]
result = search.search('pear coconut lime papaya cherry pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #359 checking search results for 'pear coconut lime papaya cherry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #359 checking search results for 'pear coconut lime papaya cherry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking search results for 'pear coconut lime papaya cherry pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9861914585899767}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9559427009277199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9346485053787114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9055832815823142}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.8760904228315041}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8317254842758894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7820817867114674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.7069173102296906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.4391853913191619}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.3339206108680955}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9861914585899767}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9559427009277199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9346485053787114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9055832815823142}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.8760904228315041}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8317254842758894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7820817867114674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.7069173102296906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.4391853913191619}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.3339206108680955}]
result = search.search('pear coconut lime papaya cherry pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #360 checking search results for 'pear coconut lime papaya cherry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #360 checking search results for 'pear coconut lime papaya cherry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking search results for 'coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.0}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #361 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #361 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking search results for 'coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #362 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #362 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking search results for 'strawberry tomato fig apricot pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.23956015389944949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14992018898789114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11849947733196663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08270213630713262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053019295461351104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.0523022950817831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.23956015389944949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14992018898789114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11849947733196663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08270213630713262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053019295461351104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.0523022950817831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('strawberry tomato fig apricot pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #363 checking search results for 'strawberry tomato fig apricot pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #363 checking search results for 'strawberry tomato fig apricot pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking search results for 'strawberry tomato fig apricot pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9724698041480282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9526619027185704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9525405513846941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9507638717822757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.939658978158309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9724698041480282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9526619027185704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9525405513846941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9507638717822757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.939658978158309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('strawberry tomato fig apricot pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #364 checking search results for 'strawberry tomato fig apricot pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #364 checking search results for 'strawberry tomato fig apricot pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking search results for 'cherry kiwi tomato lime tomato papaya apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}]
result = search.search('cherry kiwi tomato lime tomato papaya apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #365 checking search results for 'cherry kiwi tomato lime tomato papaya apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #365 checking search results for 'cherry kiwi tomato lime tomato papaya apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking search results for 'cherry kiwi tomato lime tomato papaya apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}]
result = search.search('cherry kiwi tomato lime tomato papaya apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #366 checking search results for 'cherry kiwi tomato lime tomato papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #366 checking search results for 'cherry kiwi tomato lime tomato papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking search results for 'cherry lime banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.0}]
result = search.search('cherry lime banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #367 checking search results for 'cherry lime banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #367 checking search results for 'cherry lime banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking search results for 'cherry lime banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0}]
result = search.search('cherry lime banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #368 checking search results for 'cherry lime banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #368 checking search results for 'cherry lime banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking search results for 'lime strawberry tomato tomato cherry apricot kiwi pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.23956015389944949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14992018898789114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11849947733196663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08270213630713262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053019295461351104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.0523022950817831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.23956015389944949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.14992018898789114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11849947733196663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.08270213630713262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.08207927928119318}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053019295461351104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.0523022950817831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.043131349660802495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('lime strawberry tomato tomato cherry apricot kiwi pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #369 checking search results for 'lime strawberry tomato tomato cherry apricot kiwi pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #369 checking search results for 'lime strawberry tomato tomato cherry apricot kiwi pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking search results for 'lime strawberry tomato tomato cherry apricot kiwi pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9724698041480282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9526619027185704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9525405513846941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9507638717822757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.939658978158309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9724698041480282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9526619027185704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9525405513846941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9507638717822757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.939658978158309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('lime strawberry tomato tomato cherry apricot kiwi pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #370 checking search results for 'lime strawberry tomato tomato cherry apricot kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #370 checking search results for 'lime strawberry tomato tomato cherry apricot kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking search results for 'banana fig peach lime fig banana kiwi tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.22692074650509478}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.13006072870217375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12372305440133477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.07739005105661852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05513829455423453}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.04902244765699294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.04899723201945257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.04546210104546642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.03684337389110574}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.03232852477598505}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.22692074650509478}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.13006072870217375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12372305440133477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.07739005105661852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.05513829455423453}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.04902244765699294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.04899723201945257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.04546210104546642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.03684337389110574}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.03232852477598505}]
result = search.search('banana fig peach lime fig banana kiwi tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #371 checking search results for 'banana fig peach lime fig banana kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #371 checking search results for 'banana fig peach lime fig banana kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking search results for 'banana fig peach lime fig banana kiwi tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9926745069246792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9023986110085679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8807334936289136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.8802804714399687}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.8436497593967707}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.745317737308182}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.745317737308182}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.6667094348018572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.6667094348018572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.6667094348018572}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9926745069246792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9023986110085679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8807334936289136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.8802804714399687}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.8436497593967707}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.745317737308182}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.745317737308182}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.6667094348018572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.6667094348018572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.6667094348018572}]
result = search.search('banana fig peach lime fig banana kiwi tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #372 checking search results for 'banana fig peach lime fig banana kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #372 checking search results for 'banana fig peach lime fig banana kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking search results for 'peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04337549364213977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0}]
result = search.search('peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #373 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #373 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking search results for 'peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #374 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #374 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking search results for 'pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.0}]
result = search.search('pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #375 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #375 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking search results for 'pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #376 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #376 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking search results for 'apple peach peach kiwi strawberry coconut fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.22206425085408837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.15415417676348783}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11006433851607679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05832641236676532}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.055653247092815904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.05446498036732883}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053224022843301515}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0388048087497359}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.03830427916999509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.025929348905289504}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.22206425085408837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.15415417676348783}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.11006433851607679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05832641236676532}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.055653247092815904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.05446498036732883}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.053224022843301515}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0388048087497359}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.03830427916999509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.025929348905289504}]
result = search.search('apple peach peach kiwi strawberry coconut fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #377 checking search results for 'apple peach peach kiwi strawberry coconut fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #377 checking search results for 'apple peach peach kiwi strawberry coconut fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking search results for 'apple peach peach kiwi strawberry coconut fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9999339188259535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.999861922171015}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9562186676551894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9562186676551894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.8830857231508729}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.8830857231508729}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.8830857231508729}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.46921168524142703}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.46921168524142703}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.46921168524142703}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9999339188259535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.999861922171015}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9562186676551894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9562186676551894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.8830857231508729}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.8830857231508729}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.8830857231508729}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.46921168524142703}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.46921168524142703}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.46921168524142703}]
result = search.search('apple peach peach kiwi strawberry coconut fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #378 checking search results for 'apple peach peach kiwi strawberry coconut fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #378 checking search results for 'apple peach peach kiwi strawberry coconut fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking search results for 'papaya apricot banana banana kiwi fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.24978742956302674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.10780066568351006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.10489537525612104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10358342639277586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07158318691694358}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0530048618618472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.04756076984134539}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.047416636115606224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.03684002203388176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.018524277052233522}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.24978742956302674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.10780066568351006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.10489537525612104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10358342639277586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07158318691694358}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.0530048618618472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.04756076984134539}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.047416636115606224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.03684002203388176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.018524277052233522}]
result = search.search('papaya apricot banana banana kiwi fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #379 checking search results for 'papaya apricot banana banana kiwi fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #379 checking search results for 'papaya apricot banana banana kiwi fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking search results for 'papaya apricot banana banana kiwi fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9933328395780463}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9591640982204865}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8923633816269624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.8655542663505528}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8544731033248096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.8518836079836503}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.8416132742187279}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.6992580048891035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.6039650881338764}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.4270678094193949}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9933328395780463}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9591640982204865}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8923633816269624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.8655542663505528}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8544731033248096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.8518836079836503}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.8416132742187279}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.6992580048891035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.6039650881338764}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.4270678094193949}]
result = search.search('papaya apricot banana banana kiwi fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #380 checking search results for 'papaya apricot banana banana kiwi fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #380 checking search results for 'papaya apricot banana banana kiwi fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking search results for 'blueberry tomato kiwi apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.2514639802597616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12463607510646232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('blueberry tomato kiwi apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #381 checking search results for 'blueberry tomato kiwi apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #381 checking search results for 'blueberry tomato kiwi apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking search results for 'blueberry tomato kiwi apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('blueberry tomato kiwi apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #382 checking search results for 'blueberry tomato kiwi apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #382 checking search results for 'blueberry tomato kiwi apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking search results for 'lime kiwi fig cherry coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.1541643641256654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.11607762994927237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.0827021363071326}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.05566093263355323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05526151568869791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.0}]
result = search.search('lime kiwi fig cherry coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #383 checking search results for 'lime kiwi fig cherry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #383 checking search results for 'lime kiwi fig cherry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking search results for 'lime kiwi fig cherry coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0}]
result = search.search('lime kiwi fig cherry coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #384 checking search results for 'lime kiwi fig cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #384 checking search results for 'lime kiwi fig cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking search results for 'peach pear peach lime strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.24978071508548058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.15415470965462535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12462221523903443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05909351444606051}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.049086720028502014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.047703842240176965}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04202195019449079}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.02877150884328512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.02049891307359651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.013697360878453031}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.24978071508548058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.15415470965462535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.12462221523903443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.05909351444606051}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.049086720028502014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.047703842240176965}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.04202195019449079}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.02877150884328512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.02049891307359651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.013697360878453031}]
result = search.search('peach pear peach lime strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #385 checking search results for 'peach pear peach lime strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #385 checking search results for 'peach pear peach lime strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking search results for 'peach pear peach lime strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9999373754687422}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9998887973051457}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9933061380300185}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9687947425148379}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9687947425148379}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.8818882060720595}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8570435309490375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.24786437193676933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.24786437193676933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.24786437193676933}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9999373754687422}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.9998887973051457}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.9933061380300185}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.9687947425148379}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.9687947425148379}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.8818882060720595}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.8570435309490375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.24786437193676933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.24786437193676933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.24786437193676933}]
result = search.search('peach pear peach lime strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #386 checking search results for 'peach pear peach lime strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #386 checking search results for 'peach pear peach lime strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking search results for 'papaya coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.139406011900442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.10736601635071817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10225399211004464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07478495476961346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05485564788015886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05411070940723738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.05321509213345997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.018519765553665885}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.139406011900442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.10736601635071817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.10225399211004464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.07478495476961346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 0.06099693965376308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.05485564788015886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.054487607904177324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.05411070940723738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.05321509213345997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.018519765553665885}]
result = search.search('papaya coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #387 checking search results for 'papaya coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #387 checking search results for 'papaya coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking search results for 'papaya coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9855323165586175}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9791752675054497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8809104058614148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-2.html', 'title': 'Custom Title 89', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-0.html', 'title': 'N-0', 'score': 0.9855323165586175}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-0.html', 'title': 'Custom Title 20', 'score': 0.9791752675054497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-4.html', 'title': 'N-4', 'score': 0.9789201388862714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-2.html', 'title': 'Custom Title 38', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-4.html', 'title': 'N-4', 'score': 0.9042687179431864}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-3.html', 'title': 'N-3', 'score': 0.8809104058614148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsA/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-1.html', 'title': 'N-1', 'score': 0.42696379910876053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruitsB/N-3.html', 'title': 'N-3', 'score': 0.42696379910876053}]
result = search.search('papaya coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #388 checking search results for 'papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #388 checking search results for 'papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
