package translator

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
)

const (
	bitStandard = 16

	Dest = "Dest"
	Comp = "Comp"
	Jump = "Jump"

	Comp0       binary = "0101010"
	Comp1       binary = "0111111"
	CompMinus1  binary = "0111010"
	CompD       binary = "0001100"
	CompA       binary = "0110000"
	CompNotD    binary = "0001101"
	CompNotA    binary = "0110001"
	CompMinusD  binary = "0001111"
	CompMinusA  binary = "0110011"
	CompDPlus1  binary = "0011111"
	CompAPlus1  binary = "0110111"
	CompDMinus1 binary = "0001110"
	CompAMinus1 binary = "0110010"
	CompDPlusA  binary = "0000010"
	CompDMinusA binary = "0010011"
	CompAMinusD binary = "0000111"
	CompDAndA   binary = "0000000"
	CompDOrA    binary = "0010101"

	CompM       binary = "1110000"
	CompNotM    binary = "1110001"
	CompMinusM  binary = "1110011"
	CompMPlus1  binary = "1110111"
	CompMMinus1 binary = "1110010"
	CompDPlusM  binary = "1000010"
	CompDMinusM binary = "1010011"
	CompMMinusD binary = "1000111"
	CompDAndM   binary = "1000000"
	CompDOrM    binary = "1010101"

	DestNull binary = "000"
	DestM    binary = "001"
	DestD    binary = "010"
	DestMD   binary = "011"
	DestA    binary = "100"
	DestAM   binary = "101"
	DestAD   binary = "110"
	DestAMD  binary = "111"

	JumpNull binary = "000"
	JumpJGT  binary = "001"
	JumpJEQ  binary = "010"
	JumpJGE  binary = "011"
	JumpJLT  binary = "100"
	JumpJNE  binary = "101"
	JumpJLE  binary = "110"
	JumpJMP  binary = "111"
)

type binary string

func mergeBinary(bs ...binary) binary {
	var str string
	for _, b := range bs {
		str += string(b)
	}
	return binary(str)
}

func intToBinary(n int) binary {
	return binary(strconv.FormatInt(int64(n), 2))
}

func stringToInt(str string) (int, error) {
	n, err := strconv.Atoi(str)
	if err != nil {
		return 0, err
	}
	return n, nil
}

type parsedResults interface {
	CommandType() string
	Fields() []string
}

type Translator struct {
	maps map[string]binary
}

func New() *Translator {
	return &Translator{
		maps: map[string]binary{
			"Comp0": Comp0, "Comp1": Comp1, "Comp-1": CompMinus1, "CompD": CompD,
			"CompA": CompA, "Comp!D": CompNotD, "Comp!A": CompNotA, "Comp-D": CompMinusD,
			"Comp-A": CompMinusA, "CompD+1": CompDPlus1, "CompA+1": CompAPlus1,
			"CompD-1": CompDMinus1, "CompA-1": CompAMinus1, "CompD+A": CompDPlusA,
			"CompD-A": CompDMinusA, "CompA-D": CompAMinusD, "CompD&A": CompDAndA,
			"CompD|A": CompDOrA, "CompM": CompM, "Comp!M": CompNotM,
			"Comp-M": CompMinusM, "CompM+1": CompMPlus1, "CompM-1": CompMMinus1,
			"CompD+M": CompDPlusM, "CompD-M": CompDMinusM, "CompM-D": CompMMinusD,
			"CompD&M": CompDAndM, "CompD|M": CompDOrM,

			"Dest": DestNull, "DestM": DestM, "DestD": DestD, "DestMD": DestMD,
			"DestA": DestA, "DestAM": DestAM, "DestAD": DestAD, "DestAMD": DestAMD,

			"Jump": JumpNull, "JumpJGT": JumpJGT, "JumpJEQ": JumpJEQ, "JumpJGE": JumpJGE,
			"JumpJLT": JumpJLT, "JumpJNE": JumpJNE, "JumpJLE": JumpJLE, "JumpJMP": JumpJMP,
		},
	}
}

func (t *Translator) Translate(pr parsedResults) (string, error) {
	var translatedBinary binary
	switch pr.CommandType() {
	case "A":
		fields := pr.Fields()
		if len(fields) < 1 {
			return "", errors.New("Translate: there should be more than 1 field")
		}
		// opcode
		opCode := binary("0")
		// addess
		n, err := stringToInt(fields[0])
		if err != nil {
			return "", err
		}
		rest := intToBinary(n)
		// if opcode + address is not 16bits
		if n := (len(rest) + len(opCode)); n < bitStandard {
			added := binary(strings.Repeat("0", bitStandard-n))
			translatedBinary = mergeBinary(opCode, added, rest)
		} else {
			translatedBinary = mergeBinary(opCode, rest)
		}
	case "C":
		fields := pr.Fields()
		if len(fields) < 3 {
			return "", errors.New("Translate: there should be more than 3 field")
		}
		opCode := binary("1")
		dummyCode := binary("11")
		dest, err := t.getBinaryCodeByMap(Dest, fields[0])
		if err != nil {
			return "", err
		}
		comp, err := t.getBinaryCodeByMap(Comp, fields[1])
		if err != nil {
			return "", err
		}
		jump, err := t.getBinaryCodeByMap(Jump, fields[2])
		if err != nil {
			return "", err
		}
		translatedBinary = mergeBinary(opCode, dummyCode, comp, dest, jump)
	}
	return string(translatedBinary), nil
}

func (t *Translator) getMapValue(key string) (binary, error) {
	b, ok := t.maps[key]
	if !ok {
		return binary(""), errors.New(fmt.Sprintf("getMapValue error, there is no such key: %s\n", key))
	}
	return b, nil
}

func getMapKey(prefix, stx string) string {
	return fmt.Sprintf("%s%s", prefix, stx)
}

func (t *Translator) getBinaryCodeByMap(prefix, stx string) (binary, error) {
	key := getMapKey(prefix, stx)
	b, err := t.getMapValue(key)
	if err != nil {
		return binary(""), err
	}
	return b, nil
}
