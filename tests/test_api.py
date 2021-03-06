from config import *

##############
# NAVIGATION #
##############


def test_navigation_attributes(chikin):
    """Test navigation with attributes by dot notation"""
    assert str(chikin.section) == '\section{Chikin Tales}'
    assert chikin.section.name == 'section'
    assert chikin.section.string == 'Chikin Tales'


def test_navigation_parent(chikin):
    """Test parent navigation"""
    assert chikin.section.parent.name == 'document'
    assert chikin.subsection.parent.name == 'document'


def test_navigation_children(chikin):
    """Test identification of all children"""
    assert len(list(chikin.children)) == 2
    docclass, document = chikin.children
    assert document.name == 'document'
    assert len(list(chikin.document.children)) == 7


def test_navigation_descendants(chikin):
    """Test identification of all descendants"""
    print(list(chikin.descendants))
    assert len(list(chikin.descendants)) == 28

##########
# SEARCH #
##########


def test_find_basic(chikin):
    """Find all LaTeX commands"""
    document = chikin.find('document')
    assert document.name == 'document'


def test_find_by_command(chikin):
    """Find all LaTeX blocks that match a command"""
    sections = list(chikin.find_all('section'))
    assert str(sections[0]) == '\section{Chikin Tales}'
    assert str(sections[1]) == '\section{Chikin Scream}'


################
# MODIFICATION #
################


def test_delete(chikin):
    """Delete an element from the parse tree."""
    chikin.section.delete()
    assert 'Chikin Tales' not in str(chikin)


def test_replace_single(chikin):
    """Replace an element in the parse tree"""
    chikin.section.replace(chikin.subsection)
    assert 'Chikin Tales' not in str(chikin)
    assert len(list(chikin.find_all('subsection'))) == 4


def test_replace_multiple(chikin):
    """Replace an element in the parse tree"""
    chikin.section.replace(chikin.subsection, chikin.subsection)
    assert 'Chikin Tales' not in str(chikin)
    assert len(list(chikin.find_all('subsection'))) == 5


def test_add_children(chikin):
    """Add a child to the parse tree"""
    chikin.section.add_children('asdfghjkl')
    assert 'asdfghjkl' in str(chikin.section)