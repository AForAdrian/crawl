
import testingtools
import crawler
import searchdata
import search
output = open('fruitsA-incoming-links-failed.txt', 'w')
success_output = open('fruitsA-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html')
#Test #0 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-27.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-45.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-31.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-5.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-18.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-16.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-26.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-49.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-37.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-19.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-35.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-25.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-6.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-44.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-14.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html
expected = ['https://people.scs.carleton.ca/~avamckenney/fruitsB/N-3.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-27.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-17.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-37.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-46.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-24.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-33.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-11.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-43.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html', 'https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html']
result = searchdata.get_incoming_links('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html\n\n')
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
