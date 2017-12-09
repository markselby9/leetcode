# @param {String[]} words1
# @param {String[]} words2
# @param {string[][]} pairs
# @return {Boolean}
def are_sentences_similar_two(words1, words2, pairs)
	length1 = words1.length
	length2 = words2.length
	return false if length1 != length2

	graph = {}
	pairs.each do |pair|
		w1, w2 = pair[0], pair[1]
		if graph.include? w1
			graph[w1].push w2
		else
			graph[w1] = [w2]
		end
		if graph.include? w2
			graph[w2].push w1
		else
			graph[w2] = [w1]
		end
	end

	(0..length1).each do |index|
		w1 = words1[index]
		w2 = words2[index]
		next if w1==w2
		# DFS
		stack = [w1]
		visited = [w1]
		found = false

		while stack.length > 0
			node = stack.shift

			unless graph.include? node
				return false
			end

			arr = graph[node]
			arr.each do |w|
				if visited.include? w
					next
				end
				if w == w2
					found = true
					break
				end
				stack.push w unless stack.include? w
				visited.push w
			end

			break if found
		end

		return false unless found
	end

	true
end

words1 = ["great", "acting", "skills"]
words2 = ["fine", "drama", "talent"]
pairs = [["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "talent"]]
p are_sentences_similar_two(words1, words2, pairs)
p are_sentences_similar_two(['w', '2'], ['2', 'w'], [])
