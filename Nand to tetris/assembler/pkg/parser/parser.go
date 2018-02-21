package parser

import (
	"errors"
	"fmt"
	"strings"
)

const (
	TypeA = "A"
	TypeC = "C"
	Label = "LABEL"
)

type symbolTable interface {
	Set(s string, val int)
	Get(s string) (int, bool)

	AddOneCursor()
	GetCursor() int
	IsSymbolOrLabel(s string) bool
}

type Parser struct {
	results []result
}

func New() *Parser {
	return &Parser{}
}

func (p *Parser) SetResult(i int, commandType string, fields ...string) {
	p.results[i] = newResult(commandType, fields...)
}

func (p *Parser) Results() []result {
	return p.results
}

func (p *Parser) addResult(r result) {
	p.results = append(p.results, r)
}

type result struct {
	commandType string
	fields      []string
}

func (r result) CommandType() string {
	return r.commandType
}

func (r result) Fields() []string {
	return r.fields
}

func newResult(commandType string, fields ...string) result {
	return result{commandType, fields}
}

func (p *Parser) ParseLine(line string, lineNum int, st symbolTable) (error, int) {
	lineNum++
	// check label
	if checkLabel(line) {
		lv := getLabelValue(line)
		st.Set(lv, lineNum)
		lineNum--
		return nil, lineNum
	}

	// check C command
	if checkCCommand(line) {
		eIndex, semiIndex := strings.Index(line, "="), strings.Index(line, ";")

		// C command with only equal(=)
		if checkOnlyE(eIndex, semiIndex) {
			dest, comp := line[:eIndex], line[eIndex+1:]
			p.addResult(newResult(TypeC, dest, comp, ""))
			return nil, lineNum
		}

		// C command with only semicolon(;)
		if checkOnlySemi(eIndex, semiIndex) {
			comp, jump := line[:semiIndex], line[semiIndex+1:]
			p.addResult(newResult(TypeC, "", comp, jump))
			return nil, lineNum
		}

		// C command with both equal and semicolon
		dest, comp, jump := line[:eIndex], line[eIndex+1:semiIndex], line[semiIndex+1:]
		p.addResult(newResult(TypeC, dest, comp, jump))
		return nil, lineNum
	}

	// check A command
	if checkACommand(line) {
		rest := line[1:]
		p.addResult(newResult(TypeA, rest))
		return nil, lineNum
	}

	return errors.New(fmt.Sprintf("This is not a valid command type at %d \n %v\n", lineNum, line)), lineNum
}

func checkLabel(line string) bool {
	return strings.HasPrefix(line, "(") && strings.HasSuffix(line, ")")
}

func getLabelValue(line string) string {
	return line[1 : len(line)-1]
}

func checkCCommand(line string) bool {
	eIndex, semiIndex := strings.Index(line, "="), strings.Index(line, ";")

	if eIndex < 0 {
		return semiIndex >= 0
	}

	if semiIndex < 0 {
		return eIndex >= 0
	}

	return (eIndex >= 0 || semiIndex >= 0) &&
		(semiIndex >= eIndex+2) &&
		eIndex >= 1 && semiIndex >= 1 &&
		!strings.HasSuffix(line, ";") && !strings.HasSuffix(line, "=")
}

func checkOnlyE(eIndex, semiIndex int) bool {
	return eIndex >= 1 && semiIndex < 0
}

func checkOnlySemi(eIndex, semiIndex int) bool {
	return eIndex < 0 && semiIndex >= 1
}

func checkACommand(line string) bool {
	return strings.HasPrefix(line, "@") &&
		!strings.HasSuffix(line, "@")
}
