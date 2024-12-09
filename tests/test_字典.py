from chinese_characters_words import 字典

class Test字典(object):

    def test_接口(self):
        assert 字典.包含('恒') == ['堩', '恒', '搄', '暅', '縆']
