class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        self.vertices = []
        self.vfaces = []
        self.read()

    def read(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)
                if prefix == 'v':
                    lista = []
                    for x in value.split(' '):
                        lista.append(float(x))
                    self.vertices.append(lista)

                    #self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    lista = []
                    for face in value.split(' '):
                        lista2 = []
                        for f in face.split('/'):
                            lista2.append(int(f))
                        lista.append(lista2)
                    self.vfaces.append(lista)
                    #self.vfaces.append([list(map(int, face.split('/'))) for face in value.split(' ')])