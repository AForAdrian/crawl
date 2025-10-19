
import testingtools
import crawler
import searchdata
import search
output = open('fruits25-outgoing-links-failed.txt', 'w')
success_output = open('fruits25-outgoing-links-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html')
#Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-20.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-11.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-7.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits25/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits25/N-22.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits25/N-15.html\n\n')
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
