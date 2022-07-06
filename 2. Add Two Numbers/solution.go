/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// Time : O(n)
// Space : O(n)
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var pointer1 *ListNode = l1
	var pointer2 *ListNode = l2
	var previousPointer *ListNode = nil
	var startPointer *ListNode = nil
	var carry = 0

	addNode := func(value int) {
		currentNode := &ListNode{Val: value, Next: nil}

		if previousPointer != nil {
			previousPointer.Next = currentNode
		}
		if startPointer == nil {
			startPointer = currentNode
		}
		previousPointer = currentNode
	}
	addCarry := func(sum int) int {
		result := sum + carry
		carry = 0
		if result > 9 {
			carry = 1
			result = result - 10
		}
		return result
	}
	for pointer1 != nil && pointer2 != nil {
		sum := pointer1.Val + pointer2.Val
		sum = addCarry(sum)
		addNode(sum)

		pointer1 = pointer1.Next
		pointer2 = pointer2.Next
	}
	for pointer1 != nil {
		sum := pointer1.Val
		sum = addCarry(sum)
		addNode(sum)
		pointer1 = pointer1.Next
	}
	for pointer2 != nil {
		sum := pointer2.Val
		sum = addCarry(sum)
		addNode(sum)
		pointer2 = pointer2.Next
	}
	if carry != 0 {
		addNode(carry)
	}

	return startPointer
}