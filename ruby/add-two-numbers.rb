# Definition for singly-linked list.
class ListNode
	attr_accessor :val, :next

	def initialize(val)
		@val = val
		@next = nil
	end
end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
	if !l1 or !l2
		return 0
	end
	dummy_node = ListNode.new(0)

	t1, t2 = l1, l2
	carry = 0
	t = dummy_node
	while true
		break if !t1 and !t2
		x, y = 0, 0
		x = t1.val if t1
		y = t2.val if t2
		num = x+y+carry
		if num>9
			carry = 1
			num -= 10
		else
			carry = 0
		end
		t.next = ListNode.new(num)
		t = t.next
		t1 = t1.next if t1
		t2 = t2.next if t2
	end

	if carry!=0
		t.next = ListNode.new(carry)
	end
	dummy_node.next
end

t1 = ListNode.new(2)
t1.next = ListNode.new(4)
t1.next.next = ListNode.new(3)
t2 = ListNode.new(5)
t2.next = ListNode.new(6)
# t2.next.next = ListNode.new(4)

res = add_two_numbers(t1, t2)
while res
	print res.val
	res = res.next
end
