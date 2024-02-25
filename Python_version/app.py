from util.util import read_input
from johnson.johnsonrule import JohnsonRule

if __name__ == '__main__':
  #file_path = "data/tabela_petshop"
  file_path = "data/tabela_teste.json"
  petshop = JohnsonRule(read_input(file_path))
  petshop.solution()