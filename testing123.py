term_matcher = 0
webpage_terms = open('lineByline.txt', 'r')
comparing_terms = open('traffick.txt', 'r')
for line_webpage in webpage_terms:
	#print(line_webpage)
	print("yo1")
	for line_compare in comparing_terms:
		print(line_compare)
		if line_webpage == line_compare:
			term_matcher += 1
		else:
			continue
print("Number of terms matching: ", term_matcher)