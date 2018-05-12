#!/usr/bin/python
# -*- coding: UTF-8 -*-

from model import Model

class Game(Model):
    _name = 'og.igame'

    def s1(self):
        print '\nIGAME.DEFAULT_GET()\n'
        print 'name    ',        self.default_get(['name'])
        print 'parent_id    ',   self.default_get(['parent_id'])
        print 'child_ids    ',   self.default_get(['child_ids'])
        print 'data_game    ',   self.default_get(['data_game'])
        print 'game_type    ',   self.default_get(['game_type'])
        print 'match_type    ',  self.default_get(['match_type'])
        print 'org_type    ',    self.default_get(['org_type'])
        print 'score_type    ',  self.default_get(['score_type'])
        print 'score_uom    ',   self.default_get(['score_uom'])
        print 'partner_ids    ', self.default_get(['partner_ids'])
        print 'deal_ids    ',    self.default_get(['deal_ids'])
        print 'score_ids    ',   self.default_get(['score_ids'])
        print 'groupi_ids    ',  self.default_get(['groupi_ids'])
        print 'round_ids    ',   self.default_get(['round_ids'])

        print self.search_count([])
        print self.search([],order='id desc')
        # print self.name_get([1])
        print self.name_search()
        print self.check_field_access_rights('read',['name','score_ids'])
        print self.read(1)
        print self.read(1,[])
        print self.read(1,['name'])
        print self.get_metadata(2)
        print self.check_access_rights('read')
        print self.search_read([],['name','org_type','game_type'])



class Group(Model):
    _name = 'og.igame.group'
    
    def s1(self):
        print '\nGROUP.DEFAULT_GET\n'
        print 'igame_id     ',       self.default_get(['igame_id'])
        print 'name     ',           self.default_get(['name'])
        print 'sequence     ',       self.default_get(['sequence'])
        print 'partner_ids     ',    self.default_get(['partner_ids'])


class Round(Model):
    _name = 'og.igame.round'

    def s1(self):
        print '\nROUND.DEFAULT_GET\n'
        print 'igame_id',   self.default_get(['igame_id'])
        print 'number',     self.default_get(['number'])
        print 'deal_ids',   self.default_get(['deal_ids'])
        


class Score(Model):
    _name = 'og.igame.score'

    def s1(self):
        print '\nSCORE.DEFAULT_GET\n'
        print 'score_id    ',       self.default_get(['score_id'])        
        print 'igame_id    ',       self.default_get(['igame_id'])        
        print 'group_id    ',       self.default_get(['group_id'])        
        print 'partner_id    ',     self.default_get(['partner_id'])        
        print 'round_id    ',       self.default_get(['round_id'])        
        print 'match_id    ',       self.default_get(['match_id'])        
        print 'position    ',       self.default_get(['position'])        
        print 'table_id    ',       self.default_get(['table_id'])        
        print 'deal_id    ',        self.default_get(['deal_id'])        
        print 'board_id    ',       self.default_get(['board_id'])        
        print 'score    ',          self.default_get(['score'])        
        print 'uom    ',            self.default_get(['uom'])        
        print 'rank    ',           self.default_get(['rank'])        
        print 'ns_rank    ',        self.default_get(['ns_rank'])        
        print 'ew_rank    ',        self.default_get(['ew_rank'])



class Table(Model):
    _name = 'og.table'
    
    def s1(self):
        print '\nTABLE.DEFAULT_GET\n'
        print 'table_partner_ids    ',  self.default_get(['table_partner_ids'])
        print 'partner_ids'     ,       self.default_get(['partner_ids'])
        print 'ns_partner_id    ',      self.default_get(['ns_partner_id'])
        print 'ew_partner_id    ',      self.default_get(['ew_partner_id'])
        print 'partner_id   ',          self.default_get(['partner_id'])
        print 'deal_ids    ',           self.default_get(['deal_ids'])
        print 'board_ids    ',          self.default_get(['board_ids'])
        print 'name    ',               self.default_get(['name'])



class TablePartner(Model):
    _name = 'og.table.partner'

    def s1(self):
        print '\nTABLEPARTNER.DEFAULT_GET\n'
        print 'table_id     ',   self.default_get(['table_id'])       
        print 'partner_id   ',   self.default_get(['partner_id'])       
        print 'position     ',   self.default_get(['position'])




class Deal(Model):
    _name = 'og.deal'

    def s1(self):
        print '\nDEAL.DEFAULT_GET\n'
        print 'numer    ',      self.default_get(['numer'])
        print 'dealer    ',     self.default_get(['dealer'])
        print 'vulnerable    ', self.default_get(['vulnerable'])
        print 'name    ',       self.default_get(['name'])
        print 'board_ids    ',  self.default_get(['board_ids'])



class Board(Model):
    _name = 'og.board'

    def s1():
        print '\nBOARD.DEFAULT_GET\n'
        print 'table_id    ',   self.default_get(['table_id'])
        print 'deal_id    ',   self.default_get(['deal_id'])
        print 'number    ',   self.default_get(['number'])
        print 'dealer    ',   self.default_get(['dealer'])
        print 'full_deal    ',   self.default_get(['full_deal'])




'''
class Group(Model):
    _name = 'og.igame.group'

    def s1(self):
        print self.default_get(['igame_id','name'])


def t1():
    Game().s1()
    Group().s1()


'''


def t2():
    Game().s1()
    Group().s1()
    Round().s1()
    Score().s1()
    Table().s1()
    TablePartner().s1()
    Deal().s1()

t2()









