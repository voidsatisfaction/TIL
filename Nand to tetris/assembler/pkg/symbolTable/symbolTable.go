package symbolTable

import (
	"fmt"
	"strconv"
)

type SymbolTable struct {
	cursor int
	table  map[string]int
}

func New() *SymbolTable {
	st := &SymbolTable{
		table: map[string]int{
			"R0": 0, "R1": 1, "R2": 2, "R3": 3,
			"R4": 4, "R5": 5, "R6": 6, "R7": 7,
			"R8": 8, "R9": 9, "R10": 10, "R11": 11,
			"R12": 12, "R13": 13, "R14": 14, "R15": 15,
			"SCREEN": 16384, "KBD": 24576, "SP": 0, "LCL": 1,
			"ARG": 2, "THIS": 3, "THAT": 4,
		},
		cursor: 16,
	}
	return st
}

func (st *SymbolTable) Set(s string, val int) {
	if _, ok := st.table[s]; ok {
		fmt.Printf("Warn: This symbol is already exists at symboltable: %s\n", s)
	}
	st.table[s] = val
}

func (st *SymbolTable) Get(s string) (int, bool) {
	val, ok := st.table[s]
	if !ok {
		return 0, ok
	}
	return val, ok
}

func (st *SymbolTable) AddOneCursor() {
	st.cursor++
}

func (st *SymbolTable) GetCursor() int {
	return st.cursor
}

func (st *SymbolTable) IsSymbolOrLabel(str string) bool {
	_, err := strconv.Atoi(str)
	if err != nil {
		return true
	}
	return false
}
