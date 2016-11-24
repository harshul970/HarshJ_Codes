import ReverseHashCode

	
def test_SingleLetterString():						##This test will check the single letter strings
	assert 'a' == ReverseHashCode.HashFunction(259)
	
	assert 'w' == ReverseHashCode.HashFunction(274)
	
	assert 'l' == ReverseHashCode.HashFunction(265)

	
def test_RepetitiveLetterString():					##This test will check the repetitive letters strings
	assert 'ccccc' == ReverseHashCode.HashFunction(487333920)


def test_HasFunction():								##This test will check the random string
	assert 'leepadg' == ReverseHashCode.HashFunction(680131659347)


def test_InvalidStringTest():						##This test will check the invalid Hash strings
	assert '<Incorrect Hash String>' == ReverseHashCode.HashFunction(1311)