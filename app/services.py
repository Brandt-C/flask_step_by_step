import requests as r

class Char:
    def __init__(self, name, status, species, gender, origin, image, id):
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.episodes = []
        self.id = id
        self.image = image

class showChars:
    def __init__(self):
        self.chars = {}
    
    def add_char(self, id):
        response = r.get('https://rickandmortyapi.com/api/character/' + str(id) + "/")
        if response.status_code == 200:
            data = response.json()
        na = data['name']
        stat = data['status']
        spec = data['species']
        gen = data['gender']
        ori = data['origin']['name']
        img = data['image']
        n = Char(na, stat, spec, gen, ori, img, id)
        self.chars[data['id']] = n
        
r_m = showChars()