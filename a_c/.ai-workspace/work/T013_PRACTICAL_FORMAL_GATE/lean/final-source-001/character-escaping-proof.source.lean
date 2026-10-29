module
public import AC.Structure
public import Lean.Data.Json.Basic
meta import Lean.Data.Json.Basic
@[expose] public section
namespace CharacterEscaping
def chars0 : List Char := ['u', 'r', 'n', ':', 'q', 'u', 'o', 't', 'e', ':', '\"', 'a', 'p', 'o', 's', 't', 'r', 'o', 'p', 'h', 'e', '\'']
theorem exact0 : String.ofList chars0 = "urn:quote:\"apostrophe'" := by rfl
#print axioms exact0
def chars1 : List Char := ['u', 'r', 'n', ':', 'b', 'a', 'c', 'k', 's', 'l', 'a', 's', 'h', ':', '\\', 'e', 'n', 'd']
theorem exact1 : String.ofList chars1 = "urn:backslash:\\end" := by rfl
#print axioms exact1
def chars2 : List Char := ['u', 'r', 'n', ':', 'c', 'o', 'n', 't', 'r', 'o', 'l', 's', ':', '\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', '\x7f']
theorem exact2 : String.ofList chars2 = "urn:controls:\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x7f" := by rfl
#print axioms exact2
def chars3 : List Char := ['u', 'r', 'n', ':', 'u', 'n', 'i', 'c', 'o', 'd', 'e', ':', 'é', 'Ω', '中', '😀']
theorem exact3 : String.ofList chars3 = "urn:unicode:éΩ中😀" := by rfl
#print axioms exact3
def chars4 : List Char := ['u', 'r', 'n', ':', 'm', 'i', 'x', 'e', 'd', ':', '\'', '\\', '\"', '\n', '😀']
theorem exact4 : String.ofList chars4 = "urn:mixed:'\\\"\n😀" := by rfl
#print axioms exact4
def values : List String := [String.ofList chars0, String.ofList chars1, String.ofList chars2, String.ofList chars3, String.ofList chars4]
end CharacterEscaping
def main : IO UInt32 := do
 IO.println (Lean.Json.arr (CharacterEscaping.values.map Lean.Json.str).toArray).compress
 return 0
