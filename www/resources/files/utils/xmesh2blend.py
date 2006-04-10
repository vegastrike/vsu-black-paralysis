# Vegastrike XMESH importer for Blender 2.28a.   By dandandaman <dandandaman@users.sourceforge.net>
#
#
# The Element and Xml2Obj classes have (almost) been lifted straight from <http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/149368>
# Thanks John Bair for making this so easy :-)
#
# ------------------------------
# IMPORT NESCESSARY LIBRARIES
# ------------------------------
import Blender
from Blender import Types, Object, NMesh, Scene
import os

# ------------------------------
# SETUP RUNTIME VARIABLES
# ------------------------------
global outputdir
global Name
outputpath = "/home/daniel/devel/vegastrike/models/apotheid.xmh"		# If path is invalid, I use your current working dir (printed out at end)
outputdir, Name = os.path.split(outputpath)
objtransforms = False													# FIXME:  This is not used yet!!!

if not os.path.isdir(outputdir):
	outputdir = os.curdir

os.chdir(outputdir)

import string
from xml.parsers import expat

class Element:
    'A parsed XML element'
    def __init__(self,name,attributes):
        'Element constructor'
        # The element's tag name
        self.name = name
        # The element's attribute dictionary
        self.attributes = attributes
        # The element's cdata
        self.cdata = ''
        # The element's child element list (sequence)
        self.children = []
        
    def AddChild(self,element):
        'Add a reference to a child element'
        self.children.append(element)
        
    def getAttribute(self,key):
        'Get an attribute value'
        return self.attributes.get(key)
    
    def getData(self):
        'Get the cdata'
        return self.cdata
        
    def getElements(self,name=''):
        'Get a list of child elements'
        #If no tag name is specified, return the all children
        if not name:
            return self.children
        else:
            # else return only those children with a matching tag name
            elements = []
            for element in self.children:
                if element.name == name:
                    elements.append(element)
            return elements

class Xml2Obj:
    'XML to Object'
    def __init__(self):
        self.root = None
        self.nodeStack = []
        
    def StartElement(self,name,attributes):
        'SAX start element even handler'
        # Instantiate an Element object
        element = Element(name.encode(),attributes)
        
        # Push element onto the stack and make it a child of parent
        if len(self.nodeStack) > 0:
            parent = self.nodeStack[-1]
            parent.AddChild(element)
        else:
            self.root = element
        self.nodeStack.append(element)
        
    def EndElement(self,name):
        'SAX end element event handler'
        self.nodeStack = self.nodeStack[:-1]

    def CharacterData(self,data):
        'SAX character data event handler'
        if string.strip(data):
            data = data.encode()
            element = self.nodeStack[-1]
            element.cdata += data
            return

    def Parse(self,filename):
        # Create a SAX parser
        Parser = expat.ParserCreate()

        # SAX event handlers
        Parser.StartElementHandler = self.StartElement
        Parser.EndElementHandler = self.EndElement
        Parser.CharacterDataHandler = self.CharacterData

        # Parse the XML File
        ParserStatus = Parser.Parse(open(filename,'r').read(), 1)
        return self.root
    


def getPoints(points):
	ls = list()
	for point in points.children:
		dat = {}
		for p in point.children:
			dat.update(p.attributes)
		ls.append(dat)
	return ls

def getPolygons(polygons):
	ls = list()
	for face in polygons.children:
		fac = list()
		for p in face.children:
			fac.append(p.attributes)
		ls.append(fac)
	return ls

def getVertexList(face):
	ls = list()
	for po in face:
		ls.append(po['point'])
	return ls

def getUVList(face):
	ls = list()
	for po in face:
		ls.append((po["s"],po["t"]))
	return ls

def importMesh():
	#parser = Xml2Obj()
	element = Xml2Obj().Parse(Name)

	meshAttrib = element.attributes		# A dictionary of tuples
	points = []							# A list of point dictionaries [{'x' : x, 'y' : y, 'z' : z, 'i' : i, 'j': j, 'k' : k}]
	polygons = []						# A list of polygon tuples [[('point' : point, 's' : s, 't' : t)]]
	matterialAttrib = []				# Not implemented

	meshdat = element.children

	for da in meshdat:
		if da.name == "Points":
			points = getPoints(da)
		if da.name == "Polygons":
			polygons = getPolygons(da)
	#	if da.name == "Material":
	#		matterialAttrib

	object = Object.new('NMesh',Name)
	imported = NMesh.new()
	object.link(imported)
	scene = Scene.getCurrent()
	scene.link(object)

	for vert in points:
		imported.Vert(vert['x'],vert['y'],vert['z'])
	global update_normals
	if update_normals:
		for i in range(len(imported.verts)):
			imported.verts[i] = (points[i]['i'],points[i]['j'],points[i]['k'])

	for face in polygons:
		imported.Face(getVertList(face))
		
	for i in range(len(NMesh.faces)):
		NMesh.faces[i].image = meshAttrib["texture"]
		NMesh.faces[i].uv = getUVList(polygons[i])

	global update_normals
	imported.update(update_normals)









importMesh()
Blender.Redraw()