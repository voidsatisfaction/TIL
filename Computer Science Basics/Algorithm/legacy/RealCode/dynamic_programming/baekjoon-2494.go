package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readLine(r *bufio.Reader) string {
	str, _ := r.ReadString('\n')
	return strings.TrimSpace(str)
}

func stringToIntSlice(str string) []int {
	iSlice := make([]int, len(str))
	for i := 0; i < len(str); i++ {
		n, _ := strconv.Atoi(string(str[i]))
		iSlice[i] = n
	}
	return iSlice
}

func getLeftAndRight(c, t int) (int, int) {
	if t-c > 0 {
		return (t - c), (10 + c - t)
	} else if t-c < 0 {
		return (10 - c + t), (c - t)
	}
	return 0, 0
}

func min(nums ...int) int {
	minNum := nums[0]
	for _, n := range nums {
		if n < minNum {
			minNum = n
		}
	}
	return minNum
}

func f(i, lAdded int, cState, tState []int, dp [][]int) int {
	if dp[i][lAdded] >= 0 {
		return dp[i][lAdded]
	}
	c, t := (cState[i]+lAdded)%10, tState[i]
	l, r := getLeftAndRight(c, t)
	if i == len(cState)-1 {
		dp[i][lAdded] = min(l, r)
		return dp[i][lAdded]
	}
	leftMin := f(i+1, (lAdded+l)%10, cState, tState, dp) + l
	rightMin := f(i+1, lAdded, cState, tState, dp) + r
	dp[i][lAdded] = min(leftMin, rightMin)
	return dp[i][lAdded]
}

func reconstruct(i, lAdded int, cState, tState []int, dp [][]int, p *bufio.Writer) {
	c, t := (cState[i]+lAdded)%10, tState[i]
	l, r := getLeftAndRight(c, t)
	if i == len(cState)-1 {
		if l < r {
			fmt.Fprintf(p, "%d %d\n", i+1, l)
		} else {
			fmt.Fprintf(p, "%d %d\n", i+1, -r)
		}
		return
	}
	leftMin := f(i+1, (lAdded+l)%10, cState, tState, dp) + l
	rightMin := f(i+1, lAdded, cState, tState, dp) + r
	if leftMin < rightMin {
		fmt.Fprintf(p, "%d %d\n", i+1, l)
		reconstruct(i+1, (lAdded+l)%10, cState, tState, dp, p)
	} else {
		fmt.Fprintf(p, "%d %d\n", i+1, -r)
		reconstruct(i+1, lAdded, cState, tState, dp, p)
	}
}

func main() {
	r := bufio.NewReader(os.Stdin)
	p := bufio.NewWriter(os.Stdout)
	var N int
	fmt.Sscanf(readLine(r), "%d", &N)
	currentState := stringToIntSlice(readLine(r))
	targetState := stringToIntSlice(readLine(r))
	dp := make([][]int, N)
	for i := 0; i < N; i++ {
		dp[i] = make([]int, 10)
		for j := 0; j < 10; j++ {
			dp[i][j] = -1
		}
	}

	ans := f(0, 0, currentState, targetState, dp)
	fmt.Fprintf(p, "%d\n", ans)
	reconstruct(0, 0, currentState, targetState, dp, p)
	p.Flush()
}
