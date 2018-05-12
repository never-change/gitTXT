from  model import Model

class Game(Model):
    _name = 'og.igame'

    def s1(self):
        print self.default_get(['date_game','name'])
        print self.search_count([])
        print self.search([],order='id desc')
        print self.name_get([1])
        
        #print self.name_create('wertyuiop')
        print self.search([],order='id desc')
        print self.name_search('p')
        #print self.fields_get()


        print self.check_field_access_rights('read',['name','score_ids'])
        
        print self.read(1)
        print self.read(1,[])
        print self.read(1,['name'])
        
        print self.get_metadata(2)
        print self.check_access_rights('read')
        #print self.check_access_rule(id,'create')
        
        #gid,gname =  self.name_create('wertyuiop')
        #print self.search([],order='id desc')
        #print self.unlink(gid)
        #print self.search([],order='id desc')
        
        #gid,gname =  self.name_create('wertyuiop')
        #print gid,gname
        #print self.write([gid],{'name':'pppppp'})
        #print self.read(gid,['name'])
        
        #gid = self.create({'name':'pww', 'org_type': 'swiss'})
        #print gid
        #print self.read(gid,['name','org_type','game_type'])
        print self.search_read([],['name','org_type','game_type'])
        


class Ptn(Model):
    _name = 'res.partner'
    
    def ss(self):
        print self.get_metadata(1)
        print self.open_parent(1)


def t1():
    Game().s1()
    Ptn().ss()
    

t1()