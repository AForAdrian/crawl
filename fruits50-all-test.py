
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html')


output = open('fruits50-all-outgoing-failed.txt', 'w')
success_output = open('fruits50-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html']
result = searchdata.get_outgoing_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html\n\n')
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









output = open('fruits50-all-incoming-failed.txt', 'w')
success_output = open('fruits50-all-incoming-passed.txt', 'w')

#Test #51 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html\n\n')
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









output = open('fruits50-all-pagerank-failed.txt', 'w')
success_output = open('fruits50-all-pagerank-passed.txt', 'w')

#Test #102 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html
expected = 0.01808195280176957
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html
expected = 0.022928426413570565
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html
expected = 0.01750679182106982
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html
expected = 0.02478877289603739
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html
expected = 0.01904868764048156
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html
expected = 0.024976447632762886
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html
expected = 0.021020886832165405
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html
expected = 0.019621312459575258
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html
expected = 0.01582493067849243
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html
expected = 0.021203702409582584
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html
expected = 0.021733475880946682
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html
expected = 0.023512486890770116
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html
expected = 0.020521032078930534
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html
expected = 0.020666584367551567
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html
expected = 0.02422492536118724
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html
expected = 0.021296112692564713
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html
expected = 0.024563566260840976
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html
expected = 0.014965155749157563
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html
expected = 0.01866341974192488
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html
expected = 0.02309603479833191
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html
expected = 0.019699810806851036
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html
expected = 0.02252941664731043
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html
expected = 0.015340370467515478
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html
expected = 0.019192833780611134
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html
expected = 0.016464465936013667
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html
expected = 0.0169757927537423
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html
expected = 0.020879121129498537
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html
expected = 0.028196116466136123
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html
expected = 0.015445411901758497
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html
expected = 0.016031653610443078
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html
expected = 0.022453862071676416
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html
expected = 0.019965557177111293
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html
expected = 0.01436886259697471
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html
expected = 0.021687974328279274
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html
expected = 0.022319897048681214
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html
expected = 0.0218509561429526
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html
expected = 0.01973463975614724
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html
expected = 0.015873819376002803
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html
expected = 0.018414962224977762
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html
expected = 0.024517192369952933
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html
expected = 0.01862831362809595
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html
expected = 0.018540350263185165
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html
expected = 0.018011802902362414
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html
expected = 0.01969017211916767
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html
expected = 0.02125532473797621
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html
expected = 0.01873710048205946
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html
expected = 0.01759767856747224
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html
expected = 0.017456501027369117
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html
expected = 0.022437743754489158
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html
expected = 0.017457590517472418
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html\n\n')
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









output = open('fruits50-all-idf-failed.txt', 'w')
success_output = open('fruits50-all-idf-passed.txt', 'w')

