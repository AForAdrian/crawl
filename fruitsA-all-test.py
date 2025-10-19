
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html')


output = open('fruitsA-all-outgoing-failed.txt', 'w')
success_output = open('fruitsA-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = None
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #50 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruitsA-all-incoming-failed.txt', 'w')
success_output = open('fruitsA-all-incoming-passed.txt', 'w')

#Test #51 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #101 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruitsA-all-pagerank-failed.txt', 'w')
success_output = open('fruitsA-all-pagerank-passed.txt', 'w')

#Test #102 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html
expected = 0.00880947849616102
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html
expected = 0.008846499047983169
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html
expected = 0.009006883257038334
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html
expected = 0.007754763491191957
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html
expected = 0.007538038677279526
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html
expected = 0.01138210273522217
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html
expected = 0.012782602633378081
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html
expected = 0.01191978150259852
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html
expected = 0.010867020457682225
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html
expected = 0.011142026133579024
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html
expected = 0.010887891140583776
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html
expected = 0.008271800846422634
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html
expected = 0.011916545805988004
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html
expected = 0.011579316303660131
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html
expected = 0.011302529124864737
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html
expected = 0.007905594863312888
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html
expected = 0.009568218662109124
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html
expected = 0.008452959652342806
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html
expected = 0.012381151695809443
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html
expected = 0.008752038825405416
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html
expected = 0.009698768041274203
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html
expected = 0.010756947395543918
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html
expected = 0.008369852290098677
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html
expected = 0.009258496676144437
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html
expected = 0.011302700731264232
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html
expected = 0.006412633993100728
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html
expected = 0.011291254701698296
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html
expected = 0.011512156204320409
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html
expected = 0.011736012378240443
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html
expected = 0.009250547689135453
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html
expected = 0.007390720440343274
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html
expected = 0.011154456645823681
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html
expected = 0.00852489128780138
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html
expected = 0.01038678995646717
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html
expected = 0.00801043013517454
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html
expected = 0.008858099798099534
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html
expected = 0.007787506718804841
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html
expected = 0.01041396901898389
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html
expected = 0.009824327461495655
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html
expected = 0.009666097400413055
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html
expected = 0.011831050135468216
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html
expected = 0.009370093183734274
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html
expected = 0.010323176888630756
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html
expected = 0.010633222522882724
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html
expected = 0.010630131888144531
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html
expected = 0.009386556654339736
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html
expected = 0.007845754756936617
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html
expected = 0.013371438790729918
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html
expected = 0.00900534032968973
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html
expected = 0.00983925131636898
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #152 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #152 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruitsA-all-idf-failed.txt', 'w')
success_output = open('fruitsA-all-idf-passed.txt', 'w')

#Test #153 checking IDF for word coconut
expected = 0.12029423371771174
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word apricot
expected = 0.16812275880832706
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word cherry
expected = 0.12029423371771174
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word strawberry
expected = 0.05889368905356862
result = searchdata.get_idf('strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word banana
expected = 0.10469737866669322
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word kiwi
expected = 0.15200309344505006
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word pear
expected = 0.12029423371771174
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word blueberry
expected = 0.13606154957602856
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word peach
expected = 0.16812275880832706
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word fig
expected = 0.0892673380970873
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word apple
expected = 0.13606154957602856
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word lime
expected = 0.07400058144377678
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word papaya
expected = 0.07400058144377678
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking IDF for word tomato
expected = 0
result = searchdata.get_idf('tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking IDF for word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking IDF for word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruitsA-all-tf-failed.txt', 'w')
success_output = open('fruitsA-all-tf-passed.txt', 'w')

#Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word apricot
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word lime
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word pear
expected = 0.016666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word banana
expected = 0.16666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word cherry
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word peach
expected = 0.016666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word apple
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word fig
expected = 0.05
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word kiwi
expected = 0.11666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word strawberry
expected = 0.11666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word apricot
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word lime
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word pear
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word banana
expected = 0.15151515151515152
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word cherry
expected = 0.06060606060606061
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word peach
expected = 0.15151515151515152
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word apple
expected = 0.06060606060606061
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word fig
expected = 0.030303030303030304
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word kiwi
expected = 0.06060606060606061
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word strawberry
expected = 0.12121212121212122
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word apricot
expected = 0.10416666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word lime
expected = 0.125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word pear
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word banana
expected = 0.041666666666666664
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word cherry
expected = 0.10416666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word peach
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word apple
expected = 0.125
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word fig
expected = 0.0625
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word kiwi
expected = 0.041666666666666664
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word strawberry
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word apricot
expected = 0.11764705882352941
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word lime
expected = 0.0196078431372549
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word pear
expected = 0.058823529411764705
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word banana
expected = 0.058823529411764705
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word cherry
expected = 0.0392156862745098
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word peach
expected = 0.1568627450980392
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word apple
expected = 0.0392156862745098
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word fig
expected = 0.13725490196078433
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word kiwi
expected = 0.0392156862745098
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word strawberry
expected = 0.0196078431372549
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word apricot
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word lime
expected = 0.021739130434782608
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word pear
expected = 0.17391304347826086
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word banana
expected = 0.13043478260869565
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word cherry
expected = 0.06521739130434782
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word peach
expected = 0.15217391304347827
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word apple
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word kiwi
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word strawberry
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word apricot
expected = 0.06060606060606061
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word lime
expected = 0.15151515151515152
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word pear
expected = 0.12121212121212122
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word banana
expected = 0.030303030303030304
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word cherry
expected = 0.06060606060606061
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word peach
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word apple
expected = 0.030303030303030304
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word fig
expected = 0.06060606060606061
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word kiwi
expected = 0.030303030303030304
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word strawberry
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word apricot
expected = 0.13725490196078433
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word lime
expected = 0.058823529411764705
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word pear
expected = 0.0784313725490196
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word banana
expected = 0.0784313725490196
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word cherry
expected = 0.11764705882352941
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word peach
expected = 0.0196078431372549
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word apple
expected = 0.058823529411764705
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word fig
expected = 0.0784313725490196
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word kiwi
expected = 0.058823529411764705
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word strawberry
expected = 0.13725490196078433
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word apricot
expected = 0.12903225806451613
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word lime
expected = 0.06451612903225806
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word pear
expected = 0.06451612903225806
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word banana
expected = 0.06451612903225806
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word cherry
expected = 0.08064516129032258
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word peach
expected = 0.11290322580645161
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word apple
expected = 0.11290322580645161
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word fig
expected = 0.06451612903225806
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word kiwi
expected = 0.04838709677419355
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word strawberry
expected = 0.06451612903225806
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word apricot
expected = 0.13043478260869565
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word lime
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word pear
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word cherry
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word peach
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word apple
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word fig
expected = 0.043478260869565216
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word kiwi
expected = 0.08695652173913043
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word strawberry
expected = 0.13043478260869565
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word apricot
expected = 0.10256410256410256
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word lime
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word banana
expected = 0.10256410256410256
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word cherry
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word peach
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word apple
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word fig
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word kiwi
expected = 0.10256410256410256
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word strawberry
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruitsA-all-tfidf-failed.txt', 'w')
success_output = open('fruitsA-all-tfidf-passed.txt', 'w')

#Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word coconut
expected = 0.032981667131475434
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word peach
expected = 0.011026892940091267
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word apricot
expected = 0.016357873916117573
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word strawberry
expected = 0.003862739397353744
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word banana
expected = 0.010186761933465011
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word papaya
expected = 0.00949605778943751
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word cherry
expected = 0.026174994945598874
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word apple
expected = 0.017459975482436448
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word blueberry
expected = 0.004512734901600524
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word pear
expected = 0.015436648913189839
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word coconut
expected = 0.010850276313252537
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word peach
expected = 0.007700642661358847
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word apricot
expected = 0.029436060137210285
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word strawberry
expected = 0.010311502053445632
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word banana
expected = 0.018331119216016663
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word cherry
expected = 0.005509919743454754
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word apple
expected = 0.012272453657035533
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word blueberry
expected = 0.01813245069590456
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word pear
expected = 0.021061921199563426
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word coconut
expected = 0.010918561930671814
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word peach
expected = 0.018199774625394335
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word apricot
expected = 0.018199774625394335
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word strawberry
expected = 0.003247489546541293
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word banana
expected = 0.0038731965492382735
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word papaya
expected = 0.011801480564147607
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word cherry
expected = 0.019184309548664947
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word apple
expected = 0.009941127882923338
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word blueberry
expected = 0.009941127882923338
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word pear
expected = 0.00878911319687578
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word coconut
expected = 0.009644030661821538
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word apricot
expected = 0.03238802197452078
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word strawberry
expected = 0.01134557931803995
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word banana
expected = 0.016345271200275607
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word papaya
expected = 0.0059326524171650925
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word cherry
expected = 0.004888996381875329
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word apple
expected = 0.005529811388553796
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word blueberry
expected = 0.005529811388553796
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word pear
expected = 0.018780239763260147
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word coconut
expected = 0.011973567577383552
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word peach
expected = 0.022065193013251137
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word apricot
expected = 0.022065193013251137
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word strawberry
expected = 0.007729474732870155
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word banana
expected = 0.003554196665101593
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word papaya
expected = 0.009712171773907811
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word cherry
expected = 0.004083668280478702
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word apple
expected = 0.01354297798143113
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word blueberry
expected = 0.017857334571221715
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word coconut
expected = 0.006942841588258333
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word peach
expected = 0.014413142933521965
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word apricot
expected = 0.01903328015489108
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word strawberry
expected = 0.005048948543482024
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word banana
expected = 0.014676233345288933
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word papaya
expected = 0.006344060525017155
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word cherry
expected = 0.020047018339766673
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word apple
expected = 0.015403611086001797
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word blueberry
expected = 0.01907278936998493
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word pear
expected = 0.0035061373167830923
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word coconut
expected = 0.017369273500044708
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word peach
expected = 0.016450361951706637
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word apricot
expected = 0.020394349181685242
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word strawberry
expected = 0.005762589838934296
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word banana
expected = 0.012700451230222778
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word papaya
expected = 0.0036817535331780714
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word cherry
expected = 0.0030183003281493907
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word apple
expected = 0.010068633780767373
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word blueberry
expected = 0.019645914807286134
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word pear
expected = 0.008901843239444245
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word coconut
expected = 0.005030725989125216
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word peach
expected = 0.013863765868768701
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word apricot
expected = 0.007030923311629619
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word strawberry
expected = 0.009450356508231856
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word banana
expected = 0.020723733970883597
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word cherry
expected = 0.02381096575238536
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word apple
expected = 0.011219929297106539
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word blueberry
expected = 0.021833071950822527
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word pear
expected = 0.014674756650946752
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word coconut
expected = 0.015787960560346127
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word peach
expected = 0.011283423762939646
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word apricot
expected = 0.011283423762939646
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word banana
expected = 0.013740958598566645
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word papaya
expected = 0.004966489516663257
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word cherry
expected = 0.008073450762383137
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word apple
expected = 0.026211587823037175
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word blueberry
expected = 0.017857334571221715
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word pear
expected = 0.023174092030569356
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word coconut
expected = 0.01654088102298361
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word peach
expected = 0.023117471758705398
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word strawberry
expected = 0.0027860080566133524
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word papaya
expected = 0.0035006503992118685
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word cherry
expected = 0.01654088102298361
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word apple
expected = 0.024568939552449414
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word blueberry
expected = 0.0064364888565448634
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word pear
expected = 0.0267525259092945
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #398 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #398 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #399 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #399 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #400 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #400 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #403 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #403 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #405 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #405 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #408 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #408 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #408 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruitsA-all-search-failed.txt', 'w')
success_output = open('fruitsA-all-search-passed.txt', 'w')

#Test #409 checking search results for 'papaya blueberry pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014903713746716533}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012751814955790499}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012515501963687064}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012154707687844568}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012055962197055209}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012019188126786966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.01189889571782566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011885193017067492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.011558971506774061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011339136421801566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011031895069758166}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010879105508676979}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.010763734804302426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010731590475447502}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010687001873080576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010659450513866929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.010630131888144533}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.01058763184431905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'title': 'N-38', 'score': 0.010495960255715342}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.010488050314833238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010472121146585581}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014903713746716533}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012751814955790499}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012515501963687064}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012154707687844568}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012055962197055209}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012019188126786966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.01189889571782566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011885193017067492}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.011558971506774061}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011339136421801566}]
result = search.search('papaya blueberry pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #409 checking search results for 'papaya blueberry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'papaya blueberry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'papaya blueberry pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.9975914390464435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9975701928839459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9962481400653729}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9942880566297466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.994195890391772}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9920929809299835}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9916736490736628}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.9975914390464435}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9975701928839459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9962481400653729}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9942880566297466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.994195890391772}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9920929809299835}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9916736490736628}]
result = search.search('papaya blueberry pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #410 checking search results for 'papaya blueberry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'papaya blueberry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'strawberry blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015045885853253524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013270125901345756}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012782602633378081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012530195826760567}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012355739083682963}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01230271677538768}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01229084120390814}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012249352535232688}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012103229810423685}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011736012378240446}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011575309961287432}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011413847555151466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011302529124864737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.011291254701698297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.01119388981432496}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.011154456645823681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011125230503031297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011082707867055102}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015045885853253524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013270125901345756}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012782602633378081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012530195826760567}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012355739083682963}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01230271677538768}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01229084120390814}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012249352535232688}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012103229810423685}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570148}]
result = search.search('strawberry blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #411 checking search results for 'strawberry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'strawberry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'strawberry blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 1.0000000000000002}]
result = search.search('strawberry blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #412 checking search results for 'strawberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'strawberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'blueberry blueberry papaya papaya blueberry apple strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014928540332505416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013005774843985903}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012795437069921799}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012359787164582971}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012116822576730262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011597457502695469}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011371625450113913}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011357189954755566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011304853986292449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.0112260818840942}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011214780042668298}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.010910351920967178}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.010871967829144564}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010702459273349}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.010692814676752503}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010620582327376}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.01048192518241136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010382927701153259}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014928540332505416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013005774843985903}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012795437069921799}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012359787164582971}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012116822576730262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011597457502695469}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011371625450113913}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011357189954755566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011304853986292449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.0112260818840942}]
result = search.search('blueberry blueberry papaya papaya blueberry apple strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #413 checking search results for 'blueberry blueberry papaya papaya blueberry apple strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'blueberry blueberry papaya papaya blueberry apple strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'blueberry blueberry papaya papaya blueberry apple strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.9934763785859778}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.993221191200958}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 0.9873306427852229}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.9801925865736217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.9786506840741926}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9783616290849438}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9774484379527953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 0.9736480321228695}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.9732230875886706}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9726533582162062}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.9934763785859778}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.993221191200958}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 0.9873306427852229}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.9801925865736217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.9786506840741926}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9783616290849438}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9774484379527953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 0.9736480321228695}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.9732230875886706}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9726533582162062}]
result = search.search('blueberry blueberry papaya papaya blueberry apple strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #414 checking search results for 'blueberry blueberry papaya papaya blueberry apple strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'blueberry blueberry papaya papaya blueberry apple strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013371438790729918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013090651714295071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012782602633378081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012381151695809443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012355739083682959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012326078540514243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.012038453294035877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.01191978150259852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011916545805988004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011733466741607019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011579316303660131}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011512156204320409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.011435617545340325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.01138210273522217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.011356574520041724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.011302700731264232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011302529124864737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.011291254701698296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.011142026133579024}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013371438790729918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013090651714295071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012782602633378081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012381151695809443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012355739083682959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012326078540514243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570144}]
result = search.search('pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #415 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'title': 'Custom Title 66', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #416 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'kiwi apple kiwi peach coconut apple kiwi lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.013811041635002845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012287571554003634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.0113126054623867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.011138767333464921}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.01091644726860606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.010716371960174354}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010544305526901552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010359707093983987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.010256877369539466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010252362853595771}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010173914144110868}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 0.010051327753173295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 0.009921116339787208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.009888037664846642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.009886619508687832}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.009734113674819815}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 0.009691271527391068}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.009650616252167935}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.009329703807973532}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.013811041635002845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012287571554003634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.0113126054623867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.011138767333464921}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.01091644726860606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.010716371960174354}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010544305526901552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010359707093983987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.010256877369539466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010252362853595771}]
result = search.search('kiwi apple kiwi peach coconut apple kiwi lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #417 checking search results for 'kiwi apple kiwi peach coconut apple kiwi lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'kiwi apple kiwi peach coconut apple kiwi lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'kiwi apple kiwi peach coconut apple kiwi lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'title': 'N-16', 'score': 0.9853630243829454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.9849152951042914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.9797542330031761}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.978621226023181}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 0.9758841355343876}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 0.9687126673764312}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 0.9677029953720202}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.9651986134109151}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 0.9607242339336131}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 0.958556222394693}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'title': 'N-16', 'score': 0.9853630243829454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.9849152951042914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.9797542330031761}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.978621226023181}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 0.9758841355343876}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 0.9687126673764312}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 0.9677029953720202}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.9651986134109151}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 0.9607242339336131}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 0.958556222394693}]
result = search.search('kiwi apple kiwi peach coconut apple kiwi lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #418 checking search results for 'kiwi apple kiwi peach coconut apple kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'kiwi apple kiwi peach coconut apple kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'tomato tomato banana banana papaya tomato tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.01525151027291148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013331722505749781}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01262166877475032}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012369047260519975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.012042781469008841}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011977571420184215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01190466076765155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011646043733287755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011553476278029396}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011528109983615434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011509365812349957}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.011062858225829263}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.0110110878028528}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010827136990100223}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010778836820622356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010755781616946798}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.010707303055070998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010704391523873114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.01062906906157501}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.01525151027291148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013331722505749781}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01262166877475032}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012369047260519975}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.012042781469008841}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011977571420184215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01190466076765155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011646043733287755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011553476278029396}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011528109983615434}]
result = search.search('tomato tomato banana banana papaya tomato tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #419 checking search results for 'tomato tomato banana banana papaya tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'tomato tomato banana banana papaya tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'tomato tomato banana banana papaya tomato tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 0.9999585276880488}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 0.9999504204032166}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 0.9999386300588459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 0.9999228250064509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.9999152862490998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 0.9999070893383017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.9999013524239594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.9999000175556894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9998927311846357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.9998916255184437}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9998606416461554}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9995278911576747}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 0.9999585276880488}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 0.9999504204032166}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 0.9999386300588459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 0.9999228250064509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.9999152862490998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 0.9999070893383017}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.9999013524239594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.9999000175556894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9998927311846357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.9998916255184437}]
result = search.search('tomato tomato banana banana papaya tomato tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #420 checking search results for 'tomato tomato banana banana papaya tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'tomato tomato banana banana papaya tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'pear kiwi strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.01519314076793134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012851763682500277}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012736330483504192}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012387276679346734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.01232607854051424}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011814328700827988}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011665860526667708}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011536181139326893}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011512156204320409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011395678221028186}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.011138328364379026}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011108203472054238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010896710746195156}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.010795343101714882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010721811529241294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010701181222674754}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.01060380308467715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.010465492515268246}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010457969693262507}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.01040607498131226}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.01519314076793134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012851763682500277}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012736330483504192}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012387276679346734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.01232607854051424}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011814328700827988}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011665860526667708}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011536181139326893}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011512156204320409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011395678221028186}]
result = search.search('pear kiwi strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #421 checking search results for 'pear kiwi strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'pear kiwi strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'pear kiwi strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.9999999999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.998976652482803}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.9981199037837182}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9976355454296746}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.9963800681910379}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 0.9963693747767715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.9963303468816803}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9957025684731182}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.9999999999999998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.998976652482803}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.9981199037837182}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9976355454296746}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.9963800681910379}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 0.9963693747767715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.9963303468816803}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9957025684731182}]
result = search.search('pear kiwi strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #422 checking search results for 'pear kiwi strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'pear kiwi strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'tomato peach apricot pear papaya fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015023527387279153}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012754393597676703}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012712901090082966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011667004801833622}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011611897962716406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011489326846139337}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011307517426535966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011166169881531003}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011150619971404787}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011101236571105153}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010790704852930329}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010546861234790915}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.010520679382455222}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010465080620572581}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.010350761210801609}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010264435540880154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.010250239571792172}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.010183533596584544}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.01016789212652403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.010156425829771628}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.01013263732499753}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015023527387279153}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012754393597676703}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012712901090082966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011667004801833622}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011611897962716406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011489326846139337}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011307517426535966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011166169881531003}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011150619971404787}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011101236571105153}]
result = search.search('tomato peach apricot pear papaya fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #423 checking search results for 'tomato peach apricot pear papaya fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'tomato peach apricot pear papaya fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'tomato peach apricot pear papaya fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.997102408026178}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 0.9942672066012499}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9879303004608712}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9864728374266254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9855715845016971}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9845867313106493}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.9826431731282403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9825600602448831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.981735638999667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9800267948401593}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.979845802223691}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.997102408026178}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 0.9942672066012499}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9879303004608712}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9864728374266254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9855715845016971}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9845867313106493}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.9826431731282403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9825600602448831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.981735638999667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9800267948401593}]
result = search.search('tomato peach apricot pear papaya fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #424 checking search results for 'tomato peach apricot pear papaya fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'tomato peach apricot pear papaya fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'blueberry blueberry pear apricot pear banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014806908125236641}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012523903934747123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012391324874663951}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.0121672081984779}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011781747991981489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011760422552149081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011688175876005444}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010989719457464402}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01087404671878146}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.010789560669115078}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010735292301259018}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010576307422575296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010170199142925393}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.010124558004117068}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010043022760493825}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.009866334335129982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.009856179959371032}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.009827905803662452}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014806908125236641}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012523903934747123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012391324874663951}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.0121672081984779}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011781747991981489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011760422552149081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011688175876005444}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010989719457464402}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01087404671878146}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.010789560669115078}]
result = search.search('blueberry blueberry pear apricot pear banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #425 checking search results for 'blueberry blueberry pear apricot pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'blueberry blueberry pear apricot pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'blueberry blueberry pear apricot pear banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.9932054132953867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.9907793757477299}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9847442086933786}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.9824822847086002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.9817464673888479}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9816520461877916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.9797616568354052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 0.9727062013366959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.970903453336155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9703903015604728}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.9932054132953867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.9907793757477299}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9847442086933786}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.9824822847086002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.9817464673888479}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9816520461877916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.9797616568354052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 0.9727062013366959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.970903453336155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9703903015604728}]
result = search.search('blueberry blueberry pear apricot pear banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #426 checking search results for 'blueberry blueberry pear apricot pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'blueberry blueberry pear apricot pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'coconut peach kiwi banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015120988631401723}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013177299588123694}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012275228676839377}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012002294082055292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011830870120903841}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011457368026668217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.01141261851447598}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011346311182584718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01105084482085612}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011029212711822785}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.01081627262955103}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010773803474281009}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010567201653315199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.010524284027609299}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.010381856080168783}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.0102847186823097}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.010190391150945612}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010181664288087398}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.010176060093233756}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010107107634756592}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.010098894095949308}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.010095513991826422}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.010050934069821296}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015120988631401723}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013177299588123694}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012275228676839377}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012002294082055292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011830870120903841}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011457368026668217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.01141261851447598}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011346311182584718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01105084482085612}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011029212711822785}]
result = search.search('coconut peach kiwi banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #427 checking search results for 'coconut peach kiwi banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'coconut peach kiwi banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'coconut peach kiwi banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9965648773995829}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9945103928982113}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9909739828066836}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9881790374276593}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 0.9869141127010801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9863829146028759}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9857488836058769}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9854810536364407}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9846038574816237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9843907709508557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.9840220000504649}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9965648773995829}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9945103928982113}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9909739828066836}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9881790374276593}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 0.9869141127010801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9863829146028759}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9857488836058769}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9854810536364407}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9846038574816237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9843907709508557}]
result = search.search('coconut peach kiwi banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #428 checking search results for 'coconut peach kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'coconut peach kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'pear lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013256232381846998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012693794993499197}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012546306444595406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751581}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012196571469862595}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012097405301793117}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012009265854553374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.011679788512930065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011677997293593026}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011579316303660133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.01151215620432041}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.0114159144771272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.011356574520041726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011299372311301783}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.011291254701698296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.011142026133579026}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.010968422995217284}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010922867593070491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.01087516794032207}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010783783114718044}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.0107377730565475}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.010720141333532574}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.01070821018772143}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013256232381846998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012693794993499197}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012546306444595406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751581}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012196571469862595}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012097405301793117}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012009265854553374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.011679788512930065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011677997293593026}]
result = search.search('pear lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #429 checking search results for 'pear lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'pear lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'pear lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'title': 'N-33', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 1.0000000000000002}]
result = search.search('pear lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #430 checking search results for 'pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'kiwi banana lime pear fig peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015111626132521651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01286715733079273}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01188913330962839}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011849019097945945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011576690244168356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01136400836979269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.01112056129306684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011043760161072206}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011002097895608999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010854397956456967}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010786301495794265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010578543309671467}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.01036995651118594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.010313754921151394}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.010263329880722495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010217732998777896}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.010163251209366418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010135618631878675}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.010103776514272909}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.009985811829618817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.00994052662079125}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015111626132521651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01286715733079273}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01188913330962839}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011849019097945945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011576690244168356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01136400836979269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.01112056129306684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011043760161072206}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011002097895608999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010854397956456967}]
result = search.search('kiwi banana lime pear fig peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #431 checking search results for 'kiwi banana lime pear fig peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'kiwi banana lime pear fig peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'kiwi banana lime pear fig peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9946443004815952}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9903603990635585}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9875271562735582}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9860574144921653}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9855410868993955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9846441008630885}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9845080946505461}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.984442429188649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9828098813563928}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.979906100376099}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9946443004815952}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9903603990635585}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9875271562735582}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9860574144921653}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9855410868993955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9846441008630885}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9845080946505461}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.984442429188649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9828098813563928}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.979906100376099}]
result = search.search('kiwi banana lime pear fig peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #432 checking search results for 'kiwi banana lime pear fig peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'kiwi banana lime pear fig peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'cherry apple strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015060061036723622}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.01302736861824901}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012108060832950057}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01199630783806658}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011705584910453}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.01160486074650088}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011474885973746093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.011247910230019595}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011125954197442705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011026977609857387}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010976517980381824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010970995458938052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.01096318180204098}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010829989574601823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.01076094498472769}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.010751246616222192}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010633145112093444}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010594087747770533}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.010430189199134132}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010425837168231117}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.010391062553077335}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.010317325247409253}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.01029452423155895}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.010156223012177312}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.01004671025823543}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015060061036723622}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.01302736861824901}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012108060832950057}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01199630783806658}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011705584910453}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.01160486074650088}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011474885973746093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.011247910230019595}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011125954197442705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011026977609857387}]
result = search.search('cherry apple strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #433 checking search results for 'cherry apple strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'cherry apple strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'cherry apple strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 0.9999999999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9951657795633693}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.9944093227729599}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.9933572890414071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9914285733641856}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9911758232425696}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'title': 'N-9', 'score': 0.990904688041753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.9907345373366258}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.9907197945952728}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.9902387712098629}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 0.9999999999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9951657795633693}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.9944093227729599}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.9933572890414071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9914285733641856}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9911758232425696}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'title': 'N-9', 'score': 0.990904688041753}]
result = search.search('cherry apple strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #434 checking search results for 'cherry apple strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'cherry apple strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'banana lime apple lime fig cherry banana coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.0146861063317878}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011606097261563282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.01136976556428027}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.011010426573600114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01094233930449818}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010862667944298238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010782844336489978}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01071821360786349}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010328139742478098}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.010261506697853662}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010238499985269697}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.010226277939244027}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010037839885824724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.010009757128069363}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.009930671747727063}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.009832997152029982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.009797766045113196}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.009747865045577316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 0.009714445750349052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.009662894294417518}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.009606338241379436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.00952455068961588}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.009521981423547269}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.009483504575900083}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.009425845290321817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 0.009422251165180508}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 0.009314086408664487}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.009303100456879633}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.009286086158705046}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.0146861063317878}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011606097261563282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.01136976556428027}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.011010426573600114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01094233930449818}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010862667944298238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010782844336489978}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01071821360786349}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010328139742478098}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.010261506697853662}]
result = search.search('banana lime apple lime fig cherry banana coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #435 checking search results for 'banana lime apple lime fig cherry banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'banana lime apple lime fig cherry banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'banana lime apple lime fig cherry banana coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 0.9746921632872472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.974141210617418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9659175823274034}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9628065479185526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9624733963036575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 0.9614110531257208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 0.9599516337057801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'title': 'N-43', 'score': 0.9542066979579701}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 0.9487945319797882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.945535754487788}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 0.945451794430509}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 0.9746921632872472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.974141210617418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9659175823274034}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9628065479185526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9624733963036575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 0.9614110531257208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 0.9599516337057801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'title': 'N-43', 'score': 0.9542066979579701}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 0.9487945319797882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.945535754487788}]
result = search.search('banana lime apple lime fig cherry banana coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #436 checking search results for 'banana lime apple lime fig cherry banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'banana lime apple lime fig cherry banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'fig banana peach blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014770776083662252}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012996682926041205}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012256324569194243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011972375766335834}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011701380465036403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011670452219401776}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011495976434475285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.011404057337096983}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011208837379410176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01120606376899077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.01102366131775412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.0109846667592901}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.010782275019871725}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010730955600558954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010547876923734913}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.01048455464799992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010464674906863047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.010255492805183597}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.010237325236783824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010222719958816856}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014770776083662252}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012996682926041205}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012256324569194243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011972375766335834}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011701380465036403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011670452219401776}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011495976434475285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.011404057337096983}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011208837379410176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01120606376899077}]
result = search.search('fig banana peach blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #437 checking search results for 'fig banana peach blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'fig banana peach blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'fig banana peach blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9981361534318388}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 0.9944999956068699}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9929507961834644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9882289579864943}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.9875996282478504}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.9860038777818849}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 0.9825538757191739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9819719337724963}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.980986996700656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9808988226021608}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9981361534318388}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 0.9944999956068699}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9929507961834644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9882289579864943}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.9875996282478504}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.9860038777818849}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 0.9825538757191739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9819719337724963}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.980986996700656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9808988226021608}]
result = search.search('fig banana peach blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #438 checking search results for 'fig banana peach blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'fig banana peach blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'strawberry cherry coconut peach papaya apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.01502770380751207}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012646344898500847}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012249837701865504}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011841148517235221}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01178251778510172}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01175762643311727}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011365081466390946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011179542779815766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010871820057169036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.010797419860866166}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010785027777962931}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010683712327080293}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010551900041068344}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010255870798957416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.010254178811356464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.010140482622469228}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010129299678023965}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010093587060944225}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010059966752441918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.00996860518485175}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.009883371610636226}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.009874863146698054}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.009853535253556695}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.01502770380751207}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012646344898500847}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012249837701865504}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011841148517235221}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01178251778510172}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01175762643311727}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011365081466390946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011179542779815766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010871820057169036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.010797419860866166}]
result = search.search('strawberry cherry coconut peach papaya apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #439 checking search results for 'strawberry cherry coconut peach papaya apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'strawberry cherry coconut peach papaya apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'strawberry cherry coconut peach papaya apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9896396720859474}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9848604385326423}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.9776833743944325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9759486164123653}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9748427976806389}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9727642254495674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 0.969634504230536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9689435757581267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 0.9680856438971474}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9660592287159364}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 0.9654748463140662}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 0.9651022780386961}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9896396720859474}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9848604385326423}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.9776833743944325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9759486164123653}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9748427976806389}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9727642254495674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 0.969634504230536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9689435757581267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 0.9680856438971474}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9660592287159364}]
result = search.search('strawberry cherry coconut peach papaya apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #440 checking search results for 'strawberry cherry coconut peach papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'strawberry cherry coconut peach papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'peach pear coconut pear blueberry coconut kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014434303813558574}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01216435840483038}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011905884158653422}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011270593490541684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011162862296320393}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011022937781296838}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010850057957320051}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010838213840351484}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.01063112655591037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010425761241314146}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010389453776181624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010073853875247249}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.009967892753505124}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.00996598891842921}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.009884735482358428}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.009792737854242301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.009788667035188426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.009772088127433095}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.009726641223425557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.009696628446778734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.009573238493546733}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.009541529050997291}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014434303813558574}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01216435840483038}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011905884158653422}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011270593490541684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011162862296320393}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011022937781296838}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010850057957320051}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010838213840351484}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.01063112655591037}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010425761241314146}]
result = search.search('peach pear coconut pear blueberry coconut kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #441 checking search results for 'peach pear coconut pear blueberry coconut kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'peach pear coconut pear blueberry coconut kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'peach pear coconut pear blueberry coconut kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9788152723311473}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.9764174180878484}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 0.9745495761191904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9726103157449987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 0.9650686800126278}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.960968509902197}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 0.9581211890882672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9575284419706885}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9528894206614643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.9527003737704458}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9788152723311473}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.9764174180878484}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 0.9745495761191904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9726103157449987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 0.9650686800126278}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.960968509902197}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 0.9581211890882672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9575284419706885}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9528894206614643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.9527003737704458}]
result = search.search('peach pear coconut pear blueberry coconut kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #442 checking search results for 'peach pear coconut pear blueberry coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'peach pear coconut pear blueberry coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'pear peach peach papaya pear cherry peach pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.013889783764573307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013229030245326737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012888027072116526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011890389872619929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011761659069815297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011541614998144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011400113106941443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011186497058894913}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011122060926846453}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.01110985894881897}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.010929446147188248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010669853293740825}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010664131203339052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.010637734107167148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.01063497601854619}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010520816347235395}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010203763464975878}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010182427128392103}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.013889783764573307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013229030245326737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012888027072116526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011890389872619929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011761659069815297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011541614998144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011400113106941443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011186497058894913}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011122060926846453}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.01110985894881897}]
result = search.search('pear peach peach papaya pear cherry peach pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #443 checking search results for 'pear peach peach papaya pear cherry peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'pear peach peach papaya pear cherry peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'pear peach peach papaya pear cherry peach pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 0.9976995968309214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9893497964106968}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9886253359828471}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.988615261669091}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9845214244026309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.9835789162234788}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.9829533572603757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9827931285708817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.9815210061407941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 0.978615328830307}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 0.9976995968309214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9893497964106968}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9886253359828471}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.988615261669091}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9845214244026309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.9835789162234788}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.9829533572603757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9827931285708817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.9815210061407941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 0.978615328830307}]
result = search.search('pear peach peach papaya pear cherry peach pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #444 checking search results for 'pear peach peach papaya pear cherry peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'pear peach peach papaya pear cherry peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'pear coconut apple cherry coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014698051958788018}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01291567418516245}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.01272729946877637}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011923446858897442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011705541781634052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011194064645317477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010923000331900082}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.010867037579518929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.010666131028277372}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010571849082442923}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.010462273816265872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.0104426492524828}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010365600393200362}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.010291812986119009}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.010180741097331206}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010152038410823065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.010066788369079354}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010031460269673711}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.009828915012774133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.009827147543276973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.009808573162815453}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.009781521657803148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 0.00976298944389752}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.009745544199963355}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.009592539759258454}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014698051958788018}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01291567418516245}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.01272729946877637}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011923446858897442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011705541781634052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011194064645317477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010923000331900082}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.010867037579518929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.010666131028277372}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010571849082442923}]
result = search.search('pear coconut apple cherry coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #445 checking search results for 'pear coconut apple cherry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'pear coconut apple cherry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'pear coconut apple cherry coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9963017654817719}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.9897538077841468}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 0.9852762682268115}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9843598130494267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9824559568407643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'title': 'N-39', 'score': 0.9822859956584926}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 0.9770329151983251}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.9770329151983251}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9722822459445714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9722433799745877}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9963017654817719}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.9897538077841468}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 0.9852762682268115}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9843598130494267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9824559568407643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'title': 'N-39', 'score': 0.9822859956584926}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 0.9770329151983251}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.9770329151983251}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9722822459445714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9722433799745877}]
result = search.search('pear coconut apple cherry coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #446 checking search results for 'pear coconut apple cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'pear coconut apple cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'tomato cherry pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012968600879280276}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012485277745472863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012294629390432684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012100408284548449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011990411881848493}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011919781502598523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011916545805988004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011786161475534719}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011733466741607022}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.01151215620432041}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011472370437301736}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.011291254701698297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011104750706361907}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.010899019017885469}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012968600879280276}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012485277745472863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012294629390432684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012100408284548449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011990411881848493}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011919781502598523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011916545805988004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011786161475534719}]
result = search.search('tomato cherry pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #447 checking search results for 'tomato cherry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'tomato cherry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'tomato cherry pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}]
result = search.search('tomato cherry pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #448 checking search results for 'tomato cherry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'tomato cherry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'kiwi coconut pear apple blueberry apple apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014028111325851198}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011910137004333651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011524086438473654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011423555770453564}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011113908362773886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011061172295993604}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010907420644010611}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.010578363757737961}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010291574218588125}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010255659937344208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.01024601560283797}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010195430784815052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.009987299383389535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.009968098540149356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.009613474022028902}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.009524815600373214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.009459242155692675}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.009286087232520618}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.009258175296626522}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014028111325851198}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011910137004333651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011524086438473654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011423555770453564}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011113908362773886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011061172295993604}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010907420644010611}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.010578363757737961}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010291574218588125}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010255659937344208}]
result = search.search('kiwi coconut pear apple blueberry apple apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #449 checking search results for 'kiwi coconut pear apple blueberry apple apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'kiwi coconut pear apple blueberry apple apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'kiwi coconut pear apple blueberry apple apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 0.9852142135160271}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9818290890524505}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 0.9624512653336406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 0.9610091959364941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.9604020654745324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.9591069947202473}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9527388992696799}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9519990045479843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.943076005002167}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9409430655790085}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 0.9852142135160271}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9818290890524505}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 0.9624512653336406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 0.9610091959364941}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.9604020654745324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.9591069947202473}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9527388992696799}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9519990045479843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.943076005002167}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9409430655790085}]
result = search.search('kiwi coconut pear apple blueberry apple apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #450 checking search results for 'kiwi coconut pear apple blueberry apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'kiwi coconut pear apple blueberry apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'fig banana strawberry fig pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014027236280570614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013192785944818276}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012113576491969553}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.01146778452256726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011467165809327254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011386452480040577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011044002457727818}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010838835785195958}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010821547684076512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.01062622069413854}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01061613243863207}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.010343212335184036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010324317665554023}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 0.010303855503597342}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.010281893650557162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010262135325587337}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.010224722811108368}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'title': 'Custom Title 66', 'score': 0.010149433798863195}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010111218101037637}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.009990579944807372}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.00998994380283657}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.00998876527498992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.009969243245558328}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.009936696897170224}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 0.009924393105474055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.009752759986854749}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.009696902908743851}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.009695443351709455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 0.009690763934465609}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.009676751172350093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.009654878643940488}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.009651374748580313}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014027236280570614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013192785944818276}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012113576491969553}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.01146778452256726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011467165809327254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011386452480040577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011044002457727818}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010838835785195958}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010821547684076512}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.01062622069413854}]
result = search.search('fig banana strawberry fig pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #451 checking search results for 'fig banana strawberry fig pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'fig banana strawberry fig pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'fig banana strawberry fig pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 0.9994992580721813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 0.9963881211388325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.993139138191347}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9900072898815953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9866392204528134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9828240509760456}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.9803291814128867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.9803258422125799}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 0.9802972400881669}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.9783963603520691}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.978388504525758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 0.9782469147633215}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 0.9994992580721813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 0.9963881211388325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.993139138191347}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9900072898815953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9866392204528134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9828240509760456}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.9803291814128867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.9803258422125799}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 0.9802972400881669}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.9783963603520691}]
result = search.search('fig banana strawberry fig pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #452 checking search results for 'fig banana strawberry fig pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'fig banana strawberry fig pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'strawberry peach cherry apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015095872256646065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012647090478290155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.0124934010568024}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01213290367113422}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012097129065148439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011676739310469315}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011486133293860471}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011306107700382203}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.01121077875499148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011180574167101024}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011144664682631523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010900408353254584}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010811338586289743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010607083259129515}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.01057670546319558}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010554395015085389}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010551657017955272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.010222399338579031}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015095872256646065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012647090478290155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.0124934010568024}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01213290367113422}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012097129065148439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011676739310469315}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011486133293860471}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011306107700382203}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.01121077875499148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011180574167101024}]
result = search.search('strawberry peach cherry apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #453 checking search results for 'strawberry peach cherry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'strawberry peach cherry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'strawberry peach cherry apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.99473027015319}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9921357415472594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 0.9907467277932267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9893279479784058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9887885164666667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.9858264163961394}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 0.9844110412977429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9803126301236857}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.9799495207897948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.9791903022436997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 0.9790209973473898}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.99473027015319}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9921357415472594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 0.9907467277932267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9893279479784058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9887885164666667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.9858264163961394}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 0.9844110412977429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9803126301236857}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.9799495207897948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.9791903022436997}]
result = search.search('strawberry peach cherry apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #454 checking search results for 'strawberry peach cherry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'strawberry peach cherry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'kiwi strawberry fig blueberry kiwi fig fig apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.013160266458909766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012857777416801034}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.01153019245944428}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011008418923215042}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.0110005912203384}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010968904157220401}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010870356485143654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010636756765069295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.010446596740721436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010189494604167211}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010077086723896577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.010019335383515954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.009977844555539116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.009956987046511772}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.009617951560402262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.009587954755975668}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.009489090127262349}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.009436865899101119}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.009235764684086125}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.009192314471007431}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.013160266458909766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012857777416801034}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.01153019245944428}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011008418923215042}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.0110005912203384}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010968904157220401}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010870356485143654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010636756765069295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.010446596740721436}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010189494604167211}]
result = search.search('kiwi strawberry fig blueberry kiwi fig fig apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #455 checking search results for 'kiwi strawberry fig blueberry kiwi fig fig apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'kiwi strawberry fig blueberry kiwi fig fig apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'kiwi strawberry fig blueberry kiwi fig fig apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 0.9949058361571903}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.9739783725924958}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'title': 'N-6', 'score': 0.96973012269157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9681468561449822}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9645274079801656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9615851830182259}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9597444282405324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.9594223389864744}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9462458897854945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'title': 'N-8', 'score': 0.9451707839464584}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 0.9949058361571903}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.9739783725924958}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'title': 'N-6', 'score': 0.96973012269157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9681468561449822}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9645274079801656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9615851830182259}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9597444282405324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.9594223389864744}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9462458897854945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'title': 'N-8', 'score': 0.9451707839464584}]
result = search.search('kiwi strawberry fig blueberry kiwi fig fig apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #456 checking search results for 'kiwi strawberry fig blueberry kiwi fig fig apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'kiwi strawberry fig blueberry kiwi fig fig apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'lime coconut pear fig strawberry kiwi strawberry peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014845631636666445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012639628794627525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012098540319068311}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011538078043490153}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.01135937256016454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011344580553249939}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010904072163200851}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01072154166040575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010556067815255846}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010482240745729933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.010344797385747348}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.010198201633458893}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010141974989529222}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.010095818017074536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.01006539344997406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.010034166313828124}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010019242081469577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.009971017142804193}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.00996419219445299}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.009924250421370856}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.009900248143576009}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 0.00983243430189164}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.009742020742650483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.009731492254165622}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.00973116728159728}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.009579428735728378}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.009579037410745934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.009536852262547274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014845631636666445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012639628794627525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012098540319068311}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011538078043490153}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.01135937256016454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011344580553249939}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010904072163200851}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01072154166040575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010556067815255846}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010482240745729933}]
result = search.search('lime coconut pear fig strawberry kiwi strawberry peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #457 checking search results for 'lime coconut pear fig strawberry kiwi strawberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'lime coconut pear fig strawberry kiwi strawberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'lime coconut pear fig strawberry kiwi strawberry peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9953042982301238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.9888603246946858}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9823114977956365}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'title': 'N-24', 'score': 0.9814329458327407}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.97624311547623}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9729280980819358}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9720037176616697}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9705840815254613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9700365648155577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.9695890734011883}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9953042982301238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.9888603246946858}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9823114977956365}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'title': 'N-24', 'score': 0.9814329458327407}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.97624311547623}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9729280980819358}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9720037176616697}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9705840815254613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9700365648155577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.9695890734011883}]
result = search.search('lime coconut pear fig strawberry kiwi strawberry peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #458 checking search results for 'lime coconut pear fig strawberry kiwi strawberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'lime coconut pear fig strawberry kiwi strawberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'fig peach pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015075867667245559}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013036280338956967}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012589422825848382}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012209637713097375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011897781250739843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011769429210280999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01176362618222403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011520386791382073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011323597162365969}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011317596570736273}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011124075902652119}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.01094349056704982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.01090931602396498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.010890961229857412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010780034263005424}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010662210527010418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010624445570754624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.010549086140001496}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010500806479964169}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015075867667245559}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013036280338956967}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012589422825848382}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012209637713097375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011897781250739843}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011769429210280999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01176362618222403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011520386791382073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011323597162365969}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011317596570736273}]
result = search.search('fig peach pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #459 checking search results for 'fig peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'fig peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'fig peach pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9977155507155194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.9973773992626663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9966845780187957}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9958465493907588}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.9958134852055948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9944346830120427}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.99325280552717}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9918484311548547}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9910651384942784}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9977155507155194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.9973773992626663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9966845780187957}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9958465493907588}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.9958134852055948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9944346830120427}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.99325280552717}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9918484311548547}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9910651384942784}]
result = search.search('fig peach pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #460 checking search results for 'fig peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'fig peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'papaya tomato cherry apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015112569833494115}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013015822632912196}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.012122701774986104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012104545075325683}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012077246285385163}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011818252252210948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.011719283120299162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011658888213975994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011624461673459945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011593595443255784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.01153254238703364}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011128977945248213}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011116053612495238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010835199605519862}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010788833120830477}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015112569833494115}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013015822632912196}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.012122701774986104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012104545075325683}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012077246285385163}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011818252252210948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.011719283120299162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011658888213975994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011624461673459945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011593595443255784}]
result = search.search('papaya tomato cherry apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #461 checking search results for 'papaya tomato cherry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'papaya tomato cherry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #462 checking search results for 'papaya tomato cherry apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9986452597377375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 0.9982499317784982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9946972728903042}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9942837772315674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.9927826898601644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'title': 'N-43', 'score': 0.9917221839542383}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9986452597377375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 0.9982499317784982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9946972728903042}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9942837772315674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.9927826898601644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'title': 'N-43', 'score': 0.9917221839542383}]
result = search.search('papaya tomato cherry apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #462 checking search results for 'papaya tomato cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #462 checking search results for 'papaya tomato cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #463 checking search results for 'blueberry apricot kiwi pear apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.01501768105359752}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012942222855606136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01230519483452053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.0117904629687529}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011679616612462605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011336634837991513}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010879259849133606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010559388001409414}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010482527460642184}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.010454175211389227}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.0103626961211926}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.010349654431036533}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010323798730111753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.010223055213892471}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.009993969827795457}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.009922181597708498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.009920231534447651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.009815114984016967}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 0.009812829781933805}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.009759656268951577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.009731211994183973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.009645075320962525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.009625613207800563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.009574696480375892}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.009565326464585293}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.009552360590950831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 0.009540465429635485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.009493302983458733}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.009478733643531481}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.009469772808199405}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.009460283241166234}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.01501768105359752}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012942222855606136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01230519483452053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.0117904629687529}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011679616612462605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011336634837991513}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010879259849133606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010559388001409414}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010482527460642184}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.010454175211389227}]
result = search.search('blueberry apricot kiwi pear apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #463 checking search results for 'blueberry apricot kiwi pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #463 checking search results for 'blueberry apricot kiwi pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #464 checking search results for 'blueberry apricot kiwi pear apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9927098560613332}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.990544175560112}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9842035841028489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.9803235941199242}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9778680347335577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.975459665366506}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.9732259061882755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9679005422048264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'title': 'N-36', 'score': 0.9651072364716732}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9645171744338681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 0.9643950755789973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 0.964089395706896}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 0.9636410645083046}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9927098560613332}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.990544175560112}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9842035841028489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.9803235941199242}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9778680347335577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.975459665366506}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.9732259061882755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9679005422048264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'title': 'N-36', 'score': 0.9651072364716732}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9645171744338681}]
result = search.search('blueberry apricot kiwi pear apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #464 checking search results for 'blueberry apricot kiwi pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #464 checking search results for 'blueberry apricot kiwi pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #465 checking search results for 'coconut peach strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015069637224881744}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013131574665466605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012879810735238332}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012326078540514243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012285102469046766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012276521287019372}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012032372184509059}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011906839888169514}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01172965277824994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.01138050773006541}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011327759784764614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.01124203096797201}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.01104441802477144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010844695859218009}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010835199605519862}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.010806848202104787}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.010774593734381051}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010661221818124619}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.01065068701403653}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010635168566117145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010400980624959456}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015069637224881744}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013131574665466605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012879810735238332}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012326078540514243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012285102469046766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012276521287019372}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012032372184509059}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011906839888169514}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01172965277824994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.01138050773006541}]
result = search.search('coconut peach strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #465 checking search results for 'coconut peach strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #465 checking search results for 'coconut peach strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #466 checking search results for 'coconut peach strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9987764375750302}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.9982371820490333}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9945151114093502}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9943581365813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9942900954763124}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.993624637979388}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9987764375750302}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.9982371820490333}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9945151114093502}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9943581365813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9942900954763124}]
result = search.search('coconut peach strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #466 checking search results for 'coconut peach strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #466 checking search results for 'coconut peach strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #467 checking search results for 'banana coconut pear cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012121229128731495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01185186501452244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011845316979982366}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011810708172264053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011608085618155906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011565565923425327}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.01121388111379991}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011094051177515758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010756947395543918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.010653692074815365}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010636096457835824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.01063142350119342}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010579619915247997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.01056766619070156}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010511422059003246}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.01048468099763203}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010393207067324824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.010328726021087668}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.010253962601745317}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010219824103518594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.010211194229415596}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010131579697569578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.010107208136249822}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010040954934971397}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.01001211430703491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.00986199813948443}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012121229128731495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01185186501452244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011845316979982366}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011810708172264053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011608085618155906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011565565923425327}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.01121388111379991}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011094051177515758}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010756947395543918}]
result = search.search('banana coconut pear cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #467 checking search results for 'banana coconut pear cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #467 checking search results for 'banana coconut pear cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #468 checking search results for 'banana coconut pear cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 0.9999999999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 0.99475473215244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9932952532314285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9916392978659054}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9863923166239859}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9863426485375681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.986298002367904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 0.9851240128226237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.9847910686235379}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 0.9999999999999999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 0.99475473215244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9932952532314285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9916392978659054}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9863923166239859}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9863426485375681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.986298002367904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 0.9851240128226237}]
result = search.search('banana coconut pear cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #468 checking search results for 'banana coconut pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #468 checking search results for 'banana coconut pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #469 checking search results for 'kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013371438790729918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013090651714295071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012782602633378081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012355739083682959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012326078540514243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.012038453294035877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.01191978150259852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011916545805988004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.011831050135468216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011736012378240443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011579316303660131}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011512156204320409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.01138210273522217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.011356574520041724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.011302700731264232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011302529124864737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.011154456645823681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.011142026133579024}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013371438790729918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013090651714295071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012782602633378081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012355739083682959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012326078540514243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.012038453294035877}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #469 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #469 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #470 checking search results for 'kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'title': 'Custom Title 60', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 1.0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #470 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #470 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #471 checking search results for 'cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013371438790729918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013090651714295071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012782602633378081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012381151695809443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.012122701774986104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.012038453294035877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.01191978150259852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011916545805988004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.011831050135468216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011736012378240443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011733466741607019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011512156204320409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.011435617545340325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.011302700731264232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011302529124864737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.011291254701698296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.011154456645823681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.011142026133579024}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013371438790729918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013090651714295071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012782602633378081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012381151695809443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.012122701774986104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.012038453294035877}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #471 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #471 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #472 checking search results for 'cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'title': 'Custom Title 60', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #472 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #472 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #473 checking search results for 'tomato banana cherry pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012471805091830195}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011919781502598523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011916545805988008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01177560004750239}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01172446288976651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011708080415527566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011585317443051198}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.01151215620432041}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011383312811666041}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.0110446116518882}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010959794328612098}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010883106569841046}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.01084461653568141}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010756947395543918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010711997326553632}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010692925808903714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.010613570115885684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010548567515650642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010477503165493363}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.010386805652024232}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012471805091830195}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011919781502598523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011916545805988008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01177560004750239}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.01172446288976651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011708080415527566}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011585317443051198}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.01151215620432041}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011383312811666041}]
result = search.search('tomato banana cherry pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #473 checking search results for 'tomato banana cherry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #473 checking search results for 'tomato banana cherry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #474 checking search results for 'tomato banana cherry pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9974202802099438}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9974202802099438}]
result = search.search('tomato banana cherry pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #474 checking search results for 'tomato banana cherry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #474 checking search results for 'tomato banana cherry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #475 checking search results for 'peach papaya strawberry kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015160017762855292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012930907216981648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01255437711532948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012046000923002093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011839565892478327}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011732320951934244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011496586189736145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011429730156854633}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.011205978075659356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.01108252393226906}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.010808632226797085}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010785601206589312}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010704351573676225}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.010697229395389175}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010620994779495914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010514759329812568}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.01050538850716391}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.010301095744756879}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.010291054736342965}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.01015200601685468}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.010140460610020215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.01012746702765438}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.010119475432735493}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010101510135975156}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015160017762855292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012930907216981648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01255437711532948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012046000923002093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011839565892478327}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011732320951934244}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011496586189736145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011429730156854633}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.011205978075659356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.01108252393226906}]
result = search.search('peach papaya strawberry kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #475 checking search results for 'peach papaya strawberry kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #475 checking search results for 'peach papaya strawberry kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #476 checking search results for 'peach papaya strawberry kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9950869753152344}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'title': 'N-6', 'score': 0.9944931780950264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9943919729691879}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.9943637998576266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9935318085404924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.993270379150599}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9914165344361248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.9882977012943669}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9875895183473594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9874630421184509}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9950869753152344}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'title': 'N-6', 'score': 0.9944931780950264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9943919729691879}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.9943637998576266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9935318085404924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.993270379150599}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9914165344361248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.9882977012943669}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9875895183473594}]
result = search.search('peach papaya strawberry kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #476 checking search results for 'peach papaya strawberry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #476 checking search results for 'peach papaya strawberry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #477 checking search results for 'tomato tomato pear papaya pear kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014865746661435432}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013087325407883656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011984776257118019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011894553383675505}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011803613786643404}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011651272728936101}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011482719446492413}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011352262996312307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011185886357118237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011130264499406156}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.01094885515414272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.010555371079324447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010469560846401448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.01045093066384482}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010450629392694937}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010413031331065048}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 0.010400629629924163}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010321917850783046}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.010314550370739644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010252979752276493}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 0.01023925454889771}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.01018055908268531}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.010133414138400987}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014865746661435432}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013087325407883656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011984776257118019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011894553383675505}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011803613786643404}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011651272728936101}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011482719446492413}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011352262996312307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011185886357118237}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011130264499406156}]
result = search.search('tomato tomato pear papaya pear kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #477 checking search results for 'tomato tomato pear papaya pear kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #477 checking search results for 'tomato tomato pear papaya pear kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #478 checking search results for 'tomato tomato pear papaya pear kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 0.9997936091221333}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 0.9997622252878343}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9997459021533831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.9997221128133564}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 0.9976932096112554}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.993550852295332}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 0.9934513879149804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 0.9919193707140552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'title': 'N-33', 'score': 0.9912811603017079}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.98967994097092}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 0.9997936091221333}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 0.9997622252878343}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9997459021533831}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 0.9997221128133564}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 0.9976932096112554}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.993550852295332}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 0.9934513879149804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 0.9919193707140552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'title': 'N-33', 'score': 0.9912811603017079}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.98967994097092}]
result = search.search('tomato tomato pear papaya pear kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #478 checking search results for 'tomato tomato pear papaya pear kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #478 checking search results for 'tomato tomato pear papaya pear kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #479 checking search results for 'cherry lime apple peach lime banana pear cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014776438540206285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011771185662325656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011232122801469983}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011189800938730916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011092034230193068}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011062332342363165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010640414714816675}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010637346835700943}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010561843705094474}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010540003506099418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.010534300794643535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.010385246706847212}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.010264573109958283}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.0101351840188089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010056137749344593}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.00993458414263188}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 0.009873108614935202}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.009826218794257009}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.009730843608269348}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.009692604891305055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 0.009662513259690614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.0096582128754997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.009639391249214332}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.009572489964355847}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014776438540206285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011771185662325656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011232122801469983}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011189800938730916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011092034230193068}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011062332342363165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010640414714816675}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010637346835700943}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010561843705094474}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.010540003506099418}]
result = search.search('cherry lime apple peach lime banana pear cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #479 checking search results for 'cherry lime apple peach lime banana pear cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #479 checking search results for 'cherry lime apple peach lime banana pear cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #480 checking search results for 'cherry lime apple peach lime banana pear cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9856711399330631}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9791665626960409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.9786744174724248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.9765219913781745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9738897874355922}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.9732297071686323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.972372733805693}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9683934370188718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9623572520173663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.9572723090986176}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 0.9856711399330631}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9791665626960409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.9786744174724248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.9765219913781745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9738897874355922}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.9732297071686323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.972372733805693}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9683934370188718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.9623572520173663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.9572723090986176}]
result = search.search('cherry lime apple peach lime banana pear cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #480 checking search results for 'cherry lime apple peach lime banana pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #480 checking search results for 'cherry lime apple peach lime banana pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #481 checking search results for 'apricot apple banana papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.01502987774929639}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012938981790955121}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01249366569317795}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012012195995607489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011838647991068403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.01137972308424294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011119200236272286}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011098265317868209}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010976898209624884}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.0109124904802152}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010721121770582306}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010562863648662948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010454501848029202}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010398185190231321}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010322564906808916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.010279567914870674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.010188201859660288}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.010083974050635276}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.010065481756636773}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.01001342297251813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.009974097365122218}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.00996249571989199}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.01502987774929639}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012938981790955121}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01249366569317795}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012012195995607489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011838647991068403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.01137972308424294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011119200236272286}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011098265317868209}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010976898209624884}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.0109124904802152}]
result = search.search('apricot apple banana papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #481 checking search results for 'apricot apple banana papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #481 checking search results for 'apricot apple banana papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #482 checking search results for 'apricot apple banana papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'title': 'N-41', 'score': 0.997919208920706}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9962579520574533}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9948578387310912}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 0.9930922670252733}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'title': 'N-39', 'score': 0.9906067305085817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.987679785381745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'title': 'N-36', 'score': 0.9866568070438736}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9850029106818458}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.983173004503233}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9803605149185421}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'title': 'N-41', 'score': 0.997919208920706}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9962579520574533}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 0.9948578387310912}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 0.9930922670252733}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'title': 'N-39', 'score': 0.9906067305085817}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.987679785381745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'title': 'N-36', 'score': 0.9866568070438736}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9850029106818458}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.983173004503233}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9803605149185421}]
result = search.search('apricot apple banana papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #482 checking search results for 'apricot apple banana papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #482 checking search results for 'apricot apple banana papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #483 checking search results for 'fig blueberry tomato cherry blueberry kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015085331731747397}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012687372004781807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012055218370195993}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011860486077573186}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011785390020537823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011751545690874275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011688146751711878}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011446545544938154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011287004319011607}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011088165046305058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010728297650495993}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010567457970055157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010554250053260036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.01055123368588546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.0104883443887196}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.01032682883562897}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010274102049708321}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010210453875052145}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015085331731747397}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012687372004781807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012055218370195993}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011860486077573186}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011785390020537823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011751545690874275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011688146751711878}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011446545544938154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011287004319011607}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011088165046305058}]
result = search.search('fig blueberry tomato cherry blueberry kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #483 checking search results for 'fig blueberry tomato cherry blueberry kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #483 checking search results for 'fig blueberry tomato cherry blueberry kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #484 checking search results for 'fig blueberry tomato cherry blueberry kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9886371607425757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.9872345131099698}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'title': 'N-16', 'score': 0.9851774105969743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'title': 'Custom Title 60', 'score': 0.9847622004313996}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9841988610004837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9826592728321291}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.9808762000877985}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 0.9796730654221432}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9774472985915986}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.9761674032241549}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9886371607425757}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.9872345131099698}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'title': 'N-16', 'score': 0.9851774105969743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'title': 'Custom Title 60', 'score': 0.9847622004313996}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9841988610004837}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9826592728321291}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.9808762000877985}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 0.9796730654221432}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9774472985915986}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.9761674032241549}]
result = search.search('fig blueberry tomato cherry blueberry kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #484 checking search results for 'fig blueberry tomato cherry blueberry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #484 checking search results for 'fig blueberry tomato cherry blueberry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #485 checking search results for 'fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013371438790729918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013090651714295071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012381151695809443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012355739083682959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012326078540514243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.012122701774986104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.012038453294035877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011916545805988004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.011831050135468216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011736012378240443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011733466741607019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011512156204320409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.01138210273522217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.011356574520041724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.011302700731264232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011302529124864737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.011291254701698296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.011154456645823681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.011142026133579024}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013371438790729918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013090651714295071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012381151695809443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012355739083682959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012326078540514243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.012122701774986104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570144}]
result = search.search('fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #485 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #485 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #486 checking search results for 'fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'title': 'Custom Title 60', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'title': 'Custom Title 66', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #486 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #486 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #487 checking search results for 'pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013371438790729918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013090651714295071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012782602633378081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012381151695809443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012355739083682959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012326078540514243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570144}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.012038453294035877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.01191978150259852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011916545805988004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011733466741607019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011579316303660131}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011512156204320409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.011435617545340325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.01138210273522217}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.011356574520041724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.011302700731264232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011302529124864737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.011291254701698296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.011142026133579024}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013371438790729918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013090651714295071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012782602633378081}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012527514344751578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012381151695809443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012355739083682959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.012326078540514243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.012057315046570144}]
result = search.search('pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #487 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #487 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #488 checking search results for 'pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'title': 'Custom Title 62', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'title': 'Custom Title 100', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'title': 'Custom Title 79', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'title': 'Custom Title 66', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'title': 'N-30', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #488 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #488 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #489 checking search results for 'banana strawberry coconut coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014737806363723176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013154412282057168}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012172770969225106}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01209720890595662}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012084689625197232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012025472148763788}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01196241612037615}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011879545042364964}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.011293100526797776}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011212856807478284}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011092870108477966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.011032026933199195}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010981746750118454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010820473442264772}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010691914765837045}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.010509783610854105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.01050215231545133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.010424975269231685}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.01029869602468648}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014737806363723176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013154412282057168}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012172770969225106}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01209720890595662}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012084689625197232}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012025472148763788}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01196241612037615}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011879545042364964}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.011293100526797776}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.011212856807478284}]
result = search.search('banana strawberry coconut coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #489 checking search results for 'banana strawberry coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #489 checking search results for 'banana strawberry coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #490 checking search results for 'banana strawberry coconut coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9996969576842465}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9981016867177642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9957858641270311}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.994157714474167}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.9938080113542181}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9921293483808412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.9920661724118737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.9903954036961717}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.9886785715777763}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.9880786684781565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.9875374444819012}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9996969576842465}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9981016867177642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9957858641270311}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'title': 'N-32', 'score': 0.994157714474167}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.9938080113542181}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9921293483808412}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.9920661724118737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 0.9903954036961717}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.9886785715777763}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.9880786684781565}]
result = search.search('banana strawberry coconut coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #490 checking search results for 'banana strawberry coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #490 checking search results for 'banana strawberry coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #491 checking search results for 'pear kiwi coconut coconut coconut apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014030286703151505}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012283423141960712}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012154481281548921}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011748507259830726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010863642975646263}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.010614504480262738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010567550265341645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.010417699397578606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.010141985690329692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.009999356383217963}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.009950391201069003}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.009886544808657801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.009877324347081403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.009753161462836888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.009748431099595155}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'title': 'N-18', 'score': 0.009743722330110019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.009675480900347604}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.009648554599346267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.009591196807143824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'title': 'N-13', 'score': 0.009572429250831538}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.009309748933221307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.009286703615743346}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.009247877706265067}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.009238990213907741}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 0.009222956716420783}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.009216907724676909}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 0.009200630366356754}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.009043837966898751}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014030286703151505}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012283423141960712}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012154481281548921}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011748507259830726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.010863642975646263}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.010614504480262738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010567550265341645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.010417699397578606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.010141985690329692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.009999356383217963}]
result = search.search('pear kiwi coconut coconut coconut apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #491 checking search results for 'pear kiwi coconut coconut coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #491 checking search results for 'pear kiwi coconut coconut coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #492 checking search results for 'pear kiwi coconut coconut coconut apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 0.9990749273842215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'title': 'N-39', 'score': 0.9952105033220954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.9873890617031448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.979688535210071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9743883455357449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9657240547572538}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.9515931449907866}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 0.9491728674516652}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9284855748072615}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9267204747140727}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'title': 'N-22', 'score': 0.9990749273842215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'title': 'N-39', 'score': 0.9952105033220954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.9873890617031448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.979688535210071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9743883455357449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 0.9657240547572538}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.9515931449907866}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'title': 'N-4', 'score': 0.9491728674516652}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9284855748072615}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9267204747140727}]
result = search.search('pear kiwi coconut coconut coconut apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #492 checking search results for 'pear kiwi coconut coconut coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #492 checking search results for 'pear kiwi coconut coconut coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #493 checking search results for 'apricot blueberry kiwi tomato papaya tomato blueberry peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015041426620377907}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012896647016986472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.01265135332588989}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011919740160304223}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011673754510205114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011602170665539672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011502225879986006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010939928892472294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.010873935065973988}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.010646763344403513}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.010594616161225983}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.010505263966501959}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010448173736596634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.010395688552897513}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.010176362666729714}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010021575995939428}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.009909430168372169}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 0.00978039737631546}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.00974833869618807}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015041426620377907}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012896647016986472}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.01265135332588989}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011919740160304223}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011673754510205114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011602170665539672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.011502225879986006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.010939928892472294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.010873935065973988}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.010646763344403513}]
result = search.search('apricot blueberry kiwi tomato papaya tomato blueberry peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #493 checking search results for 'apricot blueberry kiwi tomato papaya tomato blueberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #493 checking search results for 'apricot blueberry kiwi tomato papaya tomato blueberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #494 checking search results for 'apricot blueberry kiwi tomato papaya tomato blueberry peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.9999965316231437}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 0.999884053561653}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 0.9865764744130784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9857597812179961}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9829853883653167}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'title': 'Custom Title 60', 'score': 0.9778136292819043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.968188561476285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.9664586021203501}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9664418244413711}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9655479512599532}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.9999965316231437}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'title': 'N-38', 'score': 0.999884053561653}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'title': 'N-48', 'score': 0.9865764744130784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9857597812179961}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9829853883653167}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'title': 'Custom Title 60', 'score': 0.9778136292819043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.968188561476285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'title': 'N-18', 'score': 0.9664586021203501}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9664418244413711}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9655479512599532}]
result = search.search('apricot blueberry kiwi tomato papaya tomato blueberry peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #494 checking search results for 'apricot blueberry kiwi tomato papaya tomato blueberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #494 checking search results for 'apricot blueberry kiwi tomato papaya tomato blueberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #495 checking search results for 'banana apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015061562075969122}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012973365942660887}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012401651915647533}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012381151695809443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012284510225566198}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011990227439793152}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011917491252046358}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011910712548864829}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011736012378240443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.01128056980161341}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011279722676456883}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.011154456645823681}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.01106973908450321}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.01092935780271509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010887891140583776}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010835199605519864}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015061562075969122}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.012973365942660887}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012401651915647533}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012381151695809443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012284510225566198}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011990227439793152}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.011917491252046358}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011910712548864829}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011736012378240443}]
result = search.search('banana apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #495 checking search results for 'banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #495 checking search results for 'banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #496 checking search results for 'banana apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html', 'title': 'N-41', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('banana apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #496 checking search results for 'banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #496 checking search results for 'banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #497 checking search results for 'blueberry strawberry blueberry pear banana apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014986989935687008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013042383869244145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012353379154536288}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012287009941480971}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012157182497394262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011669717700523052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011594783208182963}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011586794405192368}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011014290440585295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010700291264204227}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.010506067559837011}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010477963441259761}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'title': 'N-45', 'score': 0.010321976861057233}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010320092932576444}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.010196036141662692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.01018580148740884}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.01014407717598341}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'title': 'N-5', 'score': 0.010126899024799274}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.010075365548295532}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.010062014635713969}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'title': 'N-19', 'score': 0.009778256318476126}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 0.009776864521104463}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014986989935687008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013042383869244145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012353379154536288}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012287009941480971}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012157182497394262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011669717700523052}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011594783208182963}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011586794405192368}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011014290440585295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.010700291264204227}]
result = search.search('blueberry strawberry blueberry pear banana apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #497 checking search results for 'blueberry strawberry blueberry pear banana apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #497 checking search results for 'blueberry strawberry blueberry pear banana apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #498 checking search results for 'blueberry strawberry blueberry pear banana apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.9830698965721792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9821922011110378}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9756749138791746}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9753912105768379}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.9727345426302734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 0.9710561131929082}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9708851580405102}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9708234858284481}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.9704385213885254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.9693701853131329}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'title': 'N-7', 'score': 0.9830698965721792}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9821922011110378}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9756749138791746}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9753912105768379}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.9727345426302734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 0.9710561131929082}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'title': 'N-21', 'score': 0.9708851580405102}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'title': 'N-1', 'score': 0.9708234858284481}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.9704385213885254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.9693701853131329}]
result = search.search('blueberry strawberry blueberry pear banana apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #498 checking search results for 'blueberry strawberry blueberry pear banana apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #498 checking search results for 'blueberry strawberry blueberry pear banana apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #499 checking search results for 'kiwi kiwi strawberry kiwi papaya banana banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014758301069624872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01327787765048235}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012551476331984916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012105341724206966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011428944735985784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011267199142783247}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011205274543596759}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010662742258612471}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010636458141290295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.010619136871635211}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.010565590370111191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010554737347312285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.010150359196637648}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.01012908810332885}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'title': 'N-15', 'score': 0.010083005071747819}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.00998578533194132}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.009939683808685087}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.009852213978911157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.009735063602970826}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.009648343290511572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'title': 'N-10', 'score': 0.009635307322362908}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.009626806753118418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.009622212726100483}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014758301069624872}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01327787765048235}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012551476331984916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012105341724206966}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011428944735985784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011267199142783247}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011205274543596759}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010662742258612471}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010636458141290295}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.010619136871635211}]
result = search.search('kiwi kiwi strawberry kiwi papaya banana banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #499 checking search results for 'kiwi kiwi strawberry kiwi papaya banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #499 checking search results for 'kiwi kiwi strawberry kiwi papaya banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #500 checking search results for 'kiwi kiwi strawberry kiwi papaya banana banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 0.998478966526304}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 0.9963485575965046}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9931495875535287}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9930029115256893}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 0.9878235336759653}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.9856945751016569}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.9819186821320999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9815167229277484}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 0.9800717665798215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.9797343276852885}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 0.998478966526304}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'title': 'N-47', 'score': 0.9963485575965046}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'title': 'Custom Title 26', 'score': 0.9931495875535287}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.9930029115256893}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'title': 'N-39', 'score': 0.9878235336759653}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'title': 'Custom Title 48', 'score': 0.9856945751016569}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.9819186821320999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'title': 'Custom Title 92', 'score': 0.9815167229277484}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'title': 'N-10', 'score': 0.9800717665798215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.9797343276852885}]
result = search.search('kiwi kiwi strawberry kiwi papaya banana banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #500 checking search results for 'kiwi kiwi strawberry kiwi papaya banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #500 checking search results for 'kiwi kiwi strawberry kiwi papaya banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #501 checking search results for 'apricot blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015150497014052243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013321650001355002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012402035430691793}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012149653562218718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.012008285152381712}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011989355619649172}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011865505887951657}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011736012378240443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011579316303660133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.01149218229803825}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'title': 'N-31', 'score': 0.011351517252844556}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011333628466192054}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.011246801168530536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.011072207612034302}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.010824613117168638}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010692925808903712}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010636402415376452}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015150497014052243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.013321650001355002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012402035430691793}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.012389463375719929}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012149653562218718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.012008285152381712}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011989355619649172}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.011865505887951657}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011736012378240443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.011579316303660133}]
result = search.search('apricot blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #501 checking search results for 'apricot blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #501 checking search results for 'apricot blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #502 checking search results for 'apricot blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'title': 'Custom Title 99', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'title': 'N-8', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0}]
result = search.search('apricot blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #502 checking search results for 'apricot blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #502 checking search results for 'apricot blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #503 checking search results for 'blueberry fig coconut blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015090445161179565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013069842261700085}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01253529977097717}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012312825538461705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012147301897269277}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012097733022950833}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011815499888466868}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011739774998744247}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011625964250778623}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011527808433914568}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.011059236221350008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011022113150759164}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.010919178766638768}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010730258741652407}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010622725496366727}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'title': 'N-29', 'score': 0.010611051284824206}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010606890144736278}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015090445161179565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.013069842261700085}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01253529977097717}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012312825538461705}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.012147301897269277}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.012097733022950833}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011815499888466868}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.011739774998744247}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'title': 'N-28', 'score': 0.011625964250778623}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011527808433914568}]
result = search.search('blueberry fig coconut blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #503 checking search results for 'blueberry fig coconut blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #503 checking search results for 'blueberry fig coconut blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #504 checking search results for 'blueberry fig coconut blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9984103577843827}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'title': 'Custom Title 60', 'score': 0.9942765013870473}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 0.9940186360825154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9919144873907335}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.9917872824609824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.9914634636632592}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 0.9904413057877075}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.9903148195060483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 0.98898661002688}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9889722761013474}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.9984103577843827}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'title': 'Custom Title 60', 'score': 0.9942765013870473}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'title': 'Custom Title 43', 'score': 0.9940186360825154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9919144873907335}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.9917872824609824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'title': 'N-42', 'score': 0.9914634636632592}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'title': 'Custom Title 92', 'score': 0.9904413057877075}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.9903148195060483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'title': 'N-49', 'score': 0.98898661002688}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.9889722761013474}]
result = search.search('blueberry fig coconut blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #504 checking search results for 'blueberry fig coconut blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #504 checking search results for 'blueberry fig coconut blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #505 checking search results for 'peach fig peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014961936025606111}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012836041941861913}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012505731255744605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012337964089431636}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01224679730901728}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011886918377217321}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011678081482571986}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.0116708900260188}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011505253864041094}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011449022951747387}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'title': 'N-23', 'score': 0.011420142847037663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.011377974152696578}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'title': 'N-47', 'score': 0.011294294485371151}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'title': 'N-26', 'score': 0.01126318122624411}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.011208685416259046}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'title': 'N-40', 'score': 0.011103765374564183}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.011028215056890408}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010919512022761176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.010819311149840981}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010772947584882024}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'title': 'N-41', 'score': 0.010673759576289613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'title': 'N-4', 'score': 0.010454307454678798}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.014961936025606111}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012836041941861913}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.012505731255744605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012337964089431636}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.01224679730901728}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011886918377217321}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.011678081482571986}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.0116708900260188}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011505253864041094}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011449022951747387}]
result = search.search('peach fig peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #505 checking search results for 'peach fig peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #505 checking search results for 'peach fig peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #506 checking search results for 'peach fig peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9999554732587923}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9999465321885916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9997230895072647}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9996703046542998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.9996645226272819}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'title': 'N-9', 'score': 0.9996410962400608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.9996372741819651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 0.9996212226669057}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.9985613977333985}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.9985336259360846}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.9982611802782649}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'title': 'N-43', 'score': 0.9999554732587923}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'title': 'N-3', 'score': 0.9999465321885916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.9997230895072647}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'title': 'N-30', 'score': 0.9996703046542998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'title': 'N-6', 'score': 0.9996645226272819}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'title': 'N-9', 'score': 0.9996410962400608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'title': 'N-34', 'score': 0.9996372741819651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'title': 'N-0', 'score': 0.9996212226669057}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.9985613977333985}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'title': 'N-44', 'score': 0.9985336259360846}]
result = search.search('peach fig peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #506 checking search results for 'peach fig peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #506 checking search results for 'peach fig peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #507 checking search results for 'fig strawberry tomato apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012600439921299592}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012185990315886491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01212713071310953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01192346669130035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011736012378240443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01169195897164274}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.011664900787350089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011399149477700488}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011270950450010454}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'title': 'N-46', 'score': 0.011060351520122755}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'title': 'Custom Title 11', 'score': 0.011054853058495491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'title': 'N-14', 'score': 0.010916678263840006}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'title': 'N-20', 'score': 0.010713143539587133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'title': 'Custom Title 22', 'score': 0.010712797369545946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 0.010692925808903712}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'title': 'N-9', 'score': 0.010545495572705564}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'title': 'N-17', 'score': 0.010535465726253976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'title': 'Custom Title 66', 'score': 0.010480479439543416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'title': 'N-29', 'score': 0.0103579375756507}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'title': 'N-3', 'score': 0.010317153264295487}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.010307969958388796}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'title': 'N-16', 'score': 0.010294680794503627}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 0.015258714046735455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'title': 'Custom Title 68', 'score': 0.012600439921299592}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'title': 'Custom Title 10', 'score': 0.012185990315886491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'title': 'N-35', 'score': 0.01212713071310953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.01192346669130035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 0.011736012378240443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'title': 'N-19', 'score': 0.01169195897164274}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'title': 'N-35', 'score': 0.011664900787350089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'title': 'Custom Title 62', 'score': 0.011399149477700488}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'title': 'N-32', 'score': 0.011270950450010454}]
result = search.search('fig strawberry tomato apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #507 checking search results for 'fig strawberry tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #507 checking search results for 'fig strawberry tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #508 checking search results for 'fig strawberry tomato apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'title': 'N-16', 'score': 0.9943607865241}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 0.989965356549019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.9898214542023445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9892172862703357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 0.9890921429026469}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9888989916284994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9888575150023892}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'title': 'Custom Title 27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'title': 'N-16', 'score': 0.9943607865241}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'title': 'Custom Title 67', 'score': 0.989965356549019}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'title': 'N-20', 'score': 0.9898214542023445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'title': 'N-45', 'score': 0.9892172862703357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'title': 'N-25', 'score': 0.9890921429026469}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'title': 'N-40', 'score': 0.9888989916284994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html', 'title': 'N-37', 'score': 0.9888575150023892}]
result = search.search('fig strawberry tomato apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #508 checking search results for 'fig strawberry tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #508 checking search results for 'fig strawberry tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
