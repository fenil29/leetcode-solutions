func firstUniqChar(s string) int {
	isRepearing := make(map[string]int)
	isNonRepearing := make(map[string]int)
	for pos, char := range s {
		if _, ok := isRepearing[string(char)]; !ok {
			if _, ok := isNonRepearing[string(char)]; ok {
				isRepearing[string(char)] = pos
				delete(isNonRepearing, string(char))
			} else {
				isNonRepearing[string(char)] = pos
			}
		}
	}
	min := len(s)
	found := false
	for _, element := range isNonRepearing {
		found = true
		if element < min {
			min = element
		}
	}
	if found {
		return min
	} else {
		return -1

	}
}