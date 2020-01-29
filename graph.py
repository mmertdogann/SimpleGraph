class Graph:
  def __init__(self):
    self.numberOfNodes = 0
    self.adjacentList = {} #Object (HashTable)

  def addVertext(self, node):
    self.adjacentList[node] = []
    self.numberOfNodes += 1

  def addEdge(self, node1, node2):
    #Undirected Graph

    #Because of undirected we do it twice
    self.adjacentList[node1].append(node2)
    self.adjacentList[node2].append(node1)

  def showConnections(self):
    for k, v in self.adjacentList.items():
      print ('{}: --> {}'.format(k, v))

  # def showConnections(self):


myGraph = Graph()
myGraph.addVertext('0')
myGraph.addVertext('1')
myGraph.addVertext('2')
myGraph.addVertext('3')
myGraph.addVertext('4')
myGraph.addVertext('5')
myGraph.addVertext('6')

myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.showConnections()
