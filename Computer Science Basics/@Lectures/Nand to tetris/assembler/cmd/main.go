package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"../pkg/parser"
	"../pkg/symbolTable"
	"../pkg/translator"
)

const (
	Ext = ".hack"
)

type HackAssembler struct {
	*parser.Parser
	*symbolTable.SymbolTable
	*translator.Translator
}

func newHackAssembler() *HackAssembler {
	return &HackAssembler{
		parser.New(),
		symbolTable.New(),
		translator.New(),
	}
}

func main() {
	// TODO: get lots of files once, translate them asynchronously with goroutine
	filePath := os.Args[1]
	f, err := os.Open(filePath)
	s := bufio.NewScanner(f)
	if err != nil {
		fmt.Printf("%+v\n", err)
		return
	}
	defer f.Close()

	ha := newHackAssembler()
	lineNum := -1

	// abstract string line to result struct And register label
	for s.Scan() {
		// TODO: this is parser's preworks
		line := s.Text()
		// remove line starting with prefix // or empty line
		if strings.HasPrefix(line, "//") || line == "" {
			continue
		}
		// remove strings after //
		if i := strings.Index(line, "//"); i >= 0 {
			line = line[:i]
		}
		// remove front, and back spaces
		line = strings.Trim(line, " ")

		err, lineNum = ha.Parser.ParseLine(line, lineNum, ha.SymbolTable)
		if err != nil {
			fmt.Printf("%v\n", err)
			return
		}
		// fmt.Println(line)
	}

	// re-read parsed commands, and apply symbol -> number and register undefined symbol
	for i, r := range ha.Parser.Results() {
		switch r.CommandType() {
		case "A":
			symbolOrLabel := r.Fields()[0]
			if ha.SymbolTable.IsSymbolOrLabel(symbolOrLabel) {
				val, ok := ha.SymbolTable.Get(symbolOrLabel)
				if !ok {
					// this is undefined symbol
					val = ha.SymbolTable.GetCursor()
					ha.SymbolTable.Set(symbolOrLabel, ha.SymbolTable.GetCursor())
					ha.SymbolTable.AddOneCursor()
				}
				str := strconv.Itoa(val)
				ha.Parser.SetResult(i, r.CommandType(), str)
			}
		}
		// fmt.Println(r)
	}

	// make binary codes with partition
	binaryCodes := make([]string, len(ha.Parser.Results()))
	for i, r := range ha.Parser.Results() {
		binaryCode, err := ha.Translator.Translate(r)
		if err != nil {
			fmt.Printf("%+v\n", err)
			return
		}
		binaryCodes[i] = binaryCode
		// fmt.Println(binaryCode)
	}

	filePathUntilExt := strings.LastIndex(filePath, ".")
	outFile, err := os.Create(filePath[:filePathUntilExt] + Ext)
	w := bufio.NewWriter(outFile)
	if err != nil {
		return
	}
	w.WriteString(strings.Join(binaryCodes, "\n"))
	w.Flush()
}