#Test #153 checking IDF for word apricot
expected = 0.0892673380970873
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word apple
expected = 0.0892673380970873
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word banana
expected = 0.18442457113742758
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word pear
expected = 0.05889368905356862
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word cherry
expected = 0.05889368905356862
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word fig
expected = 0.12029423371771174
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word lime
expected = 0.21759143507262685
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word coconut
expected = 0.02914634565951651
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word papaya
expected = 0.12029423371771174
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word blueberry
expected = 0.0892673380970873
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word strawberry
expected = 0.0892673380970873
result = searchdata.get_idf('strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word kiwi
expected = 0.02914634565951651
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word peach
expected = 0.0
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word peach\n\n')
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









output = open('fruits50-all-tf-failed.txt', 'w')
success_output = open('fruits50-all-tf-passed.txt', 'w')

#Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word banana
expected = 0.05263157894736842
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word pear
expected = 0.07894736842105263
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word fig
expected = 0.02631578947368421
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word lime
expected = 0.07894736842105263
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word papaya
expected = 0.05263157894736842
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word apricot
expected = 0.07894736842105263
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word peach
expected = 0.13157894736842105
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word kiwi
expected = 0.02631578947368421
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word strawberry
expected = 0.13157894736842105
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word apple
expected = 0.07894736842105263
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word banana
expected = 0.05454545454545454
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word pear
expected = 0.03636363636363636
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word fig
expected = 0.07272727272727272
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word lime
expected = 0.07272727272727272
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word papaya
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apricot
expected = 0.10909090909090909
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word peach
expected = 0.03636363636363636
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word kiwi
expected = 0.09090909090909091
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word strawberry
expected = 0.05454545454545454
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apple
expected = 0.10909090909090909
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word banana
expected = 0.10256410256410256
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word pear
expected = 0.05128205128205128
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word fig
expected = 0.05128205128205128
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word lime
expected = 0.20512820512820512
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word papaya
expected = 0.02564102564102564
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apricot
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word peach
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word kiwi
expected = 0.05128205128205128
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word strawberry
expected = 0.05128205128205128
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apple
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word banana
expected = 0.06976744186046512
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word pear
expected = 0.09302325581395349
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word fig
expected = 0.046511627906976744
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word lime
expected = 0.06976744186046512
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word papaya
expected = 0.023255813953488372
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apricot
expected = 0.09302325581395349
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word peach
expected = 0.09302325581395349
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word kiwi
expected = 0.06976744186046512
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word strawberry
expected = 0.13953488372093023
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apple
expected = 0.023255813953488372
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word banana
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word pear
expected = 0.03076923076923077
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word fig
expected = 0.09230769230769231
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word lime
expected = 0.12307692307692308
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word papaya
expected = 0.015384615384615385
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apricot
expected = 0.09230769230769231
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word peach
expected = 0.046153846153846156
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word kiwi
expected = 0.1076923076923077
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word strawberry
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apple
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word banana
expected = 0.11538461538461539
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word pear
expected = 0.09615384615384616
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word fig
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word lime
expected = 0.038461538461538464
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word papaya
expected = 0.11538461538461539
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word apricot
expected = 0.038461538461538464
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word peach
expected = 0.07692307692307693
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word kiwi
expected = 0.057692307692307696
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word strawberry
expected = 0.057692307692307696
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word apple
expected = 0.057692307692307696
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word banana
expected = 0.08
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word pear
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word fig
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word lime
expected = 0.08
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word papaya
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word apricot
expected = 0.24
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word peach
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word kiwi
expected = 0.04
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word strawberry
expected = 0.08
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word apple
expected = 0.2
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word banana
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word pear
expected = 0.2
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word lime
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word apricot
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word peach
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word kiwi
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word strawberry
expected = 0.13333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word apple
expected = 0.06666666666666667
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word banana
expected = 0.06382978723404255
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word pear
expected = 0.0425531914893617
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word fig
expected = 0.06382978723404255
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word lime
expected = 0.0851063829787234
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word papaya
expected = 0.0851063829787234
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apricot
expected = 0.14893617021276595
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word peach
expected = 0.0851063829787234
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word kiwi
expected = 0.10638297872340426
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word strawberry
expected = 0.1276595744680851
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apple
expected = 0.06382978723404255
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word banana
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word lime
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word apricot
expected = 0.16666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word peach
expected = 0.16666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word kiwi
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word strawberry
expected = 0.08333333333333333
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word apple
expected = 0.16666666666666666
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word tomato
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
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









output = open('fruits50-all-tfidf-failed.txt', 'w')
success_output = open('fruits50-all-tfidf-passed.txt', 'w')

#Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word coconut
expected = 0.0021568465257655214
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word blueberry
expected = 0.006605834923122666
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word banana
expected = 0.026629047105711637
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word pear
expected = 0.00850365442285874
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word papaya
expected = 0.03315723406039083
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word kiwi
expected = 0.00420843820722925
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word apple
expected = 0.006605834923122666
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word coconut
expected = 0.0023366726943873438
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word lime
expected = 0.021658110048863966
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word blueberry
expected = 0.008885284623590783
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word banana
expected = 0.021880960384573822
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word strawberry
expected = 0.008885284623590783
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word pear
expected = 0.005862023007845066
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word papaya
expected = 0.009644030661821538
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word kiwi
expected = 0.006137258156679829
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word apple
expected = 0.0071565936213345204
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word coconut
expected = 0.00507232104076176
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word lime
expected = 0.05857270573666875
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word blueberry
expected = 0.0095440356557343
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word banana
expected = 0.025978512761594803
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word strawberry
expected = 0.0064406193186985735
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word pear
expected = 0.004249167047585765
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word papaya
expected = 0.004393852267309213
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word kiwi
expected = 0.0021029025948996398
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apple
expected = 0.0095440356557343
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word coconut
expected = 0.003365738894720593
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word lime
expected = 0.025126853456597594
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word banana
expected = 0.021296836298815156
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word strawberry
expected = 0.010308343809936275
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word kiwi
expected = 0.003365738894720593
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word apple
expected = 0.019852379465670596
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word coconut
expected = 0.0017523072269786204
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word lime
expected = 0.025640211026962248
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word blueberry
expected = 0.0027113747984100554
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word banana
expected = 0.016463090545135076
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word strawberry
expected = 0.015472850797695514
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word pear
expected = 0.003540747034210253
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word papaya
expected = 0.014175050303884235
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word kiwi
expected = 0.00425101976868384
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apple
expected = 0.007968657650939693
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word coconut
expected = 0.0028358578623939247
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word lime
expected = 0.021171037671366244
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word blueberry
expected = 0.016821991509375966
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word banana
expected = 0.0179439946327521
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word strawberry
expected = 0.016821991509375966
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word pear
expected = 0.007557479465357401
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word papaya
expected = 0.003989782481904419
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word kiwi
expected = 0.0028358578623939247
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apple
expected = 0.0029607176565235346
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word coconut
expected = 0.00425101976868384
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word lime
expected = 0.0194238082016586
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word blueberry
expected = 0.013019718608346355
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word banana
expected = 0.005601647198729673
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word strawberry
expected = 0.0053668409586570725
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word pear
expected = 0.006939825618530336
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word papaya
expected = 0.007232208715625937
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word kiwi
expected = 0.005051982811420633
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word apple
expected = 0.007968657650939693
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word coconut
expected = 0.0058091234174656985
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word blueberry
expected = 0.009202881692036311
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word banana
expected = 0.009676281412663272
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word strawberry
expected = 0.009202881692036311
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word pear
expected = 0.0030899999126882353
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word papaya
expected = 0.01828509564869403
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word kiwi
expected = 0.0015292335560974659
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word apple
expected = 0.01779176676940638
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word coconut
expected = 0.0011521073659389834
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word lime
expected = 0.025126853456597594
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word blueberry
expected = 0.003528591850273347
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word banana
expected = 0.03460302959449238
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word strawberry
expected = 0.006963076611239761
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word pear
expected = 0.002327971189204034
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word papaya
expected = 0.004755034279946171
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word kiwi
expected = 0.004430334702865218
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word apple
expected = 0.010308343809936275
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word coconut
expected = 0.0032782273369262307
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word lime
expected = 0.008371645036182939
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word blueberry
expected = 0.0034344847609663917
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word banana
expected = 0.01400683468593049
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word strawberry
expected = 0.006779751959662912
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word pear
expected = 0.012768822531346282
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word papaya
expected = 0.009136209101438586
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word kiwi
expected = 0.0032782273369262307
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word apple
expected = 0.006779751959662912
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html and word tomato\n\n')
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


#Test #399 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #399 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #399 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #400 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #400 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','strawberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word strawberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #403 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #403 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #405 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #405 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html and word apple\n\n')
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









output = open('fruits50-all-search-failed.txt', 'w')
success_output = open('fruits50-all-search-passed.txt', 'w')

#Test #409 checking search results for 'lime papaya papaya banana kiwi pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025431433122735724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022435484876959007}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02182299887404884}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021462918332169536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021446674507065888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020558434257308147}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02026793829655089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.020238730353532432}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020189082267473974}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.020158055363515504}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020155612096383717}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.020143399026885455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.019521602826827914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.019313215157790914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.019204463733533687}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025431433122735724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022435484876959007}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02182299887404884}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021462918332169536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021446674507065888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020558434257308147}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02026793829655089}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.020238730353532432}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020189082267473974}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.020158055363515504}]
result = search.search('lime papaya papaya banana kiwi pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #409 checking search results for 'lime papaya papaya banana kiwi pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'lime papaya papaya banana kiwi pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'lime papaya papaya banana kiwi pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9878413952032575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9860607555449992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9814982175955215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9668694055121289}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 0.9654774904848004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 0.9596397920488}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9588373819482403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9558675591600401}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9521489161416418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9459340222394582}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9878413952032575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9860607555449992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9814982175955215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9668694055121289}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 0.9654774904848004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 0.9596397920488}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9588373819482403}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9558675591600401}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9521489161416418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9459340222394582}]
result = search.search('lime papaya papaya banana kiwi pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #410 checking search results for 'lime papaya papaya banana kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'lime papaya papaya banana kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'blueberry strawberry lime lime papaya apple blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027223697181145676}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023111428867966292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02295442143360212}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022809640796863134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02252837053089174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021723467494999645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02080586164363606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020419367665059147}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.02039735652252317}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.020375491425717162}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020365188324215633}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.02027401434279367}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020202223343549066}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.019856718937289977}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.019855800363121467}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.019399721151017946}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027223697181145676}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023111428867966292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02295442143360212}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022809640796863134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02252837053089174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021723467494999645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02080586164363606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020419367665059147}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.02039735652252317}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.020375491425717162}]
result = search.search('blueberry strawberry lime lime papaya apple blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #411 checking search results for 'blueberry strawberry lime lime papaya apple blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'blueberry strawberry lime lime papaya apple blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'blueberry strawberry lime lime papaya apple blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9862336446262023}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9805104773417481}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9754215703086329}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9731894761842234}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9713846912402462}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.971018570036937}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9701075391483627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9655642410751835}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.965512297193185}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.958606451648933}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9862336446262023}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9805104773417481}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9754215703086329}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9731894761842234}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9713846912402462}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.971018570036937}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9701075391483627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9655642410751835}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.965512297193185}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.958606451648933}]
result = search.search('blueberry strawberry lime lime papaya apple blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #412 checking search results for 'blueberry strawberry lime lime papaya apple blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'blueberry strawberry lime lime papaya apple blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'tomato kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022437743754489158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022319897048681214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.0218509561429526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021687974328279274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}]
result = search.search('tomato kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #413 checking search results for 'tomato kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'tomato kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'tomato kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}]
result = search.search('tomato kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #414 checking search results for 'tomato kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'tomato kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'coconut kiwi apple peach lime apple banana coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02544246951228458}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.023447478407276564}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02293251672269751}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022222241120763823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021969691966278525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021631754150958048}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.02110208822078631}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02106485191366782}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020658372123079742}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020394749189228543}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.020292596953975655}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.020256772720294604}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.019882555813388575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 0.019750694512070795}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.019722611553086373}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02544246951228458}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.023447478407276564}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02293251672269751}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022222241120763823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021969691966278525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021631754150958048}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.02110208822078631}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02106485191366782}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020658372123079742}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020394749189228543}]
result = search.search('coconut kiwi apple peach lime apple banana coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #415 checking search results for 'coconut kiwi apple peach lime apple banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'coconut kiwi apple peach lime apple banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'coconut kiwi apple peach lime apple banana coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 0.9969790109680611}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9910784951274844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.9903955301351448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9899683112006407}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9848411020130662}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9768011336652642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9753335250853334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9742813648310593}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 0.973993399409086}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9720433170839716}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 0.9969790109680611}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9910784951274844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.9903955301351448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9899683112006407}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9848411020130662}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9768011336652642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9753335250853334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9742813648310593}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 0.973993399409086}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9720433170839716}]
result = search.search('coconut kiwi apple peach lime apple banana coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #416 checking search results for 'coconut kiwi apple peach lime apple banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'coconut kiwi apple peach lime apple banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'apricot coconut lime blueberry blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.024747671084195087}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.023798218525060942}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.023005253518120702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022972268075179332}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02281328969177735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022010399474649167}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02199814723914307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021470345154719822}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02115219782255921}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02083988618246135}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.02051718360454032}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.02035383390760064}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.024747671084195087}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.023798218525060942}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.023005253518120702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022972268075179332}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02281328969177735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022010399474649167}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02199814723914307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021470345154719822}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02115219782255921}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02083988618246135}]
result = search.search('apricot coconut lime blueberry blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #417 checking search results for 'apricot coconut lime blueberry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'apricot coconut lime blueberry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'apricot coconut lime blueberry blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9977995153830543}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.9962098056293197}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9960693997474509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9949784289721222}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9889135704709101}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9888841570291166}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9883418695618282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9800991863340409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9797043897803135}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9676226919345932}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9977995153830543}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.9962098056293197}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9960693997474509}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9949784289721222}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9889135704709101}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9888841570291166}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9883418695618282}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9800991863340409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9797043897803135}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9676226919345932}]
result = search.search('apricot coconut lime blueberry blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #418 checking search results for 'apricot coconut lime blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'apricot coconut lime blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'peach cherry coconut blueberry banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027641818981134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.024739920807467394}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.023463704580762888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02317194372227718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.022390575832508995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02230291677532468}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022202716056845935}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02146248365062455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02125445040578245}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.021138880396474477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.021120295952489467}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020854741199556447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020821619664554498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.02079999784725834}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020501690141474793}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027641818981134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.024739920807467394}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.023463704580762888}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02317194372227718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.022390575832508995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02230291677532468}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022202716056845935}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02146248365062455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02125445040578245}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.021138880396474477}]
result = search.search('peach cherry coconut blueberry banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #419 checking search results for 'peach cherry coconut blueberry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'peach cherry coconut blueberry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'peach cherry coconut blueberry banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9993479661532418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.998029265556029}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.996210411264466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9959424172144785}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9940401804456589}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 0.9924077145942778}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.991872130470576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9905205156565519}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9899464830567287}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.988815019259102}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9993479661532418}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.998029265556029}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.996210411264466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9959424172144785}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9940401804456589}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 0.9924077145942778}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.991872130470576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9905205156565519}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9899464830567287}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.988815019259102}]
result = search.search('peach cherry coconut blueberry banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #420 checking search results for 'peach cherry coconut blueberry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'peach cherry coconut blueberry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'blueberry fig kiwi tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026635902775910117}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840983}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02443399711254364}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024158877608706587}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.023673331985333536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023501592337363625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02308183513470214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022506360956726923}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.02243774375448916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.022371900081297018}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021900098054801583}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021829359538684586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021377456910254222}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026635902775910117}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840983}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02443399711254364}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024158877608706587}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.023673331985333536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023501592337363625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02308183513470214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022506360956726923}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.02243774375448916}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.022371900081297018}]
result = search.search('blueberry fig kiwi tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #421 checking search results for 'blueberry fig kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'blueberry fig kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'blueberry fig kiwi tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9995366481879563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9993851904123909}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.999011640308702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.996302379707309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9953750630081637}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9930084045903507}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9928992403282507}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9995366481879563}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9993851904123909}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.999011640308702}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.996302379707309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9953750630081637}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9930084045903507}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9928992403282507}]
result = search.search('blueberry fig kiwi tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #422 checking search results for 'blueberry fig kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'blueberry fig kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'lime peach cherry kiwi cherry apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026438473838377264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022840545545941674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02277836611524048}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022526882587736767}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.022499646458277747}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022461230578036215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022167514926309174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021601798286920375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02150000026119359}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02149956985571103}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.02098333477619014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.02090631024430915}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.020881071648115524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020594840038597434}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026438473838377264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022840545545941674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02277836611524048}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022526882587736767}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.022499646458277747}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022461230578036215}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022167514926309174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021601798286920375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02150000026119359}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02149956985571103}]
result = search.search('lime peach cherry kiwi cherry apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #423 checking search results for 'lime peach cherry kiwi cherry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'lime peach cherry kiwi cherry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'lime peach cherry kiwi cherry apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.9922044169366575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9904655106720294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.989438858593724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9889472407952759}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9872473098635248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9842345123910701}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9839189514205812}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 0.9824261897756745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 0.981876357206195}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.97973221601117}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.97962372876763}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.9922044169366575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9904655106720294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.989438858593724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9889472407952759}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9872473098635248}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9842345123910701}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9839189514205812}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 0.9824261897756745}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 0.981876357206195}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.97973221601117}]
result = search.search('lime peach cherry kiwi cherry apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #424 checking search results for 'lime peach cherry kiwi cherry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'lime peach cherry kiwi cherry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'papaya fig cherry fig coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.023221368416192}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022881165552560284}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022842890439733386}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02208277435311914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022074799095469375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.021847007675061862}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02184501054439984}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021831893232201142}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021483145392484387}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021214044606030075}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.02108769032107687}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020900149150884208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.020603453482679727}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.02052865941550525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020507745302588663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.020430590446487783}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 0.020404485192431786}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.023221368416192}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022881165552560284}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022842890439733386}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02208277435311914}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022074799095469375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.021847007675061862}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02184501054439984}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021831893232201142}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021483145392484387}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021214044606030075}]
result = search.search('papaya fig cherry fig coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #425 checking search results for 'papaya fig cherry fig coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'papaya fig cherry fig coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'papaya fig cherry fig coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9945286871950587}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9942562993538194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9890394883446917}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9882702641285832}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 0.9873177313455193}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9822130527139294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.9801993993252891}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9760999447229708}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9731495293907997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9696216678121448}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9945286871950587}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9942562993538194}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9890394883446917}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9882702641285832}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 0.9873177313455193}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9822130527139294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.9801993993252891}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9760999447229708}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9731495293907997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9696216678121448}]
result = search.search('papaya fig cherry fig coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #426 checking search results for 'papaya fig cherry fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'papaya fig cherry fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022437743754489158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022319897048681214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.0218509561429526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021687974328279274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #427 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #428 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'papaya apricot apple tomato fig pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025290305547544092}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.021846273776126905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021764926085421743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021605360064625455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02132142075942718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021266983058231752}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.021150770550826266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021130902855890695}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021026989719883073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021015682412743087}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02100307615005458}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.02090712092767171}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020700597593522992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.020336599179962705}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025290305547544092}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.021846273776126905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021764926085421743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021605360064625455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02132142075942718}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021266983058231752}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.021150770550826266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021130902855890695}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021026989719883073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021015682412743087}]
result = search.search('papaya apricot apple tomato fig pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #429 checking search results for 'papaya apricot apple tomato fig pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'papaya apricot apple tomato fig pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'papaya apricot apple tomato fig pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9866118451731459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9789414214669847}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9762727845193572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9757660314696937}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9696256624410353}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9669729098034948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9574587151597818}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9567766868142905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9540025050479748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9490340358399145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9488779785166517}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9866118451731459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9789414214669847}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9762727845193572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9757660314696937}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9696256624410353}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9669729098034948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9574587151597818}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9567766868142905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9540025050479748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9490340358399145}]
result = search.search('papaya apricot apple tomato fig pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #430 checking search results for 'papaya apricot apple tomato fig pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'papaya apricot apple tomato fig pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'apricot lime papaya peach fig fig fig lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.0238053415354272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022859455491910464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02257346794324805}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02241165649298255}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022232895521745552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021948137077561252}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021387143263736186}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02130158880109752}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021159603313418377}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.021007035620564732}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.0207632945891559}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.02043924194532696}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020164660217253997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.02004977787682784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.020017357330378075}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.0238053415354272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022859455491910464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02257346794324805}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02241165649298255}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022232895521745552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021948137077561252}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021387143263736186}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02130158880109752}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021159603313418377}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.021007035620564732}]
result = search.search('apricot lime papaya peach fig fig fig lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #431 checking search results for 'apricot lime papaya peach fig fig fig lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'apricot lime papaya peach fig fig fig lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'apricot lime papaya peach fig fig fig lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.9904624868267585}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9897567132848912}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.9864258291560924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9792296735768348}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9774616054644658}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.973594993701334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9723301451797726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9657810830344227}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 0.965114545776429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9522868569536221}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.9904624868267585}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9897567132848912}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.9864258291560924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9792296735768348}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9774616054644658}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.973594993701334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9723301451797726}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9657810830344227}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 0.965114545776429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9522868569536221}]
result = search.search('apricot lime papaya peach fig fig fig lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #432 checking search results for 'apricot lime papaya peach fig fig fig lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'apricot lime papaya peach fig fig fig lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'peach blueberry blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022437743754489158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022319897048681214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.0218509561429526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021687974328279274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}]
result = search.search('peach blueberry blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #433 checking search results for 'peach blueberry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'peach blueberry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'peach blueberry blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}]
result = search.search('peach blueberry blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #434 checking search results for 'peach blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'peach blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'kiwi apricot blueberry pear blueberry cherry apple lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.024467690423337327}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02290422770582669}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022602804168991353}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02211626525159383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02188449085621793}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02143522570435496}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021411947219055514}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02134777821336885}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02134647313448259}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020575656896850158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.02023545276715398}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.020137171307063394}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.01976973410525851}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.024467690423337327}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02290422770582669}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022602804168991353}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02211626525159383}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02188449085621793}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02143522570435496}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021411947219055514}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02134777821336885}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02134647313448259}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020575656896850158}]
result = search.search('kiwi apricot blueberry pear blueberry cherry apple lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #435 checking search results for 'kiwi apricot blueberry pear blueberry cherry apple lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'kiwi apricot blueberry pear blueberry cherry apple lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'kiwi apricot blueberry pear blueberry cherry apple lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9916952371184048}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9842882060521709}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9805243100401071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9788961812515455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.9771269185460105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9746426154377825}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9705320370010432}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9566873683322626}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9553843137492672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9543358219368792}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9916952371184048}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9842882060521709}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9805243100401071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9788961812515455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.9771269185460105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9746426154377825}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9705320370010432}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9566873683322626}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9553843137492672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9543358219368792}]
result = search.search('kiwi apricot blueberry pear blueberry cherry apple lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #436 checking search results for 'kiwi apricot blueberry pear blueberry cherry apple lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'kiwi apricot blueberry pear blueberry cherry apple lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'apple apricot apple kiwi tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02438661492843875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.024336946960861902}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.02316067287367301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.022126976906512073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.0215912936129846}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021578215351394803}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.021414378613923413}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02095778769143437}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020946711011414834}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.02079675332734445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02072134828889362}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020582432817210387}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.020578901902025895}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02438661492843875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.024336946960861902}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.02316067287367301}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.022126976906512073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.0215912936129846}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021578215351394803}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.021414378613923413}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02095778769143437}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020946711011414834}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.02079675332734445}]
result = search.search('apple apricot apple kiwi tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #437 checking search results for 'apple apricot apple kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'apple apricot apple kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'apple apricot apple kiwi tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9989335179152784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 0.9969843768535838}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9969643160380142}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.9946740458881331}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9912636106206324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.9911806518206818}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9895666330000464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9878798809187396}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9857901915292314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9681763113813183}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9989335179152784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 0.9969843768535838}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9969643160380142}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.9946740458881331}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9912636106206324}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.9911806518206818}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9895666330000464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9878798809187396}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9857901915292314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9681763113813183}]
result = search.search('apple apricot apple kiwi tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #438 checking search results for 'apple apricot apple kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'apple apricot apple kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'fig apricot apple coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02397366223178339}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02362981309413001}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022755113534390102}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022449285130919802}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02155856663057165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021521220395271174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021477343145667946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02109072038644415}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02070575048707145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020676357097348674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02059124351143071}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.02051343359356078}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.020284552794944996}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 0.02019375756112475}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.01988574543784516}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.01973008058989736}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.01969981080685104}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02397366223178339}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02362981309413001}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022755113534390102}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022449285130919802}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02155856663057165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021521220395271174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021477343145667946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02109072038644415}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02070575048707145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020676357097348674}]
result = search.search('fig apricot apple coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #439 checking search results for 'fig apricot apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'fig apricot apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'fig apricot apple coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'title': 'N-20', 'score': 0.9987494433243532}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9968264493663852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 0.9887729408872289}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 0.9840517515616671}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9830754693739461}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9830433287634616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9829017551982433}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9781519170963034}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'title': 'N-20', 'score': 0.9987494433243532}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9968264493663852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 0.9887729408872289}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 0.9840517515616671}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9830754693739461}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9830433287634616}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9829017551982433}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9781519170963034}]
result = search.search('fig apricot apple coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #440 checking search results for 'fig apricot apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'fig apricot apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022437743754489158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022319897048681214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.0218509561429526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021687974328279274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #441 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #442 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'pear cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026830622684227645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762893}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.024788772896037398}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.0237862141558737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02295354041882092}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02287937361247579}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02280702152418634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.022529416647310434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022392977438062844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.02193441895665978}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946686}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021605105066206207}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026830622684227645}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762893}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.024788772896037398}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.0237862141558737}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02295354041882092}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02287937361247579}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02280702152418634}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.022529416647310434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022392977438062844}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.02193441895665978}]
result = search.search('pear cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #443 checking search results for 'pear cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'pear cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'pear cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9972884560607339}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.9961790224933542}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9972884560607339}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.9961790224933542}]
result = search.search('pear cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #444 checking search results for 'pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'lime apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028059917364751243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024017740207701973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.023764430179387497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022832158594502924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021895302943969377}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021589607978305576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021580438309521673}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.021203702409582588}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.021020886832165405}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028059917364751243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024017740207701973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.023764430179387497}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022832158594502924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021895302943969377}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021589607978305576}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021580438309521673}]
result = search.search('lime apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #445 checking search results for 'lime apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'lime apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'lime apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}]
result = search.search('lime apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #446 checking search results for 'lime apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'lime apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'fig banana kiwi apricot cherry lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026109509439581024}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.023030743666569972}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02274949928617327}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02257447484740123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02162266935612666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021422492556134203}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021380328731332415}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021040216849436917}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02077795115129127}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020409866747893555}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.02027528615981049}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.02008083876300111}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.01990332575093449}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.019794307557429502}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.01947660817317261}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026109509439581024}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.023030743666569972}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02274949928617327}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02257447484740123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02162266935612666}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021422492556134203}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021380328731332415}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021040216849436917}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02077795115129127}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020409866747893555}]
result = search.search('fig banana kiwi apricot cherry lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #447 checking search results for 'fig banana kiwi apricot cherry lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'fig banana kiwi apricot cherry lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'fig banana kiwi apricot cherry lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9899266282548058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.9890865080618368}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.987563174875038}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.985691045163875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.984389972296924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9819980844070506}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9809597603038073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9802172541358886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9784619305195955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9775251851505374}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9899266282548058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.9890865080618368}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.987563174875038}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.985691045163875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.984389972296924}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9819980844070506}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9809597603038073}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9802172541358886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9784619305195955}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9775251851505374}]
result = search.search('fig banana kiwi apricot cherry lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #448 checking search results for 'fig banana kiwi apricot cherry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'fig banana kiwi apricot cherry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'strawberry blueberry blueberry blueberry apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02368395210159446}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.023100128815505525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022767059748069803}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.022358561308676677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02230166888648157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021535752209679692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021013948743474023}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02096058643713114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.01981138737908863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.019769593411310717}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.01918434895485365}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.019184126518015317}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.019179819118750267}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.01889559290538999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.018773523973101183}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02368395210159446}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.023100128815505525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022767059748069803}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.022358561308676677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02230166888648157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021535752209679692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021013948743474023}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02096058643713114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.01981138737908863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.019769593411310717}]
result = search.search('strawberry blueberry blueberry blueberry apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #449 checking search results for 'strawberry blueberry blueberry blueberry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'strawberry blueberry blueberry blueberry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'strawberry blueberry blueberry blueberry apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9995579169884724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9982572443568009}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9932219595582701}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.9922782120901986}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9900830370357178}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.985756210832958}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9567924679747734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.9248764738346498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9246860039295575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9230192104046945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.9229568708805674}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9995579169884724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9982572443568009}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9932219595582701}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.9922782120901986}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9900830370357178}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.985756210832958}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9567924679747734}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.9248764738346498}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9246860039295575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9230192104046945}]
result = search.search('strawberry blueberry blueberry blueberry apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #450 checking search results for 'strawberry blueberry blueberry blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'strawberry blueberry blueberry blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'banana apricot pear kiwi peach fig apple banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02669542382036688}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.021969398829741145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021835586568262316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021315481077206766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02121134870313102}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.01931728072746465}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.01910934987729485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.018568561052072156}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.018388906323988208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.01838696122630557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.018361895397053588}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.018286085768456944}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 0.01811558847846262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.018070674841528692}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.017986266977083932}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.01776371509914134}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.017763057824798905}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.017758503382638013}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.017466209259237996}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.01742297041950891}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02669542382036688}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.021969398829741145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021835586568262316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021315481077206766}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02121134870313102}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.01931728072746465}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.01910934987729485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.018568561052072156}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.018388906323988208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.01838696122630557}]
result = search.search('banana apricot pear kiwi peach fig apple banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #451 checking search results for 'banana apricot pear kiwi peach fig apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'banana apricot pear kiwi peach fig apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'banana apricot pear kiwi peach fig apple banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.991831657058946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9900720911969455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9821120305601118}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9807672364038942}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9724646253976059}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9700649882914679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 0.9668298729468878}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9467766191286806}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.944226044153309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9414956913970179}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.991831657058946}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9900720911969455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9821120305601118}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9807672364038942}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9724646253976059}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9700649882914679}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 0.9668298729468878}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9467766191286806}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.944226044153309}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9414956913970179}]
result = search.search('banana apricot pear kiwi peach fig apple banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #452 checking search results for 'banana apricot pear kiwi peach fig apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'banana apricot pear kiwi peach fig apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'peach coconut lime lime apricot peach apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028099021786553494}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023949951561032377}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.023654476300907442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022559959862615272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022403953129831473}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02235293281859438}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.02169321109375239}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021396851371008625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02120489383301621}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.021055017830500646}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020654901134867114}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.020355451941848894}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020342393396352885}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020235783383539444}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028099021786553494}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023949951561032377}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.023654476300907442}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022559959862615272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022403953129831473}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02235293281859438}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.02169321109375239}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021396851371008625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02120489383301621}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.021055017830500646}]
result = search.search('peach coconut lime lime apricot peach apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #453 checking search results for 'peach coconut lime lime apricot peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'peach coconut lime lime apricot peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'peach coconut lime lime apricot peach apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9981473378940923}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9977772669269266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.99725271756077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9968110133957592}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9965564520312845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9949171435748797}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9905761539781285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9839297061076459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.982589426401446}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.9768635494488457}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9981473378940923}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9977772669269266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.99725271756077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9968110133957592}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9965564520312845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9949171435748797}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9905761539781285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9839297061076459}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.982589426401446}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.9768635494488457}]
result = search.search('peach coconut lime lime apricot peach apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #454 checking search results for 'peach coconut lime lime apricot peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'peach coconut lime lime apricot peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'papaya peach papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022437743754489158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022319897048681214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.0218509561429526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021687974328279274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}]
result = search.search('papaya peach papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #455 checking search results for 'papaya peach papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'papaya peach papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'papaya peach papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}]
result = search.search('papaya peach papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #456 checking search results for 'papaya peach papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'papaya peach papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'pear coconut lime blueberry apricot lime kiwi' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02792032723222859}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02439843785235863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02395618179110366}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021538046091542525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021411913945245605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02107917007154439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.02090908403170014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020653729076496104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.02059817630783476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020536569582383875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02041548542730444}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02038788539827668}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.020194969972381904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020140281396186184}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.019706563137006132}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.019582820282214287}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.01957916547895649}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02792032723222859}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02439843785235863}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02395618179110366}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021538046091542525}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021411913945245605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02107917007154439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.02090908403170014}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020653729076496104}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.02059817630783476}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020536569582383875}]
result = search.search('pear coconut lime blueberry apricot lime kiwi',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #457 checking search results for 'pear coconut lime blueberry apricot lime kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'pear coconut lime blueberry apricot lime kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'pear coconut lime blueberry apricot lime kiwi' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.995156275816482}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9946020989242622}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9940613376552804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9921217575232242}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9910078907545807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9902188929373036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.989204907064599}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9837104014855416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.979890928118036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.9752729524985302}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.995156275816482}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9946020989242622}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9940613376552804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9921217575232242}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9910078907545807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9902188929373036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.989204907064599}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9837104014855416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.979890928118036}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.9752729524985302}]
result = search.search('pear coconut lime blueberry apricot lime kiwi',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #458 checking search results for 'pear coconut lime blueberry apricot lime kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'pear coconut lime blueberry apricot lime kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'papaya cherry banana pear apricot coconut papaya tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026649964075665764}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022806757110759093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021915324594429728}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.020749084805214105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020743079686627978}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.020216778722816277}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.02005076539379485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.019915546679678618}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.019872563383718154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.01975365687695715}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.019299005811440815}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 0.019165292932698443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.019079976076521468}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.01885881803582018}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026649964075665764}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022806757110759093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.021915324594429728}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.020749084805214105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020743079686627978}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.020216778722816277}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.02005076539379485}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.019915546679678618}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.019872563383718154}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.01975365687695715}]
result = search.search('papaya cherry banana pear apricot coconut papaya tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #459 checking search results for 'papaya cherry banana pear apricot coconut papaya tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'papaya cherry banana pear apricot coconut papaya tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'papaya cherry banana pear apricot coconut papaya tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 0.9859065562294199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9825968510638392}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9758579263468877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9740616586152053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9557257792239491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9492984906895283}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.945625674539429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9456008165086689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9453722643761096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9451643494121856}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 0.9447312855678657}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 0.9859065562294199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9825968510638392}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9758579263468877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9740616586152053}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9557257792239491}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9492984906895283}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.945625674539429}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9456008165086689}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9453722643761096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9451643494121856}]
result = search.search('papaya cherry banana pear apricot coconut papaya tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #460 checking search results for 'papaya cherry banana pear apricot coconut papaya tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'papaya cherry banana pear apricot coconut papaya tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022437743754489158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022319897048681214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.0218509561429526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021687974328279274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #461 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #462 checking search results for 'blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #462 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #462 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #463 checking search results for 'peach apple banana tomato strawberry banana papaya coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027347528959979786}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021964580857210207}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.021276809269490684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.021262576014738813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021126518261616118}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021017360829917047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.020785286494271665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.02038410523592819}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.02015811508752954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.019639016537198774}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.01909220704202852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.018869236845146933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.018732590513070704}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.018670715489178875}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.01865491286316279}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.018648730712834648}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027347528959979786}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021964580857210207}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.021276809269490684}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.021262576014738813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021126518261616118}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021017360829917047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.020785286494271665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.02038410523592819}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.02015811508752954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.019639016537198774}]
result = search.search('peach apple banana tomato strawberry banana papaya coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #463 checking search results for 'peach apple banana tomato strawberry banana papaya coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #463 checking search results for 'peach apple banana tomato strawberry banana papaya coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #464 checking search results for 'peach apple banana tomato strawberry banana papaya coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9894801820134093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.9801575752389665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9782094851698855}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9778686612603495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9752611650540743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9717637977396414}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9699040998367452}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9697071964032062}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9670501370810438}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.953266461000448}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9894801820134093}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.9801575752389665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9782094851698855}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9778686612603495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9752611650540743}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9717637977396414}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9699040998367452}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9697071964032062}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9670501370810438}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.953266461000448}]
result = search.search('peach apple banana tomato strawberry banana papaya coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #464 checking search results for 'peach apple banana tomato strawberry banana papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #464 checking search results for 'peach apple banana tomato strawberry banana papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #465 checking search results for 'cherry tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022319897048681214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.0218509561429526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021687974328279274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}]
result = search.search('cherry tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #465 checking search results for 'cherry tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #465 checking search results for 'cherry tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #466 checking search results for 'cherry tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}]
result = search.search('cherry tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #466 checking search results for 'cherry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #466 checking search results for 'cherry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #467 checking search results for 'coconut apple kiwi strawberry banana' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027500314441871475}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022942423033897614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02244520528595911}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022240741062522457}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.022190580576788594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021675379509875945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021149816862457982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020967932762014085}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020916859514129464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020772432397772985}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.02070853725038962}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020339918441134204}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02022121969893055}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.019945057023577125}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027500314441871475}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022942423033897614}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02244520528595911}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022240741062522457}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.022190580576788594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021675379509875945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021149816862457982}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020967932762014085}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020916859514129464}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020772432397772985}]
result = search.search('coconut apple kiwi strawberry banana',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #467 checking search results for 'coconut apple kiwi strawberry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #467 checking search results for 'coconut apple kiwi strawberry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #468 checking search results for 'coconut apple kiwi strawberry banana' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9977653946081549}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.9964535684915521}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9930158799262938}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9881805921711997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9866213065838787}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.98496028211355}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9846761089017487}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.980429849840721}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9792698286121557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.977162494384538}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9977653946081549}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.9964535684915521}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9930158799262938}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9881805921711997}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9866213065838787}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.98496028211355}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9846761089017487}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.980429849840721}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9792698286121557}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.977162494384538}]
result = search.search('coconut apple kiwi strawberry banana',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #468 checking search results for 'coconut apple kiwi strawberry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #468 checking search results for 'coconut apple kiwi strawberry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #469 checking search results for 'strawberry fig apricot lime tomato apple lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02749539316064094}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023735657771873867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02323197999002452}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02153640376828439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021054011331736962}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.02105048712468029}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02099505359998656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.020802952802969853}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020350268094357294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020307348845837146}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02015636285112549}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.01956630133573852}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.019429737059517}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02749539316064094}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023735657771873867}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02323197999002452}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02153640376828439}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021054011331736962}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.02105048712468029}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02099505359998656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.020802952802969853}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020350268094357294}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020307348845837146}]
result = search.search('strawberry fig apricot lime tomato apple lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #469 checking search results for 'strawberry fig apricot lime tomato apple lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #469 checking search results for 'strawberry fig apricot lime tomato apple lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #470 checking search results for 'strawberry fig apricot lime tomato apple lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.991469901529047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9903629977042908}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9862905410624496}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9850417831057859}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9751482333981434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9746707233575045}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.9681229976790949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9636177272960058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9625975258777411}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.9457901895565035}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.991469901529047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9903629977042908}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9862905410624496}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9850417831057859}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9751482333981434}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9746707233575045}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.9681229976790949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9636177272960058}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9625975258777411}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.9457901895565035}]
result = search.search('strawberry fig apricot lime tomato apple lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #470 checking search results for 'strawberry fig apricot lime tomato apple lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #470 checking search results for 'strawberry fig apricot lime tomato apple lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #471 checking search results for 'peach pear pear lime' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026231809639625334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.024776747506242466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.023690508698014145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023397721980689408}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023358200653488016}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02294632020497667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02277573040380165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022218578066014807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022042068994437943}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.021298673609179985}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021286361188409753}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.02118473183376}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.02114253034793046}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.020901755960303005}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02074013323466623}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 0.020512092993230056}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.02049248615531378}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.026231809639625334}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.024776747506242466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.023690508698014145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023397721980689408}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023358200653488016}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02294632020497667}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02277573040380165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022218578066014807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022042068994437943}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.021298673609179985}]
result = search.search('peach pear pear lime',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #471 checking search results for 'peach pear pear lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #471 checking search results for 'peach pear pear lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #472 checking search results for 'peach pear pear lime' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.999600071514662}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 0.9995643939512352}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.999514885636116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9991053177668627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 0.9935675406085808}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9935177360675759}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.9934862483300979}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9934381149046949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9933403188245601}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9921733280361162}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.999600071514662}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 0.9995643939512352}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.999514885636116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9991053177668627}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 0.9935675406085808}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9935177360675759}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.9934862483300979}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9934381149046949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9933403188245601}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9921733280361162}]
result = search.search('peach pear pear lime',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #472 checking search results for 'peach pear pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #472 checking search results for 'peach pear pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #473 checking search results for 'peach cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022319897048681214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.0218509561429526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021687974328279274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}]
result = search.search('peach cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #473 checking search results for 'peach cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #473 checking search results for 'peach cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #474 checking search results for 'peach cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}]
result = search.search('peach cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #474 checking search results for 'peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #474 checking search results for 'peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #475 checking search results for 'cherry papaya pear papaya strawberry peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02770233214731034}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02256881527250298}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022223571645710264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021870516968343297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.02129931625167696}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021127985032636236}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 0.020440174619379813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.02040264334476839}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02035401078878325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.019808380915890343}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.019694508889941335}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.019397310020241622}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.019346641378096385}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.01920325246012936}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.0190357262414409}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.019028068337674314}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.018986868474390035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.018857728546556023}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02770233214731034}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02256881527250298}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022223571645710264}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021870516968343297}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.02129931625167696}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021127985032636236}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 0.020440174619379813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.02040264334476839}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02035401078878325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.019808380915890343}]
result = search.search('cherry papaya pear papaya strawberry peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #475 checking search results for 'cherry papaya pear papaya strawberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #475 checking search results for 'cherry papaya pear papaya strawberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #476 checking search results for 'cherry papaya pear papaya strawberry peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9997308645772448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9910347416581169}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 0.9890446459780148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9874967909030489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9825400856441722}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9824875060571259}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 0.9821349569044511}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9740202776043165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9705890863533406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9698971323012087}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9997308645772448}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9910347416581169}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 0.9890446459780148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9874967909030489}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9825400856441722}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9824875060571259}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 0.9821349569044511}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9740202776043165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9705890863533406}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9698971323012087}]
result = search.search('cherry papaya pear papaya strawberry peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #476 checking search results for 'cherry papaya pear papaya strawberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #476 checking search results for 'cherry papaya pear papaya strawberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #477 checking search results for 'banana strawberry blueberry kiwi pear apple blueberry cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025317444690292994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02251051727969268}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02246454902033132}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022326552954612427}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.021716778873151158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02157675055049158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021511770596509484}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02093825091823226}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020359169335375613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.019632213059690665}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.019431298416882296}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.019366911181166735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.01917890659864119}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.01916834291518325}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.018829214334863953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.018647539116281142}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025317444690292994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02251051727969268}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02246454902033132}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022326552954612427}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.021716778873151158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02157675055049158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021511770596509484}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02093825091823226}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020359169335375613}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.019632213059690665}]
result = search.search('banana strawberry blueberry kiwi pear apple blueberry cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #477 checking search results for 'banana strawberry blueberry kiwi pear apple blueberry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #477 checking search results for 'banana strawberry blueberry kiwi pear apple blueberry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #478 checking search results for 'banana strawberry blueberry kiwi pear apple blueberry cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9810544159396349}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9769144115448323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.974287210617535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.964931907926216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9639299238466396}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9618098958662136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.960937164467077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9573856387147732}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.9480141935013493}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9452301963069941}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9810544159396349}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9769144115448323}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.974287210617535}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.964931907926216}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9639299238466396}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9618098958662136}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.960937164467077}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9573856387147732}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.9480141935013493}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9452301963069941}]
result = search.search('banana strawberry blueberry kiwi pear apple blueberry cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #478 checking search results for 'banana strawberry blueberry kiwi pear apple blueberry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #478 checking search results for 'banana strawberry blueberry kiwi pear apple blueberry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #479 checking search results for 'blueberry papaya peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027132424788416952}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024208122534563954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.02366798082157573}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02250626306986272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022437743754489158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021954140849352266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02186799974889944}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021744134871436813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.021457844273308654}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021412427736385176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021271097698915928}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.021203702409582584}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.021038096567630643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020853508490206243}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020761408365739236}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.020626239507709452}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027132424788416952}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024208122534563954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.02366798082157573}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02250626306986272}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022437743754489158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021954140849352266}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02186799974889944}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021744134871436813}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.021457844273308654}]
result = search.search('blueberry papaya peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #479 checking search results for 'blueberry papaya peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #479 checking search results for 'blueberry papaya peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #480 checking search results for 'blueberry papaya peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9974912060164606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9963657549286672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9951113685452965}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.994682731506263}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9943806058006674}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9943621782243988}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9974912060164606}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9963657549286672}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9951113685452965}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.994682731506263}]
result = search.search('blueberry papaya peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #480 checking search results for 'blueberry papaya peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #480 checking search results for 'blueberry papaya peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #481 checking search results for 'coconut lime tomato pear apricot coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027388405543565003}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023846236044195165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.023642502542008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02346023449987996}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.023024737197577992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022722013485283524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021833893536376336}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021749061304163594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021363890943115686}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021241249834155932}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020648930557607845}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.02033167481967316}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020312684415035562}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.02027868406052669}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027388405543565003}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023846236044195165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.023642502542008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02346023449987996}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.023024737197577992}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022722013485283524}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021833893536376336}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021749061304163594}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021363890943115686}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021241249834155932}]
result = search.search('coconut lime tomato pear apricot coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #481 checking search results for 'coconut lime tomato pear apricot coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #481 checking search results for 'coconut lime tomato pear apricot coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #482 checking search results for 'coconut lime tomato pear apricot coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9999529304856642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9996626489583953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9969129938807043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9939699960435675}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.9932508805024486}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 0.9924258221544897}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9902545831833292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9899856586659999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.987313114182593}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'title': 'N-20', 'score': 0.9812769068190872}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9999529304856642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9996626489583953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9969129938807043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9939699960435675}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.9932508805024486}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 0.9924258221544897}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9902545831833292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9899856586659999}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.987313114182593}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'title': 'N-20', 'score': 0.9812769068190872}]
result = search.search('coconut lime tomato pear apricot coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #482 checking search results for 'coconut lime tomato pear apricot coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #482 checking search results for 'coconut lime tomato pear apricot coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #483 checking search results for 'apricot strawberry banana apricot banana banana pear' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027574654924902624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022547978718103656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021852323485913934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.020639555358838137}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020627429570880658}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020587776183002466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.01994013211645651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.01992658484285523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.01973319967120896}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.019606982476178307}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.019525979759501617}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.019198942166682713}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.018898880840609422}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.018683335475624688}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027574654924902624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022547978718103656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021852323485913934}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.020639555358838137}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020627429570880658}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020587776183002466}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.01994013211645651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.01992658484285523}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.01973319967120896}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.019606982476178307}]
result = search.search('apricot strawberry banana apricot banana banana pear',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #483 checking search results for 'apricot strawberry banana apricot banana banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #483 checking search results for 'apricot strawberry banana apricot banana banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #484 checking search results for 'apricot strawberry banana apricot banana banana pear' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9979123911847855}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9973457451047806}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 0.993747518102153}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9812825565150423}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.9808200873596962}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9779593213845643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9755233617860974}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.97321001688519}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9713322450570586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 0.9650200941832174}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9640849638595074}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9979123911847855}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9973457451047806}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 0.993747518102153}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9812825565150423}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.9808200873596962}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9779593213845643}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9755233617860974}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.97321001688519}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9713322450570586}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 0.9650200941832174}]
result = search.search('apricot strawberry banana apricot banana banana pear',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #484 checking search results for 'apricot strawberry banana apricot banana banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #484 checking search results for 'apricot strawberry banana apricot banana banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #485 checking search results for 'apricot papaya peach apple apple cherry lime cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025132500056641433}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.0222208642068413}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02199739790430133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021395662369594948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021376063007455582}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021323308328205347}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021311574498487695}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020534886191254775}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.020448829878525965}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02006990210013147}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.019870384178733495}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.01984782218397456}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.019607438900489816}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.01916273498177716}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.0191138219445603}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025132500056641433}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.0222208642068413}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02199739790430133}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021395662369594948}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021376063007455582}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021323308328205347}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021311574498487695}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020534886191254775}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.020448829878525965}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.02006990210013147}]
result = search.search('apricot papaya peach apple apple cherry lime cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #485 checking search results for 'apricot papaya peach apple apple cherry lime cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #485 checking search results for 'apricot papaya peach apple apple cherry lime cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #486 checking search results for 'apricot papaya peach apple apple cherry lime cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9791636681535103}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9791167993097507}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.9732131779144241}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9720698492695532}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9685848029351393}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.968457573804396}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.962107322787987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9539141051745411}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.953088433152494}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 0.9502596533261283}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9791636681535103}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9791167993097507}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.9732131779144241}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9720698492695532}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9685848029351393}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.968457573804396}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.962107322787987}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9539141051745411}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.953088433152494}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 0.9502596533261283}]
result = search.search('apricot papaya peach apple apple cherry lime cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #486 checking search results for 'apricot papaya peach apple apple cherry lime cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #486 checking search results for 'apricot papaya peach apple apple cherry lime cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #487 checking search results for 'fig apple papaya tomato blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025364930084163108}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.022107200417055536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021872680278829812}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02185496544710008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02177720295186145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.021729437548597238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021592951803303735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021503184670539365}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02133871793907319}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.021211276268073752}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02105101896082809}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.020739408883460164}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020701544580281474}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.02031226219489949}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.0202812053815139}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025364930084163108}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.022107200417055536}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021872680278829812}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02185496544710008}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02177720295186145}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.021729437548597238}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021592951803303735}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021503184670539365}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02133871793907319}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.021211276268073752}]
result = search.search('fig apple papaya tomato blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #487 checking search results for 'fig apple papaya tomato blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #487 checking search results for 'fig apple papaya tomato blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #488 checking search results for 'fig apple papaya tomato blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9963657549286671}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9961057714899609}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.988192537756199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9812593358778644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9763174459063257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9653098739629631}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9652863755240644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9640376943690768}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 0.9610285913586938}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.960532205508914}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9963657549286671}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9961057714899609}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.988192537756199}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9812593358778644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9763174459063257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9653098739629631}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 0.9652863755240644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9640376943690768}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 0.9610285913586938}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.960532205508914}]
result = search.search('fig apple papaya tomato blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #488 checking search results for 'fig apple papaya tomato blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #488 checking search results for 'fig apple papaya tomato blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #489 checking search results for 'tomato fig strawberry apricot tomato apricot pear apricot' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02771767691644711}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02291707839358931}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02244953451271177}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.0219422412821657}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.021856978405756424}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02108600084821069}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.02100524067790651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02086472285370481}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.020236540469430624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.020204319590118647}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.019623789730375256}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 0.019606814865592688}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02771767691644711}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.02291707839358931}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02244953451271177}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.0219422412821657}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.021856978405756424}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02108600084821069}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.02100524067790651}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02086472285370481}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.020236540469430624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.020204319590118647}]
result = search.search('tomato fig strawberry apricot tomato apricot pear apricot',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #489 checking search results for 'tomato fig strawberry apricot tomato apricot pear apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #489 checking search results for 'tomato fig strawberry apricot tomato apricot pear apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #490 checking search results for 'tomato fig strawberry apricot tomato apricot pear apricot' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9830317217527589}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.9828821483064925}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.974676923800241}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.97411658876724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.9727712742227035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.9685201743584445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9649921362828499}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.964501977002748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9568825441907404}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9561280387354602}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 0.9554497449338089}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9830317217527589}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 0.9828821483064925}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.974676923800241}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.97411658876724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 0.9727712742227035}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.9685201743584445}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9649921362828499}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.964501977002748}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 0.9568825441907404}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9561280387354602}]
result = search.search('tomato fig strawberry apricot tomato apricot pear apricot',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #490 checking search results for 'tomato fig strawberry apricot tomato apricot pear apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #490 checking search results for 'tomato fig strawberry apricot tomato apricot pear apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #491 checking search results for 'lime peach apple tomato peach papaya' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027313659118077357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023416789372310683}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.023118635008562573}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02286669585823247}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02262047990359738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022405243477313208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021979505082855157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021674749895332197}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02161417227368761}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.0214441567615608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021259020769087953}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.021103966124719063}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.021090154857258275}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020955096601630724}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.027313659118077357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.023416789372310683}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.023118635008562573}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02286669585823247}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02262047990359738}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022405243477313208}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021979505082855157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021674749895332197}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02161417227368761}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.0214441567615608}]
result = search.search('lime peach apple tomato peach papaya',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #491 checking search results for 'lime peach apple tomato peach papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #491 checking search results for 'lime peach apple tomato peach papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #492 checking search results for 'lime peach apple tomato peach papaya' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9968702447684552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 0.9968702447684552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9953345674650371}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9952962797280891}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9901691196371644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9900702028680697}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9891636838353477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9866878578939356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9865692261466786}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.9802215941102437}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9968702447684552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 0.9968702447684552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9953345674650371}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.9952962797280891}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 0.9901691196371644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9900702028680697}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9891636838353477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9866878578939356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9865692261466786}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.9802215941102437}]
result = search.search('lime peach apple tomato peach papaya',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #492 checking search results for 'lime peach apple tomato peach papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #492 checking search results for 'lime peach apple tomato peach papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #493 checking search results for 'cherry coconut strawberry cherry apricot apple' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.0263458699669254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.022425791153998096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022070350079623605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02200937808498899}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021867313351419775}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021864030544048625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021048189454833388}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02083876739803571}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.020652802507448807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.020512756539628047}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020381121106758642}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02026427687552134}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.0263458699669254}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.022425791153998096}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022070350079623605}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02200937808498899}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021867313351419775}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.021864030544048625}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.021048189454833388}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02083876739803571}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.020652802507448807}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.020512756539628047}]
result = search.search('cherry coconut strawberry cherry apricot apple',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #493 checking search results for 'cherry coconut strawberry cherry apricot apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #493 checking search results for 'cherry coconut strawberry cherry apricot apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #494 checking search results for 'cherry coconut strawberry cherry apricot apple' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9835822243114561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9817703322014285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9802045641293886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 0.9765564668229105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9726681160325973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9716531157272372}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9695652362093584}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9555904410577706}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.953677599355608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9535774566329611}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9835822243114561}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9817703322014285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9802045641293886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 0.9765564668229105}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9726681160325973}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 0.9716531157272372}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9695652362093584}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.9555904410577706}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.953677599355608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9535774566329611}]
result = search.search('cherry coconut strawberry cherry apricot apple',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #494 checking search results for 'cherry coconut strawberry cherry apricot apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #494 checking search results for 'cherry coconut strawberry cherry apricot apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #495 checking search results for 'lime peach fig peach strawberry coconut' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025221524442924664}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023480720593625357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022834531992587608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.022647119899172233}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02251612340549733}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022291333524088065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02197641846534507}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.02191358612183901}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021773588010740603}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.021744995438352}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.02146520263993088}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021358798223515787}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.021240195182887743}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.025221524442924664}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023480720593625357}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022834531992587608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.022647119899172233}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.02251612340549733}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022291333524088065}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02197641846534507}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.02191358612183901}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021773588010740603}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.021744995438352}]
result = search.search('lime peach fig peach strawberry coconut',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #495 checking search results for 'lime peach fig peach strawberry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #495 checking search results for 'lime peach fig peach strawberry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #496 checking search results for 'lime peach fig peach strawberry coconut' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9986489605590284}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.996514206239649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9964592793237129}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9890868963844257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9876562201791663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9859073727511257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.9848221830318995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9831360933775201}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9822520763908572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9820178236117763}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9986489605590284}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.996514206239649}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9964592793237129}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9890868963844257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9876562201791663}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9859073727511257}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.9848221830318995}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9831360933775201}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9822520763908572}]
result = search.search('lime peach fig peach strawberry coconut',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #496 checking search results for 'lime peach fig peach strawberry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #496 checking search results for 'lime peach fig peach strawberry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #497 checking search results for 'kiwi tomato' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022437743754489158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022319897048681214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.0218509561429526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021687974328279274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.024563566260840976}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}]
result = search.search('kiwi tomato',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #497 checking search results for 'kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #497 checking search results for 'kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #498 checking search results for 'kiwi tomato' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}]
result = search.search('kiwi tomato',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #498 checking search results for 'kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #498 checking search results for 'kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #499 checking search results for 'tomato banana apple cherry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028067473389718083}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022875322447799443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022511020971305824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.022381523617608482}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022306507770549763}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.02172716759040647}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021723550921760502}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02145737396877421}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.02094510649938197}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020924122528553784}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.020734228665603517}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020557691878066286}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020252906984866176}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.020104072540859153}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028067473389718083}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022875322447799443}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022511020971305824}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.022381523617608482}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.022306507770549763}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.02172716759040647}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021723550921760502}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02145737396877421}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.02094510649938197}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.020924122528553784}]
result = search.search('tomato banana apple cherry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #499 checking search results for 'tomato banana apple cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #499 checking search results for 'tomato banana apple cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #500 checking search results for 'tomato banana apple cherry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9993365406085505}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9987480223146742}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9954375604678559}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.995396754457402}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9934355588510276}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9900868170584447}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 0.9894058650940641}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0000000000000002}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9993365406085505}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9987480223146742}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9954375604678559}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.995396754457402}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9934355588510276}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9900868170584447}]
result = search.search('tomato banana apple cherry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #500 checking search results for 'tomato banana apple cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #500 checking search results for 'tomato banana apple cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #501 checking search results for 'pear pear cherry banana fig' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02504710434740677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02391964121658369}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.023795728343839945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023165968457136858}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.021797161966371877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02175718148668793}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021002469423249417}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.020851035595160123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020828889522009265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020728952518985575}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02041771369061656}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'title': 'N-36', 'score': 0.02019348158222486}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.02017466565874004}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.01977229099493681}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02504710434740677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02391964121658369}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.023795728343839945}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023165968457136858}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.021797161966371877}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.02175718148668793}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.021002469423249417}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.020851035595160123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.020828889522009265}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020728952518985575}]
result = search.search('pear pear cherry banana fig',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #501 checking search results for 'pear pear cherry banana fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #501 checking search results for 'pear pear cherry banana fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #502 checking search results for 'pear pear cherry banana fig' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9997688672411998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9997375576738483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9928077140037853}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9852623656849636}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.98518493230804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9815534695893001}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 0.975946073981608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.975627260073157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 0.9735430578474292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9689727948464024}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9997688672411998}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 0.9997375576738483}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.9928077140037853}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.9852623656849636}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 0.98518493230804}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9815534695893001}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'title': 'N-28', 'score': 0.975946073981608}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.975627260073157}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 0.9735430578474292}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.9689727948464024}]
result = search.search('pear pear cherry banana fig',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #502 checking search results for 'pear pear cherry banana fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #502 checking search results for 'pear pear cherry banana fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #503 checking search results for 'tomato strawberry lime apricot fig peach' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02546218261571018}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.023051251798768577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022904170088539618}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022528035939440097}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02250462755474315}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022361302377125587}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022057778812163933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021577518072355285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021558533345568148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021382962262986572}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.020721377991985774}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02546218261571018}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.023051251798768577}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022904170088539618}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022528035939440097}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.02250462755474315}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.022361302377125587}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022057778812163933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021577518072355285}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.021558533345568148}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021382962262986572}]
result = search.search('tomato strawberry lime apricot fig peach',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #503 checking search results for 'tomato strawberry lime apricot fig peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #503 checking search results for 'tomato strawberry lime apricot fig peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #504 checking search results for 'tomato strawberry lime apricot fig peach' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9945911251798547}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9904948472698375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9904587219304862}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9885212295562356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9866173912266644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9838721785746477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.9825904759240996}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9825373766647374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9795976508354823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 0.9775550548472207}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9945911251798547}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 0.9904948472698375}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 0.9904587219304862}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9885212295562356}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.9866173912266644}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.9838721785746477}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 0.9825904759240996}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.9825373766647374}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9795976508354823}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 0.9775550548472207}]
result = search.search('tomato strawberry lime apricot fig peach',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #504 checking search results for 'tomato strawberry lime apricot fig peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #504 checking search results for 'tomato strawberry lime apricot fig peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #505 checking search results for 'peach strawberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 0.022437743754489158}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.022319897048681214}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.0218509561429526}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.021733475880946682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 0.021687974328279274}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.028196116466136123}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 0.024976447632762886}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.02478877289603739}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 0.024517192369952933}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.02422492536118724}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.023512486890770116}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 0.02309603479833191}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 0.022928426413570565}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02252941664731043}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.022453862071676416}]
result = search.search('peach strawberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #505 checking search results for 'peach strawberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #505 checking search results for 'peach strawberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #506 checking search results for 'peach strawberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'title': 'N-45', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'title': 'N-15', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'title': 'Custom Title 21', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'title': 'Custom Title 31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html', 'title': 'N-4', 'score': 1.0}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'title': 'Custom Title 37', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'title': 'Custom Title 87', 'score': 1.0}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 1.0}]
result = search.search('peach strawberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #506 checking search results for 'peach strawberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #506 checking search results for 'peach strawberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #507 checking search results for 'pear apple banana cherry blueberry' and boost = True
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02749888512837486}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022987099434088453}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022746612936947273}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02230585840889165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021607930773094426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021473986101526954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.020964163567516677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02078437277080262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.02054009264901782}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020514438794292624}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'title': 'N-42', 'score': 0.02023203563722682}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'title': 'N-39', 'score': 0.020063276615625455}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'title': 'N-34', 'score': 0.020037817258580354}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.02749888512837486}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'title': 'N-19', 'score': 0.022987099434088453}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'title': 'N-37', 'score': 0.022746612936947273}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.02230585840889165}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'title': 'N-38', 'score': 0.021607930773094426}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'title': 'N-23', 'score': 0.021473986101526954}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'title': 'N-14', 'score': 0.020964163567516677}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'title': 'Custom Title 64', 'score': 0.02078437277080262}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.02054009264901782}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.020514438794292624}]
result = search.search('pear apple banana cherry blueberry',True)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #507 checking search results for 'pear apple banana cherry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #507 checking search results for 'pear apple banana cherry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #508 checking search results for 'pear apple banana cherry blueberry' and boost = False
fullResults = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9904391354635814}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9901969151754918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9900770516201772}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9857706772609904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.982533635733801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9799653770686552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9780959382863884}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9779743375595343}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9771277878527994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9752720790964725}]
expected = [{'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'title': 'N-11', 'score': 0.9904391354635814}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'title': 'Custom Title 28', 'score': 0.9901969151754918}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'title': 'N-3', 'score': 0.9900770516201772}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'title': 'N-40', 'score': 0.9857706772609904}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'title': 'N-33', 'score': 0.982533635733801}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'title': 'N-48', 'score': 0.9799653770686552}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'title': 'Custom Title 6', 'score': 0.9780959382863884}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'title': 'N-47', 'score': 0.9779743375595343}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'title': 'N-44', 'score': 0.9771277878527994}, {'url': 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'title': 'N-27', 'score': 0.9752720790964725}]
result = search.search('pear apple banana cherry blueberry',False)
if not testingtools.compare_search_results(result, fullResults):
  output.write("Failed Test #508 checking search results for 'pear apple banana cherry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #508 checking search results for 'pear apple banana cherry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
