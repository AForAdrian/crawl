
import testingtools
import crawler
import searchdata
import search
output = open('fruits100-page-rank-failed.txt', 'w')
success_output = open('fruits100-page-rank-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits100/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits100/N-0.html')
#Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html
expected = 0.009688099979137332
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html
expected = 0.008149730698163072
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-54.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-68.html
expected = 0.008718293735170031
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-68.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-68.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-68.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-63.html
expected = 0.010893213622522288
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-63.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-63.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-63.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-64.html
expected = 0.00898421987065145
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-64.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-64.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-64.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-31.html
expected = 0.010183108411710627
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-31.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-31.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-31.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-48.html
expected = 0.00945345246699723
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-48.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-78.html
expected = 0.010240702118974836
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-78.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-78.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-78.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-43.html
expected = 0.010377590736868392
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-43.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-38.html
expected = 0.011550646819563524
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-38.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-13.html
expected = 0.010010604863723016
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-13.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-57.html
expected = 0.010266778545706581
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-57.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-57.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-57.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-70.html
expected = 0.008681122078092546
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-70.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-70.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-70.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html
expected = 0.009891618080303666
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-35.html
expected = 0.01086245049064621
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-35.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-75.html
expected = 0.009933833266192179
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-75.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-75.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-75.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-74.html
expected = 0.010216714694201831
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-74.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-74.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-74.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-11.html
expected = 0.011294528967361928
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-11.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-92.html
expected = 0.009170756142615281
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-92.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-92.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-92.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-28.html
expected = 0.008897739696856354
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-28.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-95.html
expected = 0.009853576984581367
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-95.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-95.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-95.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-25.html
expected = 0.009016079097793625
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-25.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-25.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-25.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-5.html
expected = 0.01291147447898019
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-5.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-58.html
expected = 0.00894814512040321
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-58.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-58.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-58.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-22.html
expected = 0.01013268635352032
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-22.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-14.html
expected = 0.012212229418923984
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-14.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html
expected = 0.010676130401817127
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-59.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-45.html
expected = 0.011001292790747429
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-45.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-71.html
expected = 0.008636932373472711
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-71.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-71.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-71.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-85.html
expected = 0.010253570595589168
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-85.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-85.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-85.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-27.html
expected = 0.010946378293540417
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-27.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-47.html
expected = 0.010356675078608503
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-47.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-6.html
expected = 0.007916977734570294
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-6.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html
expected = 0.010831226847106514
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-49.html
expected = 0.010662659534052838
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-49.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html
expected = 0.010760074508006515
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-97.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-41.html
expected = 0.011249882050154706
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-41.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-34.html
expected = 0.010535878757481345
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-34.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html
expected = 0.00858986456819878
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-66.html
expected = 0.00886977531492758
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-66.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-66.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-66.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-52.html
expected = 0.007702650611126792
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-52.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-52.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-52.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-1.html
expected = 0.008883857088051663
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-99.html
expected = 0.010136525100031426
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-99.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-99.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-99.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-51.html
expected = 0.009544520407264907
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-51.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-51.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-51.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-55.html
expected = 0.010483485417208014
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-55.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-55.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-55.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-17.html
expected = 0.010590594220026988
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-17.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html
expected = 0.00881234645102528
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-80.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html
expected = 0.010399265710896763
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-37.html
expected = 0.011415605790004158
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-37.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-79.html
expected = 0.008413038082640711
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits100/N-79.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-79.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits100/N-79.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
