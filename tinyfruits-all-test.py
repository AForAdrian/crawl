
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html')


output = open('tinyfruits-all-outgoing-failed.txt', 'w')
success_output = open('tinyfruits-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html\n\n')
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









output = open('tinyfruits-all-incoming-failed.txt', 'w')
success_output = open('tinyfruits-all-incoming-passed.txt', 'w')

#Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html\n\n')
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









output = open('tinyfruits-all-pagerank-failed.txt', 'w')
success_output = open('tinyfruits-all-pagerank-passed.txt', 'w')

#Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html
expected = 0.32242792521306995
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html
expected = 0.0819555328928385
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html
expected = 0.12476521976591842
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html
expected = 0.11939323868209492
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html
expected = 0.11896585666418055
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html
expected = 0.047437705789256435
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html\n\n')
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









output = open('tinyfruits-all-idf-failed.txt', 'w')
success_output = open('tinyfruits-all-idf-passed.txt', 'w')

#Test #33 checking IDF for word kiwi
expected = 0.32192809488736235
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking IDF for word papaya
expected = 0.5145731728297582
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking IDF for word banana
expected = 0.0
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking IDF for word cherry
expected = 0.5145731728297582
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking IDF for word blueberry
expected = 0.32192809488736235
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking IDF for word pear
expected = 0.7369655941662062
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking IDF for word apple
expected = 0.32192809488736235
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking IDF for word peach
expected = 0.5145731728297582
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking IDF for word orange
expected = 0.32192809488736235
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking IDF for word fig
expected = 0.7369655941662062
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking IDF for word coconut
expected = 0.32192809488736235
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking IDF for word apricot
expected = 0.0
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking IDF for word lime
expected = 0.32192809488736235
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









output = open('tinyfruits-all-tf-failed.txt', 'w')
success_output = open('tinyfruits-all-tf-passed.txt', 'w')

#Test #47 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word kiwi
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apple
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word coconut
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word orange
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word papaya
expected = 0.2
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word banana
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word blueberry
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word peach
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word kiwi
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apple
expected = 0.14285714285714285
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word coconut
expected = 0.2857142857142857
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word orange
expected = 0.2857142857142857
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word papaya
expected = 0.14285714285714285
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word blueberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word pear
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word kiwi
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apple
expected = 0.125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word coconut
expected = 0.03125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word orange
expected = 0.09375
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word papaya
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word banana
expected = 0.125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word fig
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word blueberry
expected = 0.125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word pear
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word kiwi
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apple
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word coconut
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word orange
expected = 0.25
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word banana
expected = 0.125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word fig
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word blueberry
expected = 0.125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word peach
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word pear
expected = 0.13513513513513514
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word kiwi
expected = 0.02702702702702703
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apple
expected = 0.16216216216216217
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word coconut
expected = 0.05405405405405406
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word orange
expected = 0.05405405405405406
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word papaya
expected = 0.05405405405405406
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word banana
expected = 0.10810810810810811
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word blueberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word peach
expected = 0.10810810810810811
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word pear
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word kiwi
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apple
expected = 0.17391304347826086
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word coconut
expected = 0.13043478260869565
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word orange
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word papaya
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word banana
expected = 0.21739130434782608
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word fig
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word blueberry
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word peach
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word pear
expected = 0.1875
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word kiwi
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apple
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word coconut
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word orange
expected = 0.125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word banana
expected = 0.125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word fig
expected = 0.1875
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word blueberry
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word peach
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word kiwi
expected = 0.25
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apple
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word coconut
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word orange
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word banana
expected = 0.25
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word blueberry
expected = 0.25
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word kiwi
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apple
expected = 0.18181818181818182
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word coconut
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word orange
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word papaya
expected = 0.18181818181818182
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word banana
expected = 0.18181818181818182
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word blueberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word kiwi
expected = 0.05
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apple
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word coconut
expected = 0.05
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word orange
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word banana
expected = 0.05
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #152 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #152 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word fig
expected = 0.15
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word blueberry
expected = 0.2
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word peach
expected = 0.05
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word tomato\n\n')
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


#Test #158 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word orange
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
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









output = open('tinyfruits-all-tfidf-failed.txt', 'w')
success_output = open('tinyfruits-all-tfidf-passed.txt', 'w')

#Test #168 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word pear
expected = 0.04525008888053903
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word coconut
expected = 0.05694192097566775
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word peach
expected = 0.031595073081303486
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word kiwi
expected = 0.03872609348667805
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word papaya
expected = 0.031595073081303486
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word blueberry
expected = 0.019766560368774045
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word fig
expected = 0.04525008888053903
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word coconut
expected = 0.11672149491947882
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word papaya
expected = 0.0991299889868547
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word orange
expected = 0.11672149491947882
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word pear
expected = 0.06445710476952095
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word coconut
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word peach
expected = 0.045006031726892604
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word kiwi
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word orange
expected = 0.10363769827780657
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word blueberry
expected = 0.054703631988055924
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word fig
expected = 0.06445710476952095
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word pear
expected = 0.18271404725510207
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word peach
expected = 0.045006031726892604
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word kiwi
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word orange
expected = 0.054703631988055924
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word blueberry
expected = 0.02815674585715757
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word fig
expected = 0.18271404725510207
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word pear
expected = 0.13476451852905313
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word coconut
expected = 0.02445006963027565
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word peach
expected = 0.07620758655640758
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word kiwi
expected = 0.012385909108380427
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word papaya
expected = 0.03908124238104001
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word orange
expected = 0.02445006963027565
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word peach
expected = 0.04791160163801364
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word kiwi
expected = 0.02997453317184664
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word papaya
expected = 0.13535044877328553
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word blueberry
expected = 0.02997453317184664
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word coconut
expected = 0.02266030222847964
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word peach
expected = 0.03622045978643087
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word kiwi
expected = 0.02266030222847964
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word orange
expected = 0.044266247441115764
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word blueberry
expected = 0.08467816515990254
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word fig
expected = 0.14859721830091777
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word pear
expected = 0.06445710476952095
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word coconut
expected = 0.014291714269269087
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word papaya
expected = 0.045006031726892604
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word orange
expected = 0.04161983534638364
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word blueberry
expected = 0.054703631988055924
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word fig
expected = 0.06445710476952095
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word coconut
expected = 0.0404119177187868
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word papaya
expected = 0.12401630243933787
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word orange
expected = 0.0404119177187868
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word kiwi
expected = 0.10363769827780657
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word blueberry
expected = 0.10363769827780657
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html and word tomato\n\n')
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


