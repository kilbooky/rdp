
tiles = ['ladilmy', 'eerriin', 'orrpgma', 'orppgma']
words = ['daily', 'eerie', 'program', 'program']
for word, tile in zip(words, tiles):
	#exit('{}, {}'.format(word, tile))
	check = 0
	seen = ''
	#isSeen = False
	for letter in word:
		if letter not in tile:
			print('-> False')
			print('with {} you cannot play {}\n'.format(tile, word) )
			break
		else:
			if letter not in seen:
				
				seen.join(letter)
			else:
				continue
	
	if check == len(word):		
		print('with {} you can play {}'.format(tile, word) )
		print('letters seen:{}'.format(seen))
			