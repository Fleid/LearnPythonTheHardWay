# -*- coding: utf-8 -*-

from nose.tools import *
from ex48.parser import *

def test_parse_without_subject():
    result = parse_sentence([('verb', 'run'), ('direction', 'north')])
    
    assert_equal((result.subject,result.verb,result.object),
    			 ('player','run','north'))

def test_parse_full():
    result = parse_sentence([('noun', 'bear'), ('verb', 'eat'),
    						 ('stop', 'the'), ('noun', 'honey')])
    
    assert_equal((result.subject,result.verb,result.object),
    			 ('bear','eat','honey'))

def test_parse_error_noverb():
    assert_raises(ParserError,parse_sentence,[('noun', 'honey')])

def test_parse_error_nonoun():
    assert_raises(ParserError,parse_sentence,[('verb', 'eat'),])

def test_parse_error_nolast():
    assert_raises(ParserError,parse_sentence,[('noun', 'honey'),('verb', 'eat'),])