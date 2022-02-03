import graphviz as gv

class DisjointSet:
    def __init__(self,n):
        self._ds = [-1]*n
        self._size = n
    def find(self,x):
        if self._ds[x] < 0:
            return x
        parent = self.find(self._ds[x])
        self._ds[x] = parent
        return parent
    def union(self,x,y):
        Xr = self.find(x)
        Yr = self.find(y)
        if Xr != Yr:
            if self._ds[Xr] > self._ds[Yr]:
                self._ds[Yr] += self._ds[Xr]
                self._ds[Xr] = Yr
            else:
                self._ds[Xr] += self._ds[Yr]
                self._ds[Yr] = Xr
    def isSameSet(self,x,y):
        Xr = self.find(x)
        Yr = self.find(y)
        return Xr == Yr
    def getSet(self):
        return self._ds
    def getSize(self):
        return self._size

def show(ds):
  s = ds.getSet()
  n = ds.getSize()
  G = gv.Digraph("merry")
  G.graph_attr["rankdir"] = "BT"
  for u in range(n):
    G.node(str(u))
  for u, parent in enumerate(s):
    if parent >= 0:
      G.edge(str(u), str(parent))
  return G