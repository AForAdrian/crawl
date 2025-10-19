
import testingtools
import crawler
import searchdata
import search
output = open('fruits50-incoming-links-failed.txt', 'w')
success_output = open('fruits50-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html')
#Test #0 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #50 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
