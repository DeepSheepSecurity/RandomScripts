def match_exact(a, b):
		return a==b

"""
http://stackoverflow.com/questions/7331462/check-if-a-string-is-a-possible-abbrevation-for-a-name
"""

def is_abbreviation(abbrev, text):
		words=text.split()
		if not abbrev:
				return True
		if abbrev and not text:
				return False
		if abbrev[0]!=text[0]: # minor modification
				return False
		return (is_abbreviation(abbrev[1:],' '.join(words[1:])) or
						any(is_abbreviation(abbrev[1:],text[i+1:])
										for i in range(len(words[0]))))

def match_abbreviation(a, b):
		return (is_abbreviation(a, b) or
						is_abbreviation(b, a))

"""
http://hetland.org/coding/python/levenshtein.py
"""

def levenshtein(a, b):
		n, m = len(a), len(b)
		if n > m:
				a, b = b, a
				n, m = m, n        
		current=range(n+1)
		for i in range(1, m+1):
				previous, current = current, [i]+[0]*n
				for j in range(1, n+1):
						add, delete = previous[j]+1, current[j-1]+1
						change=previous[j-1]
						if a[j-1]!=b[i-1]:
								change=change+1
						current[j]=min(add, delete, change)
		return current[n]

def match_levenshtein(a, b, threshold=1):
		return levenshtein(a, b) <= threshold

def match_tokens(A, B):
		for a in A.split(" "):
				for b in B.split(" "):
						if (match_exact(a, b) or
								match_levenshtein(a, b)):
								return True
		return False

#Matchers=[match_exact,
#					match_abbreviation,
#					match_levenshtein,
#					match_tokens]

Matchers=[match_exact,
					match_levenshtein]

def match(names, queries, matchers=Matchers):
		matches={}
		for query in queries:
				for matcher in matchers:
						for name in names:
								if matcher(query.lower(), name.lower()):
										if query not in matches:
												matches[query]=name
												break
		unmatched=[query for query in queries 
							 if query not in matches]
		return (matches, unmatched)
		#return matches

def summarize(matches, unmatched):
	print "Matched: %.2f%%" % (100*len(matches)/float(len(matches)+len(unmatched)))
	print matches
	if unmatched!=[]:
		print "Unmatched: %s" % (", ".join(unmatched))
	else:
		print "No unmatched queries"

if __name__=="__main__":

		name_db = ["Arsenal","Man Utd","Man City","AlABC","Ahli wahdu"]
		#name_searching = ["Manchester United", "Man United", "Man U","Manchester City","Man C","Arsenal","Asrenal","Liverpool"]
		name_searching = ["albini","alabu","alkahli","ahLi Wahdu","ahLi Watsa","ahLi Wahuu"]
		summarize(*match(name_db,name_searching))

