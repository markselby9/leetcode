class TreeNode
	attr_accessor :val, :children, :is_end

	def initialize
		self.children = {}
		self.is_end = false
	end

	def get_child_node(val)
		if self.children[val.ord-97].nil?
			self.children[val.ord-97] = TreeNode.new
		end
		self.children[val.ord-97]
	end

	def has_child_node(val)
		!self.children[val.ord-97].nil?
	end

	def set_word_terminate
		self.is_end = true
	end

	def is_word_terminate
		self.is_end
	end
end

class Trie
	attr_accessor :root

	def initialize()
		self.root = TreeNode.new
	end


=begin
    Inserts a word into the trie.
    :type word: String
    :rtype: Void
=end
	def insert(word)
		return if word.nil?
		t = self.root
		word.each_char do |c|
			child = t.get_child_node(c)
			t = child
		end

		t.set_word_terminate
	end


=begin
    Returns if the word is in the trie.
    :type word: String
    :rtype: Boolean
=end
	def search(word)
		return if word.nil?
		t = self.root

		word.each_char do |c|
			unless t.has_child_node(c)
				return false
			end
			child = t.get_child_node(c)
			t = child
		end

		t.is_word_terminate
	end


=begin
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: String
    :rtype: Boolean
=end
	def starts_with(prefix)
		return if prefix.nil?
		t = self.root

		prefix.each_char do |c|
			unless t.has_child_node(c)
				return false
			end
			child = t.get_child_node(c)
			t = child
		end

		true
	end


end

trie = Trie.new
trie.insert 'ab'
raise 'wrong' unless !trie.search('a')
raise 'wrong' unless trie.starts_with('a')

trie.insert 'count'
trie.insert 'cherry'
trie.insert 'tree'
trie.insert 'hello'
trie.insert 'helloworld'
raise 'wrong' unless !trie.search('haha')
raise 'wrong' unless trie.search('count')
raise 'wrong' unless trie.starts_with('che')
raise 'wrong' unless trie.starts_with('hel')
raise 'wrong' unless trie.starts_with('c')
raise 'wrong' unless trie.search('hello')


# Your Trie object will be instantiated and called as such:
# obj = Trie.new()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.starts_with(prefix)