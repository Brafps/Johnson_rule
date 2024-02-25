

class _task():

  def __init__(self, id: str, first_stage: int, second_stage: int):   
    self.id = id
    self.first_stage = first_stage
    self.second_stage = second_stage

  def is_first_stage(self) -> bool:
    return self.first_stage < self.second_stage
  

class JohnsonRule():

  def __init__(self, dictionary: list):
    self.dictionary = dictionary
    self.objects = []
    self.size = len(dictionary)
    self.count = 0
    self.reverse_count = len(dictionary) -1
    self.id_name = [id for id in dictionary[0]][0]
    self.first_stage_name = [stage for stage in dictionary[0]][1]
    self.second_stage_name = [stage for stage in dictionary[0]][2]
    self.order = [position for position in range(self.size)]

    for item in self.dictionary:
      self.objects.append(_task(item[f'{self.id_name}'], item[f'{self.first_stage_name}'], item[f'{self.second_stage_name}']))

  def _min_time_position(self) -> tuple:
    min_time = 10**10
    for obj in self.objects:
      time_first_stage = (self.first_stage_name, obj.first_stage)
      time_second_stage = (self.second_stage_name, obj.second_stage)
      aux = min(time_first_stage[1], time_second_stage[1])

      if aux < min_time:
        min_time = aux
        objct = obj

        if objct.is_first_stage():
          stage = self.first_stage_name
        else:
          stage = self.second_stage_name

    return (objct, stage)


  def _allocation(self, position: tuple):
    if position[1] == self.first_stage_name:
      self.order[int(f'{self.count}')] = position[0]
      self.count += 1
    elif position[1] == self.second_stage_name:
      self.order[int(f'{self.reverse_count}')] = position[0]
      self.reverse_count -= 1
    self.objects.remove(position[0])
    return self.order


  def _processing_time(self, lista):
    first_stage_time = list(map(lambda x: x.first_stage, lista))
    second_stage_time = list(map(lambda x: x.second_stage, lista))
    min_time = first_stage_time[0] + second_stage_time[len(lista)-1]

    for i in range(1, len(lista)):
      if first_stage_time[i] >= second_stage_time[i-1]:
        min_time += first_stage_time[i]
      else:
        min_time += second_stage_time[i-1]
    print("O menor tempo calculado foi de: {} min.".format(min_time))


  def solution(self) -> list:
    for iteration in range(len(self.dictionary)):
      tupla = self._min_time_position()
      ordenation = self._allocation(tupla)
      
    self._processing_time(ordenation)
    
    order_solution = list(map(lambda x: x.id, ordenation))
    print("A ordem de entrada deve ser:", order_solution)