#Test #279 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
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









output = open('tinyfruits-all-search-failed.txt', 'w')
success_output = open('tinyfruits-all-search-passed.txt', 'w')

#Test #289 checking search results for 'orange fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29546744271304826}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1174178179201082}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09836736519185915}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04592567283238615}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04591793916184169}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018989447476008524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29546744271304826}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1174178179201082}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09836736519185915}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04592567283238615}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04591793916184169}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018989447476008524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #289 checking search results for 'orange fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #289 checking search results for 'orange fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking search results for 'orange fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.99269496548452}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9925278002512045}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.986987537538252}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9163829172606391}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8238939346789915}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4003028215649755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4003028215649755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4003028215649755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.99269496548452}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9925278002512045}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.986987537538252}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9163829172606391}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8238939346789915}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4003028215649755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4003028215649755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4003028215649755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #290 checking search results for 'orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #290 checking search results for 'orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking search results for 'blueberry coconut blueberry banana orange peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.241199701425045}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10010635113579174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09443630330482738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0821283770711231}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06778470577076844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0440979335540306}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0383587225487085}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03413259800680336}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.023077409512575715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.023077409512575715}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.241199701425045}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10010635113579174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09443630330482738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0821283770711231}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06778470577076844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0440979335540306}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0383587225487085}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03413259800680336}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.023077409512575715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.023077409512575715}]
result = search.search('blueberry coconut blueberry banana orange peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #291 checking search results for 'blueberry coconut blueberry banana orange peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #291 checking search results for 'blueberry coconut blueberry banana orange peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking search results for 'blueberry coconut blueberry banana orange peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9531879214295794}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8384591308586757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8291334325246514}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8270912698402044}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7938101397563527}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7480732361058772}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7195246363396777}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6582633944396558}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4988240090279852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4988240090279852}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9531879214295794}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8384591308586757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8291334325246514}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8270912698402044}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7938101397563527}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7480732361058772}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7195246363396777}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6582633944396558}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4988240090279852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4988240090279852}]
result = search.search('blueberry coconut blueberry banana orange peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #292 checking search results for 'blueberry coconut blueberry banana orange peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #292 checking search results for 'blueberry coconut blueberry banana orange peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking search results for 'orange' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #293 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #293 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking search results for 'orange' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #294 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #294 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking search results for 'blueberry papaya peach peach banana tomato blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3098736992129061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10321927276984454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0754686900142711}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.060334314433731114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05985233057955991}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04218180784063386}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.041517768106698105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0346331234828479}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0190004887051449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0190004887051449}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3098736992129061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10321927276984454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0754686900142711}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.060334314433731114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05985233057955991}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04218180784063386}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.041517768106698105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0346331234828479}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0190004887051449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0190004887051449}]
result = search.search('blueberry papaya peach peach banana tomato blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #295 checking search results for 'blueberry papaya peach peach banana tomato blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #295 checking search results for 'blueberry papaya peach peach banana tomato blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking search results for 'blueberry papaya peach peach banana tomato blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.96106346560439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9117703823579902}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8752060711186614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8645319777670463}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7486036719789204}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7303025002329034}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6343726858312447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4835828009354605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.410700340704466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.410700340704466}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.96106346560439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9117703823579902}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8752060711186614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8645319777670463}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7486036719789204}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7303025002329034}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6343726858312447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4835828009354605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.410700340704466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.410700340704466}]
result = search.search('blueberry papaya peach peach banana tomato blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #296 checking search results for 'blueberry papaya peach peach banana tomato blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #296 checking search results for 'blueberry papaya peach peach banana tomato blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking search results for 'kiwi cherry banana apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.275744302573069}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10208384478451667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.05594220444749448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.054306663245396555}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04243007540704138}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04087089852330702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.038828407081654165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03847610819192249}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03065593376937129}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.275744302573069}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10208384478451667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.05594220444749448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.054306663245396555}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04243007540704138}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04087089852330702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.038828407081654165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03847610819192249}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03065593376937129}]
result = search.search('kiwi cherry banana apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #297 checking search results for 'kiwi cherry banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #297 checking search results for 'kiwi cherry banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking search results for 'kiwi cherry banana apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8944377621366931}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8834347478585992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8580936383510539}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.855212222672242}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8392857817982873}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8316707527173023}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.662635716326872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.662635716326872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.46855420847113666}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8944377621366931}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8834347478585992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8580936383510539}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.855212222672242}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8392857817982873}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8316707527173023}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.662635716326872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.662635716326872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.46855420847113666}]
result = search.search('kiwi cherry banana apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #298 checking search results for 'kiwi cherry banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #298 checking search results for 'kiwi cherry banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking search results for 'coconut lime kiwi pear papaya apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27977291605559196}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10714788393538525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09979304461738005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05136583750833748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04308140833626215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03632754425453905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03581070547987474}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0280677698540679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02749160484143614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.022082423635506738}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27977291605559196}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10714788393538525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09979304461738005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05136583750833748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04308140833626215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03632754425453905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03581070547987474}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0280677698540679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02749160484143614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.022082423635506738}]
result = search.search('coconut lime kiwi pear papaya apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #299 checking search results for 'coconut lime kiwi pear papaya apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #299 checking search results for 'coconut lime kiwi pear papaya apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking search results for 'coconut lime kiwi pear papaya apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9081680410020823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9006608025178574}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.867706839817642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8358349745674982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7740574029271886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6267525290269447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6066919025487411}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5942379509340238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.47731713912322793}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.29116723653191123}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9081680410020823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9006608025178574}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.867706839817642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8358349745674982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7740574029271886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6267525290269447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6066919025487411}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5942379509340238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.47731713912322793}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.29116723653191123}]
result = search.search('coconut lime kiwi pear papaya apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #300 checking search results for 'coconut lime kiwi pear papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #300 checking search results for 'coconut lime kiwi pear papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking search results for 'apricot peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('apricot peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #301 checking search results for 'apricot peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #301 checking search results for 'apricot peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking search results for 'apricot peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('apricot peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #302 checking search results for 'apricot peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #302 checking search results for 'apricot peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking search results for 'blueberry apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #303 checking search results for 'blueberry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #303 checking search results for 'blueberry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking search results for 'blueberry apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #304 checking search results for 'blueberry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #304 checking search results for 'blueberry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking search results for 'fig fig blueberry peach cherry orange' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30196687321039917}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08495128793049024}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07889329224457192}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04360269652720223}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04340384654238789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.030683315317007957}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.024774386365034363}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.022771926145824017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.017320631133835425}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.016507282615864236}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30196687321039917}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08495128793049024}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07889329224457192}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04360269652720223}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04340384654238789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.030683315317007957}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.024774386365034363}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.022771926145824017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.017320631133835425}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.016507282615864236}]
result = search.search('fig fig blueberry peach cherry orange',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #305 checking search results for 'fig fig blueberry peach cherry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #305 checking search results for 'fig fig blueberry peach cherry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking search results for 'fig fig blueberry peach cherry orange' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9424832485759383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9381850561568026}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9365406951362867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7115251153935751}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6631591152012097}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.48003852140297526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3743897969296122}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3743897969296122}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3568090642113117}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.19856804974587858}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9424832485759383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9381850561568026}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9365406951362867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7115251153935751}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6631591152012097}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.48003852140297526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3743897969296122}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3743897969296122}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3568090642113117}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.19856804974587858}]
result = search.search('fig fig blueberry peach cherry orange',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #306 checking search results for 'fig fig blueberry peach cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #306 checking search results for 'fig fig blueberry peach cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking search results for 'lime papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30529974367124346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11522125581622235}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08134181964536434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04743770578925645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.039220518894086606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.039220518894086606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02453720402607222}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30529974367124346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11522125581622235}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08134181964536434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04743770578925645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.039220518894086606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.039220518894086606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02453720402607222}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('lime papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #307 checking search results for 'lime papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #307 checking search results for 'lime papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking search results for 'lime papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9925116312979549}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9685237348516849}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9468774873314472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8477613772137169}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8477613772137169}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5303778344771792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9925116312979549}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9685237348516849}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9468774873314472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8477613772137169}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8477613772137169}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5303778344771792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('lime papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #308 checking search results for 'lime papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #308 checking search results for 'lime papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking search results for 'peach kiwi peach fig apple apricot banana papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2551838835282281}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10243342133506686}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07820840581783622}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05296975712120972}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0367835363152043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03373910531448644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.032464918576357346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.028648989091619753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02002950002885096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02002950002885096}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2551838835282281}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10243342133506686}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07820840581783622}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05296975712120972}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0367835363152043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03373910531448644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.032464918576357346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.028648989091619753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02002950002885096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02002950002885096}]
result = search.search('peach kiwi peach fig apple apricot banana papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #309 checking search results for 'peach kiwi peach fig apple apricot banana papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #309 checking search results for 'peach kiwi peach fig apple apricot banana papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking search results for 'peach kiwi peach fig apple apricot banana papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8579499347346922}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7914447340738088}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7754071514043357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7292792444844522}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.701737377767675}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6574021152859398}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6463231370903375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4329426791933911}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4329426791933911}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.22962320064333885}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8579499347346922}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7914447340738088}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7754071514043357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7292792444844522}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.701737377767675}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6574021152859398}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6463231370903375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4329426791933911}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4329426791933911}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.22962320064333885}]
result = search.search('peach kiwi peach fig apple apricot banana papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #310 checking search results for 'peach kiwi peach fig apple apricot banana papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #310 checking search results for 'peach kiwi peach fig apple apricot banana papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking search results for 'pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #311 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #311 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking search results for 'pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #312 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #312 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking search results for 'peach tomato tomato tomato banana blueberry pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11525657567428234}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09597004548480666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0521030997012669}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.044458766918338215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.042498918502119565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04206919328888758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.024148572494316463}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11525657567428234}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09597004548480666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0521030997012669}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.044458766918338215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.042498918502119565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04206919328888758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.024148572494316463}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach tomato tomato tomato banana blueberry pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #313 checking search results for 'peach tomato tomato tomato banana blueberry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #313 checking search results for 'peach tomato tomato tomato banana blueberry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking search results for 'peach tomato tomato tomato banana blueberry pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9653526191811652}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9372031420711563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9186248090379698}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8067024285439562}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6357484096820486}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5219774662036322}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.33718686479947546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9653526191811652}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9372031420711563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9186248090379698}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8067024285439562}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6357484096820486}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5219774662036322}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.33718686479947546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach tomato tomato tomato banana blueberry pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #314 checking search results for 'peach tomato tomato tomato banana blueberry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #314 checking search results for 'peach tomato tomato tomato banana blueberry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking search results for 'blueberry pear coconut pear coconut tomato pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26664883921243165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10383798604269946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1019368928232841}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04653654956579122}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04426461989773817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.019267265379784633}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.013446222578458586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.013446222578458586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.012656243499194577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01037752901236735}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26664883921243165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10383798604269946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1019368928232841}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04653654956579122}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04426461989773817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.019267265379784633}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.013446222578458586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.013446222578458586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.012656243499194577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01037752901236735}]
result = search.search('blueberry pear coconut pear coconut tomato pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #315 checking search results for 'blueberry pear coconut pear coconut tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #315 checking search results for 'blueberry pear coconut pear coconut tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking search results for 'blueberry pear coconut pear coconut tomato pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9810033767765113}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9567908886592035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8697141244253035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8568583935055737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.827002931077456}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.2906434818524269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.2906434818524269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.22431289885168498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.15442817650570748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.15442817650570748}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9810033767765113}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9567908886592035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8697141244253035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8568583935055737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.827002931077456}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.2906434818524269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.2906434818524269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.22431289885168498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.15442817650570748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.15442817650570748}]
result = search.search('blueberry pear coconut pear coconut tomato pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #316 checking search results for 'blueberry pear coconut pear coconut tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #316 checking search results for 'blueberry pear coconut pear coconut tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking search results for 'banana blueberry coconut lime apple apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2962654251498458}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10265342611740245}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0979484232891416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06238260988295921}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05910080417420306}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04006547906619705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03614412290499443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03571147134084328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03128109364370344}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.031201501261373055}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2962654251498458}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10265342611740245}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0979484232891416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06238260988295921}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05910080417420306}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04006547906619705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03614412290499443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03571147134084328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03128109364370344}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.031201501261373055}]
result = search.search('banana blueberry coconut lime apple apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #317 checking search results for 'banana blueberry coconut lime apple apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #317 checking search results for 'banana blueberry coconut lime apple apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking search results for 'banana blueberry coconut lime apple apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9188578345193419}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8660254037844386}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8628814098079822}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8203850098241005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7719124320613235}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7619281393068602}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7211325713845423}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6761487041961499}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.674428294839957}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9188578345193419}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8660254037844386}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8628814098079822}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8203850098241005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7719124320613235}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7619281393068602}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7211325713845423}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6761487041961499}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.674428294839957}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5}]
result = search.search('banana blueberry coconut lime apple apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #318 checking search results for 'banana blueberry coconut lime apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #318 checking search results for 'banana blueberry coconut lime apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking search results for 'pear blueberry cherry apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10073578476304852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09631481559657418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04373455310424207}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04206919328888758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03766998883359981}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029180876518371708}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.027634329189106497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.024934382513820293}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.024934382513820293}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10073578476304852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09631481559657418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04373455310424207}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04206919328888758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03766998883359981}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029180876518371708}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.027634329189106497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.024934382513820293}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.024934382513820293}]
result = search.search('pear blueberry cherry apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #319 checking search results for 'pear blueberry cherry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #319 checking search results for 'pear blueberry cherry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking search results for 'pear blueberry cherry apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9219365139312229}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8467621516600996}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8142462801024509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8067024285439561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6307519829689988}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5389629473534837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5389629473534837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.33718686479947546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.33718686479947546}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9219365139312229}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8467621516600996}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8142462801024509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8067024285439561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6307519829689988}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5389629473534837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5389629473534837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.33718686479947546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.33718686479947546}]
result = search.search('pear blueberry cherry apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #320 checking search results for 'pear blueberry cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #320 checking search results for 'pear blueberry cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking search results for 'peach coconut banana papaya orange peach tomato apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22459762396491936}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07163153552770962}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06786558272591646}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05699281900826909}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04398850389307162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.034660194282969334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03460980669254061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0273772708310845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.027052601607256328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22459762396491936}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07163153552770962}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06786558272591646}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05699281900826909}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04398850389307162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.034660194282969334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03460980669254061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0273772708310845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.027052601607256328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('peach coconut banana papaya orange peach tomato apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #321 checking search results for 'peach coconut banana papaya orange peach tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #321 checking search results for 'peach coconut banana papaya orange peach tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking search results for 'peach coconut banana papaya orange peach tomato apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9272898670203824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7491888141300275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7480996736938264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.6965824185870333}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6954114871388907}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5999630826536244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5917665925529727}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5847487856474914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5704626909676188}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9272898670203824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7491888141300275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7480996736938264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.6965824185870333}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6954114871388907}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5999630826536244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5917665925529727}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5847487856474914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5704626909676188}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('peach coconut banana papaya orange peach tomato apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #322 checking search results for 'peach coconut banana papaya orange peach tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #322 checking search results for 'peach coconut banana papaya orange peach tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking search results for 'coconut apple coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.296331499123294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10403039436336696}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08268334135819543}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04624974494266459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040310688884251544}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04021600395773101}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03875592395190091}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0356340156425298}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02270180269087849}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.296331499123294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10403039436336696}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08268334135819543}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04624974494266459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040310688884251544}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04021600395773101}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03875592395190091}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0356340156425298}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02270180269087849}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut apple coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #323 checking search results for 'coconut apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #323 checking search results for 'coconut apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking search results for 'coconut apple coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9996998656304898}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9190627608556837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8713256756554348}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8713256756554348}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.837719040724047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7511749366808564}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6950174081593493}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.49070517313719036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.49070517313719036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9996998656304898}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9190627608556837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8713256756554348}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8713256756554348}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.837719040724047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7511749366808564}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6950174081593493}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.49070517313719036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.49070517313719036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut apple coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #324 checking search results for 'coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #324 checking search results for 'coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking search results for 'papaya tomato apple tomato orange peach papaya orange' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.20281408330401357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09673595726566504}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07144085570188599}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07018666706259882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04044075326791778}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03997691652373937}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03697821294090105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.030612278169542886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.028388109559512188}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.20281408330401357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09673595726566504}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07144085570188599}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07018666706259882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04044075326791778}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03997691652373937}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03697821294090105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.030612278169542886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.028388109559512188}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('papaya tomato apple tomato orange peach papaya orange',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #325 checking search results for 'papaya tomato apple tomato orange peach papaya orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #325 checking search results for 'papaya tomato apple tomato orange peach papaya orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking search results for 'papaya tomato apple tomato orange peach papaya orange' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.87413705001081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8717026560647096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8641111021617033}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.81314050920285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7795109886885755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.661692089560139}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.6290214570279171}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6136161258257725}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5878613214395073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.87413705001081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8717026560647096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8641111021617033}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.81314050920285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7795109886885755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.661692089560139}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.6290214570279171}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6136161258257725}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5878613214395073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('papaya tomato apple tomato orange peach papaya orange',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #326 checking search results for 'papaya tomato apple tomato orange peach papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #326 checking search results for 'papaya tomato apple tomato orange peach papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking search results for 'blueberry apple peach blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2378964794566217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11028370998036058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09049994140825827}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08657801482862645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07878019212361478}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044471160770213604}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040623026845368546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03359016431648932}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.017667888471279536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017667888471279536}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2378964794566217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11028370998036058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09049994140825827}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08657801482862645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07878019212361478}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044471160770213604}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040623026845368546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03359016431648932}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.017667888471279536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017667888471279536}]
result = search.search('blueberry apple peach blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #327 checking search results for 'blueberry apple peach blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #327 checking search results for 'blueberry apple peach blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking search results for 'blueberry apple peach blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9612553215488739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9612553215488739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9237014691762401}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8780769392169324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7607219747403955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.737828397771107}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.708089983645388}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6939274822828196}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3818958515902907}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3818958515902907}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9612553215488739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9612553215488739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9237014691762401}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8780769392169324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7607219747403955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.737828397771107}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.708089983645388}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6939274822828196}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3818958515902907}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3818958515902907}]
result = search.search('blueberry apple peach blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #328 checking search results for 'blueberry apple peach blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #328 checking search results for 'blueberry apple peach blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking search results for 'orange blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11788333578620874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11407020069458891}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044146310235372355}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04405772409580497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11788333578620874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11407020069458891}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044146310235372355}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04405772409580497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('orange blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #329 checking search results for 'orange blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #329 checking search results for 'orange blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking search results for 'orange blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9909005751034301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.95541591763266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9542335955602576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9909005751034301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.95541591763266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9542335955602576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}]
result = search.search('orange blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #330 checking search results for 'orange blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #330 checking search results for 'orange blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking search results for 'orange kiwi lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2632612985320922}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09930905627519071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08726870826004908}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07203323321735582}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.058108714191464704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04569988046984719}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04460995893874926}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.043825491249772475}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026710319377464698}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026710319377464698}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2632612985320922}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09930905627519071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08726870826004908}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07203323321735582}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.058108714191464704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04569988046984719}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04460995893874926}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.043825491249772475}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026710319377464698}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026710319377464698}]
result = search.search('orange kiwi lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #331 checking search results for 'orange kiwi lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #331 checking search results for 'orange kiwi lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking search results for 'orange kiwi lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.96425547886016}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.963366160093627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9472990125221563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8317812413114799}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.816496580927726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7335609620026787}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7090273486165375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5773502691896257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5773502691896257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5773502691896257}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.96425547886016}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.963366160093627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9472990125221563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8317812413114799}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.816496580927726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7335609620026787}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7090273486165375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5773502691896257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5773502691896257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5773502691896257}]
result = search.search('orange kiwi lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #332 checking search results for 'orange kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #332 checking search results for 'orange kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking search results for 'blueberry kiwi tomato tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303063}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1137004238652347}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040058048374050796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303063}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1137004238652347}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040058048374050796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('blueberry kiwi tomato tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #333 checking search results for 'blueberry kiwi tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #333 checking search results for 'blueberry kiwi tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking search results for 'blueberry kiwi tomato tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.951275576479978}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8658647875053789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.951275576479978}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8658647875053789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('blueberry kiwi tomato tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #334 checking search results for 'blueberry kiwi tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #334 checking search results for 'blueberry kiwi tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking search results for 'orange tomato blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11788333578620874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11407020069458891}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044146310235372355}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04405772409580497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11788333578620874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11407020069458891}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044146310235372355}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04405772409580497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('orange tomato blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #335 checking search results for 'orange tomato blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #335 checking search results for 'orange tomato blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking search results for 'orange tomato blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9909005751034301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.95541591763266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9542335955602576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9909005751034301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.95541591763266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9542335955602576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}]
result = search.search('orange tomato blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #336 checking search results for 'orange tomato blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #336 checking search results for 'orange tomato blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking search results for 'apple cherry fig peach apricot coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27213521060476387}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10075554439971512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08735438583419708}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04396962703467612}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04146988236526747}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03586469147957154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.034439849090532014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026866893716456598}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026783754300697973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27213521060476387}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10075554439971512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08735438583419708}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04396962703467612}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04146988236526747}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03586469147957154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.034439849090532014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026866893716456598}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026783754300697973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple cherry fig peach apricot coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #337 checking search results for 'apple cherry fig peach apricot coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #337 checking search results for 'apple cherry fig peach apricot coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking search results for 'apple cherry fig peach apricot coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8963819342066544}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8440187382185611}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8438965682805049}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7752243238844766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.734281148252334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7260015744338939}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5807346628948328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5789375835192485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5365059012204692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8963819342066544}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8440187382185611}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8438965682805049}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7752243238844766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.734281148252334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7260015744338939}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5807346628948328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5789375835192485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5365059012204692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple cherry fig peach apricot coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #338 checking search results for 'apple cherry fig peach apricot coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #338 checking search results for 'apple cherry fig peach apricot coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking search results for 'apple blueberry fig peach banana orange apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29251424994663466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10369241160563557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08753264689828569}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05716845859932522}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.039660166676118436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.037019111579963584}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03416286850619839}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.033958104061492925}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026997097048411273}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.022373470773945584}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29251424994663466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10369241160563557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08753264689828569}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05716845859932522}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.039660166676118436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.037019111579963584}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03416286850619839}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.033958104061492925}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026997097048411273}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.022373470773945584}]
result = search.search('apple blueberry fig peach banana orange apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #339 checking search results for 'apple blueberry fig peach banana orange apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #339 checking search results for 'apple blueberry fig peach banana orange apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking search results for 'apple blueberry fig peach banana orange apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9072236834118278}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8716148860957711}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.857264474564131}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8001774046133273}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7331457615565354}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7158462555578239}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6975545955399524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5835490406523987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4836081961993297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2738172430609585}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9072236834118278}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8716148860957711}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.857264474564131}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8001774046133273}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7331457615565354}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7158462555578239}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6975545955399524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5835490406523987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4836081961993297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2738172430609585}]
result = search.search('apple blueberry fig peach banana orange apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #340 checking search results for 'apple blueberry fig peach banana orange apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #340 checking search results for 'apple blueberry fig peach banana orange apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking search results for 'cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #341 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #341 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking search results for 'cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #342 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #342 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking search results for 'papaya peach apricot banana peach cherry papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3119129894599868}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07903001550477376}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06924185387376426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06102318399618489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04436387871567836}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034676444713230885}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.033159379615210316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03062330376642632}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.025455085295495818}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3119129894599868}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07903001550477376}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06924185387376426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06102318399618489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04436387871567836}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034676444713230885}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.033159379615210316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03062330376642632}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.025455085295495818}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('papaya peach apricot banana peach cherry papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #343 checking search results for 'papaya peach apricot banana peach cherry papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #343 checking search results for 'papaya peach apricot banana peach cherry papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking search results for 'papaya peach apricot banana peach cherry papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.967388259729257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9352028724316126}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8448710102867845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7495400712660193}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7167483277326442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6619304106089692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6619304106089692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5502180689010676}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5129470396572899}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.967388259729257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9352028724316126}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8448710102867845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7495400712660193}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7167483277326442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6619304106089692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6619304106089692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5502180689010676}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5129470396572899}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('papaya peach apricot banana peach cherry papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #344 checking search results for 'papaya peach apricot banana peach cherry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #344 checking search results for 'papaya peach apricot banana peach cherry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking search results for 'peach blueberry orange kiwi cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2896507602133057}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08421842033343047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08411106256078259}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.061958748608844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.061420385712806884}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0420300281629036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.041374048704794816}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03657523340398097}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03063010224108815}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029191762721552498}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2896507602133057}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08421842033343047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08411106256078259}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.061958748608844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.061420385712806884}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0420300281629036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.041374048704794816}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03657523340398097}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03063010224108815}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029191762721552498}]
result = search.search('peach blueberry orange kiwi cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #345 checking search results for 'peach blueberry orange kiwi cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #345 checking search results for 'peach blueberry orange kiwi cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking search results for 'peach blueberry orange kiwi cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8983426606795794}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8943104655398291}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8860046552340322}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.790582866234008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7494354992861497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7070185086651639}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7053868482257737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.662077361348143}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6309872909878983}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4966027289102648}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8983426606795794}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8943104655398291}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8860046552340322}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.790582866234008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7494354992861497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7070185086651639}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7053868482257737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.662077361348143}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6309872909878983}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4966027289102648}]
result = search.search('peach blueberry orange kiwi cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #346 checking search results for 'peach blueberry orange kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #346 checking search results for 'peach blueberry orange kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking search results for 'blueberry blueberry blueberry apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.19226012829354985}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.11589171543608555}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11090179834009874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10929605675283546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07529401145363701}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04297328599924992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04250322318502307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.017570208490198413}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.017135348673580294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017135348673580294}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.19226012829354985}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.11589171543608555}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11090179834009874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10929605675283546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07529401145363701}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04297328599924992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04250322318502307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.017570208490198413}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.017135348673580294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017135348673580294}]
result = search.search('blueberry blueberry blueberry apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #347 checking search results for 'blueberry blueberry blueberry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #347 checking search results for 'blueberry blueberry blueberry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking search results for 'blueberry blueberry blueberry apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.9288783817599077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9288783817599077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9288783817599077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.918717855841267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.918717855841267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.918717855841267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.5962886997659977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.37038486996514214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.37038486996514214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.37038486996514214}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.9288783817599077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9288783817599077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9288783817599077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.918717855841267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.918717855841267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.918717855841267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.5962886997659977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.37038486996514214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.37038486996514214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.37038486996514214}]
result = search.search('blueberry blueberry blueberry apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #348 checking search results for 'blueberry blueberry blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #348 checking search results for 'blueberry blueberry blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking search results for 'coconut pear fig apricot pear fig apple tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.23644152671982258}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1167566980496435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11067014604763242}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04561171630532816}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03327527711639687}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.032620665117418866}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.013020428724910951}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.009939371653105218}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.009914081671950837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.23644152671982258}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1167566980496435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11067014604763242}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04561171630532816}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03327527711639687}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.032620665117418866}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.013020428724910951}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.009939371653105218}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.009914081671950837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut pear fig apricot pear fig apple tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #349 checking search results for 'coconut pear fig apricot pear fig apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #349 checking search results for 'coconut pear fig apricot pear fig apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking search results for 'coconut pear fig apricot pear fig apple tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9859087162132477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9779171696692837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.93026813869827}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7333159079306638}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7051038784124815}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7014520740995228}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.21484201736417882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.2142953680628005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.15887186947995202}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9859087162132477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9779171696692837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.93026813869827}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7333159079306638}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7051038784124815}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7014520740995228}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.21484201736417882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.2142953680628005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.15887186947995202}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut pear fig apricot pear fig apple tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #350 checking search results for 'coconut pear fig apricot pear fig apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #350 checking search results for 'coconut pear fig apricot pear fig apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking search results for 'peach apricot apricot kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30529974367124346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.043731231208801805}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30529974367124346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.043731231208801805}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach apricot apricot kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #351 checking search results for 'peach apricot apricot kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #351 checking search results for 'peach apricot apricot kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking search results for 'peach apricot apricot kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9468774873314472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9218664874536563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9468774873314472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9218664874536563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach apricot apricot kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #352 checking search results for 'peach apricot apricot kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #352 checking search results for 'peach apricot apricot kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking search results for 'banana cherry tomato tomato tomato apple papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26355949310202514}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10456490654278679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05891243358140316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.046263630248160374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04436638168878134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04369024113090721}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029916678785502596}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.018716520633617163}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26355949310202514}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10456490654278679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05891243358140316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.046263630248160374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04436638168878134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04369024113090721}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029916678785502596}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.018716520633617163}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('banana cherry tomato tomato tomato apple papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #353 checking search results for 'banana cherry tomato tomato tomato apple papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #353 checking search results for 'banana cherry tomato tomato tomato apple papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking search results for 'banana cherry tomato tomato tomato apple papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9589904953588361}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9210024052386206}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8789488805847455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8174214219437016}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7188341226264066}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6466565339777288}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.40456229943955613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9589904953588361}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9210024052386206}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8789488805847455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8174214219437016}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7188341226264066}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6466565339777288}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.40456229943955613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('banana cherry tomato tomato tomato apple papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #354 checking search results for 'banana cherry tomato tomato tomato apple papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #354 checking search results for 'banana cherry tomato tomato tomato apple papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking search results for 'apricot orange coconut banana papaya kiwi kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26968988840756297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08491808955263581}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08252081481955789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06983446636787917}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.056667954610484315}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04186369741977265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03322505875891234}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03309066593024871}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03259912898545669}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.028459496470236118}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26968988840756297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08491808955263581}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08252081481955789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06983446636787917}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.056667954610484315}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04186369741977265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03322505875891234}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03309066593024871}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03259912898545669}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.028459496470236118}]
result = search.search('apricot orange coconut banana papaya kiwi kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #355 checking search results for 'apricot orange coconut banana papaya kiwi kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #355 checking search results for 'apricot orange coconut banana papaya kiwi kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking search results for 'apricot orange coconut banana papaya kiwi kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8824983570190663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8364346488578613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7181679989376429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7152630641553368}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.713802194459411}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7046383695052328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6914475766337933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6614088042675796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6151591718500686}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5849113998308185}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8824983570190663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8364346488578613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7181679989376429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7152630641553368}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.713802194459411}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7046383695052328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6914475766337933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6614088042675796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6151591718500686}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5849113998308185}]
result = search.search('apricot orange coconut banana papaya kiwi kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #356 checking search results for 'apricot orange coconut banana papaya kiwi kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #356 checking search results for 'apricot orange coconut banana papaya kiwi kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking search results for 'coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #357 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #357 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking search results for 'coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #358 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #358 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking search results for 'blueberry blueberry blueberry pear blueberry pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3125732146097308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11927765111828038}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11885068285952705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07646829836249702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05023034587255175}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04044789064653138}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03748349045285096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02835486594570122}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3125732146097308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11927765111828038}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11885068285952705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07646829836249702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05023034587255175}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04044789064653138}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03748349045285096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02835486594570122}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('blueberry blueberry blueberry pear blueberry pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #359 checking search results for 'blueberry blueberry blueberry pear blueberry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #359 checking search results for 'blueberry blueberry blueberry pear blueberry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking search results for 'blueberry blueberry blueberry pear blueberry pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9990318751288563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9990318751288563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9694359271244051}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8742913262441127}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7901623788336771}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6128975567547194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6128975567547194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6128975567547194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9990318751288563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9990318751288563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9694359271244051}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8742913262441127}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7901623788336771}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6128975567547194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6128975567547194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6128975567547194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('blueberry blueberry blueberry pear blueberry pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #360 checking search results for 'blueberry blueberry blueberry pear blueberry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #360 checking search results for 'blueberry blueberry blueberry pear blueberry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking search results for 'pear pear papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3135742490834199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1156991260771975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11111155576011718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0472353562381398}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.043054564803884574}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.029991475079910523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01693008958294677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01693008958294677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3135742490834199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1156991260771975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11111155576011718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0472353562381398}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.043054564803884574}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.029991475079910523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01693008958294677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01693008958294677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('pear pear papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #361 checking search results for 'pear pear papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #361 checking search results for 'pear pear papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking search results for 'pear pear papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9957344153189959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9725406038456526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9725406038456524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.930635243558229}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.930635243558229}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3659481431122665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3659481431122665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3659481431122665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9957344153189959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9725406038456526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9725406038456524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.930635243558229}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.930635243558229}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3659481431122665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3659481431122665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3659481431122665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('pear pear papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #362 checking search results for 'pear pear papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #362 checking search results for 'pear pear papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking search results for 'kiwi pear blueberry blueberry lime blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2707836400521829}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11807609548115268}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11273652058522356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08511478767915298}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04045647770261999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03626527215949253}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03566971143556184}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03165764426897846}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2707836400521829}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11807609548115268}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11273652058522356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08511478767915298}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04045647770261999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03626527215949253}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03566971143556184}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03165764426897846}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi pear blueberry blueberry lime blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #363 checking search results for 'kiwi pear blueberry blueberry lime blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #363 checking search results for 'kiwi pear blueberry blueberry lime blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking search results for 'kiwi pear blueberry blueberry lime blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9889680251957201}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.947637614239678}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8398268849487557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7838829760000209}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7710097812088625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6821996373576174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6673519248510581}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.49363937094423055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9889680251957201}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.947637614239678}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8398268849487557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7838829760000209}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7710097812088625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6821996373576174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6673519248510581}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.49363937094423055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi pear blueberry blueberry lime blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #364 checking search results for 'kiwi pear blueberry blueberry lime blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #364 checking search results for 'kiwi pear blueberry blueberry lime blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking search results for 'cherry cherry orange' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30410453060045656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11845614447037095}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0473495898907584}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04616740349270843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04514557300037436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03996407579289812}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.03967544792093144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.01537382076912689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30410453060045656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11845614447037095}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0473495898907584}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04616740349270843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04514557300037436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03996407579289812}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.03967544792093144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.01537382076912689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry cherry orange',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #365 checking search results for 'cherry cherry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #365 checking search results for 'cherry cherry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking search results for 'cherry cherry orange' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9981424924112162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9979200344863607}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9957154749429625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9758329114730363}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.943170571840188}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8638335465359909}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.3323090014047961}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.3323090014047961}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9981424924112162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9979200344863607}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9957154749429625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9758329114730363}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.943170571840188}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8638335465359909}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.3323090014047961}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.3323090014047961}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry cherry orange',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #366 checking search results for 'cherry cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #366 checking search results for 'cherry cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking search results for 'lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #367 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #367 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking search results for 'lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #368 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #368 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking search results for 'banana papaya pear papaya coconut apricot apple cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.24912985611158373}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08792846069702763}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06848679580667598}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05970901325251119}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03958670899067879}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03843754500331212}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03514211466471073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02565314461259963}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01885589106147763}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.24912985611158373}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08792846069702763}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06848679580667598}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05970901325251119}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03958670899067879}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03843754500331212}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03514211466471073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02565314461259963}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01885589106147763}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('banana papaya pear papaya coconut apricot apple cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #369 checking search results for 'banana papaya pear papaya coconut apricot apple cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #369 checking search results for 'banana papaya pear papaya coconut apricot apple cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking search results for 'banana papaya pear papaya coconut apricot apple cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.83449880916552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8308371996994455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7726683597487758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7596056443518746}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7391066913024804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7285537796524868}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5736237375135947}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5544991708388406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4075748262800328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.83449880916552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8308371996994455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7726683597487758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7596056443518746}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7391066913024804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7285537796524868}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5736237375135947}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5544991708388406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4075748262800328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('banana papaya pear papaya coconut apricot apple cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #370 checking search results for 'banana papaya pear papaya coconut apricot apple cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #370 checking search results for 'banana papaya pear papaya coconut apricot apple cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking search results for 'pear fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #371 checking search results for 'pear fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #371 checking search results for 'pear fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking search results for 'pear fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #372 checking search results for 'pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #372 checking search results for 'pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking search results for 'orange cherry banana pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.303545817210137}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0997478358630912}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08285773089971668}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045769439068815074}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03868454780213231}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029412029356386267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029055842463021758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.028030888547907855}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.303545817210137}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0997478358630912}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08285773089971668}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045769439068815074}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03868454780213231}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029412029356386267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029055842463021758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.028030888547907855}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange cherry banana pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #373 checking search results for 'orange cherry banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #373 checking search results for 'orange cherry banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking search results for 'orange cherry banana pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9648324746594473}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9414377399524093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8384576773541135}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.836176227300506}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6939901439506108}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6357484096820485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6280493404249688}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6058947038429281}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9648324746594473}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9414377399524093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8384576773541135}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.836176227300506}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6939901439506108}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6357484096820485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6280493404249688}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6058947038429281}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange cherry banana pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #374 checking search results for 'orange cherry banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #374 checking search results for 'orange cherry banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking search results for 'peach blueberry papaya blueberry papaya orange lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2766084397879849}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10137378497396561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07021224225884302}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06873260002831863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05670659986264524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03575649781870375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03541762120572268}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.030679300077010703}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.030272500216637646}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.028568105204840818}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2766084397879849}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10137378497396561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07021224225884302}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06873260002831863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05670659986264524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03575649781870375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03541762120572268}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.030679300077010703}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.030272500216637646}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.028568105204840818}]
result = search.search('peach blueberry papaya blueberry papaya orange lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #375 checking search results for 'peach blueberry papaya blueberry papaya orange lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #375 checking search results for 'peach blueberry papaya blueberry papaya orange lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking search results for 'peach blueberry papaya blueberry papaya orange lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8578923168804123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8567114358300801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8521250366828003}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7655607875071807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7537568949382409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.66314078494155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6543477036768295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6175067769563285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5756825159197752}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4545064719882419}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8578923168804123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8567114358300801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8521250366828003}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7655607875071807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7537568949382409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.66314078494155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6543477036768295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6175067769563285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5756825159197752}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4545064719882419}]
result = search.search('peach blueberry papaya blueberry papaya orange lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #376 checking search results for 'peach blueberry papaya blueberry papaya orange lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #376 checking search results for 'peach blueberry papaya blueberry papaya orange lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking search results for 'kiwi blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303063}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1137004238652347}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040058048374050796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303063}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1137004238652347}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040058048374050796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #377 checking search results for 'kiwi blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #377 checking search results for 'kiwi blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking search results for 'kiwi blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.951275576479978}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8658647875053789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.951275576479978}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8658647875053789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #378 checking search results for 'kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #378 checking search results for 'kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking search results for 'coconut peach blueberry pear coconut orange cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3060225112377297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08966779613175571}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0836255787117547}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04180856349748271}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.038761117406368124}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03359196820952768}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03129658215367397}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.031129317290606764}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029824814791227176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02956381628008171}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3060225112377297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08966779613175571}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0836255787117547}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04180856349748271}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.038761117406368124}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03359196820952768}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03129658215367397}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.031129317290606764}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029824814791227176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02956381628008171}]
result = search.search('coconut peach blueberry pear coconut orange cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #379 checking search results for 'coconut peach blueberry pear coconut orange cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #379 checking search results for 'coconut peach blueberry pear coconut orange cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking search results for 'coconut peach blueberry pear coconut orange cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9491191280516443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8813361186398563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7510290961325848}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7260988389656999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7029376415774051}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6728680201624384}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6446708706438603}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6390293222019102}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4729530275527643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.25084380256286076}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9491191280516443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8813361186398563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7510290961325848}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7260988389656999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7029376415774051}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6728680201624384}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6446708706438603}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6390293222019102}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4729530275527643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.25084380256286076}]
result = search.search('coconut peach blueberry pear coconut orange cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #380 checking search results for 'coconut peach blueberry pear coconut orange cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #380 checking search results for 'coconut peach blueberry pear coconut orange cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking search results for 'apple kiwi peach orange' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.24969392759280867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08863101210183807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07421295274288325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07073407693315358}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05293644979318099}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04419308079342766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.043006368990792264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03982568175487237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02654441752681524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026476877259438526}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.24969392759280867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08863101210183807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07421295274288325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07073407693315358}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05293644979318099}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04419308079342766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.043006368990792264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03982568175487237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02654441752681524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026476877259438526}]
result = search.search('apple kiwi peach orange',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #381 checking search results for 'apple kiwi peach orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #381 checking search results for 'apple kiwi peach orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking search results for 'apple kiwi peach orange' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9552445529322672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9065861907793238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9055270598987002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.860842124607288}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7744178095858276}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7423453210598753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5945746024661789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5737642589746998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5723043591135254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.42428851480003094}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9552445529322672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9065861907793238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9055270598987002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.860842124607288}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7744178095858276}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7423453210598753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5945746024661789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5737642589746998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5723043591135254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.42428851480003094}]
result = search.search('apple kiwi peach orange',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #382 checking search results for 'apple kiwi peach orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #382 checking search results for 'apple kiwi peach orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking search results for 'apple lime coconut coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29912071311965366}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10328873688567684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08413404080783252}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04371133850315848}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.041668251699880844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03667881311539609}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034685483982953125}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03452144138404044}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.028414951463605887}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29912071311965366}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10328873688567684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08413404080783252}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04371133850315848}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.041668251699880844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03667881311539609}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034685483982953125}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03452144138404044}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.028414951463605887}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple lime coconut coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #383 checking search results for 'apple lime coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #383 checking search results for 'apple lime coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking search results for 'apple lime coconut coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9277134197417478}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9006697372508451}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8651137872279427}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.773199557296108}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7497354573538327}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7461896353326738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7072116585965328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6141963203316883}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5333543320414198}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9277134197417478}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9006697372508451}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8651137872279427}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.773199557296108}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7497354573538327}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7461896353326738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7072116585965328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6141963203316883}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5333543320414198}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple lime coconut coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #384 checking search results for 'apple lime coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #384 checking search results for 'apple lime coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking search results for 'lime apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3074633155170225}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10265342611740245}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07116834968915606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04274693519677292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3074633155170225}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10265342611740245}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07116834968915606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04274693519677292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('lime apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #385 checking search results for 'lime apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #385 checking search results for 'lime apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking search results for 'lime apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9535877368991585}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9011172544194608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8683776088944807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8628814098079822}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9535877368991585}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9011172544194608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8683776088944807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8628814098079822}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('lime apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #386 checking search results for 'lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #386 checking search results for 'lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking search results for 'banana banana blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('banana banana blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #387 checking search results for 'banana banana blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #387 checking search results for 'banana banana blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking search results for 'banana banana blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('banana banana blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #388 checking search results for 'banana banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #388 checking search results for 'banana banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
