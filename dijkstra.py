
class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []  #hrany, které začínají v tomto vrcholu (seznam typu Edge)
        self.minDistance = float('inf') #minimální vzdálenost, za kterou se lze dostat do tohoto vrcholu z vrcholu, nad kterým byla provedena funkce computePath() (celočíselný typ)
        self.previousVertex = None #předchozí vrchol - vrchol, přes který vede cesta do tohoto vrcholu pro minimální cestu (typ Vertex)
        

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight



class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def computePath(self, sourceId):
        source = next((v for v in self.vertexes if v.id == sourceId), None)
        if not source:
            print(f"Vertex with ID {sourceId} not found.")
            return

        source.minDistance = 0
        queue = [source]

        while queue:
            current_vertex = queue.pop(0)

            for edge in current_vertex.edges:
                new_distance = current_vertex.minDistance + edge.weight
                target_vertex = next((v for v in self.vertexes if v.id == edge.target), None)
                
                if new_distance < target_vertex.minDistance:
                    target_vertex.minDistance = new_distance
                    target_vertex.previousVertex = current_vertex
                    queue.append(target_vertex)

    def getShortestPathTo(self, targetId):
        target = next((v for v in self.vertexes if v.id == targetId), None)
        if not target:
            print(f"Vertex with ID {targetId} not found.")
            return

        path = []
        current_vertex = target

        while current_vertex:
            path.insert(0, current_vertex)
            current_vertex = current_vertex.previousVertex

        return path

    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes = vertexes

        for edge in edgesToVertexes:
            source_vertex = next((vertex for vertex in self.vertexes if vertex.id == edge.source), None)
            target_vertex = next((vertex for vertex in self.vertexes if vertex.id == edge.target), None)
            if source_vertex and target_vertex:
                source_vertex.edges.append(edge)

    def resetDijkstra(self):
        for v in self.vertexes:
            v.minDistance = float('inf')
            v.previousVertex = None

    def getVertexes(self):
        return self.vertexes