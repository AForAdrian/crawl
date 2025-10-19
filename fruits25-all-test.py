
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html')


output = open('fruits25-all-outgoing-failed.txt', 'w')
success_output = open('fruits25-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = None
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits25-all-incoming-failed.txt', 'w')
success_output = open('fruits25-all-incoming-passed.txt', 'w')

#Test #26 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #50 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits25-all-pagerank-failed.txt', 'w')
success_output = open('fruits25-all-pagerank-passed.txt', 'w')

#Test #52 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html
expected = 0.028174759999999986
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html
expected = 0.051696559999999975
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html
expected = 0.03159579999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html
expected = 0.033838480000000004
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html
expected = 0.03692783999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html
expected = 0.03434247999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html
expected = 0.021270039999999987
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html
expected = 0.051393999999999995
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html
expected = 0.04550911999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html
expected = 0.03690907999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html
expected = 0.04014835999999998
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html
expected = 0.03686656
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html
expected = 0.033533439999999984
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html
expected = 0.04654291999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html
expected = 0.0414408
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html
expected = 0.05466807999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html
expected = 0.043232999999999994
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html
expected = 0.01904219999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html
expected = 0.03892039999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html
expected = 0.028309039999999987
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html
expected = 0.04810359999999998
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html
expected = 0.048347039999999994
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html
expected = 0.05204075999999999
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html
expected = 0.05083659999999998
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html
expected = 0.04630903999999998
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits25-all-idf-failed.txt', 'w')
success_output = open('fruits25-all-idf-passed.txt', 'w')

#Test #78 checking IDF for word kiwi
expected = 0.12029423371771174
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking IDF for word cherry
expected = 0.0
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking IDF for word papaya
expected = 0.0
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking IDF for word pear
expected = 0.05889368905356862
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking IDF for word coconut
expected = 0.12029423371771174
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking IDF for word apricot
expected = 0.05889368905356862
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking IDF for word fig
expected = 0.12029423371771174
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking IDF for word banana
expected = 0.18442457113742758
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking IDF for word blueberry
expected = 0.05889368905356862
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking IDF for word peach
expected = 0.0
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking IDF for word lime
expected = 0.0
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking IDF for word strawberry
expected = 0.0
result = searchdata.get_idf('strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking IDF for word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking IDF for word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking IDF for word apple
expected = 0.12029423371771174
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking IDF for word tomato
expected = 0
result = searchdata.get_idf('tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking IDF for word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking IDF for word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits25-all-tf-failed.txt', 'w')
success_output = open('fruits25-all-tf-passed.txt', 'w')

#Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word blueberry
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word fig
expected = 0.10909090909090909
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word coconut
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apricot
expected = 0.07272727272727272
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word peach
expected = 0.01818181818181818
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word papaya
expected = 0.07272727272727272
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word kiwi
expected = 0.05454545454545454
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word banana
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word pear
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word cherry
expected = 0.05454545454545454
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word blueberry
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word fig
expected = 0.16666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word coconut
expected = 0.03333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word apricot
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word peach
expected = 0.016666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word papaya
expected = 0.05
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word kiwi
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word banana
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word pear
expected = 0.15
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word cherry
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word blueberry
expected = 0.09259259259259259
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word fig
expected = 0.09259259259259259
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word coconut
expected = 0.07407407407407407
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word apricot
expected = 0.018518518518518517
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word peach
expected = 0.018518518518518517
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word papaya
expected = 0.09259259259259259
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word kiwi
expected = 0.07407407407407407
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word banana
expected = 0.09259259259259259
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word pear
expected = 0.18518518518518517
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word cherry
expected = 0.07407407407407407
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word blueberry
expected = 0.07407407407407407
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word fig
expected = 0.09259259259259259
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word coconut
expected = 0.09259259259259259
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word apricot
expected = 0.07407407407407407
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word peach
expected = 0.05555555555555555
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word papaya
expected = 0.14814814814814814
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word kiwi
expected = 0.07407407407407407
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word banana
expected = 0.16666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word pear
expected = 0.09259259259259259
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word cherry
expected = 0.037037037037037035
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word blueberry
expected = 0.06896551724137931
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word fig
expected = 0.1724137931034483
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word coconut
expected = 0.034482758620689655
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word apricot
expected = 0.10344827586206896
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word peach
expected = 0.034482758620689655
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word papaya
expected = 0.13793103448275862
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word kiwi
expected = 0.034482758620689655
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word banana
expected = 0.06896551724137931
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word pear
expected = 0.06896551724137931
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word cherry
expected = 0.10344827586206896
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word blueberry
expected = 0.13636363636363635
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word fig
expected = 0.13636363636363635
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word coconut
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word apricot
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word peach
expected = 0.045454545454545456
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word papaya
expected = 0.045454545454545456
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #152 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #152 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word kiwi
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word banana
expected = 0.18181818181818182
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word pear
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word cherry
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word blueberry
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word fig
expected = 0.09375
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word coconut
expected = 0.09375
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word apricot
expected = 0.21875
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word peach
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word papaya
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word kiwi
expected = 0.03125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word pear
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word cherry
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word blueberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word coconut
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word apricot
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word peach
expected = 0.2
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word papaya
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word kiwi
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word pear
expected = 0.2
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word cherry
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word blueberry
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word fig
expected = 0.1
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word coconut
expected = 0.06
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apricot
expected = 0.06
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word peach
expected = 0.06
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word papaya
expected = 0.12
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word kiwi
expected = 0.08
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word banana
expected = 0.06
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word pear
expected = 0.14
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word cherry
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word blueberry
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word coconut
expected = 0.08
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word apricot
expected = 0.12
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word peach
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word papaya
expected = 0.16
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word kiwi
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word banana
expected = 0.08
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word pear
expected = 0.08
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word cherry
expected = 0.12
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits25-all-tfidf-failed.txt', 'w')
success_output = open('fruits25-all-tfidf-passed.txt', 'w')

#Test #213 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word kiwi
expected = 0.01240155273739913
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word blueberry
expected = 0.006071556118074172
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word apricot
expected = 0.006071556118074172
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word coconut
expected = 0.015368255653415196
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word banana
expected = 0.04101462692918852
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word apple
expected = 0.00938325240924977
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word fig
expected = 0.015368255653415196
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word kiwi
expected = 0.006675742044297133
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word blueberry
expected = 0.006415547005497948
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word apricot
expected = 0.007946500733719867
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word coconut
expected = 0.006675742044297133
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word banana
expected = 0.015208048528470469
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word apple
expected = 0.016231250442311055
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word fig
expected = 0.009919722371000582
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word kiwi
expected = 0.009217098356891351
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word blueberry
expected = 0.007392976736066969
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apricot
expected = 0.005964949287103142
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word coconut
expected = 0.015100641268186226
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word banana
expected = 0.023150979092818654
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apple
expected = 0.012183801272907425
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word fig
expected = 0.01796926681825092
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word kiwi
expected = 0.018951307193998384
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word blueberry
expected = 0.007800486549069939
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word apricot
expected = 0.007800486549069939
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word coconut
expected = 0.012861282527909692
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word banana
expected = 0.01004150921771007
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word apple
expected = 0.006549754456599251
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word fig
expected = 0.0033057741298957635
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word kiwi
expected = 0.00738613147022325
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word blueberry
expected = 0.003616104585169806
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apricot
expected = 0.007084571195508225
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apple
expected = 0.00738613147022325
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word fig
expected = 0.021277374851608032
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word kiwi
expected = 0.005030725989125216
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word blueberry
expected = 0.00832496743137005
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apricot
expected = 0.003668150916437207
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word coconut
expected = 0.021571607012108827
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word banana
expected = 0.018878015874743782
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apple
expected = 0.017004293566508805
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word fig
expected = 0.009919722371000582
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word kiwi
expected = 0.013356426642475827
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word blueberry
expected = 0.008098089771498661
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apricot
expected = 0.004950854670969278
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word coconut
expected = 0.010112446315772362
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word banana
expected = 0.015503515981597573
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apple
expected = 0.01654088102298361
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word fig
expected = 0.01654088102298361
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word kiwi
expected = 0.01240155273739913
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word blueberry
expected = 0.0075239954715694704
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word apricot
expected = 0.00155904618446634
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word coconut
expected = 0.01240155273739913
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word banana
expected = 0.023561262002487267
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word fig
expected = 0.015368255653415196
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word kiwi
expected = 0.010211644886310885
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word blueberry
expected = 0.0062046268314725535
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word apricot
expected = 0.010861443346405389
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word coconut
expected = 0.012673358422452536
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word banana
expected = 0.019429681870009544
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word apple
expected = 0.007714509797962978
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word fig
expected = 0.007714509797962978
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word kiwi
expected = 0.01389124338138478
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word blueberry
expected = 0.005483556310194886
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word apricot
expected = 0.006800879335501042
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word coconut
expected = 0.005690604709731066
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word banana
expected = 0.021296836298815156
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word apple
expected = 0.011200524453185806
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word fig
expected = 0.0267525259092945
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits25-all-search-failed.txt', 'w')
success_output = open('fruits25-all-search-passed.txt', 'w')

#Test #334 checking search results for 'apple cherry peach cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.05204075999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.05204075999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}]
result = search.search('apple cherry peach cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #334 checking search results for 'apple cherry peach cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #334 checking search results for 'apple cherry peach cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking search results for 'apple cherry peach cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}]
result = search.search('apple cherry peach cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #335 checking search results for 'apple cherry peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #335 checking search results for 'apple cherry peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking search results for 'blueberry pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.051929962666491934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05169655999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05139400000000001}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.050699879618620554}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048166765008811306}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045961165162451634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04345688493403583}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04123863362820064}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.040013625721926176}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.051929962666491934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05169655999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05139400000000001}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.050699879618620554}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048166765008811306}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045961165162451634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04345688493403583}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04123863362820064}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.040013625721926176}]
result = search.search('blueberry pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #336 checking search results for 'blueberry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #336 checking search results for 'blueberry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking search results for 'blueberry pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9973105915545212}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.99627123002383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9943418535113956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.987776116459863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9875006802850282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9874700455811329}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9973105915545212}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.99627123002383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9943418535113956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.987776116459863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9875006802850282}]
result = search.search('blueberry pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #337 checking search results for 'blueberry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #337 checking search results for 'blueberry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking search results for 'pear fig banana lime blueberry peach fig coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04522850030565583}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.045181891164934956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04475144975618511}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04438366972114811}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04356979924467028}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.04324185617764523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04076800203357316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.040330403434391524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.03978363251128147}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03755019458999331}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04522850030565583}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.045181891164934956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04475144975618511}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04438366972114811}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04356979924467028}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.04324185617764523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04076800203357316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.040330403434391524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.03978363251128147}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03755019458999331}]
result = search.search('pear fig banana lime blueberry peach fig coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #338 checking search results for 'pear fig banana lime blueberry peach fig coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #338 checking search results for 'pear fig banana lime blueberry peach fig coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking search results for 'pear fig banana lime blueberry peach fig coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 0.9836257305076145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9752697859494561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 0.9736435780470271}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9663653091531401}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9652968524359787}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9354967813056567}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9328615510001973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9309750368367661}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 0.9200099189599423}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9092576494689424}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 0.9836257305076145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9752697859494561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 0.9736435780470271}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9663653091531401}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9652968524359787}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9354967813056567}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9328615510001973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9309750368367661}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 0.9200099189599423}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9092576494689424}]
result = search.search('pear fig banana lime blueberry peach fig coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #339 checking search results for 'pear fig banana lime blueberry peach fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #339 checking search results for 'pear fig banana lime blueberry peach fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking search results for 'papaya papaya coconut tomato cherry tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.0414408}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.0414408}]
result = search.search('papaya papaya coconut tomato cherry tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #340 checking search results for 'papaya papaya coconut tomato cherry tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #340 checking search results for 'papaya papaya coconut tomato cherry tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking search results for 'papaya papaya coconut tomato cherry tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}]
result = search.search('papaya papaya coconut tomato cherry tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #341 checking search results for 'papaya papaya coconut tomato cherry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #341 checking search results for 'papaya papaya coconut tomato cherry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking search results for 'lime blueberry peach apple strawberry papaya coconut pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05259504143088997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05133505410046151}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.050169521925575784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.046351714349082855}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04527071048499736}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.044852366354592096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.044628309812058974}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04117224111929526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03969171012301267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03726007916532562}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.0363599988879816}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05259504143088997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05133505410046151}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.050169521925575784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.046351714349082855}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04527071048499736}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.044852366354592096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.044628309812058974}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04117224111929526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03969171012301267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03726007916532562}]
result = search.search('lime blueberry peach apple strawberry papaya coconut pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #342 checking search results for 'lime blueberry peach apple strawberry papaya coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #342 checking search results for 'lime blueberry peach apple strawberry papaya coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking search results for 'lime blueberry peach apple strawberry papaya coconut pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9947612804861392}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9930071575451352}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.9886259394658384}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.984622953521831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9810069293349368}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9761746882043777}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9759552593832016}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.963351362861927}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9626639405040823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9620795431427258}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9947612804861392}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9930071575451352}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.9886259394658384}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.984622953521831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9810069293349368}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9761746882043777}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9759552593832016}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.963351362861927}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9626639405040823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9620795431427258}]
result = search.search('lime blueberry peach apple strawberry papaya coconut pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #343 checking search results for 'lime blueberry peach apple strawberry papaya coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #343 checking search results for 'lime blueberry peach apple strawberry papaya coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking search results for 'banana lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.0414408}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.04014835999999998}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.0414408}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.04014835999999998}]
result = search.search('banana lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #344 checking search results for 'banana lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #344 checking search results for 'banana lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking search results for 'banana lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}]
result = search.search('banana lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #345 checking search results for 'banana lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #345 checking search results for 'banana lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking search results for 'papaya papaya apricot blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05019887292678222}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04819116659835767}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04807386859588193}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04641825080902632}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.046045052148472654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04582062966758875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.045711549723756954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.045394170478997714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.045251274062835745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.037365449208915276}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 0.037024025946831324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.03686656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.036469398694027204}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05019887292678222}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04819116659835767}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04807386859588193}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04641825080902632}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.046045052148472654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04582062966758875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.045711549723756954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.045394170478997714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.045251274062835745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.037365449208915276}]
result = search.search('papaya papaya apricot blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #346 checking search results for 'papaya papaya apricot blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #346 checking search results for 'papaya papaya apricot blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking search results for 'papaya papaya apricot blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9973214144928236}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9943664858848036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9943497801702429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9943341919781299}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9942994315682785}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9875854827692931}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9874553555269675}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9973214144928236}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9943664858848036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9943497801702429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9943341919781299}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9942994315682785}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9875854827692931}]
result = search.search('papaya papaya apricot blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #347 checking search results for 'papaya papaya apricot blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #347 checking search results for 'papaya papaya apricot blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking search results for 'peach fig cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}]
result = search.search('peach fig cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #348 checking search results for 'peach fig cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #348 checking search results for 'peach fig cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking search results for 'peach fig cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}]
result = search.search('peach fig cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #349 checking search results for 'peach fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #349 checking search results for 'peach fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking search results for 'coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.0414408}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.0414408}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #350 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #350 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking search results for 'coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #351 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #351 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking search results for 'coconut strawberry blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05171894330321509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05150119400176816}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.050923355110252325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05074294583254139}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.046489401052547355}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.044198220140763224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.044079080371258114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043057819763514305}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03925987906316398}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05171894330321509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05150119400176816}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.050923355110252325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05074294583254139}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.046489401052547355}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.044198220140763224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.044079080371258114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043057819763514305}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03925987906316398}]
result = search.search('coconut strawberry blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #352 checking search results for 'coconut strawberry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #352 checking search results for 'coconut strawberry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking search results for 'coconut strawberry blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9988501162485587}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9981577413230115}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9968789981339107}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9962209091237055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.995960388277313}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9959479972131083}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9908424156565422}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9988501162485587}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9981577413230115}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9968789981339107}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9962209091237055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.995960388277313}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9959479972131083}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9908424156565422}]
result = search.search('coconut strawberry blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #353 checking search results for 'coconut strawberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #353 checking search results for 'coconut strawberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking search results for 'blueberry banana kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.0522118022309382}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04978178796192654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.048883325642839856}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04788029043837449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.046253584347342586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04466003392489346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04401600304338446}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04305332865174969}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.039456614012482516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03865448508411825}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.0522118022309382}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04978178796192654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.048883325642839856}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04788029043837449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.046253584347342586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04466003392489346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04401600304338446}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04305332865174969}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.039456614012482516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03865448508411825}]
result = search.search('blueberry banana kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #354 checking search results for 'blueberry banana kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #354 checking search results for 'blueberry banana kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking search results for 'blueberry banana kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9988024875346715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9967700451445808}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9965849123557543}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9958441156466055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9957895568039716}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9903458503017867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9853872223536856}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9821119633489395}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.981342507279716}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.979250932633704}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9988024875346715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9967700451445808}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9965849123557543}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9958441156466055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9957895568039716}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9903458503017867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9853872223536856}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9821119633489395}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.981342507279716}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.979250932633704}]
result = search.search('blueberry banana kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #355 checking search results for 'blueberry banana kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #355 checking search results for 'blueberry banana kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking search results for 'lime cherry strawberry pear kiwi apricot peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.053336667075587346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04909708731409667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04646704220516171}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.04554807026273179}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04497603964864005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.044574989924680945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.044542269116208115}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.041360464223792394}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04053541297723484}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03766185980945791}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.03700648922529201}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.053336667075587346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04909708731409667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04646704220516171}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.04554807026273179}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04497603964864005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.044574989924680945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.044542269116208115}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.041360464223792394}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04053541297723484}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03766185980945791}]
result = search.search('lime cherry strawberry pear kiwi apricot peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #356 checking search results for 'lime cherry strawberry pear kiwi apricot peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #356 checking search results for 'lime cherry strawberry pear kiwi apricot peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking search results for 'lime cherry strawberry pear kiwi apricot peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.9969256401575233}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9964190227102654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9837590386468409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9836950229933694}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9787547884074251}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9781522793294252}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9768083864611802}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9756455151815714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9712151158529753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9657822772194972}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9655019373018571}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.9969256401575233}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9964190227102654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9837590386468409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9836950229933694}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9787547884074251}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9781522793294252}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9768083864611802}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9756455151815714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9712151158529753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9657822772194972}]
result = search.search('lime cherry strawberry pear kiwi apricot peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #357 checking search results for 'lime cherry strawberry pear kiwi apricot peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #357 checking search results for 'lime cherry strawberry pear kiwi apricot peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking search results for 'apricot cherry coconut kiwi strawberry papaya fig pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.052336217885692066}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04627248809040176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04602199357769026}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04537409779668065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04533049432367202}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04420820684004182}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.041059659676150904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04100326514835576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04050107463803155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.039883371551958764}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.052336217885692066}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04627248809040176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04602199357769026}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04537409779668065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04533049432367202}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04420820684004182}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.041059659676150904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04100326514835576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04050107463803155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.039883371551958764}]
result = search.search('apricot cherry coconut kiwi strawberry papaya fig pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #358 checking search results for 'apricot cherry coconut kiwi strawberry papaya fig pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #358 checking search results for 'apricot cherry coconut kiwi strawberry papaya fig pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking search results for 'apricot cherry coconut kiwi strawberry papaya fig pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9951082353332426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9857326407408946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9714142316977746}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9688742280741598}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9683944888776753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9624179927018485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9573450884993964}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9519092291418516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9468733620213932}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9368092576973968}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9951082353332426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9857326407408946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9714142316977746}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9688742280741598}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9683944888776753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9624179927018485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9573450884993964}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9519092291418516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9468733620213932}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9368092576973968}]
result = search.search('apricot cherry coconut kiwi strawberry papaya fig pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #359 checking search results for 'apricot cherry coconut kiwi strawberry papaya fig pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #359 checking search results for 'apricot cherry coconut kiwi strawberry papaya fig pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking search results for 'pear blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.051929962666491934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05169655999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05139400000000001}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.050699879618620554}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048166765008811306}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045961165162451634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04345688493403583}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04123863362820064}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.040013625721926176}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.051929962666491934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05169655999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05139400000000001}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.050699879618620554}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048166765008811306}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045961165162451634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04345688493403583}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04123863362820064}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.040013625721926176}]
result = search.search('pear blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #360 checking search results for 'pear blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #360 checking search results for 'pear blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking search results for 'pear blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9973105915545212}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.99627123002383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9943418535113956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.987776116459863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9875006802850282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9874700455811329}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9973105915545212}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.99627123002383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9943418535113956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.987776116459863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9875006802850282}]
result = search.search('pear blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #361 checking search results for 'pear blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #361 checking search results for 'pear blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking search results for 'apple papaya fig pear strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05184287771388114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.050490664462890966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05010006876084221}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04723921537343667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04711282509165634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045841140990333186}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04477927162346076}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.043299432394671225}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04321402059391161}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04121512921577831}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05184287771388114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.050490664462890966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05010006876084221}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04723921537343667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04711282509165634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045841140990333186}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04477927162346076}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.043299432394671225}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04321402059391161}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04121512921577831}]
result = search.search('apple papaya fig pear strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #362 checking search results for 'apple papaya fig pear strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #362 checking search results for 'apple papaya fig pear strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking search results for 'apple papaya fig pear strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9945543815702956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9938539398434274}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9892554251554558}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9849218955392829}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9839625908710334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9824233269037431}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9823047303084048}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9744717585948663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9736216127916275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9691180372706083}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9945543815702956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9938539398434274}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9892554251554558}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9849218955392829}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9839625908710334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9824233269037431}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9823047303084048}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9744717585948663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9736216127916275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9691180372706083}]
result = search.search('apple papaya fig pear strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #363 checking search results for 'apple papaya fig pear strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #363 checking search results for 'apple papaya fig pear strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking search results for 'peach kiwi apple blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05304308030943956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.04917731130572412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04754508332399261}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.046042389813208386}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.0460420076636253}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04482905544099776}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.0446966904923344}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04295825379285634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04260319744429965}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 0.038920399999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03877057288364743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.038073525133732085}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05304308030943956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.04917731130572412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04754508332399261}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.046042389813208386}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.0460420076636253}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04482905544099776}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.0446966904923344}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04295825379285634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04260319744429965}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 0.038920399999999994}]
result = search.search('peach kiwi apple blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #364 checking search results for 'peach kiwi apple blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #364 checking search results for 'peach kiwi apple blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking search results for 'peach kiwi apple blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9945628043247475}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9944965113037563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9942336887921953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9909124095302718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9850565214400491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9848966679093047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9834124968972789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9702751644001321}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9615734572102567}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9945628043247475}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9944965113037563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9942336887921953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9909124095302718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9850565214400491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9848966679093047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9834124968972789}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9702751644001321}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9615734572102567}]
result = search.search('peach kiwi apple blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #365 checking search results for 'peach kiwi apple blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #365 checking search results for 'peach kiwi apple blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking search results for 'coconut blueberry lime strawberry papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05171894330321508}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05150119400176816}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05092335511025231}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.050742945832541374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04648940105254735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.044198220140763224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04407908037125811}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043057819763514305}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03925987906316397}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05171894330321508}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05150119400176816}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05092335511025231}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.050742945832541374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04648940105254735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.044198220140763224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04407908037125811}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043057819763514305}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03925987906316397}]
result = search.search('coconut blueberry lime strawberry papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #366 checking search results for 'coconut blueberry lime strawberry papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #366 checking search results for 'coconut blueberry lime strawberry papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking search results for 'coconut blueberry lime strawberry papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9988501162485586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9981577413230113}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9968789981339106}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9962209091237054}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.995960388277313}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9959479972131082}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.990842415656542}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9988501162485586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9981577413230113}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9968789981339106}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9962209091237054}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.995960388277313}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9959479972131082}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.990842415656542}]
result = search.search('coconut blueberry lime strawberry papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #367 checking search results for 'coconut blueberry lime strawberry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #367 checking search results for 'coconut blueberry lime strawberry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking search results for 'apricot strawberry apple pear tomato apple tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.0524586492231755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.050628890693909155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04678887682762698}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04664684710852247}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.044332930094204734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.043289205882234914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04274448620148616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04212071693329597}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04065586127222697}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.03946721541187319}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.0524586492231755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.050628890693909155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04678887682762698}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04664684710852247}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.044332930094204734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.043289205882234914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04274448620148616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04212071693329597}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04065586127222697}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.03946721541187319}]
result = search.search('apricot strawberry apple pear tomato apple tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #368 checking search results for 'apricot strawberry apple pear tomato apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #368 checking search results for 'apricot strawberry apple pear tomato apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking search results for 'apricot strawberry apple pear tomato apple tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9910132000696328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9810587940442022}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9806947953514016}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9793473819903913}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.9697163436525018}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 0.9697104343376535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9595846282359928}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9512204560807794}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9467680208070687}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9394782107954819}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9910132000696328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9810587940442022}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9806947953514016}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9793473819903913}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.9697163436525018}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 0.9697104343376535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9595846282359928}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9512204560807794}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9467680208070687}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9394782107954819}]
result = search.search('apricot strawberry apple pear tomato apple tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #369 checking search results for 'apricot strawberry apple pear tomato apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #369 checking search results for 'apricot strawberry apple pear tomato apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking search results for 'apricot pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05064335114142774}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05045819083631697}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04819116659835767}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04748346021953028}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04636660316337297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.045394170478997714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.045251274062835745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.044689006320666295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04028413692706494}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.039434628413168415}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05064335114142774}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05045819083631697}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04819116659835767}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04748346021953028}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04636660316337297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.045394170478997714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.045251274062835745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.044689006320666295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04028413692706494}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.039434628413168415}]
result = search.search('apricot pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #370 checking search results for 'apricot pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #370 checking search results for 'apricot pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking search results for 'apricot pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9962117366803153}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9961986273949823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9943418535113956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9943341919781299}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9930848869471629}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9877519752327256}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 0.9823511181444726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.9822226465332191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.982137897574087}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 0.9820145511359454}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9962117366803153}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9961986273949823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9943418535113956}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9943341919781299}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9930848869471629}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9877519752327256}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 0.9823511181444726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.9822226465332191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.982137897574087}]
result = search.search('apricot pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #371 checking search results for 'apricot pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #371 checking search results for 'apricot pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking search results for 'pear tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.05204075999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.05204075999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}]
result = search.search('pear tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #372 checking search results for 'pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #372 checking search results for 'pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking search results for 'pear tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}]
result = search.search('pear tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #373 checking search results for 'pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #373 checking search results for 'pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking search results for 'banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.0414408}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.04014835999999998}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.0414408}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.04014835999999998}]
result = search.search('banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #374 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #374 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking search results for 'banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #375 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #375 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking search results for 'apricot lime kiwi fig banana strawberry apricot apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05050262405392998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04767608267683935}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04740975604488055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.044717444146014404}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.044682522974983666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04371558256633312}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.043081548141570315}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03999933258935759}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.037677435205944854}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03682215005140179}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.0363884598673572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.03620005955227505}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.035900785713746754}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05050262405392998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04767608267683935}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04740975604488055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.044717444146014404}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.044682522974983666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04371558256633312}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.043081548141570315}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03999933258935759}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.037677435205944854}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03682215005140179}]
result = search.search('apricot lime kiwi fig banana strawberry apricot apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #376 checking search results for 'apricot lime kiwi fig banana strawberry apricot apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #376 checking search results for 'apricot lime kiwi fig banana strawberry apricot apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking search results for 'apricot lime kiwi fig banana strawberry apricot apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9853936722905322}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9807900807138802}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9806134159377814}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9803650712845479}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9652162262639136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9626705091142058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9607786564748068}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9605894942889058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9536823875888109}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9303053602832262}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9853936722905322}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9807900807138802}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9806134159377814}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9803650712845479}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9652162262639136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9626705091142058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9607786564748068}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9605894942889058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9536823875888109}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9303053602832262}]
result = search.search('apricot lime kiwi fig banana strawberry apricot apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #377 checking search results for 'apricot lime kiwi fig banana strawberry apricot apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #377 checking search results for 'apricot lime kiwi fig banana strawberry apricot apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking search results for 'strawberry strawberry strawberry lime coconut peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.0414408}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.0414408}]
result = search.search('strawberry strawberry strawberry lime coconut peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #378 checking search results for 'strawberry strawberry strawberry lime coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #378 checking search results for 'strawberry strawberry strawberry lime coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking search results for 'strawberry strawberry strawberry lime coconut peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}]
result = search.search('strawberry strawberry strawberry lime coconut peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #379 checking search results for 'strawberry strawberry strawberry lime coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #379 checking search results for 'strawberry strawberry strawberry lime coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking search results for 'fig cherry cherry kiwi lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05199367151413964}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04913602817166681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.047890075459950346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04617365578962886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045670733134589275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04449450435781301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04415125250773304}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04331962061052803}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04298838135285815}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.041050019012927506}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05199367151413964}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04913602817166681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.047890075459950346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04617365578962886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045670733134589275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04449450435781301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04415125250773304}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04331962061052803}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04298838135285815}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.041050019012927506}]
result = search.search('fig cherry cherry kiwi lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #380 checking search results for 'fig cherry cherry kiwi lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #380 checking search results for 'fig cherry cherry kiwi lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking search results for 'fig cherry cherry kiwi lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9943752960520141}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9943418535113955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9943418535113955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.990570138919314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9905482416286572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9904365460293005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9814256081785234}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9812605898940008}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9943752960520141}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9943418535113955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9943418535113955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.990570138919314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9905482416286572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9904365460293005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9814256081785234}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9812605898940008}]
result = search.search('fig cherry cherry kiwi lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #381 checking search results for 'fig cherry cherry kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #381 checking search results for 'fig cherry cherry kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking search results for 'apple pear apricot blueberry papaya cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05134515845990935}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05059142207167467}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04814526123363281}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.046556394857257294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04543760914987735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04528039365629157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04469761646430216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04393111140509196}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.043810159742647556}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.04225354660266941}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05134515845990935}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05059142207167467}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04814526123363281}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.046556394857257294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04543760914987735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04528039365629157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04469761646430216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04393111140509196}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.043810159742647556}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.04225354660266941}]
result = search.search('apple pear apricot blueberry papaya cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #382 checking search results for 'apple pear apricot blueberry papaya cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #382 checking search results for 'apple pear apricot blueberry papaya cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking search results for 'apple pear apricot blueberry papaya cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9949740547892726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9887083079816673}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9812254452368243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9802059302436322}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9786226021939312}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9762517940403689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9696184107667288}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.9690120148740133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9629626727356483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9595795765530463}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9949740547892726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9887083079816673}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9812254452368243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9802059302436322}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9786226021939312}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9762517940403689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9696184107667288}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.9690120148740133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9629626727356483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9595795765530463}]
result = search.search('apple pear apricot blueberry papaya cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #383 checking search results for 'apple pear apricot blueberry papaya cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #383 checking search results for 'apple pear apricot blueberry papaya cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking search results for 'kiwi banana coconut lime apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05282521911007827}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.048103403973903974}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04716883317919393}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04712565505858093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04485075714444605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04477761545875645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04355632958438813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.040052038357724494}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03928773028725581}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03876860237126903}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05282521911007827}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.048103403973903974}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04716883317919393}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04712565505858093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04485075714444605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04477761545875645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04355632958438813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.040052038357724494}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03928773028725581}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03876860237126903}]
result = search.search('kiwi banana coconut lime apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #384 checking search results for 'kiwi banana coconut lime apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #384 checking search results for 'kiwi banana coconut lime apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking search results for 'kiwi banana coconut lime apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9952351979236266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9855333863727986}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9853911882318409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9786839678633801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.978563764180052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9781389102237017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9756302180897515}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9742912180211426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9669303327980123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9664880590559182}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9662900015891959}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9952351979236266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9855333863727986}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9853911882318409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9786839678633801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.978563764180052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9781389102237017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9756302180897515}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9742912180211426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9669303327980123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9664880590559182}]
result = search.search('kiwi banana coconut lime apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #385 checking search results for 'kiwi banana coconut lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #385 checking search results for 'kiwi banana coconut lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking search results for 'fig pear kiwi cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.051842877713881144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.047306954208131614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04711282509165634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04666380557818905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04490552566242634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.044371046176140745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04434992870392792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.043559100316465774}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.041141533953089775}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04082459404252135}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.051842877713881144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.047306954208131614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04711282509165634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04666380557818905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04490552566242634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.044371046176140745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04434992870392792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.043559100316465774}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.041141533953089775}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04082459404252135}]
result = search.search('fig pear kiwi cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #386 checking search results for 'fig pear kiwi cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #386 checking search results for 'fig pear kiwi cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking search results for 'fig pear kiwi cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9946506775184378}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9945308335049905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.992165915163495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9851304521756664}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9841941202612718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9744717585948663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9597718187119437}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9581508529682491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.957151013169795}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9528823869221771}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9946506775184378}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9945308335049905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.992165915163495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9851304521756664}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9841941202612718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9744717585948663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9597718187119437}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9581508529682491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.957151013169795}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9528823869221771}]
result = search.search('fig pear kiwi cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #387 checking search results for 'fig pear kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #387 checking search results for 'fig pear kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking search results for 'cherry apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.05204075999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.05204075999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}]
result = search.search('cherry apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #388 checking search results for 'cherry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #388 checking search results for 'cherry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking search results for 'cherry apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}]
result = search.search('cherry apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #389 checking search results for 'cherry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #389 checking search results for 'cherry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking search results for 'peach strawberry fig apple coconut fig apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.0473240780830898}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.04566929673113546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04564854377043604}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04481397201715216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.044697111598280985}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.043126167616255554}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.042581707048483984}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03836938722399006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03820126183494687}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.037705337928261355}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.0473240780830898}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.04566929673113546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04564854377043604}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04481397201715216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.044697111598280985}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.043126167616255554}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.042581707048483984}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03836938722399006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03820126183494687}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.037705337928261355}]
result = search.search('peach strawberry fig apple coconut fig apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #390 checking search results for 'peach strawberry fig apple coconut fig apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #390 checking search results for 'peach strawberry fig apple coconut fig apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking search results for 'peach strawberry fig apple coconut fig apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9821572378960743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9788412710083142}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9677154183535693}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9644956939341202}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9639712796333715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 0.9593299376049783}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9587454375351561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.925884327136302}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9093259441963594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 0.8965451488517239}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9821572378960743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9788412710083142}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9677154183535693}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9644956939341202}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9639712796333715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 0.9593299376049783}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9587454375351561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.925884327136302}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9093259441963594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 0.8965451488517239}]
result = search.search('peach strawberry fig apple coconut fig apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #391 checking search results for 'peach strawberry fig apple coconut fig apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #391 checking search results for 'peach strawberry fig apple coconut fig apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking search results for 'cherry pear fig blueberry blueberry banana tomato kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.049577367684073316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04742127987547569}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.047163741207207}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04710801560364634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04459045253494089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04394329126573987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.042649913481419305}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.041489333032689556}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.041102739985014757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.035891695730925065}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.049577367684073316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04742127987547569}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.047163741207207}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04710801560364634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04459045253494089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04394329126573987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.042649913481419305}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.041489333032689556}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.041102739985014757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.035891695730925065}]
result = search.search('cherry pear fig blueberry blueberry banana tomato kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #392 checking search results for 'cherry pear fig blueberry blueberry banana tomato kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #392 checking search results for 'cherry pear fig blueberry blueberry banana tomato kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking search results for 'cherry pear fig blueberry blueberry banana tomato kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9918423385893794}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9808517724244482}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9719413789413373}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9664213462698201}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9655930781728997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9610266258140152}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9596681477734499}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9590070922334744}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9580501725061707}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9485195365954069}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9918423385893794}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9808517724244482}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9719413789413373}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9664213462698201}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9655930781728997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9610266258140152}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9596681477734499}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9590070922334744}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9580501725061707}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9485195365954069}]
result = search.search('cherry pear fig blueberry blueberry banana tomato kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #393 checking search results for 'cherry pear fig blueberry blueberry banana tomato kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #393 checking search results for 'cherry pear fig blueberry blueberry banana tomato kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking search results for 'peach papaya lime apple cherry fig peach strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05199367151413964}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05092634415686568}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04999474497234266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04988246146579397}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.047890075459950346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.046098478741399315}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04582062966758875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04469387404124821}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.042850993910705314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04120734266825497}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05199367151413964}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05092634415686568}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04999474497234266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04988246146579397}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.047890075459950346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.046098478741399315}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04582062966758875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04469387404124821}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.042850993910705314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04120734266825497}]
result = search.search('peach papaya lime apple cherry fig peach strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #394 checking search results for 'peach papaya lime apple cherry fig peach strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #394 checking search results for 'peach papaya lime apple cherry fig peach strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking search results for 'peach papaya lime apple cherry fig peach strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9943664858848037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9943059477514148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9909005751034301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9908268229728038}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9905482416286572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9904509373584496}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9820860970558916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9812312677439874}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9943664858848037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9943059477514148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9909005751034301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9908268229728038}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9905482416286572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9904509373584496}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9820860970558916}]
result = search.search('peach papaya lime apple cherry fig peach strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #395 checking search results for 'peach papaya lime apple cherry fig peach strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #395 checking search results for 'peach papaya lime apple cherry fig peach strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking search results for 'apricot peach apple peach banana banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05456683975064179}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.050218001661136255}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04776098932811458}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04766401731832388}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04552105262587446}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045439033882641054}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.044935668469700964}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04065709962607809}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03908085507065995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.038151329000953485}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05456683975064179}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.050218001661136255}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04776098932811458}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04766401731832388}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04552105262587446}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045439033882641054}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.044935668469700964}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04065709962607809}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03908085507065995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.038151329000953485}]
result = search.search('apricot peach apple peach banana banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #396 checking search results for 'apricot peach apple peach banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #396 checking search results for 'apricot peach apple peach banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking search results for 'apricot peach apple peach banana banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.998148092097652}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9938094565697314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9878316343173279}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9873991953635001}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.985872502604583}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9832915913828133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9829841565680152}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9762824052002124}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9671552417781846}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.9502587154482401}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.998148092097652}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9938094565697314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.9878316343173279}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9873991953635001}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.985872502604583}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9832915913828133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9829841565680152}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9762824052002124}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9671552417781846}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.9502587154482401}]
result = search.search('apricot peach apple peach banana banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #397 checking search results for 'apricot peach apple peach banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #397 checking search results for 'apricot peach apple peach banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking search results for 'kiwi papaya pear blueberry blueberry tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04965188302053221}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04685336208592844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.0464124439938241}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04621240560689815}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.045227390802279006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04441268452852852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04402751543201004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.041647879876536925}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04051407728755596}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03863945675494371}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.03846395490886599}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04965188302053221}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04685336208592844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.0464124439938241}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04621240560689815}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.045227390802279006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04441268452852852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04402751543201004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.041647879876536925}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04051407728755596}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03863945675494371}]
result = search.search('kiwi papaya pear blueberry blueberry tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #398 checking search results for 'kiwi papaya pear blueberry blueberry tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #398 checking search results for 'kiwi papaya pear blueberry blueberry tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking search results for 'kiwi papaya pear blueberry blueberry tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9776374318921439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9759073462314483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 0.9662110961191861}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9661027166698878}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9597459440792441}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9558476714789189}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9551343627107947}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9485708752617429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9480143039998129}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.9466161304393353}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9459551620742758}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9776374318921439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9759073462314483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 0.9662110961191861}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9661027166698878}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9597459440792441}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9558476714789189}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9551343627107947}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9485708752617429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9480143039998129}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.9466161304393353}]
result = search.search('kiwi papaya pear blueberry blueberry tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #399 checking search results for 'kiwi papaya pear blueberry blueberry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #399 checking search results for 'kiwi papaya pear blueberry blueberry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking search results for 'blueberry tomato fig apple apricot banana strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05050992500248119}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05021182324766989}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04799516473741739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04676747358613972}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045456259410158024}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04512058544393934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.043602062248821044}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04025397023758862}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.037735509168849345}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.03649432051898941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.035786515810439075}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05050992500248119}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05021182324766989}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04799516473741739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04676747358613972}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.045456259410158024}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04512058544393934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.043602062248821044}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04025397023758862}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.037735509168849345}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.03649432051898941}]
result = search.search('blueberry tomato fig apple apricot banana strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #400 checking search results for 'blueberry tomato fig apple apricot banana strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #400 checking search results for 'blueberry tomato fig apple apricot banana strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking search results for 'blueberry tomato fig apple apricot banana strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9927218861261702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9914624902423811}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9882603618026243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9770461516681422}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9766525050460529}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9734483320116294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.971360838535661}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9713112604375899}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9695856903081594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.953925389492579}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9927218861261702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9914624902423811}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9882603618026243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9770461516681422}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9766525050460529}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9734483320116294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.971360838535661}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9713112604375899}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9695856903081594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.953925389492579}]
result = search.search('blueberry tomato fig apple apricot banana strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #401 checking search results for 'blueberry tomato fig apple apricot banana strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #401 checking search results for 'blueberry tomato fig apple apricot banana strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking search results for 'kiwi peach fig coconut banana banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05414463298261745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04702132665103462}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04625213301046447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.0455117573107461}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04313736258389146}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04197410072513743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.041950681546831216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.040304546040107296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.03977122773195006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.0372501656554722}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05414463298261745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04702132665103462}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04625213301046447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.0455117573107461}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04313736258389146}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04197410072513743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.041950681546831216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.040304546040107296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.03977122773195006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.0372501656554722}]
result = search.search('kiwi peach fig coconut banana banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #402 checking search results for 'kiwi peach fig coconut banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #402 checking search results for 'kiwi peach fig coconut banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking search results for 'kiwi peach fig coconut banana banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9987273218757606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9904249972308788}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9805548395551877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9757029838216742}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9728316699714183}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9726946725284256}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9725812735301272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9725792241062664}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9703393599063498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9478839095085}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 0.9470389830527706}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9987273218757606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9904249972308788}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9805548395551877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9757029838216742}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9728316699714183}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9726946725284256}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9725812735301272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9725792241062664}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9703393599063498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9478839095085}]
result = search.search('kiwi peach fig coconut banana banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #403 checking search results for 'kiwi peach fig coconut banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #403 checking search results for 'kiwi peach fig coconut banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking search results for 'tomato fig papaya papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}]
result = search.search('tomato fig papaya papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #404 checking search results for 'tomato fig papaya papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #404 checking search results for 'tomato fig papaya papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking search results for 'tomato fig papaya papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}]
result = search.search('tomato fig papaya papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #405 checking search results for 'tomato fig papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #405 checking search results for 'tomato fig papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking search results for 'lime coconut apple coconut lime apple papaya peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466808}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051337981519116796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05092634415686568}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04744755273230061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04566417649567887}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04525127406283575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.044323696972627044}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04402589335760777}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.04014835999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03824656504799213}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466808}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051337981519116796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05092634415686568}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04744755273230061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04566417649567887}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04525127406283575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.044323696972627044}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04402589335760777}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.04014835999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03824656504799213}]
result = search.search('lime coconut apple coconut lime apple papaya peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #406 checking search results for 'lime coconut apple coconut lime apple papaya peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #406 checking search results for 'lime coconut apple coconut lime apple papaya peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking search results for 'lime coconut apple coconut lime apple papaya peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9945281921095935}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.99433419197813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9930637844977852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9909005751034301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9904909332334904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9813951946654981}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9721248451018178}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9719880697506762}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9716715713652317}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9945281921095935}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.99433419197813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9930637844977852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9909005751034301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9904909332334904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9813951946654981}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9721248451018178}]
result = search.search('lime coconut apple coconut lime apple papaya peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #407 checking search results for 'lime coconut apple coconut lime apple papaya peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #407 checking search results for 'lime coconut apple coconut lime apple papaya peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #408 checking search results for 'kiwi fig kiwi tomato banana pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.049719954955504395}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.0468433929488755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04411833273852624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04339477046244135}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04093226318252638}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.040227140807824094}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.03920751248369826}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.039105507480257214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03806203879299232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.03465400244621251}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.034173712542695155}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.049719954955504395}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.0468433929488755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04411833273852624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04339477046244135}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04093226318252638}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.040227140807824094}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.03920751248369826}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.039105507480257214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03806203879299232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.03465400244621251}]
result = search.search('kiwi fig kiwi tomato banana pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #408 checking search results for 'kiwi fig kiwi tomato banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #408 checking search results for 'kiwi fig kiwi tomato banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #409 checking search results for 'kiwi fig kiwi tomato banana pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.978034623784919}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.943895032143596}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9384248427802038}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9302728062422649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9258890371338209}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9214006743409262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9184677610710295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9125343089985705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9045291208164415}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.8839358090823136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.8838935806599834}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.978034623784919}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.943895032143596}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9384248427802038}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9302728062422649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9258890371338209}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9214006743409262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9184677610710295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9125343089985705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9045291208164415}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.8839358090823136}]
result = search.search('kiwi fig kiwi tomato banana pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #409 checking search results for 'kiwi fig kiwi tomato banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'kiwi fig kiwi tomato banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'strawberry peach blueberry apricot kiwi banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.0523012874139239}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04960129917535255}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04883959902017672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04790795474315678}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.046256902205205966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04469094265398591}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.044100468248171716}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04222676459960494}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03944899616412042}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03829609747037471}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.0523012874139239}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04960129917535255}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04883959902017672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04790795474315678}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.046256902205205966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04469094265398591}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.044100468248171716}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04222676459960494}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03944899616412042}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03829609747037471}]
result = search.search('strawberry peach blueberry apricot kiwi banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #410 checking search results for 'strawberry peach blueberry apricot kiwi banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'strawberry peach blueberry apricot kiwi banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'strawberry peach blueberry apricot kiwi banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9988741335429537}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9956215721778992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9937846374156143}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9909180529595356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9856983026056998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9820216838731647}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9780297321436702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9767252931696839}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.975700561708544}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9702843292271658}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9988741335429537}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9956215721778992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9937846374156143}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9909180529595356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9856983026056998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9820216838731647}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9780297321436702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9767252931696839}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.975700561708544}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9702843292271658}]
result = search.search('strawberry peach blueberry apricot kiwi banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #411 checking search results for 'strawberry peach blueberry apricot kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'strawberry peach blueberry apricot kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'fig kiwi tomato fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051667106618341924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.050632724701541953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04784180594663988}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.046361198210568715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04629550798724445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04548977227379671}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.04523095451915302}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04256614879456598}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04214309276870136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04100678222435813}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051667106618341924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.050632724701541953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04784180594663988}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.046361198210568715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04629550798724445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04548977227379671}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.04523095451915302}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04256614879456598}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04214309276870136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04100678222435813}]
result = search.search('fig kiwi tomato fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #412 checking search results for 'fig kiwi tomato fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'fig kiwi tomato fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'fig kiwi tomato fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9997077889596604}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9995748604630614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9994302641866682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9960956083238596}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9960194708135434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9895498451743868}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9895268002634633}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 0.9857562537342205}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9851874674386496}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9845754121750975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9845754121750975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9845202006963433}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9997077889596604}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9995748604630614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9994302641866682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9960956083238596}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9960194708135434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9895498451743868}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9895268002634633}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 0.9857562537342205}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9851874674386496}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9845754121750975}]
result = search.search('fig kiwi tomato fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #413 checking search results for 'fig kiwi tomato fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'fig kiwi tomato fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'coconut lime apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466808}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05133798151911679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05092634415686568}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04744755273230061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.045664176495678874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04525127406283575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04432369697262704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04402589335760777}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.04014835999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03824656504799212}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466808}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05133798151911679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.05092634415686568}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04744755273230061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.045664176495678874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04525127406283575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04432369697262704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04402589335760777}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.04014835999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03824656504799212}]
result = search.search('coconut lime apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #414 checking search results for 'coconut lime apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'coconut lime apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'coconut lime apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9945281921095934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.99433419197813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9930637844977851}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9909005751034301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9904909332334902}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.981395194665498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9721248451018177}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9719880697506761}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9716715713652317}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9945281921095934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.99433419197813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9930637844977851}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.9909005751034301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9904909332334902}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.981395194665498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9721248451018177}]
result = search.search('coconut lime apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #415 checking search results for 'coconut lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'coconut lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'pear blueberry pear fig pear kiwi tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04804151805787434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04647708468912379}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.045127591118565825}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04335225750495898}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04278088905310732}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.04251945064301553}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04192788703254693}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04173670501122447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04112733165419804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.040754025071244274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04804151805787434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04647708468912379}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.045127591118565825}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04335225750495898}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04278088905310732}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.04251945064301553}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04192788703254693}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04173670501122447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04112733165419804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.040754025071244274}]
result = search.search('pear blueberry pear fig pear kiwi tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #416 checking search results for 'pear blueberry pear fig pear kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'pear blueberry pear fig pear kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'pear blueberry pear fig pear kiwi tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9895424572226615}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9827072585043619}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9747871039733893}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9619199928070747}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9613222379099898}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9292981594495721}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9286718766381503}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9012647425043683}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9008435017086797}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.8955133624039375}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9895424572226615}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9827072585043619}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9747871039733893}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9619199928070747}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9613222379099898}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9292981594495721}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9286718766381503}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9012647425043683}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9008435017086797}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.8955133624039375}]
result = search.search('pear blueberry pear fig pear kiwi tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #417 checking search results for 'pear blueberry pear fig pear kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'pear blueberry pear fig pear kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'apple cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.05204075999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.05204075999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}]
result = search.search('apple cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #418 checking search results for 'apple cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'apple cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'apple cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}]
result = search.search('apple cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #419 checking search results for 'apple cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'apple cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'apricot cherry blueberry peach strawberry apple banana blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05036400121648613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.049017076549279726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04768232489180173}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04712197400615646}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04606759027249137}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.044818826239269874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.044531563234966064}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04116880801843591}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03776243202814015}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.0362724937685426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.035526988069947425}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.05036400121648613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.049017076549279726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04768232489180173}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04712197400615646}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04606759027249137}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.044818826239269874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.044531563234966064}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04116880801843591}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.03776243202814015}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.0362724937685426}]
result = search.search('apricot cherry blueberry peach strawberry apple banana blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #420 checking search results for 'apricot cherry blueberry peach strawberry apple banana blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'apricot cherry blueberry peach strawberry apple banana blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'apricot cherry blueberry peach strawberry apple banana blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9934366136376689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9897872817711347}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9862511726012954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9785195414669866}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9742234534848384}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.969062361844535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9678202406974943}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9620651538228999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.9601146438356193}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9565123517831012}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9934366136376689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9897872817711347}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9862511726012954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9785195414669866}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9742234534848384}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.969062361844535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9678202406974943}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9620651538228999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.9601146438356193}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9565123517831012}]
result = search.search('apricot cherry blueberry peach strawberry apple banana blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #421 checking search results for 'apricot cherry blueberry peach strawberry apple banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'apricot cherry blueberry peach strawberry apple banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'kiwi apricot fig pear papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.051513086767299036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.047575752907730924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.0472334130500217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04505044470718742}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04423027110219387}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04367586512313611}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04314172333611606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.042906021888558445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04080949231643269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03987817603639604}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.051513086767299036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.047575752907730924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.0472334130500217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04505044470718742}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04423027110219387}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04367586512313611}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04314172333611606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.042906021888558445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04080949231643269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03987817603639604}]
result = search.search('kiwi apricot fig pear papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #422 checking search results for 'kiwi apricot fig pear papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'kiwi apricot fig pear papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'kiwi apricot fig pear papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9943418535113955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9902241224060483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9859876608522133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9847660353186398}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9789410782977798}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9769659745461501}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9597167583802129}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9551109481473572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9422882012190487}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9269234361771043}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9943418535113955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9902241224060483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9859876608522133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9847660353186398}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9789410782977798}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9769659745461501}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9597167583802129}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9551109481473572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9422882012190487}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.9269234361771043}]
result = search.search('kiwi apricot fig pear papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #423 checking search results for 'kiwi apricot fig pear papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'kiwi apricot fig pear papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'peach pear blueberry pear peach kiwi fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04848647052881343}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.04843993748171445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.047670037814953166}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04578888346393876}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04376055363396796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.043518916024217806}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04301816540060489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04290533969649502}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04283425103555208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.040263495933125365}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.04848647052881343}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.04843993748171445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.047670037814953166}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04578888346393876}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04376055363396796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.043518916024217806}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04301816540060489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04290533969649502}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04283425103555208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.040263495933125365}]
result = search.search('peach pear blueberry pear peach kiwi fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #424 checking search results for 'peach pear blueberry pear peach kiwi fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'peach pear blueberry pear peach kiwi fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'peach pear blueberry pear peach kiwi fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.995030772803296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9911612396246827}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9889339142574388}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9859970292897594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9749616601225014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9734143892145244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9412234522564287}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9397499068047582}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.937905162912454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9376449126941935}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.995030772803296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9911612396246827}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9889339142574388}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9859970292897594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9749616601225014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9734143892145244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9412234522564287}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.9397499068047582}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.937905162912454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9376449126941935}]
result = search.search('peach pear blueberry pear peach kiwi fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #425 checking search results for 'peach pear blueberry pear peach kiwi fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'peach pear blueberry pear peach kiwi fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'fig apricot peach kiwi blueberry kiwi cherry tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.052332608173749094}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04975465491282301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.04379254756072592}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04319872660490649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.040465952707134704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03924884007724444}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.03872368168003194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.03801471302637218}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.03579302917497874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.03461613072930334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.034538841116401334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.03432008424205538}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.03386283247713693}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.052332608173749094}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04975465491282301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'title': 'N-7', 'score': 0.04379254756072592}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04319872660490649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.040465952707134704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03924884007724444}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.03872368168003194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.03801471302637218}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.03579302917497874}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.03461613072930334}]
result = search.search('fig apricot peach kiwi blueberry kiwi cherry tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #426 checking search results for 'fig apricot peach kiwi blueberry kiwi cherry tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'fig apricot peach kiwi blueberry kiwi cherry tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'fig apricot peach kiwi blueberry kiwi cherry tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.97871720203206}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9572790588904734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.9383358714852287}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9373992827444917}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.924254382508498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9201751676423948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9174661757252399}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9078444724456883}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.8935133692756888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.8925547003850818}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.97871720203206}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.9572790588904734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 0.9383358714852287}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9373992827444917}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.924254382508498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9201751676423948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9174661757252399}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9078444724456883}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.8935133692756888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.8925547003850818}]
result = search.search('fig apricot peach kiwi blueberry kiwi cherry tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #427 checking search results for 'fig apricot peach kiwi blueberry kiwi cherry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'fig apricot peach kiwi blueberry kiwi cherry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'cherry pear banana tomato lime apple kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05245116930472852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.0488284537963692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.047485309965152274}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04671355215842061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.045465010925258245}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04478422576315333}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04477834335244515}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04088294195873666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.0391553474229284}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03703802346408591}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.036506302549132244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.036363770117691194}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05245116930472852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.0488284537963692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.047485309965152274}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04671355215842061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.045465010925258245}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04478422576315333}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04477834335244515}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.04088294195873666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.0391553474229284}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.03703802346408591}]
result = search.search('cherry pear banana tomato lime apple kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #428 checking search results for 'cherry pear banana tomato lime apple kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'cherry pear banana tomato lime apple kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'cherry pear banana tomato lime apple kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9890873072190436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9865384345557194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9847250778190981}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9839421933987111}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9821761573232256}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.981773988950284}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9772323123699795}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9756432166528666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.9752664224124826}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9657664244671457}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.9890873072190436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9865384345557194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9847250778190981}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9839421933987111}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9821761573232256}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.981773988950284}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 0.9772323123699795}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 0.9756432166528666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 0.9752664224124826}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9657664244671457}]
result = search.search('cherry pear banana tomato lime apple kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #429 checking search results for 'cherry pear banana tomato lime apple kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'cherry pear banana tomato lime apple kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.05466807999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.051696559999999975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.051393999999999995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.05083659999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.048347039999999994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 0.04810359999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04654291999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04630903999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04550911999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.043232999999999994}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #430 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #431 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'kiwi apricot strawberry strawberry fig peach strawberry peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.051728580472514676}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.049393066745451825}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04790815707605254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04465616716269895}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04403305343199788}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04347654113952383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04325797011622014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04253097555618488}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04161011451276753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.041042903190968885}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'title': 'N-12', 'score': 0.051728580472514676}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.049393066745451825}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.04790815707605254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'title': 'N-13', 'score': 0.04465616716269895}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'title': 'N-22', 'score': 0.04403305343199788}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.04347654113952383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'title': 'Custom Title 79', 'score': 0.04325797011622014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'title': 'N-0', 'score': 0.04253097555618488}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.04161011451276753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.041042903190968885}]
result = search.search('kiwi apricot strawberry strawberry fig peach strawberry peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #432 checking search results for 'kiwi apricot strawberry strawberry fig peach strawberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'kiwi apricot strawberry strawberry fig peach strawberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'kiwi apricot strawberry strawberry fig peach strawberry peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.995569175258434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9942770910704625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9937433097629844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9909222379705676}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9903984283838364}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9893702009455199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9624618812658742}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9554420399626561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9553368893866512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9534732383502689}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'title': 'N-3', 'score': 0.995569175258434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'title': 'N-8', 'score': 0.9942770910704625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'title': 'Custom Title 63', 'score': 0.9937433097629844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'title': 'N-24', 'score': 0.9909222379705676}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'title': 'Custom Title 87', 'score': 0.9903984283838364}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'title': 'N-5', 'score': 0.9893702009455199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'title': 'Custom Title 26', 'score': 0.9624618812658742}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'title': 'N-4', 'score': 0.9554420399626561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'title': 'Custom Title 76', 'score': 0.9553368893866512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'title': 'N-15', 'score': 0.9534732383502689}]
result = search.search('kiwi apricot strawberry strawberry fig peach strawberry peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #433 checking search results for 'kiwi apricot strawberry strawberry fig peach strawberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'kiwi apricot strawberry strawberry fig peach strawberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
